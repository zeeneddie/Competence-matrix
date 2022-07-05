from .models import Model
from .enum import ModelType

#--------------------------------------------------
# Преобразование данных из JSON в дерево типа Model
#--------------------------------------------------
def FillModelTree(data):
    tmp = []
    for currentModel in data["children"]:
        modelType = None
        match currentModel["name"][0]:
            case 'З':
                modelType = ModelType.Knowledge
            case 'У':
                modelType = ModelType.Skill
            case 'В':
                modelType = ModelType.Possession
            case 'И':
                modelType = ModelType.Indicator
            case _:
                modelType = ModelType.Competence
        tmp.append(Model(currentModel["name"], modelType ,  currentModel["description"], FillModelTree(currentModel) if "children" in currentModel else None))
    return tmp
#--------------------
# Прямой обход дерева
#--------------------
def CLR(subroot, key):
    if subroot.children == None or subroot.name == key:
        return subroot
    for currentModel in subroot.children:
        return CLR(currentModel, key)
    """
    if subroot.children != None:
        if key != subroot.name:
                for currentModel in subroot.children:
                    CLR(currentModel, key)
                return None
        else:
            return subroot
    else:
        return None
    """
#------------------------------
# Обновить данные модели дерева
#------------------------------
def UpdateModel(dataList, dataModel):
    return None
#-------------------------
# Добавить модель в дерево
#-------------------------     
def AddModel(dataList, dataModel):
    return None
#-------------------------
# Удалить модель из дерева
#-------------------------     
def DeleteModel(dataList, dataModel):
    return None
#-----------------------------
# Генерация дерева компетенций
#-----------------------------
def CreateTree(data):
    result = ""
    for currentModel in data:
        liClass = ""
        if currentModel.children == None:
            liClass = "Leaf"
        else:
            liClass = "Closed"
        if currentModel == data[-1]:
            liClass += " IsLast"
        result += """
        <li class = 'Node Expand""" + liClass + """'>
            <div class = 'Expand'></div>
            <div class = 'Content' style='background-color:#FFFFE0;'>""" + currentModel.name + """</div>
            <div class = 'Content'>""" + currentModel.description + """</div>"""
        if currentModel.children != None:
            result += "<ul class = 'Container'>" + CreateTree(currentModel.children) + "</ul>"
        result += "</li>"
    return result
#------------------------------
# Список моделей modelType типа
#------------------------------
def selectList(data, modelType):
    result = ""
    for currentModel in data:
        result += "<option onclick='UpdateCookieModel(value, id)' id = '" + modelType.name + "' value = '" + currentModel.name + "'>" + currentModel.name + "</option>"
    return result