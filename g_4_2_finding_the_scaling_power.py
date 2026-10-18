# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane", "matplotlib"]
# ///

from pennylane import numpy as np

grad = 0.5
intercept = -0.47


def plotter(n_list, opt_steps, grad, intercept):
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    ax.plot(n_list, np.log2(opt_steps), "o", label="data")
    ax.plot(n_list, grad * n_list + intercept, "--", label="line of best fit")
    ax.set_xlabel("number of qubits $n$")
    ax.set_ylabel(r"$\log_2 S$")
    ax.legend()
    return fig


if __name__ == "__main__":
    n_list = np.array([3, 4, 5, 6, 7])
    opt_steps = np.array([2, 3, 4, 6, 8])

    fit_grad, fit_intercept = np.polyfit(n_list, np.log2(opt_steps), 1)
    print(f"least-squares fit: grad = {fit_grad:.3f}, intercept = {fit_intercept:.3f}")
    print(f"C = 2**intercept = {2**intercept:.3f}")

    plot = plotter(n_list, opt_steps, grad, intercept)

    import matplotlib.pyplot as plt

    plt.show()
