# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp
from pennylane import numpy as np

from g_1_1_oracle_action_in_a_uniform_superposition import oracle_matrix

n_bits = 4
dev = qp.device("default.qubit", wires=n_bits)


def diffusion_matrix():
    psi_piece = (1 / 2 ** (n_bits - 1)) * np.ones((2**n_bits, 2**n_bits))
    ident_piece = np.eye(2**n_bits)

    return psi_piece - ident_piece


@qp.qnode(dev)
def difforacle_amp(combo):
    for wire in range(n_bits):
        qp.Hadamard(wires=wire)

    qp.QubitUnitary(oracle_matrix(combo), wires=range(n_bits))
    qp.QubitUnitary(diffusion_matrix(), wires=range(n_bits))

    return qp.state()


if __name__ == "__main__":
    print(np.real(difforacle_amp([0, 0, 0, 0])))
