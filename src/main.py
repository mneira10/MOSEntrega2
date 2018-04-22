import network as nt
import mnist_loader
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import dataHandler as dh

training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
net = nt.Network([784, 100, 10])
print "printing evaluation"
print net.evaluate(test_data)
print "saving network"
net.saveNetwork("a")
print "network saved"
# print "loading network"
# net1 = nt.Network([784, 100, 10])
# net1.loadNetwork("a")
# print net.evaluate(test_data)

# training_data, validation_data, test_data = mnist_loader.load_data_wrapper()



