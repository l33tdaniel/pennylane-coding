# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane", "matplotlib"]
# ///

import pennylane as qp
from pennylane import numpy as np

dev = qp.device("default.qubit", wires=1)


@qp.qnode(dev)
def apply_rx(theta, state):
    if state == 1:
        qp.PauliX(wires=0)

    qp.RX(theta, wires=0)

    return qp.state()


def plotter(angles, output_states):
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    ax.plot(angles, np.real(output_states[:, 0]), label=r"Re$\langle 0|\psi\rangle$")
    ax.plot(angles, np.imag(output_states[:, 1]), label=r"Im$\langle 1|\psi\rangle$")
    ax.set_xlabel(r"$\theta$")
    ax.set_ylabel("amplitude")
    ax.set_title(r"$RX(\theta)|0\rangle$")
    ax.legend()
    return fig


if __name__ == "__main__":
    angles = np.linspace(0, 4 * np.pi, 200)
    output_states = np.array([apply_rx(t, 0) for t in angles])

    plot = plotter(angles, output_states)

    import matplotlib.pyplot as plt

    plt.show()
