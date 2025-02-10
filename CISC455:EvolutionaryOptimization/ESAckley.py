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

class Population:
    """Manages a group of agents and implements offspring generation and selection strategies."""
    
    def __init__(self, population_size, search_space_bounds, sigma_init):
        # Initialize the agent population.
        self.agents = [Agent(search_space_bounds, sigma_init) for _ in range(population_size)]
        self.search_space_bounds = search_space_bounds
        self.sigma_init = sigma_init

    def generate_offspring(self, num_offspring, learning_rate, sigma_bound):
        """Generates offspring by mutating randomly chosen parent agents."""
        offspring = []
        for _ in range(num_offspring):
            parent = np.random.choice(self.agents)  # Random parent selection.
            child = parent.mutate(learning_rate, self.search_space_bounds, sigma_bound)
            offspring.append(child)
        return offspring

    def select_survivors(self, offspring, population_size, selection_strategy):
        """
        Select the next generation based on the given selection strategy.
        
        "plus" (μ + λ): Combines current agents with offspring, sorts by fitness, then selects the top individuals.
        "comma" (μ, λ): Uses only offspring (requires offspring count >= population size).
        """
        if selection_strategy.lower() in ["plus", "+"]:
            combined = self.agents + offspring
            ordered = sorted(combined, key=lambda agent: agent.fitness)
            self.agents = ordered[:population_size]
        elif selection_strategy.lower() in ["comma", ","]:
            if len(offspring) < population_size:
                raise ValueError("For comma selection, the number of offspring must be at least the population size.")
            ordered_offspring = sorted(offspring, key=lambda agent: agent.fitness)
            self.agents = ordered_offspring[:population_size]
        else:
            raise ValueError(f"Unknown selection strategy: {selection_strategy}. Please use 'plus' or 'comma'.")

    def get_best_agent(self):
        """Returns the agent with the best (lowest) fitness and its fitness value."""
        best_agent = min(self.agents, key=lambda agent: agent.fitness)
        return best_agent, best_agent.fitness

# ------------------------------------------------------------------------------------------------
# EvolutionStrategy encapsulates the overall optimization process.
class EvolutionStrategy:
    """Implements the evolution strategy algorithm and controls the optimization loop."""
    
    def __init__(self,
                 agent_num_genes,          # Number of dimensions for each agent.
                 search_space_bounds,      # Bounds for each dimension.
                 population_size=4,
                 num_offspring=8,         # Number of offspring to generate.
                 sigma_init=1,
                 sigma_bound=0.01,
                 max_evals=250,
                 selection_strategy="plus" # Selection method: "plus" or "comma".
                 ):
        # Ensure that the number of dimensions matches the number of provided bounds.
        assert agent_num_genes == len(search_space_bounds), "Dimension mismatch between agent_num_genes and search_space_bounds."
        
        # For comma selection, ensure there are enough offspring.
        if selection_strategy.lower() in ["comma", ","] and num_offspring < population_size:
            raise ValueError("For comma selection, the number of offspring must be at least the population size.")

        # Set initial parameters.
        self.agent_num_genes = agent_num_genes
        self.population_size = population_size
        self.num_offspring = num_offspring
        self.sigma_init = sigma_init
        self.search_space_bounds = search_space_bounds
        self.sigma_bound = sigma_bound
        self.max_evals = max_evals
        self.selection_strategy = selection_strategy
        # Initialize the population of agents.
        self.population = Population(population_size, search_space_bounds, sigma_init)
        self.learning_rate = 1 / np.sqrt(agent_num_genes)  # Adaptation rate for mutation step-size.
        if ACKLEY:
            self.trajectory = []  # Stores the trajectory of the best solutions.
