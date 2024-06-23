def sum_1k(M):
    sum = 0
    for k in range(1,M+1):
        sum += 1/k
    return(sum)

def test_sum_1k():
    assert abs(sum_1k(3) - 11.0/6.0) < 1E-15

test_sum_1k()


