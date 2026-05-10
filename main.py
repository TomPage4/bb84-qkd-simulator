import bb84.key
import bb84.quantum_channel
import bb84.eve
import bb84.analysis
import bb84.message

EVE = False
NOISE = True
KEY_QUBIT_COUNT = 1024

def main():

    # Alice generates random qubits to send to Bob over the quantum channel.
    alice_qubits = bb84.key.generate_key(KEY_QUBIT_COUNT)
    channel_qubits = alice_qubits.copy()

    # Simulate real world noise (e.g. heat, vibrations) and potential eavesdropping on the channel.
    if NOISE:
        channel_qubits = bb84.quantum_channel.channel_noise(channel_qubits)

    if EVE:
        channel_qubits = bb84.eve.eavesdropper(channel_qubits)

    # Bob measures the qubits he receives, each in a randomly chosen basis.
    bob_results = bb84.key.measure_qubits(channel_qubits)

    # Alice and Bob publicly compare which basis they each used per qubit.
    # Bits where they chose different bases are discarded, leaving the sifted key.
    alice_key, bob_key = bb84.key.sift_key(alice_qubits, bob_results)

    # Calculate the quantum bit error rate to check the channel for eavesdropping.
    # A QBER above 5% suggests the channel has been compromised.
    qber = bb84.analysis.calculate_qber(alice_key, bob_key)
    print(f"Sifted key length: {len(alice_key)} bits")
    print(f"QBER: {qber * 100:.1f}%")

    if qber > 0.05:
        print("QBER exceeds 5%, eavesdropping likely detected. Aborting.")
        bb84.analysis.plot_qber(qber)
        return

    print("Key exchange successful, channel appears secure.")

    bb84.analysis.plot_qber(qber)
    bb84.analysis.plot_basis_agreement(alice_qubits, bob_results)
    bb84.analysis.plot_key_errors(alice_key, bob_key)

    # Alice enters the message she wants to send to Bob.
    # The key must be at least as long as the message in bits.
    message_bits = bb84.message.input_message()
    chars_possible = len(alice_key) // 8
    chars_needed = len(message_bits) // 8

    if chars_needed > chars_possible:
        print(f"Key is too short for the full message. Only the first {chars_possible} of {chars_needed} characters will be sent.")

    # Alice encrypts her message using the shared key and sends it over a normal channel.
    ciphertext, bits_used = bb84.message.encrypt_message(message_bits, alice_key)

    # Bob decrypts the ciphertext using his copy of the key.
    recovered = bb84.message.decrypt_message(ciphertext, bob_key[:bits_used])

    original_preview = ''.join(
        chr(int(message_bits[i:i+8], 2)) for i in range(0, bits_used, 8)
    )

    print(f"Alice sent: \"{original_preview}\"")
    print(f"Bob received: \"{recovered}\"")

    if original_preview == recovered:
        print("Bob recovered the message correctly.")
    else:
        mismatches = sum(1 for a, b in zip(original_preview, recovered) if a != b)
        print(f"{mismatches} of {len(original_preview)} characters were corrupted by noise or eavesdropping.")

main()