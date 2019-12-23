import exercise
import random

def test_digits():
    a = exercise.digits(3467)
    e = 4.0
    assert a == e

def test_words():
    a = exercise.words("Hello World")
    e = 2
    assert a == e

def test_Mtable():
    a = exercise.Mtable(3)
    e = [3,6,9,12,15,18,21,24,27,30]
    assert a == e

def test_Mtable2():
    a = exercise.Mtable2(3,5)
    e = [3,6,9,12,15,]
    assert a == e


def test_bigger():
    x = random.random()
    y = random.random()
    a = exercise.bigger(x,y)
    e = max(x,y)
    assert a == e


def test_biggest_in_list():
    for count in range(10,50):
        n = [random.random() for _ in range(count)]
        a = exercise.biggest_in_list(n)
        e = max(n)
        assert a == e

def test_fizzbizz():
    a = exercise.fizzbizz(20)
    e = [1, 2, 'fizz', 4, 'bizz', 'fizz', 7, 8, 'fizz', 'bizz', 11, 'fizz', 13, 14, 'fizzbizz', 16, 17, 'fizz', 19, 'bizz']
    assert a == e

def test_fizzbizz1():
    a = exercise.fizzbizz(-5)
    e = 0
    assert a == e

def test_panagram():
    a = exercise.panagram("The quick brown fox jumps over the lazy dog")
    e = True
    assert a == e
def test_pangram1():
    a = exercise.panagram("The quick brown fox jumped over the lazy dog")
    e = False
    assert a == e
def test_pangram2():
    a = exercise.panagram("The Quick brown Fox jumps over the lazy dog")
    e = True
    assert a == e 

def test_feq():
    a = exercise.freq("Hello World")
    e = {' ': 1, 'o': 2, 'e': 1, 'H': 1, 'l': 3, 'r': 1, 'd': 1, 'W': 1}
    assert a == e




def test_evaluate():
    a = exercise.evaluate("32+5*")
    e = 25
    assert a == e

def test_evaluate1():
    a = exercise.evaluate("82/3-")
    e = 1
    assert a == e
    
import pytest
def test_evaluate2():
    with pytest.raises(ZeroDivisionError):
        exercise.evaluate("80/")
