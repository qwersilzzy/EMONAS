
import matplotlib.pyplot as plt
import numpy as np

def plot_pareto_frontier(save_location, Xs, Ys, maxX=True, maxY=True):
    '''Pareto frontier selection process'''
    sorted_list = sorted([[Xs[i], Ys[i]] for i in range(len(Xs))], reverse=maxY)
    print('sorted_list:::', sorted_list)
    pareto_front = [sorted_list[0]]
    print('pareto_front:::', pareto_front)
    for pair in sorted_list[1:]:
        if maxY:
            if pair[1] >= pareto_front[-1][1]:
                pareto_front.append(pair)
        else:
            if pair[1] <= pareto_front[-1][1]:
                pareto_front.append(pair)

    '''Plotting process'''
    plt.scatter(Xs, Ys)
    pf_X = [pair[0] for pair in pareto_front]
    pf_Y = [pair[1] for pair in pareto_front]
    print('pf_X:::', pf_X)
    print('pf_Y:::', pf_Y)
    plt.plot(pf_X, pf_Y)
    plt.legend(['20 epoch in micro search'])
    plt.xlabel("Number of ones of the neuron network")
    plt.ylabel("Classification error on CIFAR-10")
    plt.title('number of ones versus accuracy in random search')
    plt.savefig(save_location)
    plt.show()

def pareto_frontier_calculation(Xs, Ys, maxX=True, maxY=True):
    '''Pareto frontier selection process'''
    sorted_list = sorted([[Xs[i], Ys[i]] for i in range(len(Xs))], reverse=maxY)
    print('sorted_list:::', sorted_list)
    pareto_front = [sorted_list[0]]
    print('pareto_front:::', pareto_front)
    for pair in sorted_list[1:]:
        if maxY:
            if pair[1] >= pareto_front[-1][1]:
                pareto_front.append(pair)
        else:
            if pair[1] <= pareto_front[-1][1]:
                pareto_front.append(pair)

    pf_X = [pair[0] for pair in pareto_front]
    pf_Y = [pair[1] for pair in pareto_front]
    print('pf_X:::', pf_X)
    print('pf_Y:::', pf_Y)
    return pf_X, pf_Y


def single_pareto_plot(save_location, pf_X, pf_Y, Xs, Ys):
    plt.scatter(Xs, Ys)
    plt.plot(pf_X, pf_Y)
    plt.legend(['100 epoch in macro search'])
    plt.xlabel("Number of ones of the neuron network")
    plt.ylabel("Classification error on CIFAR-10")
    plt.title('EMONAS in evolutionary search')
    plt.savefig(save_location)
    plt.show()

def mixed_pareto_plot(pf_X_0, pf_Y_0, Xs_0, Ys_0, pf_X_1, pf_Y_1, Xs_1, Ys_1, save_location):
    plt.scatter(Xs_0, Ys_0)
    plt.plot(pf_X_0, pf_Y_0)
    plt.scatter(Xs_1, Ys_1)
    plt.plot(pf_X_1, pf_Y_1)

    plt.legend(loc="upper right", labels=["evolutionary_architecture", "pareto_front_evolutionary",
                                          "random_architecture","pareto_front_random"])

    plt.xlabel("Number of ones of the neuron network")
    plt.ylabel("Classification error on CIFAR-10")
    plt.title('EMONAS pareto front of searching')
    plt.savefig(save_location)
    plt.show()

# def mixed_pareto_plot_another_label(pf_X_0, pf_Y_0, Xs_0, Ys_0, pf_X_1, pf_Y_1, Xs_1, Ys_1, save_location):
#     plt.scatter(Xs_0, Ys_0)
#     plt.plot(pf_X_0, pf_Y_0)
#     plt.scatter(Xs_1, Ys_1)
#     plt.plot(pf_X_1, pf_Y_1)
#
#     plt.legend(loc="upper right", labels=["evo_archi_20", "pareto_front_evo_20",
#                                           "evo_archi_100","pareto_front_evo_100"])
#
#     plt.xlabel("Number of ones of the neuron network")
#     plt.ylabel("Classification error on CIFAR-10")
#     plt.title('EMONAS pareto front of searching')
#     plt.savefig(save_location)
#     plt.show()

def mix_testing_ed_pareto_plot(pf_X_0, pf_Y_0, Xs_0, Ys_0, pf_X_1, pf_Y_1, Xs_1, Ys_1, save_location):


    plt.scatter(Xs_0, Ys_0)
    plt.plot(pf_X_0, pf_Y_0)
    plt.scatter(Xs_1, Ys_1)
    plt.plot(pf_X_1, pf_Y_1)
    plt.legend(loc="upper right", labels=["evolutionary_architecture", "pareto_front_evolutionary",
                                          "random_architecture","pareto_front_random"])

    plt.xlabel("Number of ones of the neuron network")
    plt.ylabel("Classification error on CIFAR-10")
    plt.title('number of ones versus accuracy')

    plt.show()


def test_of_multiple_legend():
    import matplotlib.pyplot as plt
    import matplotlib.colors
    import numpy as np;
    np.random.seed(1)
    import pandas as pd
    plt.rcParams["figure.subplot.right"] = 0.8
    v = np.random.rand(30, 4)
    v[:, 2] = np.random.choice(np.arange(1980, 2015, 5), size=30)
    v[:, 3] = np.random.randint(5, 13, size=30)

    df = pd.DataFrame(v, columns=["x", "y", "year", "quality"])
    df.year = df.year.values.astype(int)
    fig, ax = plt.subplots()
    for i, (name, dff) in enumerate(df.groupby("year")):
        c = matplotlib.colors.to_hex(plt.cm.jet(i / 7.))
        dff.plot(kind='scatter', x='x', y='y', label=name, c=c,
                 s=dff.quality ** 2, ax=ax)

    leg = plt.legend(loc=(1.03, 0), title="Year")
    ax.add_artist(leg)
    h = [plt.plot([], [], color="gray", marker="o", ms=i, ls="")[0] for i in range(5, 13)]
    plt.legend(handles=h, labels=range(5, 13), loc=(1.03, 0.5), title="Quality")
    plt.show()



def main():

    # save_location = 'data/search_parameters/20230206_macro_random_evolutionary/hamming_versus_acc_macro_mixed.pdf'
    save_location = 'data/search_parameters/20230206_macro_random_evolutionary/random/hamming_versus_acc_macro_random_single.pdf'

    '''evolutionary search result'''
    file_Xs_evolution = 'data/search_parameters/20230206_macro_random_evolutionary/evo/learnable_parameters_ones_counting.txt'
    Xs_evolution = np.loadtxt(file_Xs_evolution)

    file_Ys_evolution = 'data/search_parameters/20230206_macro_random_evolutionary/evo/valid_acc.txt'
    Ys_evolution = 100 - np.loadtxt(file_Ys_evolution)

    pf_X_evolution, pf_Y_evolution = pareto_frontier_calculation(Xs_evolution, Ys_evolution, maxX=True, maxY=False)

    # single_pareto_plot(save_location, pf_X_evolution, pf_Y_evolution, Xs_evolution, Ys_evolution)
    '''evolutionary search result'''

    '''random search result'''
    file_Xs_random = 'data/search_parameters/20230206_macro_random_evolutionary/random/learnable_parameters_ones_counting.txt'
    Xs_random = np.loadtxt(file_Xs_random)

    file_Ys_random = 'data/search_parameters/20230206_macro_random_evolutionary/random/valid_acc.txt'
    Ys_random = 100 - np.loadtxt(file_Ys_random)

    pf_X_random, pf_Y_random = pareto_frontier_calculation(Xs_random, Ys_random, maxX=True, maxY=False)

    # single_pareto_plot(save_location, pf_X_random, pf_Y_random, Xs_random, Ys_random)
    '''random search result'''


    #
    # mixed_pareto_plot(pf_X_evolution, pf_Y_evolution, Xs_evolution, Ys_evolution, pf_X_random, pf_Y_random, Xs_random, Ys_random, save_location)

    #
    # mixed_pareto_plot_another_label(pf_X_evolution, pf_Y_evolution, Xs_evolution, Ys_evolution, pf_X_random, pf_Y_random, Xs_random, Ys_random, save_location)

    return

# def another_main():
#
#
#     save_location = 'data/search_parameters/20230206_evo_epoch_diff/hamming_versus_acc_macro_epoch_diff_mix.pdf'
#
#     '''20 epoch search result'''
#     file_Xs_evolution = 'data/search_parameters/20230206_evo_epoch_diff/epoch_20/learnable_parameters_ones_counting.txt'
#     Xs_evolution = np.loadtxt(file_Xs_evolution)
#
#     file_Ys_evolution = 'data/search_parameters/20230206_evo_epoch_diff/epoch_20/valid_acc.txt'
#     Ys_evolution = 100 - np.loadtxt(file_Ys_evolution)
#
#     pf_X_evolution, pf_Y_evolution = pareto_frontier_calculation(Xs_evolution, Ys_evolution, maxX=True, maxY=False)
#
#     # single_pareto_plot(save_location, pf_X_evolution, pf_Y_evolution, Xs_evolution, Ys_evolution)
#     '''20 epoch search result'''
#
#     '''100 epoch search result'''
#     file_Xs_random = 'data/search_parameters/20230206_evo_epoch_diff/epoch_100/learnable_parameters_ones_counting.txt'
#     Xs_random = np.loadtxt(file_Xs_random)
#
#     file_Ys_random = 'data/search_parameters/20230206_evo_epoch_diff/epoch_100/valid_acc.txt'
#     Ys_random = 100 - np.loadtxt(file_Ys_random)
#
#     pf_X_random, pf_Y_random = pareto_frontier_calculation(Xs_random, Ys_random, maxX=True, maxY=False)
#
#     # single_pareto_plot(save_location, pf_X_random, pf_Y_random, Xs_random, Ys_random)
#     '''100 epoch search result'''
#
#
#
#     mixed_pareto_plot_another_label(pf_X_evolution, pf_Y_evolution, Xs_evolution, Ys_evolution, pf_X_random, pf_Y_random, Xs_random, Ys_random, save_location)
#
#     return
if __name__ == "__main__":
    main()
    # another_main()