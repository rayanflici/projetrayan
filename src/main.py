import sympy as sp 
from visualisation import tracer_approximation, tracer_reste
from composition import dl_composition
from dl import dl_exp, dl_ln1p, dl_sin, dl_cos

x = sp.symbols('x')

def main():
    n = 3

    # Visualisation
    tracer_approximation(sp.exp(x), 0, n, "exp(x)")
    tracer_reste(sp.exp(x), 0, n, "exp(x)")

    tracer_approximation(sp.log(1+x), 0, n, "ln(1+x)")
    tracer_reste(sp.log(1+x), 0, n, "ln(1+x)")

    tracer_approximation(sp.sin(x), 0, n, "sin(x)")
    tracer_reste(sp.sin(x), 0, n, "sin(x)")

    tracer_approximation(sp.cos(x), 0, n, "cos(x)")
    tracer_reste(sp.cos(x), 0, n, "cos(x)")

    # Composition
    f = sp.exp(x)
    g = sp.sin(x)
    resultat = dl_composition(f, g, 0, 3)
    print("DL de exp(sin(x)) :", resultat)

    # DL usuels 
    print(dl_exp(3))
    print(dl_ln1p(3))
    print(dl_sin(3))
    print(dl_cos(3))


if __name__ == "__main__":
    main()