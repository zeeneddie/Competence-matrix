# -------------------------------------------------------------------
# Модель компетенций, индикаторов и ЗУВов (Знания, умения, владения)
#-------------------------------------------------------------------
class Model:
    def __init__(self, name, description, children):
        self.name = name
        self.description = description
        self.children = children