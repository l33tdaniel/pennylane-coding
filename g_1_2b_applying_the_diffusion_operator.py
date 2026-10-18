# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp
from pennylane import numpy as np

from g_1_1_oracle_action_in_a_uniform_superposition import oracle_matrix
from g_1_2a_the_diffusion_operator import diffusion_matrix

n_bits = 4
dev = qp.device("default.qubit", wires=n_bits)


@qp.qnode(dev)
def two_difforacle_amp(combo):
    for wire in range(n_bits):
        qp.Hadamard(wires=wire)

    for _ in range(2):
        qp.QubitUnitary(oracle_matrix(combo), wires=range(n_bits))
        qp.QubitUnitary(diffusion_matrix(), wires=range(n_bits))

    return qp.state()


if __name__ == "__main__":
    print(np.real(two_difforacle_amp([0, 0, 0, 0])))
