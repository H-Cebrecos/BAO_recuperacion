
def evaluate_fitness(sol, x_dim, y_dim) -> float: 
    holes = sum(not cell for row in sol for cell in row)
    value = x_dim * y_dim
    value = value - holes
    return value