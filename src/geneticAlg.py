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

# def crossover():

# def mutate();


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
