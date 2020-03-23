from django import forms

class CompareTwoForm(forms.Form):
    Player1 = forms.CharField(label='Player 1', max_length=100)
    Player2 = forms.CharField(label='Player 2', max_length=100)

class TeamForm(forms.Form):
    Goalkeeper1 = forms.CharField(label='Goalkeeper 1', max_length=100)
    Goalkeeper2 = forms.CharField(label='Goalkeeper 2', max_length=100)
    Defender1 = forms.CharField(label='Defender 1', max_length=100)
    Defender2 = forms.CharField(label='Defender 2', max_length=100)
    Defender3 = forms.CharField(label='Defender 3', max_length=100)
    Defender4 = forms.CharField(label='Defender 4', max_length=100)
    Defender5 = forms.CharField(label='Defender 5', max_length=100)
    Midfielder1 = forms.CharField(label='Midfielder 1', max_length=100)
    Midfielder2 = forms.CharField(label='Midfielder 2', max_length=100)
    Midfielder3 = forms.CharField(label='Midfielder 3', max_length=100)
    Midfielder4 = forms.CharField(label='Midfielder 4', max_length=100)
    Midfielder5 = forms.CharField(label='Midfielder 5', max_length=100)
    Forward1 = forms.CharField(label='Forward 1', max_length=100)
    Forward2 = forms.CharField(label='Forward 2', max_length=100)
    Forward3 = forms.CharField(label='Forward 3', max_length=100)
