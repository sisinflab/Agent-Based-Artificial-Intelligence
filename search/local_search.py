import math
import random
from search.Node import Node


class HillClimbing:

    def __init__(self, problem):
        self.problem = problem

    def __repr__(self):
        return 'Hill Climbing'

    def run(self):
        # initial node with initial state
        node = Node(state=self.problem.initial_state,
                    parent=None,
                    action=None,
                    cost=0,
                    depth=0)

        while True:
            # the local search looks only to the nearest states
            new_states = self.problem.successors(node.state)

            # no more neighbours to explore
            if not new_states:
                return 'Stop', node.state

            # select the best neighbour given the objective function
            best_neighbor, best_action = max(new_states, key=lambda x: self.problem.value(x[0]))

            # check if there is not any improvement
            if self.problem.value(node.state) >= self.problem.value(best_neighbor):
                return 'Ok', node.state

            # next neighbour to explore
            node = node.expand(state=best_neighbor,
                               action=best_action,
                               cost=1)


class SimulatedAnnealing:

    def __init__(self, problem, min_temp=0, max_time=100, lam=0.001):
        self.problem = problem
        self.min_temp = min_temp
        self.max_time = max_time
        self.lam = lam

    def __repr__(self):
        return 'Simulated Annealing'

    def linear_schedule(self, temp):
        return temp - self.lam

    def proportional_schedule(self, temp):
        return temp - self.lam * temp

    def exponential_schedule(self, temp, time):
        return temp * math.exp(-self.lam * time)

    def run(self, initial_temp=100):
        # set time at the beginning of the search
        time = 0
        temp = initial_temp

        # initial node with initial state
        node = Node(state=self.problem.initial_state,
                    parent=None,
                    action=None,
                    cost=0,
                    depth=0)

        while temp > self.min_temp and time < self.max_time:
            # the local search looks only to the nearest states
            new_states = self.problem.successors(node.state)

            # no more neighbours to explore
            if not new_states:
                return 'Stop', node

            # select the best neighbour given the objective function
            selected_neighbour, selected_action = random.choice(new_states)

            score_diff = self.problem.value(selected_neighbour) - self.problem.value(node.state)

            if score_diff > 0 or random.uniform(0, 1) < math.exp(score_diff / temp):
                # new state to explore
                node = node.expand(state=selected_neighbour,
                                   action=selected_action,
                                   cost=1)
            # update temperature
            temp = self.exponential_schedule(temp, time)
            # update time
            time += 1

        print(f'temp: {temp}, time: {time}')
        return 'Ok', node.state


class Genetic:

    def __init__(self, problem, population=1000, generations=100, p_mutation=0.1, gene_pool=None):
        self.problem = problem
        self.population = population
        self.generations = generations
        self.couples = int(self.population / 2)
        self.p_mutation = p_mutation
        self.gene_pool = gene_pool

    def __repr__(self):
        return 'Genetic'

    def select(self, population):
        fitnesses = list(map(self.problem.value, population))
        return random.choices(population=population, weights=fitnesses, k=2)

    def crossover(self, couple):
        parent_a, parent_b = couple
        split = random.randrange(0, len(parent_a))
        return tuple(list(parent_a[:split]) + list(parent_b[split:]))

    def mutation(self, state):
        if random.uniform(0, 1) > self.p_mutation or self.gene_pool is None:
            return state
        new_state = list(state)
        new_state[random.randrange(len(state))] = random.choice(self.gene_pool)
        return tuple(new_state)

    def run(self):
        population = [self.problem.random() for _ in range(self.population)]
        for e in range(self.generations):
            best = max(population, key=lambda x: self.problem.value(x))
            print(f'Generation: {e} - max score: {self.problem.value(best)}')
            new_generation = [
                self.mutation(
                    self.crossover(
                        self.select(population)
                    )
                )
                for _ in range(self.population)]
            population = new_generation
        return 'ok', max(population, key=lambda x: self.problem.value(x))
