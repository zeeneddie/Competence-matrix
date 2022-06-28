from django.shortcuts import render
from .models import Model, KSP
from .json import loadJSON

def index(request):
    data = loadJSON()
    modelList = []
    for currentCompetence in data['competence']:
        indicatorList = []
        for currentIndicator in currentCompetence["indicator"]:
            KSPList = []
            for currentKSP in currentIndicator["KSP"]:
                isKnowledge = False
                isSkills = False
                isPossession = False
                match currentKSP["name"][0]:
                    case 'З':
                        isKnowledge = True
                    case 'У':
                        isSkills = True
                    case 'В':
                        isPossession = True
                KSPList.append(KSP(currentKSP["name"], currentKSP["description"], isKnowledge, isSkills, isPossession))
            indicatorList.append(Model(currentIndicator["name"], currentIndicator["description"], KSPList))
        modelList.append(Model(currentCompetence["name"], currentCompetence["description"], indicatorList))
    return render(request, 'main/index.html', {'modelList': modelList})