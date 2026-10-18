# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp
from pennylane import numpy as np

n_bits = 4
dev = qp.device("default.qubit", wires=n_bits)


def oracle_matrix(combo):
    index = np.ravel_multi_index(combo, [2] * len(combo))  # Index of solution
    my_array = np.identity(2 ** len(combo))  # Create the identity matrix
    my_array[index, index] = -1
    return my_array


@qp.qnode(dev)
def oracle_amp(combo):
    for wire in range(n_bits):
        qp.Hadamard(wires=wire)

    qp.QubitUnitary(oracle_matrix(combo), wires=range(n_bits))

    return qp.state()


if __name__ == "__main__":
    print(np.real(oracle_amp([0, 0, 0, 1])))
