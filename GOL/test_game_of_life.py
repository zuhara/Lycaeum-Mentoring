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

def test_two_initial_state():
    a = game_of_life.function1(p = [[3,3],[1,2]])
    e = [[False , False , False , False , False , False , False , False],
         [False , False , True , False , False , False , False , False],
         [False , False , False , False , False , False , False , False],
         [False , False , False , True , False , False , False , False],
         [False , False , False , False , False , False , False , False],
         [False , False , False , False , False , False , False , False],
         [False , False , False , False , False , False , False , False],
         [False , False , False , False , False , False , False , False],]
    assert a == e

def test_many_initial_state():
    a = game_of_life.function1(p = [[3,3],[1,2],[2,2],[2,3]])
    e = [[False , False , False , False , False , False , False , False],
         [False , False , True , False , False , False , False , False],
         [False , False , True , True , False , False , False , False],
         [False , False , False , True , False , False , False , False],
         [False , False , False , False , False , False , False , False],
         [False , False , False , False , False , False , False , False],
         [False , False , False , False , False , False , False , False],
         [False , False , False , False , False , False , False , False],]
    assert a == e

#Any live cell with fewer than two live neighbours dies, as if by underpopulation.
def test_rule_one_case_one():
    list = [[False , False , False , False , False , False , False , False],
            [False , False , False , False , False , False , False , False],
            [False , False , False , False , False , False , False , False],
            [False , False , False , True , False , False , False , False],
            [False , False , False , False  , False , False , False , False],
            [False , False , False , False , False , False , False , False],
            [False , False , False , False , False , False , False , False],
            [False , False , False , False , False , False , False , False],]
    a = game_of_life.next_gen(l=list)
    e = [[False , False , False , False , False , False , False , False],
         [False , False , False , False , False , False , False , False],
         [False , False , False , False , False , False , False , False],
         [False , False , False , False , False , False , False , False],
         [False , False , False , False , False , False , False , False],
         [False , False , False , False , False , False , False , False],
         [False , False , False , False , False , False , False , False],
         [False , False , False , False , False , False , False , False],]
    assert a == e

def test_rule_one_case_two():
    list = [[False , False , False , False , False , False , False , False],
            [False , False , False , False , False , False , False , False],
            [False , False , False , False , False , False , False , False],
            [False , False , False , True , False , False , False , False],
            [False , False , False , True  , False , False , False , False],
            [False , True , False , False , False , False , False , False],
            [False , True , False , False , False , False , False , False],
            [False , True , False , False , False , False , False , False],]
    a = game_of_life.next_gen(l=list)
    e = [[False , False , False , False , False , False , False , False],
         [False , False , False , False , False , False , False , False],
         [False , False , False , False , False , False , False , False],
         [False , False , False , False , False , False , False , False],
         [False , False , False , False , False , False , False , False],
         [False , False , False , False , False , False , False , False],
         [False , False , False , False , False , False , False , False],
         [False , False , False , False , False , False , False , False],]
    assert a == e
    
