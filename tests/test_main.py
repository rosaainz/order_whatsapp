import pytest
from lib.main import calculate_total

@pytest.mark.parametrize(
    "input_x, expected",
    [
        ("""
          5 rol xoconostle 
          5 rol FR
          5 rol canela
          5 rol Almendra 
          5 chocolatín 
          5 croissant 
          5 conchas chocó
          5 conchas vainilla **
            """, 550),
        ("""
            - 4 roles de canela 
            - 4 chocolatines 
            - 2 roles de Almendra 
            - 1 concha de vainilla ** 
            """, 100),
        ("""
            Buenos días, te doy mi pedido 😬😬😬
            2 Berlinesas
            2 roles de xoconostle 
            2 chocolatines
            1 rol de almendras 
            4 medias luna 
            3 roles glaseados
            1 concha de vainilla **
            """, 170),
        ("""
            2 Berlinesas de Queso Mascarpone
            2 Roles de Xoconostle
            2 Croissants de Higo
            2 Chocolatines
            2 Rol de Almendra
            4 Media Luna de Jamón y Queso
            2 conchas vainilla ***
            2 roles glaseados
            """, 360)
    ]
)
def test_total_params(input_x, expected):
    assert calculate_total(input_x) == expected







