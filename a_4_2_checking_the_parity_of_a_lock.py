# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

from pennylane import numpy as np

from a_4_1_the_multi_solution_oracle import multisol_pair_circuit, n_bits


def parity_checker(combos):
    parity = 0
    x_tilde_strs = [np.binary_repr(n, n_bits - 1) for n in range(2 ** (n_bits - 1))]
    x_tildes = [[int(s) for s in x_tilde_str] for x_tilde_str in x_tilde_strs]
    for x_tilde in x_tildes:
        if np.isclose(multisol_pair_circuit(x_tilde, combos)[1], 1):
            parity = (parity + 1) % 2

    return parity


if __name__ == "__main__":
    combos = [[0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 0, 1]]
    print(f"parity = {parity_checker(combos)}")
