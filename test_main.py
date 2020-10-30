import main


def test_10():
    assert main.largest_prime_below(10) == 7, 'Failed for the number 10.'

def test_1000000():
    assert main.largest_prime_below(1000000) == 999983, 'Failed for the number 1000000.'

def test_13():
    assert main.largest_prime_below(13) == 11, 'Failed for the number 13.'