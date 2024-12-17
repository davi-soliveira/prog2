import math

def new_eq(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Não há raízes reais"
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        return raiz1, raiz2
