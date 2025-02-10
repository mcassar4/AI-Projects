# Evolutionary Optimization: Minimizing the Ackley Function

## Introduction

This project implements an Evolutionary Strategy (ES) algorithm to minimize the Ackley function, a well-known multimodal optimization problem. Designed for educational purposes, this project serves as a foundational example of evolutionary algorithms for an Evolutionary Optimization class.

The project emphasizes modularity and extensibility, allowing students and researchers to experiment with various benchmark functions and optimization parameters.

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

## Project Structure

- **ackley.py**: Defines the Ackley function and visualization tools.
- **agent.py**: Implements the `Agent` class for individual solutions.
- **population.py**: Manages the population of agents and selection mechanisms.
- **evolution_strategy.py**: Coordinates the optimization process.
- **main.py**: Entry point for running the optimization and visualization.

---

## How to Use

### Prerequisites

- Python 3.x
- `matplotlib` for visualization
- `numpy` for numerical operations

### Running the Optimization

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/evolutionary-optimization.git
   cd evolutionary-optimization
   ```

2. Install required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the main script:
   ```bash
   python main.py
   ```

### Configuration

Modify the following parameters in `main.py` to experiment with the algorithm:
- `population_size`: Number of agents in the population.
- `num_offspring`: Number of offspring generated per generation.
- `sigma_init`: Initial mutation step size.
- `selection_strategy`: Choose between `"plus"` or `"comma"` selection strategies.

---

## Video Visualization

Watch a 3D visualization of the optimization process:

<iframe src="https://www.youtube.com/embed/example_video_id" frameborder="0" allowfullscreen></iframe>

---

## Educational Value

This project demonstrates the following concepts:
- The role of mutation and selection in evolutionary algorithms.
- The effects of different selection strategies on convergence.
- The importance of visualization in understanding optimization trajectories.

---

## Contribution

Feel free to fork the repository and submit pull requests for:
- Additional benchmark functions.
- Alternative evolutionary algorithms.
- Improved visualizations.

---

## License

This project is licensed under the MIT License.

