# A PyTest for Azure Pipeline
import pytest

def sum(x, y):
  return x + y

def test_simplesum():
  assert sum(1,1) == 2
  
def test_failingsum():
  assert sum(1,2) == 3
