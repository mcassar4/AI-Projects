# Evolutionary Optimization: Minimizing the Ackley Function

## Introduction

This project implements an Evolutionary Strategy (ES) algorithm to minimize the Ackley function, a well-known multimodal optimization problem. Designed for educational purposes, this project serves as a foundational example of evolutionary algorithms for an Evolutionary Optimization class.

The project emphasizes modularity and extensibility, allowing me to experiment with application in other domains.

---

## Features

- **Ackley Function Implementation**: A challenging multimodal function to test optimization algorithms.
- **Agent Class**: Represents individual solutions with mutation capabilities.
- **Population Management**: Handles offspring generation, mutation, and selection.
- **Selection Strategies**:
  - **(μ + λ)**: Combines parents and offspring to retain the best solutions across generations.
  - **(μ, λ)**: Considers only offspring, encouraging exploration.
- **Visualization**: 3D plotting of the Ackley function and trajectory of the best solution.
- **Configurable Parameters**:
  - Population size
  - Number of offspring
  - Mutation step size
  - Selection strategy

---

## Project Functions

- **ackley**: Defines the Ackley function and visualization tools.
- **agent**: Implements the `Agent` class for individual solutions.
- **population**: Manages the population of agents and selection mechanisms.
- **evolution_strategy**: Coordinates the optimization process.
- **main**: Entry point for running the optimization and visualization.

---

## How to Use

### Prerequisites

- Python 3.x
- `matplotlib` for visualization
- `numpy` for numerical operations

### Running the Optimization

1. Create a pipenv and install the dependancies:
   ```bash
   pipenv install
   ```
2. Run the main script:
   ```bash
   pipenv run python3 ESAckley.py
   ```

### Configuration

Modify the following parameters in `ESAckley.py` to experiment with the algorithm:
- `population_size`: Number of agents in the population.
- `num_offspring`: Number of offspring generated per generation.
- `sigma_init`: Initial mutation step size.
- `selection_strategy`: Choose between `"plus"` or `"comma"` selection strategies.

## Educational Value

This project demonstrates the following concepts:
- The role of adpative mutation and different selection strategies in evolutionary algorithms.
- The effects of different selection strategies on convergence.
- The importance of visualization in understanding optimization trajectories.
