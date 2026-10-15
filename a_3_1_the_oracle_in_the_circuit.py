# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp

from a_2_1_the_matrix_form_of_the_oracle import oracle_matrix

n_bits = 4
dev = qp.device("default.qubit", wires=n_bits)


@qp.qnode(dev)
def pair_circuit(x_tilde, combo):
    for i in range(n_bits - 1):
        if x_tilde[i] == 1:
            qp.PauliX(wires=i)

    qp.Hadamard(wires=n_bits - 1)
    qp.QubitUnitary(oracle_matrix(combo), wires=range(n_bits))
    qp.Hadamard(wires=n_bits - 1)

    return qp.probs(wires=n_bits - 1)


if __name__ == "__main__":
    print(pair_circuit([0, 1, 1], [0, 1, 1, 0]))
    print(pair_circuit([0, 1, 0], [0, 1, 1, 0]))
