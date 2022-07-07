#Tableau et calcul matriciel avec Numpy
#Création de tableau avec la fonction numpy.array(); Les tableau sont utilisé comme Vecteur ou Matrice
# Fonctions pour le calcul matriciel : numpy.dot() / numpy.linalg.det() / numpy.linalg.inv() / numpy.linalg.eig()...

#Phase 01 : Importation du module Numpy et lui donner l'alias np pour alléger ensuite l'écriture de l'appel

import numpy as np

#Tableau monodimensionnels (1D) / numpy.array()

a = np.array([1,9,5])
print("Le tableau (Vecteur) a :\n",a)

#Savoir le type du résultat numpy.array() avec la fonction type()

type(a)
print("Le type de la matrice a est\n", type(a))
print(type([1,9,5]))

#Tableau bidimensionnels(2D) : il faut transmettre à numpy.array() une liste de listes grâce à des crochets imbriqués.
 
a = np.array([[1,9,5],[4,5,6]])
print("La matrice a\n", a)

#La fonction numpy.size() renvoie le nombre d’éléments du tableau.

b = np.array([2,4,6,8])
np.size(b)
print("La taille du tableu b est :\n", np.size(b))

c = np.array([[1,3,5,7],[0,9,5,1]])
np.size(c)
print("La taille de la matrice c est :\n", np.size(c))

#La fonction numpy.shape() renvoie la taille/dim du tableau/matrice.

b = np.array([2,4,6,8])
np.shape(b)
print("La taille de b est: \n", np.shape(b))

c = np.array([[1,3,5,7],[0,9,5,1]])
np.shape(c)
print("Les dimensions de c sont: \n", np.shape(c))

#Produit terme à terme : grâce à l’opérateur * Il faut dans ce cas que les deux tableaux aient la même taille.

m1 = np.array([[1,3,7],[2,4,9]])
m2 = np.array([[2,4,6],[3,1,5]])
print("Le produit terme à terme de m1 et m2 est : \n", m1*m2)

#Produit matriciel : numpy.dot()

m1 = np.array([[1,3,7],[2,4,9],[2,2,2]])
m2 = np.array([[2,4],[2,2],[1,1]])
print("Le produit de m1 et m2, en utilisant la fonction np.dot(), est: \n", np.dot(m1,m2))

#Le produit d’une matrice de taille n x m par une matrice m x p donne une matrice n x p.
# A partir de la version 3 de python on peut utiliser @ pour calculer le produit matriciel

d = np.array([[1,3,7],[2,4,9],[2,2,2],[1,1,1]])
print ("Le produit de b*d en utilisant le signe @ est : \n",b@d)

#La transposé

print("La transposé de m2 est: \n",m2.T)

#Complexe conjugué - numpy.conj()

u = np.array([[2j,4+3j],[2+5j,5],[3,6+2j]])
print("La conjuguée complexe de u est : \n", np.conj(u))

#Transposé complexe conjugué

u = np.array([[2j,4+3j],[2+5j,5],[3,6+2j]])
print("La transposée de la complexe conjuguée de u est : \n", np.conj(u).T)

#Afin de récupérer uns partie d'un tableau on utilise le Slicing (tranchage), En indiquant entre crochets des indices pour définir le début et la fin de la tranche et à les séparer par deux-points
#Il est aussi possible de ne pas mettre de début ou de fin.

t = np.array([12, 25, 34, 56, 87]) 
print ("Les trois premiers éléments du tableau sont : \n", t[:3])
print ("Les deux derniers éléments du tableau sont : \n", t[3:5])

#Slicing des tableaux 2D

f = np.array ([[1,2,3],[4,5,6]])
print("Le deuxième élément de la première ligne est: \n", f[0,1])
print("Les deux dernières colonnes de f sont: \n", f[:,1:3])
print("Le première colonne de f est : \n", f[:,0])
print("La première ligne de f est  : \n", f[0,:])

#Avertissement a[:,n] donne un tableau 1D correspondant à la colonne d’indice n de a. Si on veut obtenir un tableau 2D correspondant à la colonne d’indice n, il faut faire du slicing en utilisant a[:,n:n+1].

#Tableaux de 0 : numpy.zeros(), renvoie un tableau 1D de n zéros.

o = np.zeros(5)
print("Tableau de cinqs 0 :\n", o)

#Zeros((m,n)) renvoie tableau 2D de taille m x n, c’est-à-dire de shape (m,n)
p = np.zeros((4,4)) 
print("Matrice 4*4 de 0 : \n", p)

#Tableaux de 1 : numpy.ones()

o = np.ones(5)
print("Tableau de cinqs 1 :\n", o)
p = np.ones((4,4)) 
print("Matrice 4*4 de 1 : \n", p)

#Matrice identité : numpy.eye(), eye(n) renvoie tableau 2D carré de taille n x n, avec des uns sur la diagonale et des zéros partout ailleurs.

p = np.eye(4) 
print("Matrice identité 4*4 : \n", p)

