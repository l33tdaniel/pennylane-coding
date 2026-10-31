# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp

from p_2_1_powers_of_u import U_power_2k

estimation_wires = [0, 1, 2]
target_wires = [3]


def apply_controlled_powers_of_U(unitary):
    num_estimation_wires = len(estimation_wires)

    for i, wire in enumerate(estimation_wires):
        k = num_estimation_wires - i - 1
        qp.ctrl(
            qp.QubitUnitary(U_power_2k(unitary, k), wires=target_wires), control=wire
        )


if __name__ == "__main__":
    U = qp.T.compute_matrix()
    print(qp.draw(apply_controlled_powers_of_U)(U))
