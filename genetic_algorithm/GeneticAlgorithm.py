# coding: utf-8

from Element import Element
from random import randint


class GeneticAlgorithm:

    __population = []
    __new_population = []
    __blanks = []
    __eval_count = 0

    def __init__(self, generations_size, population_size, board_current_state, mutation_prob=1):
        self.__generations_size = generations_size
        self.__population_size = population_size
        self.__board_current_state = board_current_state
        self.__mutation_prob = mutation_prob
        # self.__check_rep()

    def execute(self):
        self.__initialize_population()

        for i in range(self.__generations_size):
            self.__evaluate_elements()
            # TODO: self.__generation()
            return self.__determine_best()

    def __determine_best(self):
        self.__sort_population_by_eval()
        return self.__population[-1]

    def __generation(self):
        new_population = []

        for i in range(self.__population_size):
            # new_population.append(self.__population[i].mutation(self.__mutation_prob))
            pass
        # self.__population = new_population

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
        self.__population = sorted(self.__population, key=lambda element: element.get_evaluation())

    def __initialize_population(self):
        self.__count_blanks()
        self.__population = []

        while len(self.__population) < self.__population_size and len(self.__population) < len(self.__blanks):
            el = Element(self.__mutation_prob, "10", self.__board_current_state)

            catchEquals = False

            for element in self.__population:
                if el.chromosome == element.chromosome:
                    catchEquals = True

            if not catchEquals:
                self.__population.append(el)

    def __sum_evaluations(self):
        eval_sum = 0
        for i in range(len(self.__population)):
            eval_sum += self.__population[i].get_evaluation()
        self.eval_count = eval_sum

    def __evaluate_elements(self):
        for i in range(len(self.__population)):
            self.__population[i].evaluate()
        self.__sum_evaluations()

    def __count_blanks(self):
        self.__blanks = []
        for i in range(0, len(self.__board_current_state), 2):
            if self.__board_current_state[i: i + 2] == '00':
                if i not in self.__blanks:
                    self.__blanks.append(i)

    # Testing purpose: garantee consistency
    # TODO: improve it
    def __check_rep(self):
        assert isinstance(self.__generations_size, int)
        assert isinstance(self.__population_size, int)
        assert len(self.__population) == self.__population_size
