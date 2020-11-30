from shor.layers import Qbits


def test_qubits_init():
    from shor.layers import Qubits

    Qubits(2)


def test_qbits_iterable():
    qbits = Qbits(4)

    # Implements iterable, so we get all of the nice
    # python indexing functionality
    even = qbits[::2]  # Get the even indexed qbits
    odd = qbits[1::2]  # Get the odd indexed qbits

    print(even)
    print(odd)
