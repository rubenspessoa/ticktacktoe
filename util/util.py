from genetic_algorithm import Element

board = [[' ' for j in xrange(3)] for i in xrange(3)]
numbered_board = [[(3*i + j) for j in xrange(3)] for i in xrange(3)]

def evaluates_play(pos, gamer):
    is_valid = False
    for i in range(3):
        for j in range(3):
            if pos == ((i) * 3) + j:
                if board[i][j] == ' ':
                    board[i][j] = gamer
                    is_valid = True
    return is_valid

def print_out_board():
    for i in range(3):
        out = ""
        for j in range(3):
            if j < 2:
                out += " " + str(board[i][j]) + " |"
            else:
                out += " " + str(board[i][j]) + " "
        print out

        if (i < 2):
            lines = ""
            for j in range(3):
                if j < 2:
                    lines += "---|"
                else:
                    lines += "---"
            print lines

def board_as_element():
    chromosome = ""

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                chromosome += "00"
            elif board[i][j] == 'X':
                chromosome += "01"
            elif board[i][j] == 'O':
                chromosome += "10"

    return chromosome


def print_out_numbered_board():
    for i in range(3):
        out = ""
        for j in range(3):
            if j < 2:
                out += " " + str(numbered_board[i][j]) + " |"
            else:
                out += " " + str(numbered_board[i][j]) + " "
        print out

        if (i < 2):
            lines = ""
            for j in range(3):
                if j < 2:
                    lines += "---|"
                else:
                    lines += "---"
            print lines

def somebody_won():
    return _win_diag() or _win_col() or _win_line()

def is_dead_heat():
    return not somebody_won() and not has_empty_places()

def is_finished():
    return somebody_won() or is_dead_heat()

def has_empty_places():
    ans = False
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                ans = True
    return ans

def _win_line():
    won = False
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            won = True
    return won

def _win_col():
    won = False
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != ' ':
            won = True
    return won

def _win_diag():
    won = False
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        won = True
    elif board[0][2] == board[1][1] == board[2][0] != ' ':
        won = True
    return won
