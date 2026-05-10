import random

def eavesdropper(qubits):

    eve_results = []

    for bit, basis in qubits:
        # Eve picks a basis at random, she has no way of knowing which Alice used.
        eve_basis = random.choice("+x")

        if eve_basis == basis:
            # Correct basis gives the original bit, Eve learns the value without disturbing it.
            measured_bit = bit
        else:
            # Wrong basis forces a random result and corrupts the qubit.
            measured_bit = random.randint(0, 1)

        eve_results.append((measured_bit, eve_basis))

    return eve_results