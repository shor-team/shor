from shor.layers import Qbits


def test_init():
    from shor.layers import Qubits

    Qubits(2)


def test_iterable():
    qbits = Qbits(5)

    # Implements iterable, so we get all of the nice
    # python indexing functionality
    even = qbits[::2]  # Get the even indexed qbits
    odd = qbits[1::2]  # Get the odd indexed qbits

    assert len(even) == 3
    assert len(odd) == 2
    assert even == [0, 2, 4]
    assert odd == [1, 3]
