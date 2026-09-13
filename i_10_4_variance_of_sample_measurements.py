# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane", "matplotlib"]
# ///

import pennylane as qp
from pennylane import numpy as np


def variance_experiment(n_shots):
    n_trials = 100

    dev = qp.device("default.qubit", wires=1, shots=n_shots)

    @qp.qnode(dev)
    def circuit():
        qp.Hadamard(wires=0)
        return qp.expval(qp.PauliZ(wires=0))

    results = np.array([circuit() for _ in range(n_trials)])

    return np.var(results)


def variance_scaling(n_shots):
    estimated_variance = 0

    estimated_variance = 1 / n_shots

    return estimated_variance


def plotter(shot_vals, results_experiment, results_scaling):
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    ax.plot(shot_vals, results_experiment, "o-", label="experiment")
    ax.plot(shot_vals, results_scaling, "--", label="1 / n_shots")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("number of shots")
    ax.set_ylabel("variance in expectation value")
    ax.legend()
    return fig


if __name__ == "__main__":
    shot_vals = [10, 20, 40, 100, 200, 400, 1000, 2000, 4000]

    results_experiment = [variance_experiment(shots) for shots in shot_vals]
    results_scaling = [variance_scaling(shots) for shots in shot_vals]
    plot = plotter(shot_vals, results_experiment, results_scaling)

    import matplotlib.pyplot as plt

    plt.show()
