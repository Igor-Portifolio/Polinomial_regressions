import numpy as np
import matplotlib
from Polinomial_regressions import data
from Polinomial_regressions import Linear_alg_logic
matplotlib.use('TkAgg')  # Forçar backend TkAgg
import matplotlib.pyplot as plt

# User input: number of points the user wants to generate between [0 100] | Degree of the polynomial fit
k = int(input('Entre com o numero de pontos que quer gerar: '))
degree = int(input('Entre com o grau do polinomio que se deseja '))

# Import data
x_vals, y_vals = data.make_data(k)

# Transforming data in to matrix
x_matrix = np.array(x_vals)
y_matrix = np.array(y_vals)
column = []

# Extracting the coefficients based on the x and y point
coeficients = Linear_alg_logic.coef(x_matrix, y_matrix, degree)

#  Polinomial fit
f = Linear_alg_logic.polynomial_value(coeficients)


# Funtion to return two significant digits of a number
def round_to_two_significant_digits(c):
    aux = round(c, 2)
    return aux


# Function to automate the graph title
def create_polynomial_label(coefi):
    termos = []
    for i, c in enumerate(coefi):
        if c == 0:
            continue
        if i == 0:
            termos.append(f"{round_to_two_significant_digits(c)}")
        elif i == 1:
            termos.append(f"{round_to_two_significant_digits(c)}x")
        else:
            termos.append(f"{round_to_two_significant_digits(c)}x^{i}")
    expressao = " + ".join(termos)
    return f"y = {expressao}"


# Creat graph label
label = create_polynomial_label(coeficients)

# x values
x_valores = np.linspace(-50, 150, 100)  # 100 valores entre 0 e 300

# y values
y_valores = f(x_valores)

# Use a style
plt.style.use('fivethirtyeight')

# Creating graphs
plt.plot(x_valores, y_valores, label=label, color='green')  # Linha azul
plt.xlabel('x')
plt.ylabel('y')
plt.title('Polinomial Regression')
plt.scatter(x_vals[:k], y_vals[:k], color='blue', label='Pontos')
plt.axhline(0, color='black', linewidth=1)  # Linha do eixo x
plt.axvline(0, color='black', linewidth=1)  # Linha do eixo y
plt.grid(True)
plt.legend(fontsize=10)

# Mostrar o gráfico
plt.show()
