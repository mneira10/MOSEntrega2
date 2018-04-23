import network as nt
import mnist_loader
import numpy as np
import dataHandler as dh
import geneticAlg as ga
import random
# from numpy.random import choice

training_data, validation_data, test_data = mnist_loader.load_data_wrapper()


def iterate(networks):

    chosen = []
    # escogemos a los 10 mejores
    for i in range(10):
        chosen.append(i)

    # for i in chosen:
    #     print networks[i].fitness

    temps = []
    for i in range(len(chosen)/2):
        # se crean hijos segun la mejor poblacion
        # son1, son2 = ga.crossover(networks[chosen[i*2]],networks[chosen[i*2+1]])
        # probs= [(len(networks)-x+0.0)/(len(networks)*(len(networks)+1)/2) for x in range(len(networks))]
        # probs = [1.0/len(networks) for x in range(len(networks))]
        son1, son2 = ga.crossover(networks[random.choice(chosen)], 
                                  networks[random.choice(chosen)])
        for i in range(5):
            ga.mutate(son1)
            ga.mutate(son2)

        temps.append(son1)
        temps.append(son2)

    # networks = np.array(networks)
    # uniq = list(set(chosen))
    # networks = np.delete(networks,uniq)
    # networks = networks[chosen]
    # print uniq
    # print len(networks)
    # networks = networks.tolist()

    while(len(networks) > 10):
        networks.pop(-1)

    for i in temps:
        networks.append(i)
    # print(len(networks))
    ga.calcFitnessAll(networks, test_data)
    prints = []
    for net in networks:
        prints.append(net.fitness)
    print(prints)
    prints = np.array(prints)
    with open("metaResults.txt", "a") as myfile:
        myfile.write(str(np.average(prints)) + " " +
                     str(np.max(prints)) + " " + str(np.min(prints)) + "\n")

    # for i in networks:
    #     print i.fitness
    # ga.rank(networks)


networks = ga.genPopulation(10)
# networks[0].fitness
# for i in networks:
#     print i.fitness
ga.calcFitnessAll(networks, test_data)
# for i in networks:
#     print i.fitness
# ga.rank(networks)

for i in range(100):
    iterate(networks)
# for i in networks:
#     print i.fitness


# print np.delete(a, ind2remove)

# son1 ,son2 = ga.crossover(net1,net2)
