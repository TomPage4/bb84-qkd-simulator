import random

def generate_key(qubit_count):

    qubit_key = []

    # Each qubit is a random bit encoded in a randomly chosen basis.
    # The basis is either rectilinear (+) or diagonal (x).
    for _ in range(qubit_count):
        basis = random.choice("+x")
        bit = random.randint(0, 1)

        qubit_key.append((bit, basis))

    return qubit_key

def measure_qubits(alice_qubits):

    bob_results = []

    for bit, alice_basis in alice_qubits:
        # Bob picks a basis at random without knowing which Alice used.
        bob_basis = random.choice("+x")

        if bob_basis == alice_basis:
            # Correct basis gives the original bit.
            measured_bit = bit
        else:
            # Wrong basis gives a random result, as in real quantum measurement.
            measured_bit = random.randint(0, 1)

        bob_results.append((measured_bit, bob_basis))

    return bob_results

def sift_key(alice_qubits, bob_results):

    alice_key = []
    bob_key = []

    for i in range(len(alice_qubits)):
        alice_bit, alice_basis = alice_qubits[i]
        bob_bit, bob_basis = bob_results[i]

        # Only keep bits where Alice and Bob used the same basis.
        # These are the only positions where Bob's measurement is guaranteed to match Alice's bit.
        if alice_basis == bob_basis:
            alice_key.append(alice_bit)
            bob_key.append(bob_bit)

    return alice_key, bob_key