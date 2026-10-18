# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp

from g_3_2_building_the_diffusion_operator import hadamard_transform
from g_4_1a_make_a_guess import diffusion
from g_5_1_preparing_a_multi_solution_oracle import oracle_multi

n_bits = 5
query_register = list(range(n_bits))
aux = [n_bits]
all_wires = query_register + aux
dev = qp.device("default.qubit", wires=all_wires, shots=None)


def grover_iter_multi(combos, num_steps):
    @qp.qnode(dev)
    def inner_circuit():
        qp.PauliX(wires=n_bits)
        qp.Hadamard(wires=n_bits)
        hadamard_transform(query_register)

        for _ in range(num_steps):
            oracle_multi(combos)
            diffusion(n_bits)
        return qp.probs(wires=query_register)

    return inner_circuit()


if __name__ == "__main__":
    combos = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 1]]
    probs = grover_iter_multi(combos, 3)
    print(f"P(solution) after 3 steps = {probs[0] + probs[1]:.4f}")
