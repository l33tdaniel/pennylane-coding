# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane", "matplotlib"]
# ///

import pennylane as qp
from pennylane import numpy as np

dev = qp.device("default.qubit", wires=2)


@qp.qnode(dev)
def circuit_1(theta):
    qp.RX(theta, wires=0)
    qp.RY(2 * theta, wires=1)

    return qp.expval(qp.PauliZ(0)), qp.expval(qp.PauliZ(1))


@qp.qnode(dev)
def circuit_2(theta):
    qp.RX(theta, wires=0)
    qp.RY(2 * theta, wires=1)

    return qp.expval(qp.PauliZ(0) @ qp.PauliZ(1))


def zi_iz_combination(ZI_results, IZ_results):
    combined_results = np.zeros(len(ZI_results))

    combined_results = ZI_results * IZ_results

    return combined_results


def plotter(theta, ZI_results, IZ_results, ZZ_results, combined_results):
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    ax.plot(theta, ZI_results, label=r"$\langle Z I \rangle$")
    ax.plot(theta, IZ_results, label=r"$\langle I Z \rangle$")
    ax.plot(theta, ZZ_results, lw=4, alpha=0.4, label=r"$\langle Z Z \rangle$")
    ax.plot(
        theta, combined_results, "--", label=r"$\langle ZI\rangle\langle IZ\rangle$"
    )
    ax.set_xlabel(r"$\theta$")
    ax.set_ylabel("expectation value")
    ax.legend()
    return fig


if __name__ == "__main__":
    theta = np.linspace(0, 2 * np.pi, 100)

    circuit_1_results = np.array([circuit_1(t) for t in theta])

    ZI_results = circuit_1_results[:, 0]
    IZ_results = circuit_1_results[:, 1]
    combined_results = zi_iz_combination(ZI_results, IZ_results)

    ZZ_results = np.array([circuit_2(t) for t in theta])

    plot = plotter(theta, ZI_results, IZ_results, ZZ_results, combined_results)

    import matplotlib.pyplot as plt

    plt.show()
