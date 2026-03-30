import sympy as sp
from taylor import taylor

x = sp.symbols('x')

def dl_composition(f, g, a, n):

    dl_f = taylor(f, a, n)
    dl_g = taylor(g, a, n)

    dl_composed = dl_f.subs(x, dl_g)
    dl_composed = sp.series(dl_composed, x, a, n)
    dl_composed = sp.expand(dl_composed)
    return dl_composed


# Example usuel : 
def_f = sp.exp(x)
def_g = sp.sin(x)
a = 0
n = 3
dl_result = dl_composition(def_f, def_g, a, n)
print(f"Le développement limité de f(g(x)) au point {a} à l'ordre {n} est : {dl_result}")

def_f = sp.exp(x)
def_g = sp.cos(x)-1 
a = 0
n = 3
dl_result = dl_composition(def_f, def_g, a, n)
print(f"Le développement limité de f(g(x)) au point {a} à l'ordre {n} est : {dl_result}")


