import network as nt
import mnist_loader
import numpy as np
import dataHandler as dh
import geneticAlg as ga

training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
# print(len(test_data))
# net = nt.Network([784, 100, 10])
# print "printing evaluation"
# print net.evaluateNormed(test_data)
# print net.fitness
# print "saving network"
# net.saveNetwork("a")
# print "network saved"
# print "loading network"
# net1 = nt.Network([784, 100, 10])
# net1.loadNetwork("a")
# print net.evaluate(test_data)

# training_data, validation_data, test_data = mnist_loader.load_data_wrapper()


# dh.mostrarImagenInd(0)
networks = ga.genPopulation(5)
networks[0].fitness
for i in networks:
    print i.fitness
ga.calcFitnessAll(networks,test_data)
for i in networks:
    print i.fitness
ga.rank(networks)
for i in networks:
    print i.fitness
totals, running_total = ga.rankArray(networks)
print totals
print running_total
chosen = []
for i in range(10):
    chosen.append(ga.chooseMetodoRanking(totals,running_total))
print chosen
