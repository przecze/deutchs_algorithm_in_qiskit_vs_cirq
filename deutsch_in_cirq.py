import cirq

from common import to_braket

def get_output_state(circuit):
    return to_braket(circuit.final_state_vector())

# Create the qubits
qubits = [cirq.LineQubit(0), cirq.LineQubit(1)]

# Create a circuit
init = cirq.Circuit(
    cirq.H(qubits[0]),
    cirq.X(qubits[1]),
    cirq.H(qubits[1])
)

balanced = cirq.Circuit(
    cirq.CNOT(*qubits)
)

unbalanced0 = cirq.Circuit()

unbalanced1 = cirq.Circuit(
    cirq.X(qubits[1])
)

end = cirq.Circuit(
    cirq.H(qubits[0]),
    cirq.measure(qubits[0], key='m')
)

# Simulate the circuit several times.
simulator = cirq.Simulator()
# expected: only 1s for balanced, only 0s for unbalanced
for kind, oracle in (('b', balanced),
                     ('u', unbalanced0),
                     ('u', unbalanced1)):
    result = simulator.run(init + oracle + end, repetitions=10)
    print(kind, result)
