import tqdm

from typing import Callable
from Pheromone import Pheromone
from Solution import Solution

from Common.Piece import Piece
from Common.Choice import Choice
from Common.heuristic import *


import numpy as np

def ACO(n_ants, iterations, seed, alpha, beta, max_pieces: int, max_size: int, x_dim: int, y_dim: int, heuristic: Callable):
    
    pheromones = Pheromone.initialize_pheromones(max_pieces)
    
    
    
    pieces = Piece.generate_random_pieces(max_pieces, max_size)
    fitness_average = 0
    best_fitness = 0
    best_solution = []
    i = 0
    
    progress_bar = tqdm.tqdm(range(iterations), desc="iterations", leave=False)
    for i in progress_bar:
        Solution_list = []
        
        progress_ants = tqdm.tqdm(range(n_ants), desc="ants", leave=False)
        for j in progress_ants:
            solution = Solution.construct_solution(pheromones, x_dim, y_dim, pieces, max_pieces, alpha, beta, heuristic)
            Solution_list.append(solution)
            fitness = solution.evaluate_fitness()
            fitness_average = fitness + fitness_average
            if (fitness > best_fitness):
                best_solution = solution
                best_fitness = fitness
        #guardo valores historicos para graficas
        #bestFitnessEvolution.append(best_fitness)
        #mediaFitnessEvolution.append(fitness_average/n_ants)
        #fitness_average = 0
        #
        #for k in range(len(Pheromones)):
        #    pheromoneHistory.append(Pheromones[k].placeOrder)

        #30% del tiempo
        Pheromones = Pheromone.update_pheromones(pheromones, Solution_list, max_pieces, pieces)
        
        i = i + 1 
    progress_bar.close()

    return best_solution

def main():
    #for i in tqdm.tqdm(range(100), desc="runs"):
        sol: Solution.Solution = ACO(n_ants=1, iterations=1, seed=12, alpha=0.6, beta=0.5, max_pieces=7, max_size=10, x_dim=30, y_dim=20, heuristic=heuristic1)
        sol.printSol()
        #pieces = Piece.generate_random_pieces(6, 3)
        #solution = Solution(5, 10, pieces, 6)
        #i = 0
        #for piece in pieces:
        #    i += 1    
        #    print(np.array([[i]*piece.x_dim] * piece.y_dim) ,'\n')
        #solution.place_Choice(Choice.Choice(pieces[3],0,2), 0)
        #solution.printSol()
main()