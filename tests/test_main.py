
from lib.main import calculate_total

def test_total():
    message = """
    2 Berlinesas de Queso Mascarpone
    2 Roles de Xoconostle
    2 Croissants de Higo
    2 Chocolatines
    2 Rol de Almendra
    4 Media Luna de Jamón y Queso
    2 conchas vainilla ***
    2 roles glaseados
    """

    assert calculate_total(message) == 2







