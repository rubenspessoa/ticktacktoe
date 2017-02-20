# coding: utf-8

from random import randint, uniform


class Element:

    # CONSTANTS #
    __lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    __columns = [[0, 3, 6], [1, 4, 7], [2, 5, 8]]
    __diagonals = [[0, 4, 8], [2, 4, 6]]
    #############

    __chromosome_size = 9
    __evaluation = 0
    __blanks = []
    changing_index = 0
    chromosome = ""

    def __init__(self, mutation_prob, symbol, board_state):
        self.__mutation_prob = mutation_prob
        self.__symbol = symbol
        self.chromosome = board_state
        self.__initialize_element()

    def get_evaluation(self):
        return self.__evaluation

    def evaluate(self):
        final_grade = 0

        for line in self.__lines:
            if self.changing_index in line:
                if not self.__is_blocked(line):
                    final_grade += self.__close_to_win_per(line)

        for column in self.__columns:
            if self.changing_index in column:
                if not self.__is_blocked(column):
                    final_grade += self.__close_to_win_per(column)

        for diagonal in self.__diagonals:
            if self.changing_index in diagonal:
                if not self.__is_blocked(diagonal):
                    final_grade += self.__close_to_win_per(diagonal)

        self.__evaluation = final_grade

    def __is_blocked(self, line):
        for index in line:
            aux = index * 2
            gene = self.chromosome[aux: aux + 2]
            if gene != '00' and gene != self.__symbol:
                return True
        return False

    def __close_to_win_per(self, line):
        count_symbols = 0

        for index in line:
            aux = index * 2
            gene = self.chromosome[aux: aux + 2]
            if gene == self.__symbol:
                count_symbols += 1

        return count_symbols

    def __count_blanks(self):
        self.__blanks = []
        for i in range(0, len(self.chromosome), 2):
            if self.chromosome[i: i + 2] == '00':
                if i not in self.__blanks:
                    self.__blanks.append(i)

    def __initialize_element(self):
        self.__count_blanks()

        randIndex = randint(0, len(self.__blanks) - 1)
        self.changing_index = self.__blanks[randIndex]/2

        new_chromosome = ""

        for i in range(0, len(self.chromosome), 2):
            if i != self.__blanks[randIndex]:
                new_chromosome += self.chromosome[i: i + 2]
            else:
                new_chromosome += self.__symbol

        self.chromosome = new_chromosome