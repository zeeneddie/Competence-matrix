from django.shortcuts import render
from .json import loadJSON
from .modelList import FillModelList, CreateTree, modelList

def index(request):
    data = loadJSON()
    modelList = FillModelList(data)
    tree = "<ul class = 'Container'>" + CreateTree(modelList) + "</ul>"
    return render(request, 'main/index.html', {'tree': tree})