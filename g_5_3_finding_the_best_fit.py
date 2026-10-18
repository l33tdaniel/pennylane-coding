# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane", "matplotlib"]
# ///

from pennylane import numpy as np

grad = -0.5
intercept = 2.03


def plotter(m_list, opt_steps, grad, intercept):
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    ax.plot(m_list, np.log2(opt_steps), "o", label="data")
    ax.plot(m_list, grad * m_list + intercept, "--", label="line of best fit")
    ax.set_xlabel(r"$m = \log_2 M$")
    ax.set_ylabel(r"$\log_2 S$")
    ax.legend()
    return fig


if __name__ == "__main__":
    m_list = np.array([0, 1, 2])
    opt_steps = np.array([4, 3, 2])

    fit_grad, fit_intercept = np.polyfit(m_list, np.log2(opt_steps), 1)
    print(f"least-squares fit: grad = {fit_grad:.3f}, intercept = {fit_intercept:.3f}")
    print(f"log2(pi/4 * sqrt(2**5)) = {np.log2(np.pi / 4 * np.sqrt(2**5)):.3f}")

    plot = plotter(m_list, opt_steps, grad, intercept)

    import matplotlib.pyplot as plt

    plt.show()
