import numpy as np

from pymoo.model.crossover import Crossover
from pymoo.operators.crossover.util import crossover_mask
from pymoo.rand import random


class PointCrossover(Crossover):

    def __init__(self, n_points):
        super().__init__(2, 2)
        self.n_points = n_points

    def _do(self, problem, pop, parents, **kwargs):

        # get the X of parents and count the matings
        X = pop.get("X")[parents.T]
        _, n_matings, n_var = X.shape

        # start point of crossover
        r = np.row_stack([random.perm(n_var-1) + 1 for _ in range(n_matings)])[:, :self.n_points]
        r.sort(axis=1)
        r = np.column_stack([r, np.full(n_matings, n_var)])

        # the mask do to the crossover
        M = np.full((n_matings, n_var), False)

        # create for each individual the crossover range
        for i in range(n_matings):

            j = 0
            while j < r.shape[1] - 1:
                a, b = r[i, j], r[i, j + 1]
                M[i, a:b] = True
                j += 2

        _X = crossover_mask(X, M)
        return pop.new("X", _X)


# def main():
#     import numpy as np
#     import matplotlib.pyplot as plt
#     from pymoo.model.population import Population
#
#     # Define the number of variables and the bounds of the search space
#     n_var = 5
#     bounds = [(0, 10), (0, 10), (0, 10), (0, 10), (0, 10)]
#
#     # Create a population of 10 individuals
#     pop = Population(n_individuals=10)
#     pop.set('X', np.random.uniform(0, 10, (10, n_var)))
#
#     # Print the population before crossover
#     print("Population before crossover:")
#     print(pop.get('X'))
#
#     # Apply the PointCrossover operator to the population
#     point_crossover = PointCrossover(2)
#     parents = np.array([[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]])
#     offspring = point_crossover.do(problem=None, pop=pop, parents=parents)
#
#     # Print the population after crossover
#     print("\nPopulation after crossover:")
#     print(offspring.get('X'))
#
#     # Visualize the crossover points
#     fig, ax = plt.subplots()
#     ax.scatter(pop.get('X')[:, 0], pop.get('X')[:, 1], color='blue')
#     ax.scatter(offspring.get('X')[:, 0], offspring.get('X')[:, 1], color='red')
#     ax.set_xlabel('Variable 1')
#     ax.set_ylabel('Variable 2')
#     ax.set_title('Before and After Crossover')
#     plt.show()

def main():
    import numpy as np
    import matplotlib.pyplot as plt
    from pymoo.model.population import Population

    # Define the number of variables and the bounds of the search space
    n_var = 2
    bounds = [(0, 10), (0, 10)]

    # Create a population of 4 individuals
    pop = Population(n_individuals=4)
    pop.set('X', np.random.uniform(0, 10, (4, n_var)))

    # Print the population before crossover
    print("Population before crossover:")
    print(pop.get('X'))

    # Apply the PointCrossover operator to the population
    point_crossover = PointCrossover(1)
    parents = np.array([[0, 1], [2, 3]])
    offspring = point_crossover.do(problem=None, pop=pop, parents=parents)

    # Print the population after crossover
    print("\nPopulation after crossover:")
    print(offspring.get('X'))

    # Visualize the crossover points
    fig, ax = plt.subplots()
    ax.scatter(pop.get('X')[:, 0], pop.get('X')[:, 1], color='blue')
    ax.scatter(offspring.get('X')[:, 0], offspring.get('X')[:, 1], color='red')
    ax.set_xlabel('Variable 1')
    ax.set_ylabel('Variable 2')
    ax.set_title('Before and After Crossover')
    plt.show()


if __name__ == '__main__':
    main()



