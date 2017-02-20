# coding: utf-8

from util import util
from genetic_algorithm.GeneticAlgorithm import GeneticAlgorithm

def main():
    players_turn = True

    print "Location map:"
    util.print_out_numbered_board()

    while not util.is_finished():
        if players_turn:
            print "Current game state:"
            util.print_out_board()
            print "YOUR TURN!"

            insert_pos = int(raw_input("Insert in position: "))
            while not util.evaluates_play(insert_pos, "X") and util.has_empty_places():
                insert_pos = int(raw_input("Insert in another position: "))
        else:
            print "Current game state:"
            util.print_out_board()
            print "COMPUTER TURN!"

            board_current_state = util.board_as_element()
            ag = GeneticAlgorithm(2, 5, board_current_state)
            answer = ag.execute()
            while not util.evaluates_play(answer.changing_index, "O") and util.has_empty_places():
                ag = GeneticAlgorithm(2, 5, board_current_state)
                answer = ag.execute()

            del ag, answer, board_current_state

        if util.somebody_won():
            if players_turn:
                print "You won."
            else:
                print "You lost."
            util.print_out_board()

        elif util.is_dead_heat():
            print "Is Dead Heat."

        players_turn = not players_turn

if __name__ == '__main__':
    main()
