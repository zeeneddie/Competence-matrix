from django.shortcuts import render
from .json import loadJSON
from .modelTree import FillModelTree, CreateTree, CLR, selectList
from .enum import ModelType

def index(request):
    data = loadJSON()
    modelTree = FillModelTree(data)
    return render(
        request, 
        'main/index.html', 
        {
            'tree': "<ul class = 'Container'>" + CreateTree(modelTree) + "</ul>", 
            'competenceList': selectList(modelTree, ModelType.Competence)
        }
    )
def modelInfo(request):
    data = loadJSON()
    modelTree = FillModelTree(data)
    currentCompetence = CLR(modelTree[0], request.COOKIES.get('modelCompetence'))
    currentIndicator = CLR(modelTree[0], request.COOKIES.get('modelIndicator'))
    currentKnowledge = CLR(modelTree[0], request.COOKIES.get('modelKnowledge'))
    currentSkill = CLR(modelTree[0], request.COOKIES.get('modelSkill'))
    currentPossession = CLR(modelTree[0], request.COOKIES.get('modelPossession'))
    return render(request, 'main/index.html', 
    {
        'tree': "<ul class = 'Container'>" + CreateTree(modelTree) + "</ul>", 
        'competenceList': selectList(modelTree, ModelType.Competence),
        'competenceInfo': currentCompetence.description,
        'indicatorList': selectList(currentCompetence.children, ModelType.Indicator),
        'indicatorInfo': currentIndicator.description,
        'knowledgeList': selectList(currentIndicator.children, ModelType.Knowledge),
        'knowledgeInfo': currentKnowledge.description,
        'skillList': selectList(currentIndicator.children, ModelType.Skill),
        'skillInfo': currentSkill.description,
        'possessionList': selectList(currentIndicator.children, ModelType.Possession),
        'possessionInfo': currentPossession.description
    })