import game_of_life

def test_no_initial_state():
    a = game_of_life.function1(p = [])
    e = [[False , False , False , False , False , False , False , False],
         [False , False , False , False , False , False , False , False],
         [False , False , False , False , False , False , False , False],
         [False , False , False , False , False , False , False , False],
         [False , False , False , False , False , False , False , False],
         [False , False , False , False , False , False , False , False],
         [False , False , False , False , False , False , False , False],
         [False , False , False , False , False , False , False , False],]
    assert a == e

def test_one_initial_state():
    a = game_of_life.function1(p = [[3,3]])
    e = [[False , False , False , False , False , False , False , False],
         [False , False , False , False , False , False , False , False],
         [False , False , False , False , False , False , False , False],
         [False , False , False , True , False , False , False , False],
         [False , False , False , False , False , False , False , False],
         [False , False , False , False , False , False , False , False],
         [False , False , False , False , False , False , False , False],
         [False , False , False , False , False , False , False , False],]
    assert a == e
