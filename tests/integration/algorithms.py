from shor.algorithms.shor import factor
import random

# Seed for tests
random.seed(0)


def test_shor_factoring():
    N = 3 * 5

    a, b = factor(N)

    assert a == 3 or a == 5
    assert b == N / a

    N = 3 * 7

    a, b = factor(N)

    assert a == 3 or a == 7
    assert b == N / a
