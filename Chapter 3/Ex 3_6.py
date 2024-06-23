double = lambda x: x*2

def test_double():
    assert double(2) == 4
    assert abs(double(0.1) - 0.2) < 1E-15
    assert double([1,2]) == [1,2,1,2]
    assert double((1,2)) == (1,2,1,2)
    assert double(3+4*1j) == 6+8*1j
    assert double("hello") == "hellohello"

test_double()