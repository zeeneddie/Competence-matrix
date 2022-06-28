from django.shortcuts import render
from .models import Model
import json
import os
import codecs

def index(request):
    data = loadJSON()
    competence = []
    for currentCompetence in data['competence']:
        indicator = []
        KSP = []
        for currentIndicator in currentCompetence["indicator"]:
            for currentKSP in currentIndicator["KSP"]:
                KSP.append(Model("KSP", currentKSP["name"], currentKSP["description"], None))
            indicator.append(Model("indicator", currentIndicator["name"], currentIndicator["description"], KSP))
        competence.append(Model("competence", currentCompetence["name"], currentCompetence["description"], indicator))
    return render(request, 'main/index.html', {'competence': competence})

def loadJSON():
    file = codecs.open(os.path.dirname(os.path.abspath(__file__)) + "\DB.json", 'r', "utf_8_sig")
    data = json.load(file)
    return data
def saveJSON(data):
    file = codecs.open(os.path.dirname(os.path.abspath(__file__)) + "\DB.json", 'w', "utf_8_sig")
    json.dump(data, file, indent=3)