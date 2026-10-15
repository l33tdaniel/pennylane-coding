# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

from pennylane import numpy as np

from a_6_1_the_hadamard_transform_for_multiple_solutions import (
    multisol_hoh_circuit,
    n_bits,
)


def multisol_combo(n_bits, how_many):
    sol_nums = np.random.choice(2**n_bits, size=how_many, replace=False)
    return [[int(s) for s in np.binary_repr(n, n_bits)] for n in sol_nums]


def deutsch_jozsa(promise_var):
    if promise_var == 0:
        how_many = 2 ** (n_bits - 1)
    else:
        how_many = np.random.choice([0, 2**n_bits])
    combos = multisol_combo(n_bits, how_many)

    probs = multisol_hoh_circuit(combos)
    if np.isclose(probs[0], 1):
        return 1
    return 0


if __name__ == "__main__":
    for promise_var in [0, 1, 0, 1]:
        print(f"promise_var = {promise_var}, guess = {deutsch_jozsa(promise_var)}")
