# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp
from pennylane import numpy as np

n_bits = 5
dev = qp.device("default.qubit", wires=n_bits)


def oracle_matrix(combo):
    index = np.ravel_multi_index(combo, [2] * len(combo))  # Index of solution
    my_array = np.identity(2 ** len(combo))  # Create the identity matrix
    my_array[index, index] = -1
    return my_array


def diffusion_matrix():
    psi_piece = (1 / 2**n_bits) * np.ones(2**n_bits)
    ident_piece = np.eye(2**n_bits)
    return 2 * psi_piece - ident_piece


@qp.qnode(dev)
def grover_circuit(combo, num_steps):
    for wire in range(n_bits):
        qp.Hadamard(wires=wire)

    for _ in range(num_steps):
        qp.QubitUnitary(oracle_matrix(combo), wires=range(n_bits))
        qp.QubitUnitary(diffusion_matrix(), wires=range(n_bits))

    return qp.state()


my_steps = 4

if __name__ == "__main__":
    combo = [0, 0, 0, 0, 0]
    for steps in range(8):
        amp = np.real(grover_circuit(combo, steps)[0])
        print(f"{steps} steps: solution probability = {amp**2:.4f}")
    print(f"my_steps = {my_steps}")
