from django.shortcuts import render
import json

def index(request):
    return render(request, 'main/index.html')

def loadJSON():
    with open('DB.json', 'r') as file:
        data = json.load(file)
    return data

def saveJSON(data):
    with open('DB.json', 'w') as file:
        json.dump(data, file, indent=3)