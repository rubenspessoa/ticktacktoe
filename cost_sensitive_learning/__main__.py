# coding: utf-8

import util

def main():
    players_turn = True

    print "Location map:"
    util.print_out_numbered_board()

    while not util.is_finished():
        if players_turn:
            print "YOUR TURN!"
            print "Current game state:"
            util.print_out_board()
            insert_pos = int(raw_input("Insert in position: "))
            while not util.evaluates_play(insert_pos, "X") and util.has_empty_places():
                insert_pos = int(raw_input("Insert in another position: "))
        else: # COST SENSITIVE LEARNING
            print "COMPUTER TURN!"
            print "Current game state:"
            util.print_out_board()

        if util.somebody_won():
            if players_turn:
                print "You won."
            else:
                print "You lost."
        elif util.is_dead_heat():
            print "Is Dead Heat."

        players_turn = not players_turn

if __name__ == '__main__':
    main()
