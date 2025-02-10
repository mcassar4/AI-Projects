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
