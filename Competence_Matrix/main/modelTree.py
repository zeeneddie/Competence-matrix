from django import db
from .models import Model

#--------------------------------------------------
# Преобразование данных из JSON в дерево типа Model
#--------------------------------------------------
def FillModelTree(data):
    tmp = []
    for currentModel in data["children"]:
        tmp.append(Model(currentModel["name"],  currentModel["description"], FillModelTree(currentModel) if "children" in currentModel else None))
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
    for currentModel in dataList:
        if currentModel.name == dataModel.name:
            currentModel.description = dataModel.description
            break
        UpdateModel(currentModel.children, dataModel)
#-------------------------
# Добавить модель в дерево
#-------------------------     
def AddModel(dataList, dataModel):
    return None
#-----------------------------
# Генерация дерева компетенций
#-----------------------------
def CreateTree(data):
    tmp = ""
    for currentModel in data:
        liClass = ""
        if currentModel.children == None:
            liClass = "Leaf"
        else:
            liClass = "Closed"
        if currentModel == data[-1]:
            liClass += " IsLast"
        tmp += """
        <li class = 'Node Expand""" + liClass + """'>
            <div class = 'Expand'></div>
            <div class = 'Content'>""" + currentModel.name + "</div>"
        if currentModel.children != None:
            tmp += "<ul class = 'Container'>" + CreateTree(currentModel.children) + "</ul>"
        tmp += "</li>"
    return tmp