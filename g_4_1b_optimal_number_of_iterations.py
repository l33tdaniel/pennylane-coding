# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

from g_4_1a_make_a_guess import grover_iter


def local_max_arg(num_list):
    for j in range(1, len(num_list)):
        if num_list[j] < num_list[j - 1]:
            return j
    return len(num_list)


if __name__ == "__main__":
    n_list = range(3, 7)
    opt_steps = []

    for n_bits in n_list:
        combo = [0] * n_bits  # A simple combination
        step_list = range(1, 10)  # Try out some large number of steps

        probs = [grover_iter(combo, steps)[0] for steps in step_list]
        opt_steps.append(local_max_arg(probs))

    print(
        "The optimal number of Grover steps for qubits in",
        [3, 4, 5, 6],
        "is",
        opt_steps,
        ".",
    )
