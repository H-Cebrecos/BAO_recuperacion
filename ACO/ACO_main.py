import tqdm
import time

from Pheromone import Pheromone
from Solution import Solution

from Common import Piece as Piece



def ACO(n_ants, iterations, seed, alpha, beta, max_pieces: int, max_size: int, x_dim: int, y_dim: int):
    pheromones = Pheromone.initialize_pheromones(max_pieces)
    pieces = Piece.Piece.generate_random_pieces(max_pieces, max_size)
    mediaDeFitness = 0
    best_fitness = 0
    best_solution = []
    i = 0
    progress_bar = tqdm.tqdm(range(iterations), desc="iterations", leave=False)
    for i in progress_bar:
        Solution_list = []
        for j in range(n_ants):
            solution = Solution.construct_solution(pheromones, x_dim, y_dim, pieces, max_pieces, alpha, beta)
            Solution_list.append(solution)
            fitness = solution.evaluate_fitness()
            mediaDeFitness = fitness + mediaDeFitness
            if (fitness > best_fitness):
                best_solution = solution
                best_fitness = fitness
        #guardo valores historicos para graficas
        #bestFitnessEvolution.append(best_fitness)
        #mediaFitnessEvolution.append(mediaDeFitness/n_ants)
        #mediaDeFitness = 0
        #
        #for k in range(len(Pheromones)):
        #    pheromoneHistory.append(Pheromones[k].placeOrder)

        Pheromones = Pheromone.update_pheromones(pheromones, Solution_list, max_pieces, pieces)

        i = i + 1 
    progress_bar.close()
    return best_solution

def main():
    for i in tqdm.tqdm(range(100), desc="runs"):
        sol: Solution.Solution = ACO(10, 100, 12, 0.5, 0.5, 9, 4, 20, 40)
        #sol.printSol()
   
main()