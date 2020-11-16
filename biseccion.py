import math
import numpy as np #Manejo de arrays
"bokita el mas grande"
MAX_ITERATIONS=100
TOLERANCE=0.001
DECIMALS=5

R=4.5
s=10
n=5

A=0
B=9

#Definir la función función
def f1(x):
    return np.pi*x*x*(3*R-x)/3 - s/(n*9.5)

def f2(x):
    return 4*np.pi*R*R*R/3

def bisection(f, a, b, tol, max_iterations):
    p=(a+b)/2
    n=1
    error=1
    data=[]
    data.append((n, p))

    while((error>tol and n<max_iterations) or n==1):

        if np.sign(f(a))==np.sign(f(p)):
            a=p
        else:
            b=p

        p_new=(a+b)/2
        #Elegir la fórmula del error
        error=abs((p_new-p)/p_new)
        n+=1
        p=p_new
        data.append((n, p))
    
    return data

def main():

    result=[]
    result=bisection(f1, A, B, TOLERANCE, MAX_ITERATIONS)
    print_table(result)
    result=bisection(f2, A, B, TOLERANCE, MAX_ITERATIONS)
    print_table(result)

def print_table(data):
    print("\n"+65*'*')
    print("Iteración", "\t", "Raíz", "\t\t\t")
    print(65*'_'+"\n")
    for element in data:
        print(str(element[0]).ljust(16), "{:.{prec}f}".format(element[1], prec=DECIMALS))
    print("\n"+65*'*')

main()
        
