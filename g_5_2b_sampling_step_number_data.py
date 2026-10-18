# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

from pennylane import numpy as np

from g_4_1b_optimal_number_of_iterations import local_max_arg
from g_5_2a_optimal_steps_for_many_solutions import grover_iter_multi, n_bits

if __name__ == "__main__":
    m_list = range(3)
    opt_steps = []

    for m_bits in m_list:
        combos = [[int(s) for s in np.binary_repr(j, n_bits)] for j in range(2**m_bits)]
        step_list = range(1, 10)

        indices = [np.ravel_multi_index(combo, [2] * n_bits) for combo in combos]
        probs = [
            np.sum(grover_iter_multi(combos, steps)[indices]) for steps in step_list
        ]
        opt_steps.append(local_max_arg(probs))

    print(
        "The optimal number of Grover steps for the number of solutions in",
        [1, 2, 4],
        "is",
        opt_steps,
        ".",
    )
