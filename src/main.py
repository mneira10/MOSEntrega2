import network as nt
import mnist_loader
import numpy as np
import dataHandler as dh
import geneticAlg as ga

training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
# print(len(test_data))
# net1 = nt.Network([784, 100, 10])
# net2 = nt.Network([784, 100, 10])
# print net.biases
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
# print dh.darDigitoInd(0)

def iterate(networks):
    
    # totals, running_total = ga.rankArray(networks)
    # print totals
    # print running_total
    chosen = []
    #escoger metodo rank 

    # for i in range(20):
    #     chosen.append(ga.chooseMetodoRanking(totals,running_total))
    
    #escogemos los 0.6 mejores
    
    for i in range(int(0.6*len(networks))):
        chosen.append(i)

    print chosen
    for i in chosen:
        print networks[i].fitness

    temps = []
    for i in range(len(chosen)/2):
        son1, son2 = ga.crossover(networks[chosen[i*2]],networks[chosen[i*2+1]])
        ga.mutate(son1)
        ga.mutate(son2)
        ga.mutate(son1)
        ga.mutate(son2)
        temps.append(son1)
        temps.append(son2)

    networks = np.array(networks)
    # uniq = list(set(chosen))
    # networks = np.delete(networks,uniq)
    networks = networks[chosen]
    # print uniq
    # print len(networks)
    networks = networks.tolist()
    for i  in temps:
        networks.append(i)
    # print(len(networks))
    ga.calcFitnessAll(networks,test_data)
    prints = []
    for net in networks:
        prints.append(net.fitness)
    print (prints)
    prints = np.array(prints)
    with open("metaResults.txt", "a") as myfile:
        myfile.write(str(np.average(prints)) + " " + str(np.max(prints))+ " " +str(np.min(prints)) +"\n")


    # for i in networks:
    #     print i.fitness
    # ga.rank(networks)



networks = ga.genPopulation(10)
# networks[0].fitness
# for i in networks:
#     print i.fitness
ga.calcFitnessAll(networks,test_data)
# for i in networks:
#     print i.fitness
# ga.rank(networks)

for i in range(100):
    iterate(networks)
# for i in networks:
#     print i.fitness





# print np.delete(a, ind2remove)

# son1 ,son2 = ga.crossover(net1,net2)
