import numpy as np

def is_square(m):
    return m.shape[0] == m.shape[1] and len(m.shape) == 2

def is_unitary(m):
    return np.allclose(np.eye(m.shape[0]), m.dot(m.conj().T))
