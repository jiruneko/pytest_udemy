from operator import le
from matplotlib.pyplot import text


def test_calculate():
  result = 5 * 2
  assert result == 10

def test_len():
  text = "hello world"
  assert len(text) == 11

def test_contain():
  text = ("hello world!")
  assert "rld" in text
