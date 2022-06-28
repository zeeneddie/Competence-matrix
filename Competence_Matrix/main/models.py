from django.db import models

#--------------------------------------------------------
# Компетенции, индикаторы и ЗУВ (Знания, умения, владения)
#--------------------------------------------------------
class Model:
    def __init__(self, name, description, children):
        self.name = name
        self.description = description
        self.children = children
    def __str__(self):
        return self.name
class KSP:
    def __init__(self, name, description, isKnowledge, isSkills, isPossession):
        self.name = name
        self.description = description
        self.isKnowledge = isKnowledge
        self.isSkills = isSkills
        self.isPossession = isPossession
    def __str__(self):
        return self.name