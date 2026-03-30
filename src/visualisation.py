import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from taylor import taylor

x = sp.symbols('x')

def tracer_approximation(f, a, n, nom):
    Tn = taylor(f, a, n)

    f_num = sp.lambdify(x, f, "numpy")
    Tn_num = sp.lambdify(x, Tn, "numpy")

    X = np.linspace(a - 1, a + 1, 400)

    plt.figure()
    plt.plot(X, f_num(X), label=nom)
    plt.plot(X, Tn_num(X), "--", label=f"T_{n}(x)")
    plt.legend()
    plt.title(f"Approximation locale de {nom}")
    plt.grid()
    plt.show()

plt.savefig("approximation.png")
plt.close()


def tracer_reste(f, a, n, nom):
    Tn = taylor(f, a, n)
    Rn = f - Tn

    Rn_num = sp.lambdify(x, Rn, "numpy")

    X = np.linspace(a - 1, a + 1, 400)

    plt.figure()
    plt.plot(X, Rn_num(X))
    plt.title(f"Reste R_{n}(x) pour {nom}")
    plt.grid()
    plt.show()

plt.savefig("reste.png")
plt.close()