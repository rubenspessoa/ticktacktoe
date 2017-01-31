# coding: utf-8

import util

board = [[' ' for j in xrange(3)] for i in xrange(3)]
numbered_board = [[(3*i + j) for j in xrange(3)] for i in xrange(3)]

def main():
    players_turn = True

    print "Location map:"
    print_out_numbered_board()

    while not is_finished():
        if players_turn:
            print "YOUR TURN!"
            print "Current game state:"
            print_out_board()
            insert_pos = int(raw_input("Insert in position: "))
            while not evaluates_play(insert_pos, "X") and has_empty_places():
                insert_pos = int(raw_input("Insert in another position: "))
        else: # COST SENSITIVE LEARNING
            print "COMPUTER TURN!"
            print "Current game state:"
            print_out_board()
        final_message()
        players_turn = not players_turn

def final_message():
    if somebody_won():
        if players_turn:
            print "You won."
        else:
            print "You lost."
    elif is_dead_heat():
        print "Is Dead Heat."

if __name__ == '__main__':
    main()
