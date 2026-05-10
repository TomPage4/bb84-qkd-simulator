# BB84 Quantum Key Distribution Simulation

A Python simulation of the BB84 Quantum Key Distribution (QKD), built while preparing for a research internship in accessible quantum computing technologies. The goal was to get hands on with the core ideas of quantum cryptography by implementing them from scratch, encoding qubits, simulating eavesdropping, measuring error rates, and using the resulting key to encrypt and decrypt a real message.

## What is BB84?

BB84 lets two parties, Alice and Bob, establish a shared secret key using quantum mechanics. Its security comes from a law of physics: you cannot measure a quantum system without disturbing it. Any eavesdropper on the channel will introduce detectable errors, and the protocol will abort before a compromised key is ever used.

## How the simulation works

The simulation runs in two phases.

### Phase 1: Quantum key generation

Alice generates random qubits, each encoded in a randomly chosen basis (rectilinear `+` or diagonal `x`). In the real world these would be photons sent down a fibre optic cable. The qubits travel through the quantum channel, where noise and eavesdropping can be toggled independently. If Eve is active, she intercepts each qubit, measures it in a randomly chosen basis, and re sends it, simulating an intercept and re send attack. Because she does not know Alice's basis, she disturbs the qubits roughly half the time.

Bob measures each qubit in his own randomly chosen basis. Alice and Bob then publicly compare which basis they each used and discard any mismatched qubits. What remains is the sifted key. The Quantum Bit Error Rate (QBER) is calculated from this, a channel with noise and no Eve sits close to 0%, with Eve, it is pushed around 25%. If it exceeds 5%, the protocol aborts.

### Phase 2: Classical message transmission

Alice encrypts her message using the shared key with XOR encryption. The ciphertext is sent over a normal channel and Bob decrypts it using his copy of the key.

## Configuration

At the top of `main.py`:

```python
# toggle Eve's eavesdropping on or off
EVE = True
# toggle channel noise on or off
NOISE = True
# number of qubits Alice sends
KEY_QUBIT_COUNT = 1024
```

Increasing `KEY_QUBIT_COUNT` gives a longer sifted key, which allows longer messages to be fully encrypted.

## Plots

Three plots are saved to the `plots/` directory after each run.

**qber**: Shows the overall bit error rate against the 5% abort threshold.

**basis_agreement**: Shows how many qubits were kept after sifting versus discarded due to basis mismatch.

**key_errors**: Shows how many bits in the final sifted key agree between Alice and Bob and how many differ.

## Dependencies

```
matplotlib
```

Install with:

```
pip install matplotlib
```

## Running the simulation

```
python main.py
```

Alice will be prompted to enter a message, then the results will print to the terminal, and save the three plots to the `plots/` directory.