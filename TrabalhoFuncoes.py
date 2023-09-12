from sympy import symbols, Eq, solve

# Definindo a variável
x = symbols('x')

def f_to_function(equation):
    """Converte uma string de equação para uma função."""
    return lambda var: eval(equation.replace('x', str(var)))

def compose(func1, func2, value):
    """Calcula a composição de duas funções em um valor específico."""
    return func1(func2(value))

# Exemplo de uso:
if __name__ == "__main__":
    # Definindo as funções
    f_equation = input("Digite f(x): ").replace('^', '**')
    g_equation = input("Digite g(x): ").replace('^', '**')

    f = f_to_function(f_equation)
    g = f_to_function(g_equation)

    # Teste 1
    val = 4
    result_g_f = compose(g, f, val)
    print(f"(g°f)({val}) = {result_g_f}")

    # Teste 2
    result_f_f = compose(f, f, val)
    print(f"(f°f)({val}) = {result_f_f}")

    # Teste 3
    result_g_g = compose(g, g, val)
    print(f"(g°g)({val}) = {result_g_g}")

    # Teste 4
    result_f_g = compose(f, g, val)
    print(f"(f°g)({val}) = {result_f_g}")
