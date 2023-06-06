
from lib.main import calculate_total

def test_total():
    message = """
   5 rol xoconostle 
   5 rol FR
   5 rol canela
   5 rol Almendra 
   5 chocolatín 
   5 croissant 
   5 conchas chocó
   5 conchas vainilla **
    """

    assert calculate_total(message) == 2







