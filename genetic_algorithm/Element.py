# coding: utf-8

from random import randint

class Element:

    __chromosome_size = 9
    __evaluation = 0
    chromosome = ""

    def __init__(self)
        self.initialize_element()

    def initialize_element(self):
        possibilities = ["00", "01", "10"]

        for i in range(self.__chromosome_size):
            self.chromosome += possibilities[randint(0, 2)]

        return self.chromosome

    def calculate_evaluation(self):
        pass

    def get_evaluation(self):
        return self.__evaluation

    def mutation(self):
        pass


