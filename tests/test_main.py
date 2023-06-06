
from lib.main import calculate_total

def test_total():
    message = """
    Buenos días, te doy mi pedido 😬😬😬
    2 Berlinesas
    2 roles de xoconostle 
    2 chocolatines
    1 rol de almendras 
    4 medias luna 
    3 roles glaseados
    1 concha de vainilla **
    """

    assert calculate_total(message) == 150







