import math
import numpy as np 
#Hola jaja
MSG_MAX_ITERATIONS="El algoritmo ha excedido la cantidad máxima de iteraciones permitidas."

DECIMALS=5
#Definir semilla, tolerancia y máximo de iteraciones
P=1
MAX_ITERATIONS=1000
TOLERANCE=0.001

#Definir parametros del problema en cuestión
R=4.25
s=10
n=6
c=0.01

#Definir la función
def f(x):
    #La que esta entre comillas es la del tp
    return np.pi*x*x*(3*R-x)/3 - (4/3)*np.pi*R*R*R*c+x


"""Función que recibe la semilla inicial, la función, la cantidad máxima de iteraciones
y la tolerancia, en ese orden. Se devuelve una lista con todas las iteraciones y el respectivo
valor de la raíz calculada en cada una."""

def fixed_point(p, f, max, tol):

    error=tol+1
    i=1
    data=[]
    while(error > tol):

        p_old = p
        p = f(p)
        error = abs((p-p_old)/p)
        data.append((i, p))

        if(i>max):
            raise Exception(MSG_MAX_ITERATIONS)
 
        i+=1

    return data

"""Imprime la lista de manera divertida"""
def print_table(data):
    print("\n"+65*'*')
    print("Iteración", "\t", "Raíz")
    print(65*'_'+"\n")
    for element in data:
        print(str(element[0]).ljust(16), "{:.{prec}f}".format(element[1], prec=DECIMALS))
    print("\n"+65*'*')

def main():
    result=[]
    result=fixed_point(P, f, MAX_ITERATIONS, TOLERANCE)
    print_table(result)

main()
