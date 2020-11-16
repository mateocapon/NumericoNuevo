import math
import numpy as np #Manejo de arrays

MSG_MAX_ITERATIONS="El algoritmo ha excedido la cantidad máxima de iteraciones permitidas."

TOLERANCE=0.000001
MAX_ITERATIONS=10000

q=1.602e-19
epsilon=11.7*88.5e-15
Vth=0.0259
k=1.381e-23

T=300



def f(x):
    return 5.425e14-(x/(Vth*np.log(9*x*x/1e20)+1.2))

def der_f(x):
    return 2*x

def NR_method(f, der_f, x0, max, tol):
    data=[]
    p=x0
    error=tol+1
    i=0
    while(error>tol):
        i+=1
        if(i>max):
            raise Exception(MSG_MAX_ITERATIONS)
        data.append((i, p))
        p_old=p
        p=p_old-(f(p_old)/der_f(p_old))
        error=abs((p-p_old)/p)
            
    return data

def secant_method(f, x0, x1, max, tol):
    data=[]
    p0=x0
    p1=x1
    data.append((1,p0))
    data.append((2,p1))
    error=tol+1
    i=2
    while(error>tol):
        i+=1

        if(i>max):
            raise Exception(MSG_MAX_ITERATIONS)

        p_new=p1-(f(p1)*(p1-p0))/(f(p1)-f(p0))
        data.append((i, p_new))
        error=abs((p_new-p1)/p_new)
        p0=p1
        p1=p_new
            
    return data

def print_table(data, tol):
    print("\n"+65*'*')
    print("Iteración", "\t", "Raíz", "\t\t\t", "Tolerancia: ", tol)
    print(65*'_'+"\n")
    for element in data:
        print(element[0], 15*' '+"{:e}".format(element[1]))
    print("\n"+65*'*')

def main():
    result=[]
    result=secant_method(f, 1e15, 1e19, MAX_ITERATIONS, TOLERANCE)
    print_table(result, TOLERANCE)

main()