# coding: utf-8

from random import randint


class Element:

    __chromosome_size = 9
    __evaluation = 0
    chromosome = ""
    possibilities = ["00", "01", "10"]

    def __init__(self, board_state=""):
        self.chromosome = board_state
        self.mutation()

    def mutation(self):
        # Find out blank spaces
        blanks = []
        for i in range(0, len(self.chromosome), 2):
            if self.chromosome[i: i+2] == '00':
                blanks.append(i)

        randIndex = randint(0, len(blanks) - 1)
        print randIndex, blanks[randIndex]

        new_chromosome = ""
        for i in range(0, len(self.chromosome), 2):
            if i != randIndex:
                new_chromosome += self.chromosome[i: i+2]
            else:
                new_chromosome += self.possibilities[randint(0, 2)]

        print self.chromosome
        print new_chromosome
        self.chromosome = new_chromosome

    def calculate_evaluation(self):
        pass

    def get_evaluation(self):
        return self.__evaluation

    def evaluate(self):
        pass

    def count_blanks(self):
        sum = 0
        for i in range(0, 18, 2):
            if self.chromosome[i: i+2] == '00':
               sum += 1
        return sum



