import numpy as np

from pymoo.model.mutation import Mutation
from pymoo.operators.repair.out_of_bounds_repair import OutOfBoundsRepair
from pymoo.rand import random


class PolynomialMutation(Mutation):
    def __init__(self, eta, prob=None, var_type=np.double):
        super().__init__()
        self.eta = float(eta)
        self.var_type = var_type
        if prob is not None:
            self.prob = float(prob)
        else:
            self.prob = None

    def _do(self, problem, pop, **kwargs):

        X = pop.get("X").astype(np.double)
        Y = np.full(X.shape, np.inf)

        if self.prob is None:
            self.prob = 1.0 / problem.n_var

        do_mutation = random.random(X.shape) < self.prob

        Y[:, :] = X

        xl = np.repeat(problem.xl[None, :], X.shape[0], axis=0)[do_mutation]
        xu = np.repeat(problem.xu[None, :], X.shape[0], axis=0)[do_mutation]

        if self.var_type == np.int:
            xl -= 0.5
            xu += (0.5 - 1e-16)

        X = X[do_mutation]

        delta1 = (X - xl) / (xu - xl)
        delta2 = (xu - X) / (xu - xl)

        mut_pow = 1.0 / (self.eta + 1.0)

        rand = random.random(X.shape)
        mask = rand <= 0.5
        mask_not = np.logical_not(mask)

        deltaq = np.zeros(X.shape)

        xy = 1.0 - delta1
        val = 2.0 * rand + (1.0 - 2.0 * rand) * (np.power(xy, (self.eta + 1.0)))
        d = np.power(val, mut_pow) - 1.0
        deltaq[mask] = d[mask]

        xy = 1.0 - delta2
        val = 2.0 * (1.0 - rand) + 2.0 * (rand - 0.5) * (np.power(xy, (self.eta + 1.0)))
        d = 1.0 - (np.power(val, mut_pow))
        deltaq[mask_not] = d[mask_not]

        # mutated values
        _Y = X + deltaq * (xu - xl)

        # back in bounds if necessary (floating point issues)
        _Y[_Y < xl] = xl[_Y < xl]
        _Y[_Y > xu] = xu[_Y > xu]

        # set the values for output
        Y[do_mutation] = _Y

        if self.var_type == np.int:
            Y = np.rint(Y).astype(np.int)

        off = OutOfBoundsRepair().do(problem, pop.new("X", Y))

        return off



from pymop.problem import Problem
class MyProblem(Problem):
    def __init__(self):
        super().__init__(n_var=3, n_obj=1, n_constr=0, xl=0, xu=1)

    def _evaluate(self, X, out, *args, **kwargs):
        f = X[:, 0] + np.sum(X[:, 1:], axis=1)
        out["F"] = f

from pymoo.model.population import Population

def main():
    # Define problem
    problem = MyProblem()

    # Generate a population of 10 individuals, each with 30 variables
    np.random.seed(1)
    X = np.random.randint(0, 10, size=(10, 3))

    # Evaluate the initial population
    F, CV, G = problem.evaluate(X, return_values_of=["F", "CV", "G"])

    # Create a Population object and set the X and F values
    pop = Population(n_individuals=X.shape[0])
    pop.set("X", X)
    pop.set("F", F)

    # Define mutation operator
    mutation = PolynomialMutation(eta=20)

    # Mutate population
    off = mutation.do(problem, pop)

    print("Original population:")
    print(pop.get("X"))
    print("\nMutated population:")
    print(off.get("X"))

if __name__ == '__main__':
    main()





