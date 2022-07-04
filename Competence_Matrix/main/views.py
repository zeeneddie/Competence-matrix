from django.shortcuts import render
from .json import loadJSON
from .modelTree import FillModelTree, CreateTree, CLR

def index(request):
    data = loadJSON()
    modelTree = FillModelTree(data)
    return render(
        request, 
        'main/index.html', 
        {
            'tree': "<ul class = 'Container'>" + CreateTree(modelTree) + "</ul>", 
            'competenceList': selectList(modelTree)
        }
    )
def selectList(data):
    tmp = ""
    for currentCompetence in data:
        tmp += """
        <option value = '""" + currentCompetence.name + """'>""" + currentCompetence.name + """</option>
        """
    return tmp
def modelInfo(request):
    data = loadJSON()
    modelTree = FillModelTree(data)
    modelName = request.POST.get('modelName')
    currentModel = CLR(modelTree[0], modelName)
    return render(request, 'main/index.html', 
    {
        'tree': "<ul class = 'Container'>" + CreateTree(modelTree) + "</ul>", 
        'competenceList': selectList(modelTree),
        'competenceInfo': currentModel.description,
        'indicatorList': selectList(currentModel.children)
    })