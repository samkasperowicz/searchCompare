from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.finder.dijkstra import DijkstraFinder
from pathfinding.finder.bi_a_star import BiAStarFinder
from pathfinding.finder.ida_star import IDAStarFinder
from pathfinding.finder.best_first import BestFirst
from pathfinding.finder.breadth_first import BreadthFirstFinder
import time
import random

def generate_list(rows, cols, density_of_zeros):
    my_list = [
        [1 if random.random() > density_of_zeros else 0 for _ in range(cols)] 
        for _ in range(rows)
    ]
    my_list[0][0] = 1
    my_list[-1][-1] = 1
    return my_list

def create_grid(matrix):
    return Grid(matrix=matrix)

def find_path(grid, start, end, finder):
    start_node = grid.node(start[0], start[1])
    end_node = grid.node(end[0], end[1])
    
    start = time.time()

    path, _ = finder.find_path(start_node, end_node, grid)

    end = time.time()
    timeElapsed = end - start
    return path, timeElapsed

# Specify the size of the list and the density of zeros
rows = int(input("Enter grid size (will be NxN)"))
cols = rows
density_of_zeros = float(input("Enter density of zeros"))  # Adjust this value to control the density of zeros

# Generate the list
matrix = generate_list(rows, cols, density_of_zeros)

start_position = (0, 0)
end_position = (rows - 1, cols - 1)

# Best First
grid = create_grid(matrix)
best_first_finder = BestFirst(diagonal_movement=DiagonalMovement.always)
path_best_first, timeStat_best_finder = find_path(grid, start_position, end_position, best_first_finder)
print(f"Best first path: {len(path_best_first)}, time taken: {timeStat_best_finder}\n")

# A* Finder
grid = create_grid(matrix)
a_star_finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
path_a_star, timeStat_a_star = find_path(grid, start_position, end_position, a_star_finder)
print(f"A* algorithm path: {len(path_a_star)}, time taken: {timeStat_a_star}\n")

# Djikstra Finder
grid = create_grid(matrix)
djikstra_finder = DijkstraFinder(diagonal_movement=DiagonalMovement.always)
path_djikstra, timeStat_djikstra = find_path(grid, start_position, end_position, djikstra_finder)
print(f"Djikstra algorithm path: {len(path_djikstra)}, time taken: {timeStat_djikstra}\n")

# Bi-directional A*
grid = create_grid(matrix)
bidirec_a_star_finder = BiAStarFinder(diagonal_movement=DiagonalMovement.always)
path_bidirec_a_star, timeStat_bidirec_a_star = find_path(grid, start_position, end_position, bidirec_a_star_finder)
print(f"Bi-directional A* algorithm path: {len(path_bidirec_a_star)}, time taken: {timeStat_bidirec_a_star}\n")

# BFS
grid = create_grid(matrix)
breadth_finder = BreadthFirstFinder(diagonal_movement=DiagonalMovement.always)
path_breadth, timeStat_breadth = find_path(grid, start_position, end_position, breadth_finder)
print(f"BFS path: {len(path_breadth)}, time taken: {timeStat_breadth}\n")

# Iterative Deepening A*
grid = create_grid(matrix)
id_a_star_finder = IDAStarFinder(diagonal_movement=DiagonalMovement.always)
path_id_a_star, timeStat_id_a_star = find_path(grid, start_position, end_position, id_a_star_finder)
print(f"Iterative Deepening A* algorithm path: {len(path_id_a_star)}, time taken: {timeStat_id_a_star}\n")