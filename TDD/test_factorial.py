from factorial import factorial

def test_factorial_0():
    assert factorial(0) == 1
    
def test_factorial():
    assert factorial(3) == 1*2*3
