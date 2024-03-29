import math

import numpy as np

from pymoo.model.selection import Selection
from pymoo.rand import random
from pymoo.util.misc import random_permuations


class TournamentSelection(Selection):
    """
      The Tournament selection is used to simulated a tournament between individuals. The pressure balances
      greedy the genetic algorithm will be.
    """

    def __init__(self, func_comp=None, pressure=2):
        """

        Parameters
        ----------
        func_comp: func
            The function to compare two individuals. It has the shape: comp(pop, indices) and returns the winner.
            If the function is None it is assumed the population is sorted by a criterium and only indices are compared.

        pressure: int
            The selection pressure to bie applied. Default it is a binary tournament.
        """

        # selection pressure to be applied
        self.pressure = pressure

        self.f_comp = func_comp
        if self.f_comp is None:
            raise Exception("Please provide the comparing function for the tournament selection!")

    def _do(self, pop, n_select, n_parents=1, **kwargs):
        # number of random individuals needed
        n_random = n_select * n_parents * self.pressure

        # number of permutations needed
        n_perms = math.ceil(n_random / len(pop))

        # get random permutations and reshape them
        P = random_permuations(n_perms, len(pop))[:n_random]
        P = np.reshape(P, (n_select * n_parents, self.pressure))

        # compare using tournament function
        S = self.f_comp(pop, P, **kwargs)

        return np.reshape(S, (n_select, n_parents))


def compare(a, a_val, b, b_val, method, return_random_if_equal=False):
    if method == 'larger_is_better':
        if a_val > b_val:
            return a
        elif a_val < b_val:
            return b
        else:
            if return_random_if_equal:
                return random.choice([a, b])
            else:
                return None
    elif method == 'smaller_is_better':
        if a_val < b_val:
            return a
        elif a_val > b_val:
            return b
        else:
            if return_random_if_equal:
                return random.choice([a, b])
            else:
                return None
    else:
        raise Exception("Unknown method.")


import numpy as np
from pymoo.model.population import Population


def main():
    # Create a population with fixed fitness values
    pop = Population(10)
    pop.set('F', np.array([0.1, 0.5, 0.3, 0.7, 0.2, 0.6, 0.8, 0.4, 0.9, 0.0]))

    # Define a function for comparing two individuals
    def func_comp(pop, indices, **kwargs):
        winners = []
        for i in range(indices.shape[0]):
            a, b = indices[i]
            winner = compare(a, pop[a].F, b, pop[b].F, method='smaller_is_better')
            winners.append(winner)
        return np.array(winners)

    # Create the TournamentSelection object
    selection = TournamentSelection(func_comp=func_comp, pressure=2)

    # Select 5 parents from the population
    parents_pairs = selection.do(pop, n_select=5)
    print("Selected parents pairs indices:", parents_pairs)

    # Determine the actual selected parents
    parents = func_comp(pop, parents_pairs)
    print("Selected parents indices:", parents)

if __name__ == "__main__":
    main()
