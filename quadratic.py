def roots(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante > 0:
        raiz_cuadrada = discriminante**0.5
        raiz_1 = (-b + raiz_cuadrada) / (2*a)
        raiz_2 = (-b - raiz_cuadrada) / (2*a)
        return f"({raiz_1}, {raiz_2})"
    if discriminante == 0:
        raiz = -b / (2*a)
        return f"({raiz})"
    else:
        return "( )"


def value_y(a, b, c, x):
    return a*x**2 + b*x + c


def to_string(a, b, c):
    return f"f(x) = {a}*x^2 + {b}*x + {c}"


def derivation(a, b, c):
    return f"f'(x) = {2*a} * X + {b}"
