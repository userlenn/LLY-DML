# quantum_optimizer.py

import numpy as np
import pennylane as qml
from pennylane.optimize import AdamOptimizer

class QuantumOptimizer:
    def __init__(self, stepsize=0.01):
        self.optimizer = AdamOptimizer(stepsize=stepsize)

    def optimize(self, cost_fn, initial_params, steps=100):
        params = initial_params
        for i in range(steps):
            params = self.optimizer.step(cost_fn, params)
            if i % 10 == 0:
                print(f"Step {i}: Cost = {cost_fn(params)}")
        return params
