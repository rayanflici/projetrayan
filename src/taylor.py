import sympy as sp
x = sp.symbols('x')
def taylor (f, a, n): 
    sommme = 0
    for k in range (n+1) : 
        sommme += f.diff(x, k).subs(x, a) / sp.factorial(k) * (x-a)**k
    return sp.simplify (sommme)
