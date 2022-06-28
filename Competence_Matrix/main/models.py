from django.db import models

#--------------------------------------------------------
# Компетенции, индикаторы и ЗУВ (Знания, умения, владения)
#--------------------------------------------------------
class Model:
    def __init__(self, type, name, description, children):
        self.type = type
        self.name = name
        self.description = description
        self.children = children
    def __str__(self):
        return self.name