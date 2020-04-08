from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import TeamForm, CompareTwoForm
from .lasso import run_model
from .connect_to_api import connect
from fpl import FPL
import asyncio
import aiohttp
import unicodedata

import requests
import json

# Create your views here.
from django.http import HttpResponse

team = []
comparison_list = []
APIS = ["https://fantasy.premierleague.com/api/bootstrap-static/"]

def all_players(request):
    players = list_players()
    players.sort()
    return render(request, 'home/all-players.html', {'players': players})

def build_team(request):
    bestPlayers = calculate_best_players()
    return render(request, 'home/best-team.html', {'bestPlayers': bestPlayers})

def compare_players(request):
    tempList = []
    if request.method  == 'POST':
        form = CompareTwoForm(request.POST)
        if form.is_valid():
            tempList.append(form.cleaned_data['Player1'])
            tempList.append(form.cleaned_data['Player2'])
            for player in tempList:
                comparison_list.append(player.split(" "))
            return HttpResponseRedirect('suggestions/')
    else:
        form = CompareTwoForm()
    return render(request, 'home/compare-two-players.html', {'form': form})

def compare_players_suggestions(request):
    comparison = calculate_comparisons(comparison_list)
    return render(request, 'home/compare-two-results.html', {'comparison': comparison})

def get_name(request):
    tempTeam = []
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            tempTeam.append(form.cleaned_data['Goalkeeper1'])
            tempTeam.append(form.cleaned_data['Goalkeeper2'])
            tempTeam.append(form.cleaned_data['Defender1'])
            tempTeam.append(form.cleaned_data['Defender2'])
            tempTeam.append(form.cleaned_data['Defender3'])
            tempTeam.append(form.cleaned_data['Defender4'])
            tempTeam.append(form.cleaned_data['Defender5'])
            tempTeam.append(form.cleaned_data['Midfielder1'])
            tempTeam.append(form.cleaned_data['Midfielder2'])
            tempTeam.append(form.cleaned_data['Midfielder3'])
            tempTeam.append(form.cleaned_data['Midfielder4'])
            tempTeam.append(form.cleaned_data['Midfielder5'])
            tempTeam.append(form.cleaned_data['Forward1'])
            tempTeam.append(form.cleaned_data['Forward2'])
            tempTeam.append(form.cleaned_data['Forward3'])

            for player in tempTeam:
                team.append(player.split(" "))
            return HttpResponseRedirect('team-suggestions/')
    else:
        form = TeamForm()
    return render(request, 'home/input-team.html', {'form': form})

def home_page(request):
    return render(request, 'home/index.html')

def suggest_players(request):
    suggestions = parse_players(team)
    return render(request, 'home/team-results.html', {'suggestions': suggestions})




# Helper methods below this line #

def calculate_best_players():
    json_object = connect(APIS[0])
    predicted_scores = run_model(json_object)
    keys = list(predicted_scores)
    keys.sort(reverse = True)
    best0, best1, best2, best3, best4 = keys[0], keys[1], keys[2], keys[3], keys[4]
    best5, best6, best7, best8, best9 = keys[5], keys[6], keys[7], keys[8], keys[9]
    best10, best11, best12, best13, best14 = keys[10],  keys[11], keys[12], keys[13], keys[14]

    player0, player1, player2, player3, player4 = predicted_scores[best0], predicted_scores[best1], predicted_scores[best2], predicted_scores[best3], predicted_scores[best4]
    player5, player6, player7, player8, player9 = predicted_scores[best5], predicted_scores[best6], predicted_scores[best7], predicted_scores[best8], predicted_scores[best9]
    player10, player11, player12, player13, player14 = predicted_scores[best10], predicted_scores[best11], predicted_scores[best12], predicted_scores[best13], predicted_scores[best14]

    return "The 15 best possible players are: " + player0 + ", " + player1 + ", " + player2 + ", " + player3 + ", " + player4 + ", " + player5 + ", " + player6 + ", " + player7 + ", " + player8 + ", " + player9 + ", " + player10 + ", " + player11 + ", " + player12 + ", " + player13 + ", and " + player14 + ". Good luck trying to fit them all into your team!"
    
def calculate_comparisons(inputtedTeam):
    playersList= []
    json_object = connect(APIS[0])
    confidence_level = ''
    secondPlayer = False
    for inputtedPlayer in inputtedTeam:
        for person in json_object:
            if format_name(person['first_name']) == format_name(inputtedPlayer[0]) and format_name(person['second_name']) == format_name(inputtedPlayer[1]):
                playersList.append(person)
                if secondPlayer:
                    playerIdTuple = (firstPlayerId, person['id'])
                else:
                    secondPlayer = True
                    firstPlayerId = person['id']
    predicted_scores = run_model(playersList)
    player1_pred_score, player2_pred_score = list(predicted_scores.keys())[0], list(predicted_scores.keys())[1]
    adj_p1_pred_score, adj_p2_pred_score = player1_pred_score / 38, player2_pred_score / 38

    playerFormTuple = asyncio.run(playerExample(playerIdTuple))

    if playerFormTuple[0] > 3.0:
        adj_p1_pred_score = adj_p1_pred_score * 2
    elif playerFormTuple[0] == 0.0:
        adj_p1_pred_score = adj_p1_pred_score * 0.5

    if abs(adj_p1_pred_score - adj_p2_pred_score) < 1.5:
        confidence_level = 'only slightly confident'
    elif abs(adj_p1_pred_score - adj_p2_pred_score) < 3.0:
        confidence_level = 'moderately confident'
    else:
        confidence_level = 'extremely confident'

    comparison_list, inputtedTeam = [], []
    return "We are " + confidence_level + ' that ' + predicted_scores[max(player1_pred_score, player2_pred_score)] +  " will outpeform " + predicted_scores[min(player1_pred_score, player2_pred_score)] + " this week."

def format_name(text):
    try:
        text = unicode(text, 'utf-8')
    except NameError: # unicode is a default on python 3 
        pass

    text = str(unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode("utf-8"))
    finalText = text.lower()
    return finalText

def list_players():
    json_object = connect(APIS[0])
    players = []
    for player in json_object:
        players.append(player['first_name'] + " " + player['second_name'])
    return players

def parse_players(inputtedTeam):
    json_object = connect(APIS[0])
    playersList = []
    for inputtedPlayer in inputtedTeam:
        for person in json_object:
            if format_name(person['first_name']) == format_name(inputtedPlayer[0]) and format_name(person['second_name']) == format_name(inputtedPlayer[1]):
                playersList.append(person)
    player_score_predictions = run_model(playersList)
    keys = list(player_score_predictions.keys())
    keys.sort()

    worst_player_score = keys[0]
    second_worst_player_score = keys[1]
    third_worst_player_score = keys[2]

    worst_player_name = player_score_predictions[worst_player_score]
    second_worst_player_name = player_score_predictions[second_worst_player_score]
    third_worst_player_name = player_score_predictions[third_worst_player_score]

    return "Your worst predicted players in order are " + worst_player_name + ", " + second_worst_player_name + ", and " + third_worst_player_name + ". You should consider benching these players or finding replacements on the transfer market."

async def playerExample(inputtedPlayerTuple):
    session = aiohttp.ClientSession()
    fpl = FPL(session)
    playerOne = await fpl.get_player(inputtedPlayerTuple[0])
    playerTwo = await fpl.get_player(inputtedPlayerTuple[1])
    playerFormTuple = (float(playerOne.__dict__['form']), float(playerTwo.__dict__['form']))
    await session.close()
    return playerFormTuple
