import random

def channel_noise(qubits):
    
    noised_qubits = []

    for bit, basis in qubits:
        # Each qubit has a 2% chance of being flipped in transit.
        # This simulates real world noise in the quantum channel (e.g. heat, vibrations).
        if random.random() < 0.02:
            noised_qubits.append((int(not bit), basis))
        else:
            noised_qubits.append((bit, basis))

    return noised_qubits