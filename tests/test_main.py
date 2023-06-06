
from lib.main import calculate_total

def test_total():
    message = """
  2 Concha Vainilla

  2 Concha Vainilla

  1 Concha Vainilla

  1 Concha Vainilla

  2 Concha Vainilla
    """

    assert calculate_total(message) == 20







