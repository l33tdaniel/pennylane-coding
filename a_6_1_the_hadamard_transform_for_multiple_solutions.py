# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp
from pennylane import numpy as np

from a_4_1_the_multi_solution_oracle import multisol_oracle_matrix

n_bits = 4
dev = qp.device("default.qubit", wires=n_bits)


@qp.qnode(dev)
def multisol_hoh_circuit(combos):
    for wire in range(n_bits):
        qp.Hadamard(wires=wire)

    qp.QubitUnitary(multisol_oracle_matrix(combos), wires=range(n_bits))

    for wire in range(n_bits):
        qp.Hadamard(wires=wire)

    return qp.probs(wires=range(n_bits))


if __name__ == "__main__":
    all_combos = [[int(s) for s in np.binary_repr(n, n_bits)] for n in range(2**n_bits)]
    for how_many in range(2**n_bits + 1):
        prob_zero = multisol_hoh_circuit(all_combos[:how_many])[0]
        print(f"{how_many:2d} solutions: P(0) = {prob_zero:.4f}")
