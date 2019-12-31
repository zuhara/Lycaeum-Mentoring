from digits import digits
def test_digits_1():
    assert digits(5) == 1
    assert digits(8) == 1
def test_digits_2():
    for i in [19,56,99]:
        assert digits(i) == 2
        
def test_more_than_2():
    assert digits(3456) == 4
    assert digits(654) == 3
    assert digits(45321 == 5)
    
