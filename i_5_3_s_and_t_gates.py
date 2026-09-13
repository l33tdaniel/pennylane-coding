# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp

dev = qp.device("default.qubit", wires=1)


@qp.qnode(dev)
def many_rotations():
    qp.Hadamard(wires=0)
    qp.S(wires=0)
    qp.adjoint(qp.T)(wires=0)
    qp.RZ(0.3, wires=0)
    qp.adjoint(qp.S)(wires=0)

    return qp.state()


if __name__ == "__main__":
    print(many_rotations())
