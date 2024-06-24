import Common.Choice as Choice

#This heuristic returns the relative size of a piece, favouring larger pieces.
def heuristic1(choice: Choice, x_dim: int, y_dim: int) -> float:
    size = choice.piece.x_dim * choice.piece.y_dim
    return size / (x_dim * y_dim)