import threading
from . import portriko, nepal

def get_sources() -> list(dict()): 
    result = list()
    for cls in (portriko.Portoriko, nepal.Nepal):
        result.append(cls().get_menu())

    return result