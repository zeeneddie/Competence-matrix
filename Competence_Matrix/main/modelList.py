from asyncio.windows_events import NULL
from email.policy import default
from .enum import ModelType
from .models import Model

modelList = []
def FillModelList(data):
    tmp = []
    for currentModel in data["children"]:
        currentModelType = None
        match currentModel["name"][0]:
            case 'И':
                currentModelType = ModelType.Indicator
            case 'З':
                currentModelType = ModelType.Knowledge
            case 'У':
                currentModelType = ModelType.Skills
            case 'В':
                currentModelType = ModelType.Possession
            case _:
                currentModelType = ModelType.Competence
        tmp.append(Model(currentModel["name"],  currentModel["description"], currentModelType, FillModelList(currentModel) if "children" in currentModel else None))
    return tmp
def UpdateModelList(data):
    return None
def CreateTree(data):
    tmp = ""
    for currentModel in data:
        liClass = ""
        if currentModel.type in { ModelType.Knowledge, ModelType.Skills, ModelType.Possession } or currentModel.children == None:
            liClass = "Leaf"
        else:
            liClass = "Closed"
        tmp += """
        <li class = 'Node Expand""" + liClass + """'>
            <div class = 'Expand'></div>
            <div class = 'Content'>""" + currentModel.name + "</div>"
        if currentModel.children != None:
            tmp += "<ul class = 'Container'>" + CreateTree(currentModel.children) + "</ul>"
        tmp += "</li>"
    return tmp