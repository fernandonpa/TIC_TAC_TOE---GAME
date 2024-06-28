import math
import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countX = 0
    countO = 0
    for row in board:
        for cell in row:
            if cell == X:
                countX += 1
            if cell == O:
                countO += 1
    if countX > countO:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                actions.append((row, col))
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    tempCopy = copy.deepcopy(board)
    x, y = action
    if tempCopy[x][y] is not EMPTY:
        raise Exception("Not a valid action")
    else:
        tempCopy[x][y] = player(board)
    return tempCopy

def checkRow(board, player):
    """
    Check the row values
    """
    for row in board:
        if row == [player, player, player]:
            return True
    return False

def checkCol(board, player):
    """
    Check the column values
    """
    for col in range(len(board[0])):
        if (board[0][col], board[1][col], board[2][col]) == (player, player, player):
            return True
    return False

def checkDia(board, player):
    """
    Check the diagonal values
    """
    if (board[0][0], board[1][1], board[2][2]) == (player, player, player):
        return True
    elif (board[0][2], board[1][1], board[2][0]) == (player, player, player):
        return True
    else:
        return False

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if checkRow(board, X) or checkCol(board, X) or checkDia(board, X):
        return X
    if checkRow(board, O) or checkCol(board, O) or checkDia(board, O):
        return O
    else:
        return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    else:
        return 0

def max_value(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        best_value = -math.inf
        best_action = None
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_action = action
        return best_action

    elif current_player == O:
        best_value = math.inf
        best_action = None
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value
                best_action = action
        return best_action
