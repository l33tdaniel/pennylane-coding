# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp

from a_2_1_the_matrix_form_of_the_oracle import oracle_matrix

n_bits = 4
dev = qp.device("default.qubit", wires=n_bits)


@qp.qnode(dev)
def hoh_circuit(combo):
    for wire in range(n_bits):
        qp.Hadamard(wires=wire)

    qp.QubitUnitary(oracle_matrix(combo), wires=range(n_bits))

    for wire in range(n_bits):
        qp.Hadamard(wires=wire)

    return qp.probs(wires=range(n_bits))


if __name__ == "__main__":
    print(hoh_circuit([0, 1, 1, 0]))
