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
    
# ------------------------------------------------------------------------------------------------

class Agent:
    """Represents an agent with an n-dimensional position and associated mutation step size."""
    def __init__(self, search_space_bounds, sigma_init, position=None):
        # If no initial position is provided, randomly initialize within each dimension's bounds.
        if position is None:
            self.position = np.array([np.random.uniform(low, high) for low, high in search_space_bounds])
        else:
            self.position = np.array(position)
        self.sigma = sigma_init  # Mutation step size for self-adaptation.
        self.fitness = self.evaluate_fitness()
    
    def evaluate_fitness(self):
        """Evaluates the agent's fitness using the Ackley function."""
        return ackley(self.position)
    
    def mutate(self, learning_rate, search_space_bounds, sigma_bound):
        """
        Performs mutation by adapting the step size and adding Gaussian noise to each dimension.
        Clipping ensures the mutated position remains within the provided bounds.
        """
        new_sigma = self.sigma * np.exp(learning_rate * np.random.normal())
        new_sigma = np.clip(new_sigma, sigma_bound, None)
        new_position = self.position + new_sigma * np.random.normal(size=self.position.shape)
        # Apply clipping per dimension using corresponding lower and upper bounds.
        new_position = np.array([np.clip(val, low, high) for val, (low, high) in zip(new_position, search_space_bounds)])
        mutated_agent = Agent(search_space_bounds, new_sigma, position=new_position)
        return mutated_agent

# ------------------------------------------------------------------------------------------------
