#---------------------------------
# Модель компетенций, индикаторов и ЗУВов (Знания, умения, владения)
#---------------------------------
class Model:
    def __init__(self, name, description, type, children):
        self.name = name
        self.description = description
        self.type = type
        self.children = children
    def __str__(self):
        return self.name