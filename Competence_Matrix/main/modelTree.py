from pyexpat import model
from .models import Model
from .enum import ModelType

#--------------------------------------------------
# Преобразование данных из JSON в дерево типа Model
#--------------------------------------------------
def FillModelTree(data):
    tmp = []
    try:
        for currentModel in data["children"]:
            tmp.append(Model(currentModel["name"], GetModelType(currentModel["type"]), currentModel["description"].strip(), FillModelTree(currentModel) if "children" in currentModel else None))
    except:
        return None
    return tmp
#--------------------------------------------------
# Преобразование данных из дерева типа Model в JSON
#--------------------------------------------------
def FillJSONDictionary(data):
    childrenList = []
    for currentModel in data.children:
        children = {
            "name": currentModel.name,
            "description": currentModel.description,
            "type": currentModel.type.name,
            "children": FillJSONDictionary(currentModel) if currentModel.children != None else None
        }
        childrenList.append(children)
    return childrenList
#---------------------
# Содержится ли модель
#---------------------
def Contains(root, key):
    for model in root.children:
        if model.name == key:
            return True
    return False
#--------------------------------------
# Прямой обход дерева (нахождение узла)
#--------------------------------------
def ModelFind(subroot, key):
    if subroot.name != key:
        if subroot.children != None:
            model = Model(None,None,None,None)
            for currentModel in subroot.children:
                result = ModelFind(currentModel, key)
                if result != None:
                    if result.name == key:
                        return result
            return model
        else:
            return None
    else:
        return subroot
#---------------------------------------
# Прямой обход дерева (обновление модели)
#---------------------------------------
def ModelUpdate(subroot, currentModelList, key, value):
    modelList = []
    if currentModelList is None:
        currentModelList = []
    currentModelList.append(subroot)
    if subroot.children:
        for currentModel in subroot.children:
            if currentModel.name == key:
                currentModel.description = value
            modelList.extend(ModelUpdate(currentModel, currentModelList[:], key, value))
    else:
        modelList.append(currentModelList)
    return modelList
#---------------------------------------
# Прямой обход дерева (удаление модели)
#---------------------------------------
def ModelDelete(subroot, currentModelList, key):
    modelList = []
    if currentModelList is None:
        currentModelList = []
    currentModelList.append(subroot)
    if subroot.children:
        for currentModel in subroot.children:
            if currentModel.name == key:
                subroot.children.remove(currentModel)
            modelList.extend(ModelDelete(currentModel, currentModelList[:], key))
    else:
        modelList.append(currentModelList)
    return modelList
#---------------------------------------
# Прямой обход дерева (добавление модели)
#---------------------------------------
def ModelAdd(subroot, currentModelList, key, modelName, modelDescription, modelType):
    modelList = []
    if currentModelList is None:
        currentModelList = []
    currentModelList.append(subroot)
    if subroot.children:
        for currentModel in subroot.children:
            if currentModel.name == key:
                if currentModel.children == None:
                    currentModel.children = []
                currentModel.children.append(Model(modelName, modelType, modelDescription, None))
                continue
            modelList.extend(ModelAdd(currentModel, currentModelList[:], key, modelName, modelDescription, modelType))
    else:
        modelList.append(currentModelList)
    return modelList
#----------------------
# Получение типа модели
#----------------------
def GetModelType(currentModelType):
    match currentModelType:
        case "Competence":
            return ModelType.Competence
        case "Indicator":
            return ModelType.Indicator
        case "Knowledge":
            return ModelType.Knowledge
        case "Skill":
            return ModelType.Skill
        case "Possession":
            return ModelType.Possession  
#-----------------------------
# Генерация дерева компетенций
#-----------------------------
def CreateTree(data):
    result = ""
    for currentModel in data.children:
        liClass = ""
        if currentModel.children == None:
            liClass = "Leaf"
        else:
            liClass = "Closed"
        if currentModel == data.children[-1]:
            liClass += " IsLast"
        color = ""
        match currentModel.type:
            case ModelType.Competence:
                color = "#FFF8DC"
            case ModelType.Indicator:
                color = "#FFDEAD"
            case _:
                color = "#FFEBCD"
        result += """
            <li class = 'Node Expand""" + liClass + """'>
                <div class = 'Expand'></div>
                <div class = 'Content' style='background-color:""" + color + """;'>""" + currentModel.name + """</div>
                <div class = 'Content'>""" + currentModel.description + """</div>"""
        if currentModel.children != None:
            result += "<ul class = 'Container'>" + CreateTree(currentModel) + "</ul>"
        result += "</li>"
    return result
#------------------------------
# Список моделей modelType типа
#------------------------------
def SelectList(data, model, modelType):
    result = ""
    if data.children:
        for currentModel in data.children:
            if currentModel.type == modelType:
                style = ""
                if model != None and currentModel.name == model.name:
                    style = "style='background: #FFFACD;'"
                result += "<option " + style + " onclick='UpdateCookieModel(value, id)' id = '" + modelType.name + "' value = '" + currentModel.name + "'>" + currentModel.name + "</option>"
    return result
#---------------------------
# Возвращает описание модели
#---------------------------
def ModelInfo(model):
    return "" if model == None else model