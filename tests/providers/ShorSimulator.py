from shor.gates import H
from shor.layers import Qbits
from shor.providers.ShorSimulator import ShorSimulator


def test_quantum_simulator_init():
    from shor.providers.ShorSimulator import ShorSimulator

    ShorSimulator()


def test_run():
    from shor.quantum import Circuit

    circuit = Circuit().add(Qbits(1)).add(H())
    circuit.run(10, ShorSimulator())


def test_result_str_representation():
    from shor.providers.ShorSimulator import ShorSimulatorResult

    result = ShorSimulatorResult({0: 20, 7: 34}, 5)

    assert str(result) == repr(result) == "{'00000': 20, '00111': 34}"


def test_result_get():
    from shor.providers.ShorSimulator import ShorSimulatorResult

    result = ShorSimulatorResult({0: 20, 7: 34}, 5)

    assert 20 == result["00000"] == result["0"] == result[0] == result[0b00000] == result.get(0)
    assert 34 == result["00111"] == result["111"] == result[7] == result[0b00111] == result[0b111] == result.get(7)
