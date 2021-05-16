import cirq
import random

print("reload")

def hadamard(qubits):
    return cirq.Circuit(*(cirq.H(q) for q in qubits))

def measure(qubits):
    return cirq.Circuit(*(cirq.measure(q, key=i) for i, q in enumerate(qubits[:-1])))

def get_oracle(s, qubits):
    gates = []
    for qubit, si in zip(qubits[:-1], s):
        if si == '1':
            gates.append(cirq.CNOT(qubit, qubits[-1]))
    return cirq.Circuit(*gates)

n = 10
qubits = cirq.LineQubit.range(n)
s = ''.join(random.choice(('0', '1')) for i in range(n-1))
sim = cirq.Simulator()

print("s: ", s)
circuit = cirq.Circuit(cirq.X(qubits[-1])) + hadamard(qubits) + get_oracle(s, qubits) + hadamard(qubits) + measure(qubits)
print(sim.run(circuit))
