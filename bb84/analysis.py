import matplotlib.pyplot as plt

def calculate_qber(alice_key, bob_key):

    mismatch = 0

    # Count positions where Alice and Bob's sifted key bits differ.
    for i in range(len(alice_key)):
        if alice_key[i] != bob_key[i]:
            mismatch += 1
    
    return mismatch / len(alice_key)

def plot_qber(qber):
    plt.figure()
    plt.bar(["QBER"], [qber * 100], color="steelblue")
    plt.axhline(5, color="red", linestyle="--", label="Threshold (5%)")
    plt.ylim(0, 100)
    plt.ylabel("Error rate (%)")
    plt.title("Quantum Bit Error Rate")
    plt.legend()
    plt.savefig("plots/qber.png") 
 
def plot_basis_agreement(alice_qubits, bob_results):
    matched = 0
    for i in range(len(alice_qubits)):
        if alice_qubits[i][1] == bob_results[i][1]:
            matched += 1
    discarded = len(alice_qubits) - matched
    plt.figure()
    plt.bar(["Matched", "Discarded"], [matched, discarded], color="steelblue")
    plt.ylabel("Number of qubits")
    plt.title("Basis Agreement After Sifting")
    plt.savefig("plots/basis_agreement.png")

def plot_key_errors(alice_key, bob_key):
    correct = 0
    errors = 0
    for i in range(len(alice_key)):
        if alice_key[i] == bob_key[i]:
            correct += 1
        else:
            errors += 1
    plt.figure()
    plt.bar(["Correct", "Errors"], [correct, errors], color="steelblue")
    plt.ylabel("Number of bits")
    plt.title("Final Key Bit Comparison")
    plt.savefig("plots/key_errors.png")
