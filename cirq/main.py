import cirq

def run_deutsch():
# Pick a qubit.
    qubits = [cirq.GridQubit(0, i) for i in (0, 1)]

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
    for oracle in (balanced, unbalanced0, unbalanced1):
        print(init + oracle + end)
        print(simulator.run(init + oracle + end, repetitions=100))
