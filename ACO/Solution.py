from  Common.Piece import Piece
from  Common.Choice import Choice
from Pheromone import Pheromone
import random

import numpy as np

#This class represents a complete
class Solution:
    def __init__(self, x_dim: int, y_dim: int, pieces: list, max_pieces: int):
        self.x_dim = x_dim
        self.y_dim = y_dim
        self.pieces = pieces
        #the repeated reference approach to initialization
        #provides a speedup of >300 (99.67% inprovement) over iteration for very large boards (tested with 3000x3000 board)
        self.board = [[False] * x_dim] * y_dim
        self.used_pieces = [False] * max_pieces
        self.pieces_order = [0] * max_pieces
        self.pieces_pos = [[[0,0]]* 2] * max_pieces


    def __get_candidates(self) -> list:
        Candidates = []
        for candidate in self.pieces:
            if not self.does_use_piece(candidate):
                choice = self.get_Choice(candidate)
                if choice.x_pos != -1:
                    Candidates.append(choice)               
        return Candidates
    
    
    
    
    
    
    #todo seed all random values.
    
    
    
    
    
    def __random_choice(Candidates, Probabilities):
        for i in range(len(Candidates)):
            if random.random() < Probabilities[i]: #good option for experimenting an using other choosing algos
                return Candidates[i]
        return False
    
    def construct_solution(Pheromones: list, x_dim: int, y_dim: int, pieces: list, max_pieces: int, alpha: float, beta: float):
        solution = Solution(x_dim, y_dim, pieces, max_pieces)
        Candidates = solution.__get_candidates() #candidates are always valid
        order = 0
        while (len(Candidates) > 0):
            Probabilities = Pheromone.calculate_probabilities(Candidates, Pheromones, order, alpha, beta, x_dim, y_dim)
            choice = Solution.__random_choice(Candidates, Probabilities)
            if choice != False:
                solution.place_Choice(choice, order)
                Candidates = solution.__get_candidates()
                order = order + 1
                
                return solution

    def does_Choice_fit(self, choice: Choice) -> bool:
        if choice.piece.x_dim + choice.x_pos > self.x_dim:
            return False
        if choice.piece.y_dim + choice.y_pos > self.y_dim:
            return False
        for i in range(choice.piece.x_dim):
            for j in range(choice.piece.y_dim):
                if self.board[choice.x_pos + i][choice.y_pos + j]:
                    return False
        return True
    
    def get_Choice (self, piece: Piece) -> Choice:
        for i in range(self.x_dim):  # Recorre todas las posiciones del espacio
            for j in range(self.y_dim):
                posible = Choice(piece, i, j)
                if self.does_Choice_fit(posible):
                    return Choice(piece, i, j)
        return Choice(piece, -1, -1)
                
    def place_Choice(self, choice: Choice, order: int):
        for i in range(choice.piece.x_dim):
            for j in range(choice.piece.y_dim):
                self.board[choice.x_pos + i][choice.y_pos + j] = True
        self.used_pieces[self.pieces.index(choice.piece)] = True
        self.pieces_order[self.pieces.index(choice.piece)] = order
        self.pieces_pos[self.pieces.index(choice.piece)] = [[choice.x_pos,choice.y_pos],[choice.x_pos + choice.piece.x_dim-1,choice.y_pos + choice.piece.y_dim-1]]

    def does_use_piece(self, piece: Piece):
        return self.used_pieces[self.pieces.index(piece)]
    
    def get_piece_order(self, piece: Piece):
        return self.pieces_order[self.pieces.index(piece)]
    
    def piece_in_pos(self, x, y):
        i = 0
        for piece in self.pieces_pos:
            if x>= piece[0][0] and x <= piece[1][0]:
                if y>= piece[0][1] and y <= piece[1][1]:
                    return i
            i = i + 1
        return -1

   

    
    def huecos (self) -> list:
        return []
    #    board_copy = copy.deepcopy(self.board)
    #    array = []
    #    for i in range(self.x_dim):
    #        for j in range(self.y_dim):
    #            if board_copy[i][j] == 0:
    #                board_copy[i][j] = 1
    #                array.append(Solution.__explore_adyacent(board_copy, i, j))
    #    return array

    def evaluate_fitness(self) -> float: 
        espacios = self.huecos()
        value = 100
        value = value - len(espacios) * 5 #penalizar numero de huecos
        for hueco in espacios:
            value = value - (1/hueco) * 3
        return value
    
    def printSol (self):
        board = np.array(self.board, dtype=int)
        
        print("ocupancy:\n")
        print(board)
        print('\n\n')
        print("pieces:\n")
        for y in range (self.y_dim):
            #print('|', end='')  
            for x in range (self.x_dim):
                if self.piece_in_pos(x, y) != -1:
                    board[x][y] = self.piece_in_pos(x, y) + 1#print(' ',"{:03d}".format(self.piece_in_pos(j, i)), end='')
                else:
                    board[x][y] = 0
                    #print("  ·  ", end= '')
            #print('|')    

        i = 0
        print(board)
        
        
        
        for piece in self.pieces:
            print(i + 1, piece.x_dim, piece.y_dim)
            i = i + 1