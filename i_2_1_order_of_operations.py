# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp

dev = qp.device("default.qubit", wires=3)


def my_circuit(theta, phi):
    qp.CNOT(wires=[0, 1])
    qp.RX(theta, wires=2)
    qp.Hadamard(wires=0)
    qp.CNOT(wires=[2, 0])
    qp.RY(phi, wires=1)

    return qp.probs(wires=[0, 1, 2])


if __name__ == "__main__":
    my_qnode = qp.QNode(my_circuit, dev)
    print(my_qnode(0.1, 0.2))
    print(qp.draw(my_qnode)(0.1, 0.2))
