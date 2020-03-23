import json
import requests

def connect(url):
    return requests.get(url).json()['elements'] #returns json object