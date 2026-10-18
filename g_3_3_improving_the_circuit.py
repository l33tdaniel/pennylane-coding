# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp

from g_3_1_building_the_oracle_with_multi_controlled_gates import (
    aux,
    dev,
    oracle,
    query_register,
)
from g_3_2_building_the_diffusion_operator import diffusion, hadamard_transform


@qp.qnode(dev)
def grover_circuit(combo):
    hadamard_transform(query_register)
    qp.PauliX(wires=aux)
    qp.Hadamard(wires=aux)

    oracle(combo)
    diffusion()

    return qp.probs(wires=query_register)


if __name__ == "__main__":
    print(grover_circuit([0, 0, 0, 0, 0]))
