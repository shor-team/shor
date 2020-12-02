import matplotlib.pyplot as plt

from shor.providers.base import Result
from shor.quantum import Circuit

# import pydot


def plot_circuit(circuit: Circuit, to_file="model.png"):
    """Converts a Quantum Circuit into a diagram, and saves to a file

    Args:
        circuit: A quantum :func:`Circuit() <shor.quantum.Circuit>` object
        to_file: File name of the plot image.

    Returns:
        A Jupyter notebook Image object if Jupyter is installed.
        This enables in-line display of the circuit diagram in notebooks.
    """
    pass


def circuit_to_dot(circuit: Circuit):
    """Converts a Quantum Circuit into Dot format
    See: pydot

    Args:
        circuit: A shor.quantum.Circuit object
    """
    pass


def plot_results(result: Result):
    plt.bar(list(result.counts.keys()), result.counts.values())
    plt.xticks([i for i in range(0, 2 ** result.sig_bits, 5)])
    plt.show()
