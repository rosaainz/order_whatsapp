import pytest
from lib.main import calculate_total

@pytest.mark.parametrize(
    "input_x, expected",
    [
        ("""
            2 Concha Vainilla
            1 Conch Choc
            2 Croissa
            """, {'concha de vainilla' : 2, 'concha de chocolate' : 1, 'croissant': 2})
    ]
)
def test_total_params_pass(input_x, expected):
    assert calculate_total(input_x) == expected