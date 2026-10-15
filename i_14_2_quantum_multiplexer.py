# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp

dev = qp.device("default.qubit", wires=3)

state = [0, 1]


@qp.qnode(device=dev)
def apply_control_sequence(state):
    if state[0] == 1:
        qp.PauliX(wires=0)
    if state[1] == 1:
        qp.PauliX(wires=1)

    qp.PauliX(wires=2)
    qp.Hadamard(wires=2)

    # 01: X on the third qubit
    qp.PauliX(wires=0)
    qp.Toffoli(wires=[0, 1, 2])
    qp.PauliX(wires=0)

    # 10: Z = HXH on the third qubit
    qp.PauliX(wires=1)
    qp.Hadamard(wires=2)
    qp.Toffoli(wires=[0, 1, 2])
    qp.Hadamard(wires=2)
    qp.PauliX(wires=1)

    # 11: Y = S X S^dagger on the third qubit
    qp.adjoint(qp.S)(wires=2)
    qp.Toffoli(wires=[0, 1, 2])
    qp.S(wires=2)

    return qp.state()


if __name__ == "__main__":
    print(apply_control_sequence(state))
