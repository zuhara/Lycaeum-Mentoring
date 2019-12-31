from mode import mode
import statistics
import pytest

def test_mode_1():
    assert mode([2]) == 2
def test_mode_3():
    assert mode([1,3,3]) == 3
def test_mode():
    assert mode([1,3,3,5,5]) == 
