from django.shortcuts import redirect, render
from .json import loadJSON, saveJSON
from .enum import ModelType
from .models import Model
from . import modelTree

#------------------
# Основная страница
#------------------
def index(request):
    data = loadJSON()
    tree = []
    tree.append(Model(None, None, None, modelTree.FillModelTree(data)))
    return render(
        request, 
        'main/index.html', 
        {
            'tree': "<ul class = 'Container'>" + modelTree.CreateTree(tree[0]) + "</ul>", 
            'competenceList': modelTree.SelectList(tree[0], None, ModelType.Competence)
        }
    )
#---------------------------
# Вывод информации о моделях
#---------------------------
def modelInfo(request):
    data = loadJSON()
    tree = []
    tree.append(Model(None, None, None, modelTree.FillModelTree(data)))
    currentCompetence = modelTree.CLR_ModelFind(tree[0], request.COOKIES.get('modelCompetence'))
    currentIndicator = modelTree.CLR_ModelFind(tree[0], request.COOKIES.get('modelIndicator'))
    currentKnowledge = modelTree.CLR_ModelFind(tree[0], request.COOKIES.get('modelKnowledge'))
    currentSkill = modelTree.CLR_ModelFind(tree[0], request.COOKIES.get('modelSkill'))
    currentPossession = modelTree.CLR_ModelFind(tree[0], request.COOKIES.get('modelPossession'))
    match request.COOKIES.get('currentModelType'):
        case 'Competence':
            return render(request, 'main/index.html', 
            {
                'tree': "<ul class = 'Container'>" + modelTree.CreateTree(tree[0]) + "</ul>", 
                'competenceList': modelTree.SelectList(tree[0], currentCompetence, ModelType.Competence),
                'competenceInfo': modelTree.ModelInfo(currentCompetence.description),
                'indicatorList': modelTree.SelectList(currentCompetence, currentIndicator, ModelType.Indicator)
            })
        case 'Indicator':
            return render(request, 'main/index.html', 
            {
                'tree': "<ul class = 'Container'>" + modelTree.CreateTree(tree[0]) + "</ul>", 
                'competenceList': modelTree.SelectList(tree[0], currentCompetence, ModelType.Competence),
                'competenceInfo': modelTree.ModelInfo(currentCompetence.description),
                'indicatorList': modelTree.SelectList(currentCompetence, currentIndicator, ModelType.Indicator),
                'indicatorInfo': modelTree.ModelInfo(currentIndicator.description),
                'knowledgeList': modelTree.SelectList(currentIndicator, currentKnowledge, ModelType.Knowledge),
                'skillsList': modelTree.SelectList(currentIndicator, currentSkill, ModelType.Skill),
                'possessionList': modelTree.SelectList(currentIndicator, currentPossession, ModelType.Possession)
            })
        case _:
            return render(request, 'main/index.html', 
            {
                'tree': "<ul class = 'Container'>" + modelTree.CreateTree(tree[0]) + "</ul>", 
                'competenceList': modelTree.SelectList(tree[0], currentCompetence, ModelType.Competence),
                'competenceInfo': modelTree.ModelInfo(currentCompetence.description),
                'indicatorList': modelTree.SelectList(currentCompetence, currentIndicator, ModelType.Indicator),
                'indicatorInfo': modelTree.ModelInfo(currentIndicator.description),
                'knowledgeList': modelTree.SelectList(currentIndicator, currentKnowledge, ModelType.Knowledge),
                'knowledgeInfo': modelTree.ModelInfo(currentKnowledge.description if modelTree.Contains(currentIndicator, currentKnowledge.name) else ""),
                'skillsList': modelTree.SelectList(currentIndicator, currentSkill, ModelType.Skill),
                'skillInfo': modelTree.ModelInfo(currentSkill.description if modelTree.Contains(currentIndicator, currentSkill.name) else ""),
                'possessionList': modelTree.SelectList(currentIndicator, currentPossession, ModelType.Possession),
                'possessionInfo': modelTree.ModelInfo(currentPossession.description if modelTree.Contains(currentIndicator, currentPossession.name) else "")
            })
#----------------
# Добавить модель
#----------------
def modelAdd(request):
    return redirect('modelInfo')
#-------------------------
# Изменить описание модели
#-------------------------
def modelChange(request):
    data = loadJSON()
    tree = []
    tree.append(Model(None, None, None, modelTree.FillModelTree(data)))
    modelName = request.COOKIES.get("model" + request.COOKIES.get("currentModelType"))
    modelDescription = request.COOKIES.get('modelDescription')
    tree = modelTree.CLR_ModelUpdate(tree[0], tree, modelName, modelDescription)[0][0]
    modelDict = {
        "children": modelTree.FillJSONDictionary(tree)
    }
    saveJSON(modelDict)
    return redirect('modelInfo')
#-------------------------
# Удалить модель
#-------------------------
def modelDelete(request):
    data = loadJSON()
    tree = []
    tree.append(Model(None, None, None, modelTree.FillModelTree(data)))
    modelName = request.COOKIES.get("model" + request.COOKIES.get("currentModelType"))
    tree = modelTree.CLR_ModelDelete(tree[0], tree, modelName)[0][0]
    modelDict = {
        "children": modelTree.FillJSONDictionary(tree)
    }
    saveJSON(modelDict)
    return redirect('modelInfo')