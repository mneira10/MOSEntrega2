from numpy.random import choice
z = [1,2,3]
b =3 
a = [(b-x + 0.0)/(b*(b+1)/2) for x in range(b)]
print choice(z,p=[1.0/3,1.0/3,1.0/3])