# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp

from g_3_1_building_the_oracle_with_multi_controlled_gates import aux, query_register


def hadamard_transform(my_wires):
    for wire in my_wires:
        qp.Hadamard(wires=wire)


def diffusion():
    hadamard_transform(query_register)
    qp.MultiControlledX(
        wires=query_register + aux, control_values=[0] * len(query_register)
    )
    hadamard_transform(query_register)


if __name__ == "__main__":
    print(qp.draw(diffusion)())
