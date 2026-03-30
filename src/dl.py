import sympy as sp
from taylor import taylor

x = sp.symbols('x')


def dl_exp(n):
    print("Calcul du développement limité de exp(x) en 0 à l'ordre",n)
    return taylor(sp.exp(x), 0, n)


def dl_ln1p(n):
    print ("Calcul du développement limité de ln(1+x) en 0 à l'ordre", n)
    return taylor(sp.log(1 + x), 0, n)


def dl_sin(n):
    print("Calcul du développement limité de sin(x) en 0 à l'ordre", n)
    return taylor(sp.sin(x), 0, n)


def dl_cos(n):
    print("Calcul du développement limité de cos(x) en 0 à l'ordre", n)
    return taylor(sp.cos(x), 0, n)
