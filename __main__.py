# coding: utf-8

import util.util

def main():
    players_turn = True

    print "Location map:"
    util.util.print_out_numbered_board()

    while not util.util.is_finished():
        if players_turn:
            print "YOUR TURN!"
            print "Current game state:"
            util.util.print_out_board()
            insert_pos = int(raw_input("Insert in position: "))
            while not util.util.evaluates_play(insert_pos, "X") and util.util.has_empty_places():
                insert_pos = int(raw_input("Insert in another position: "))
        else:
            print "COMPUTER TURN!"
            print "MUST DO SOMETHING"
            print "Current game state:"
            util.util.print_out_board()

        if util.util.somebody_won():
            if players_turn:
                print "You won."
            else:
                print "You lost."
        elif util.util.is_dead_heat():
            print "Is Dead Heat."

        players_turn = not players_turn

if __name__ == '__main__':
    main()
