import numpy as np

def set_pi (a, b):
    if a == "pi":
        a = np.pi
    elif b == "pi":
        b = np.pi




def calculadora (a, b, operador):
    if operador == "+":
        return a + b
    elif operador == "-":
        return a-b
    elif operador == "*":
        return a*b
    elif operador == "/":
        return a/b
    elif operador == "^":
        return a^b
    elif operador == "raiz":
        return np.power(a, 1/b)

#teste