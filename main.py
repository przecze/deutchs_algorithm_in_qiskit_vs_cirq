import qiskit as qs
from qiskit import QuantumCircuit, transpile
from qiskit.providers.aer import QasmSimulator

from numpy import array, sqrt
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit.providers.aer.extensions.snapshot import Snapshot
from qiskit.providers.aer.extensions.snapshot_statevector import *

sim = QasmSimulator()

def to_braket(array):
    """ helper for pretty printing """
    state = []
    for im, base_state in zip(array, ('|00>', '|10>', '|01>', '|11>')):
        if im:
            if not im.imag:
                state.append(f'{im.real:.1f}{base_state}')
            else:
                state.append(f'({im:.1f}){base_state}')

    return " + ".join(state)


def get_output(cin, qr):
    """ prints the circuit together with output state """
    c = cin.copy()
    c.append(Snapshot('snap', 'statevector', 2), qr)
    result = sim.run(qs.transpile(c, sim), shots=1).result()
    snap = result.data()['snapshots']['statevector']['snap'][0]
    print(cin)
    print(to_braket(snap))

# deutsch

regs = [QuantumRegister(2, 'q'), ClassicalRegister(1, 'c')]

# state initialization: apply x on output bit, and H on all
init = QuantumCircuit(*regs)
init.x(1)
init.h(0)
init.h(1)
init.barrier()

# balanced is a c-not - output depends on input
balanced = QuantumCircuit(*regs)
balanced.cx(0,1)
balanced.barrier()

# unbalanced is a 'not' - output is fliped independent of input
unbalanced = QuantumCircuit(*regs)
unbalanced.x(1)
unbalanced.barrier()

# at the end, apply h to input bit and measure it
end = QuantumCircuit(*regs)
end.h(0)
end.measure(0, 0)

# expected: only 1s for balanced, only 0s for inbalanced
print("balanced", sim.run(qs.transpile(init+balanced+end, sim), shots=100).result().get_counts())
print("unbalanced", sim.run(qs.transpile(init+unbalanced+end, sim), shots=100).result().get_counts())
