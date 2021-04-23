import qiskit as qs
from qiskit import QuantumCircuit, transpile
from qiskit.providers.aer import QasmSimulator

sim = QasmSimulator()

# one qubit, one classic register
circ = qs.QuantumCircuit(1,1)
circ.measure([0], [0])
print(circ)
print(sim.run(qs.transpile(circ, sim), shots=100).result().get_counts())

circ.data.pop()
circ.h(0)
circ.measure([0], [0])
print(circ)
print(sim.run(qs.transpile(circ, sim), shots=100).result().get_counts())

