from textwrap import indent
from django.shortcuts import redirect, render
from .json import loadJSON, saveJSON
from .modelTree import FillModelTree, CreateTree, CLR_ModelFind, SelectList, ModelInfo, CLR_ModelUpdate, FillJSONDictionary
from .enum import ModelType
from .models import Model

def index(request):
    data = loadJSON()
    modelTree = []
    modelTree.append(Model(None, None, None, FillModelTree(data)))
    return render(
        request, 
        'main/index.html', 
        {
            'tree': "<ul class = 'Container'>" + CreateTree(modelTree[0]) + "</ul>", 
            'competenceList': SelectList(modelTree[0], ModelType.Competence)
        }
    )
def modelInfo(request):
    data = loadJSON()
    modelTree = []
    modelTree.append(Model(None, None, None, FillModelTree(data)))
    currentCompetence = CLR_ModelFind(modelTree[0], request.COOKIES.get('modelCompetence'))
    currentIndicator = CLR_ModelFind(modelTree[0], request.COOKIES.get('modelIndicator'))
    currentKnowledge = CLR_ModelFind(modelTree[0], request.COOKIES.get('modelKnowledge'))
    currentSkill = CLR_ModelFind(modelTree[0], request.COOKIES.get('modelSkill'))
    currentPossession = CLR_ModelFind(modelTree[0], request.COOKIES.get('modelPossession'))
    match request.COOKIES.get('currentModelType'):
        case 'Competence':
            return render(request, 'main/index.html', 
            {
                'tree': "<ul class = 'Container'>" + CreateTree(modelTree[0]) + "</ul>", 
                'competenceList': SelectList(modelTree[0], ModelType.Competence),
                'competenceInfo': ModelInfo(currentCompetence.description),
                'indicatorList': SelectList(currentCompetence, ModelType.Indicator)
            })
        case 'Indicator':
            return render(request, 'main/index.html', 
            {
                'tree': "<ul class = 'Container'>" + CreateTree(modelTree[0]) + "</ul>", 
                'competenceList': SelectList(modelTree[0], ModelType.Competence),
                'competenceInfo': ModelInfo(currentCompetence.description),
                'indicatorList': SelectList(currentCompetence, ModelType.Indicator),
                'indicatorInfo': ModelInfo(currentIndicator.description),
                'knowledgeList': SelectList(currentIndicator, ModelType.Knowledge),
                'skillsList': SelectList(currentIndicator, ModelType.Skill),
                'possessionList': SelectList(currentIndicator, ModelType.Possession)
            })
        case 'Knowledge':
            return render(request, 'main/index.html', 
            {
                'tree': "<ul class = 'Container'>" + CreateTree(modelTree[0]) + "</ul>", 
                'competenceList': SelectList(modelTree[0], ModelType.Competence),
                'competenceInfo': ModelInfo(currentCompetence.description),
                'indicatorList': SelectList(currentCompetence, ModelType.Indicator),
                'indicatorInfo': ModelInfo(currentIndicator.description),
                'knowledgeList': SelectList(currentIndicator, ModelType.Knowledge),
                'knowledgeInfo': ModelInfo(currentKnowledge.description),
                'skillsList': SelectList(currentIndicator, ModelType.Skill),
                'possessionList': SelectList(currentIndicator, ModelType.Possession)
            })
        case 'Skill':
            return render(request, 'main/index.html', 
            {
                'tree': "<ul class = 'Container'>" + CreateTree(modelTree[0]) + "</ul>", 
                'competenceList': SelectList(modelTree[0], ModelType.Competence),
                'competenceInfo': ModelInfo(currentCompetence.description),
                'indicatorList': SelectList(currentCompetence, ModelType.Indicator),
                'indicatorInfo': ModelInfo(currentIndicator.description),
                'knowledgeList': SelectList(currentIndicator, ModelType.Knowledge),
                'skillsList': SelectList(currentIndicator, ModelType.Skill),
                'skillInfo': ModelInfo(currentSkill.description),
                'possessionList': SelectList(currentIndicator, ModelType.Possession)
            })
        case 'Possession':
            return render(request, 'main/index.html', 
            {
                'tree': "<ul class = 'Container'>" + CreateTree(modelTree[0]) + "</ul>", 
                'competenceList': SelectList(modelTree[0], ModelType.Competence),
                'competenceInfo': ModelInfo(currentCompetence.description),
                'indicatorList': SelectList(currentCompetence, ModelType.Indicator),
                'indicatorInfo': ModelInfo(currentIndicator.description),
                'knowledgeList': SelectList(currentIndicator, ModelType.Knowledge),
                'skillsList': SelectList(currentIndicator, ModelType.Skill),
                'possessionList': SelectList(currentIndicator, ModelType.Possession),
                'possessionInfo': ModelInfo(currentPossession.description)
            })
def modelAdd(request):
    return None
def modelChange(request):
    data = loadJSON()
    modelTree = []
    modelTree.append(Model(None, None, None, FillModelTree(data)))
    modelName = request.COOKIES.get('modelName')
    modelDescription = request.COOKIES.get('modelDescription')
    modelTree = CLR_ModelUpdate(modelTree[0], modelTree, modelName, modelDescription)[0][0]
    modelDict = {
        "children": FillJSONDictionary(modelTree)
    }
    saveJSON(modelDict)
    return redirect('modelInfo')
def modelDel(request):
    return None