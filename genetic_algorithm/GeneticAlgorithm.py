# coding: utf-8

import Element
from random import randint

class GeneticAlgorithm:

    __population = []
    __new_population = []
    __eval_count = 0

    def __init__(self, generations_size, population_size):
        self.__generations_size = generations_size
        self.__population_size = population_size
        self.__check_rep()

    def __roulette(self):
        self.__sum_evaluations()
        self.__sort_population_by_eval()
        chosen_element_eval = randint(0, self.eval_count)

        i = 0
        current_eval = self.__population[i]

        while current_eval < chosen_element_eval:
            i += 1
            current_eval = self.__population[i]

        return self.__population[i]

    def __generation(self):
        new_el = Element()


    def __sort_population_by_eval(self):
        self.__population = sorted(self.__population, key=lambda element: Element.get_evaluation())

    def __initialize___population(self):
        for i in range(self.__population_size):
            self.__population.append(Element.initialize_element())

    def __sum_evaluations(self):
        eval_sum = 0
        for i in range(self.__population_size):
            eval_sum += self.__population[i].get_evaluation()
        self.eval_count = eval_sum

    # Testing purpose: garantee consistency
    # TODO: improve it
    def __check_rep(self):
        assert isinstance(self.__generations_size, int)
        assert isinstance(self.__population_size, int)
        assert len(self.__population) == self.__population_size
