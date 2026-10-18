# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp

from g_3_2_building_the_diffusion_operator import hadamard_transform


def oracle(combo):
    n_bits = len(combo)
    qp.MultiControlledX(wires=list(range(n_bits + 1)), control_values=combo)


def diffusion(n_bits):
    hadamard_transform(range(n_bits))
    qp.MultiControlledX(wires=list(range(n_bits + 1)), control_values=[0] * n_bits)
    hadamard_transform(range(n_bits))


def grover_iter(combo, num_steps):
    n_bits = len(combo)
    query_register = list(range(n_bits))
    aux = [n_bits]
    all_wires = query_register + aux
    dev = qp.device("default.qubit", wires=all_wires)

    @qp.qnode(dev)
    def inner_circuit():
        qp.PauliX(wires=aux)
        qp.Hadamard(wires=aux)
        hadamard_transform(query_register)

        for _ in range(num_steps):
            oracle(combo)
            diffusion(n_bits)

        return qp.probs(wires=query_register)

    return inner_circuit()


if __name__ == "__main__":
    print(grover_iter([0, 1, 1], 2))
