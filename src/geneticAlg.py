import numpy as np
import network as nt
import random


def fitness(network, data):
    return network.evaluateNormed(data)

# def filter():


def calcFitnessAll(networks, data):
    for network in networks:
        network.evaluateNormed(data)

    return networks.sort(key=lambda x: x.fitness, reverse=True)


def rank(networks):
    for i in range(len(networks)):
        networks[i].fitness = len(networks)-i


def crossover(parent1, parent2):
    son1 = nt.Network([784, 100, 10])
    son2 = nt.Network([784, 100, 10])

    for i in range(len(parent1.weights)):
        # print "parent"
        # print parent1.weights
        partir1 = parent1.weights[i].shape[0]/2
        parteA1 = parent1.weights[i][partir1:, :]
        parteB1 = parent1.weights[i][:partir1, :]

        partir2 = parent2.weights[i].shape[0]/2
        parteA2 = parent2.weights[i][partir2:, :]
        parteB2 = parent2.weights[i][:partir2, :]

        # print "son"
        

        son1.weights[i] = (np.concatenate((parteA1, parteB2), axis=0))
        # print son1.weights

        son2.weights[i] = np.concatenate((parteA2, parteB1), axis=0)

    for i in range(len(parent1.biases)):
        partir1 = parent1.biases[i].shape[0]/2
        parteA1 = parent1.biases[i][partir1:, :]
        parteB1 = parent1.biases[i][:partir1, :]

        partir2 = parent2.biases[i].shape[0]/2
        parteA2 = parent2.biases[i][partir2:, :]
        parteB2 = parent2.biases[i][:partir2, :]

        son1.biases[i] = np.concatenate((parteA1, parteB2), axis=0)

        son2.biases[i] = np.concatenate((parteA2, parteB1), axis=0)

    return son1, son2

def mutate(network):
    for i in range(len(network.weights)):
        # print i
        # print network.weights
        # print network.weights[i].shape[0]
        # print network.weights[i].shape
        x = int(random.random()*network.weights[i].shape[0])
        y = int(random.random()*network.weights[i].shape[1])
        network.weights[i][x][y] = mutateWeight()

        x = int(random.random()*network.biases[i].shape[0])
        y = int(random.random()*network.biases[i].shape[1])
        network.biases[i][x][y] = mutateWeight()


        



def mutateWeight():
    a = random.random()
    if(a<0.5):
        return  (0.1+random.random()*2-1)%1 * -1
    else:
        return  (0.1+random.random()*2-1)%1

def genPopulation(num):
    networks = []
    for i in range(num):
        networks.append(nt.Network([784, 100, 10]))
    return networks


def rankArray(networks):
    totals = []
    running_total = 0

    for network in networks:
        running_total += network.fitness
        totals.append(running_total)
    return totals, running_total


def chooseMetodoRanking(totals, running_total):
    rnd = random.random() * running_total
    for i, total in enumerate(totals):
        if rnd < total:
            return i
