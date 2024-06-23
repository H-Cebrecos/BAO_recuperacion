from ACO import ACO
import tqdm
import random
from Common.fitness import evaluate_fitness
from Common.heuristic import *

def evaluate_variation_alpha_beta(tests: int, runs: int, alpha: float, beta: float, increment: float):
    print(f"doing {runs} runs with alpha={alpha} and beta={beta} with {tests} different seeds.\n")
    for i in range(tests):
        print(f"test {i + 1}:\n")
        random.seed(i)
        
        print("default")
        fitnesses = []
        for i in tqdm.tqdm(range(runs), desc="runs"):
            sol = ACO(n_ants=10, iterations=10, alpha=alpha, beta=beta, max_pieces=30, max_size=10, x_dim=20, y_dim=20, heuristic=heuristic1)
            fitnesses.append(evaluate_fitness(sol.board, sol.x_dim, sol.y_dim))
        average = sum(fitnesses) / len(fitnesses) if fitnesses else 0
        print("average fitness of the solution:",average)
        
        print(f"increase of {increment} in alpha")
        fitnesses = []
        for i in tqdm.tqdm(range(runs), desc="runs"):
            sol = ACO(n_ants=10, iterations=10, alpha=alpha+increment, beta=beta, max_pieces=30, max_size=10, x_dim=20, y_dim=20, heuristic=heuristic1)
            fitnesses.append(evaluate_fitness(sol.board, sol.x_dim, sol.y_dim))
        average = sum(fitnesses) / len(fitnesses) if fitnesses else 0
        print("average fitness of the solution:",average)

        print(f"decrease of {-increment} in alpha")
        fitnesses = []
        for i in tqdm.tqdm(range(runs), desc="runs"):
            sol = ACO(n_ants=10, iterations=10, alpha=alpha-increment, beta=beta, max_pieces=30, max_size=10, x_dim=20, y_dim=20, heuristic=heuristic1)
            fitnesses.append(evaluate_fitness(sol.board, sol.x_dim, sol.y_dim))
        average = sum(fitnesses) / len(fitnesses) if fitnesses else 0
        print("average fitness of the solution:",average)
        
        print(f"increase of {increment} in beta")
        fitnesses = []
        for i in tqdm.tqdm(range(runs), desc="runs"):
            sol = ACO(n_ants=10, iterations=10, alpha=alpha, beta=beta+increment, max_pieces=30, max_size=10, x_dim=20, y_dim=20, heuristic=heuristic1)
            fitnesses.append(evaluate_fitness(sol.board, sol.x_dim, sol.y_dim))
        average = sum(fitnesses) / len(fitnesses) if fitnesses else 0
        print("average fitness of the solution:",average)

        print(f"decrease of {-increment} in beta")
        fitnesses = []
        for i in tqdm.tqdm(range(runs), desc="runs"):
            sol = ACO(n_ants=10, iterations=10, alpha=alpha, beta=beta-increment, max_pieces=30, max_size=10, x_dim=20, y_dim=20, heuristic=heuristic1)
            fitnesses.append(evaluate_fitness(sol.board, sol.x_dim, sol.y_dim))
        average = sum(fitnesses) / len(fitnesses) if fitnesses else 0
        print("average fitness of the solution:",average)

        print(f"increase of {increment} in both")
        fitnesses = []
        for i in tqdm.tqdm(range(runs), desc="runs"):
            sol = ACO(n_ants=10, iterations=10, alpha=alpha+increment, beta=beta+increment, max_pieces=30, max_size=10, x_dim=20, y_dim=20, heuristic=heuristic1)
            fitnesses.append(evaluate_fitness(sol.board, sol.x_dim, sol.y_dim))
        average = sum(fitnesses) / len(fitnesses) if fitnesses else 0
        print("average fitness of the solution:",average)
        
        print(f"decrease of {increment} in both")
        fitnesses = []
        for i in tqdm.tqdm(range(runs), desc="runs"):
            sol = ACO(n_ants=10, iterations=10, alpha=alpha-increment, beta=beta-increment, max_pieces=30, max_size=10, x_dim=20, y_dim=20, heuristic=heuristic1)
            fitnesses.append(evaluate_fitness(sol.board, sol.x_dim, sol.y_dim))
        average = sum(fitnesses) / len(fitnesses) if fitnesses else 0
        print("average fitness of the solution:",average)

def evaluate_more_ants_or_iterations(tests: int, runs: int, ants: int, iterations: int):
    print(f"doing {runs} runs of {iterations} iterations with {ants} ants with {tests} different seeds.\n")
    for i in range(tests):
        print(f"test {i + 1}:\n")
        random.seed(i)
        
        print("default")
        fitnesses = []
        for i in tqdm.tqdm(range(runs), desc="runs"):
            sol = ACO(n_ants=ants, iterations=iterations, alpha=0.6, beta=0.5, max_pieces=30, max_size=10, x_dim=20, y_dim=20, heuristic=heuristic1)
            fitnesses.append(evaluate_fitness(sol.board, sol.x_dim, sol.y_dim))
        average = sum(fitnesses) / len(fitnesses) if fitnesses else 0
        print("average fitness of the solution:",average)
        
        print("double ants")
        fitnesses = []
        for i in tqdm.tqdm(range(runs), desc="runs"):
            sol = ACO(n_ants=ants*2, iterations=iterations, alpha=0.6, beta=0.5, max_pieces=30, max_size=10, x_dim=20, y_dim=20, heuristic=heuristic1)
            fitnesses.append(evaluate_fitness(sol.board, sol.x_dim, sol.y_dim))
        average = sum(fitnesses) / len(fitnesses) if fitnesses else 0
        print("average fitness of the solution:",average)

        print("double iterations")
        fitnesses = []
        for i in tqdm.tqdm(range(runs), desc="runs"):
            sol = ACO(n_ants=ants, iterations=iterations*2, alpha=0.6, beta=0.5, max_pieces=30, max_size=10, x_dim=20, y_dim=20, heuristic=heuristic1)
            fitnesses.append(evaluate_fitness(sol.board, sol.x_dim, sol.y_dim))
        average = sum(fitnesses) / len(fitnesses) if fitnesses else 0
        print("average fitness of the solution:",average)

#evaluate_more_ants_or_iterations(tests=3, runs=6, ants=10, iterations=10)ç
evaluate_variation_alpha_beta(tests=3, runs= 6, alpha=0.5, beta=0.5, increment=0.1)