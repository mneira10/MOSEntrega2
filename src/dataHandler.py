import mnist_loader
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np


def guardarImagen(imagen, nombreArchivo = "digito.png"):
    plt.imsave(nombreArchivo, np.array(imagen).reshape(28,28), cmap=cm.gray)

def mostrarImagen(imagen):
    plt.imshow(np.array(imagen).reshape(28,28))
    plt.show()
    plt.close()

def guardarImagenInd(ind, nombreArchivo = "digito.png"):
    training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
    imagen = training_data[ind][0]
    plt.imsave(nombreArchivo, np.array(imagen).reshape(28,28), cmap=cm.gray)

def mostrarImagenInd(ind):
    training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
    imagen = training_data[ind][0]
    plt.imshow(np.array(imagen).reshape(28,28))
    plt.show()
    plt.close()

def darDigitoInd(ind):
    training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
    imagen = training_data[ind][1]
    return np.where(data==1)[0][0]

def darDigito(vector):
    return np.where(vector==1)[0][0]




