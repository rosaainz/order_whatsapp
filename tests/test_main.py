
from lib.main import calculate_total

def test_total():
    message = """
    - 4 roles de canela 
    - 4 chocolatines 
    - 2 roles de Almendra 
    - 2 conchas de vainilla **
    """

    assert calculate_total(message) == 2







