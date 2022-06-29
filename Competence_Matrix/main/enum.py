from enum import Enum
from telnetlib import STATUS

class ModelType(Enum):
    Competence = 1
    Indicator = 2
    Knowledge = 3
    Skills = 4
    Possession = 5