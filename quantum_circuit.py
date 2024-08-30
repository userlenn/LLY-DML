# quantum_circuit.py

import pennylane as qml
from pennylane import numpy as np

def create_quantum_circuit(params, n_qubits=3):
    "I defined this function to specifically make a quantum circuit with Hadamard and L-Gates."
    dev = qml.device('default.qubit', wires=n_qubits)

    @qml.qnode(dev)
    def circuit(params):
        for i in range(n_qubits):
            qml.Hadamard(wires=i)
            qml.RX(params[i], wires=i)
            # Example L-Gate (can be replaced with actual gate logic)
            qml.RZ(params[i] * 0.5, wires=i)
        return qml.expval(qml.PauliZ(0))

    return circuit
