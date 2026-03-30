import sympy as sp
from taylor import taylor

x = sp.symbols('x')

def limite_par_dl(f, a, n):
 
    dl = taylor(f, a, n)
    
    limite = sp.limit(dl, x, a)
    
    return limite


# Exemple :
import sympy as sp

x = sp.symbols('x')

dl = taylor(sp.exp(x), 0, 3)

limite_par_dl = sp.limit(dl, x, 0)

print("La limite de (exp(x)-1)/x lorsque x tend vers 0 vaut :", limite_par_dl)

#Un autre exemple :
import sympy as sp

x = sp.symbols('x')

dl = taylor(sp.sin(x), 0, 3)

limite_par_dl = sp.limit(dl/x, x, 0)

print("La limite de sin(x)/x lorsque x tend vers 0 vaut :", limite_par_dl)
