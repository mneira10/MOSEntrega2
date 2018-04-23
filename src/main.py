import network as nt
import mnist_loader
import numpy as np
import dataHandler as dh
import geneticAlg as ga
import random

#se cargan los datos 
training_data, validation_data, test_data = mnist_loader.load_data_wrapper()


def iterate(networks):

    chosen = []
    # escogemos a los 10 mejores
    for i in range(10):
        chosen.append(i)

    temps = []
    for i in range(len(chosen)/2):

        # se crean hijos segun los mejores individuos de la poblacion
     
        son1, son2 = ga.crossover(networks[random.choice(chosen)], 
                                  networks[random.choice(chosen)])
        #y se mutan
        for i in range(5):
            ga.mutate(son1)
            ga.mutate(son2)

        temps.append(son1)
        temps.append(son2)

    #se eliminan todos los individuos salvo los 10 mejores
    while(len(networks) > 10):
        networks.pop(-1)

    #se agregan los hijos
    for i in temps:
        networks.append(i)

    #se calcula el fitness de todos y se ordena la poblacion
    #por fitness descendientemente
    ga.calcFitnessAll(networks, test_data)

    #imprimimos a consola 
    prints = []
    for net in networks:
        prints.append(net.fitness)
    print(prints)

    #exportamos a un archivo al mejor de esta generacion, 
    #el promedio de la generacion y el peor de la generacion
    prints = np.array(prints)
    with open("metaResults.txt", "a") as myfile:
        myfile.write(str(np.average(prints)) + " " +
                     str(np.max(prints)) + " " + str(np.min(prints)) + "\n")


#se inicializa la poblacion
networks = ga.genPopulation(10)

#se calcula el fitness inicial
ga.calcFitnessAll(networks, test_data)

#se realizan 100 generaciones
for i in range(100):
    iterate(networks)
