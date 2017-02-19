# coding: utf-8

import Element
from random import randint


class GeneticAlgorithm:

    __population = []
    __new_population = []
    __eval_count = 0

    def __init__(self, generations_size, population_size, board_current_state, mutation_prob):
        self.__generations_size = generations_size
        self.__population_size = population_size
        self.__board_current_state = board_current_state
        self.__mutation_prob = mutation_prob
        # self.__check_rep()

    def execute(self):
        self.__initialize_population()

        for i in range(self.__generations_size):
            self.__evaluate_elements()
            self.__generation()

        # self.__determine_best()

    def __determine_best(self):
        self.__sort_population_by_eval()
        return self.__population[0]

    def __generation(self):
        new_population = []
        for i in range(self.__population_size):
            # new_population.append(self.__population[i].mutation(self.__mutation_prob))
            pass
        self.__population = new_population

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

    def __sort_population_by_eval(self):
        self.__population = sorted(self.__population, key=lambda element: Element.get_evaluation())

    def __initialize_population(self):
        for i in range(self.__population_size):
            el = Element.Element(self.__board_current_state)
            self.__population.append(el)

    def __sum_evaluations(self):
        eval_sum = 0
        for i in range(self.__population_size):
            # eval_sum += self.__population[i].get_evaluation()
            pass
        self.eval_count = eval_sum

    def __evaluate_elements(self):
        for i in range(self.__population_size):
            pass
            # self.__population[i].evaluate()
        self.__sum_evaluations()

    # Testing purpose: garantee consistency
    # TODO: improve it
    def __check_rep(self):
        assert isinstance(self.__generations_size, int)
        assert isinstance(self.__population_size, int)
        assert len(self.__population) == self.__population_size
