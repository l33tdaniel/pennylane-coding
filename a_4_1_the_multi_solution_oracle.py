# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp
from pennylane import numpy as np

n_bits = 4
dev = qp.device("default.qubit", wires=n_bits)


def multisol_oracle_matrix(combos):
    indices = [np.ravel_multi_index(combo, [2] * len(combo)) for combo in combos]

    my_array = np.identity(2**n_bits)
    for index in indices:
        my_array[index, index] = -1

    return my_array


@qp.qnode(dev)
def multisol_pair_circuit(x_tilde, combos):
    for i in range(n_bits - 1):
        if x_tilde[i] == 1:
            qp.PauliX(wires=i)

    qp.Hadamard(wires=n_bits - 1)
    qp.QubitUnitary(multisol_oracle_matrix(combos), wires=range(n_bits))
    qp.Hadamard(wires=n_bits - 1)

    return qp.probs(wires=n_bits - 1)


if __name__ == "__main__":
    combos = [[0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 0, 1]]
    print(multisol_pair_circuit([0, 1, 1], combos))
    print(multisol_pair_circuit([1, 0, 0], combos))
