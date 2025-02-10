"""
CISC 455: Evolution Strategy with One Mutation Step-Size Self-Adaptation
Author: Manny Cassar

Description:
This script implements an Evolution Strategy (ES) optimization algorithm 
to minimize the Ackley function using an object-oriented approach.

Two selection schemes are supported:
- "plus": (μ + λ) selection: parents and offspring are combined, and the best μ individuals are kept.
- "comma": (μ, λ) selection: only offspring are considered.

Additional checks are included to avoid pitfalls such as having too few offspring when using the "comma" strategy.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Global flag to control whether Ackley-related functions are active.
ACKLEY = True

if ACKLEY:
    # The Ackley function is a widely-used benchmark in optimization.
    def ackley(x, a=20, b=0.2, c=2 * np.pi):
        """Computes the Ackley function."""
        n = len(x)
        sum_sq = np.sum(x ** 2)
        sum_cos = np.sum(np.cos(c * x))
        term1 = -a * np.exp(-b * np.sqrt(sum_sq / n))
        term2 = -np.exp(sum_cos / n)
        return term1 + term2 + a + np.exp(1)
    
