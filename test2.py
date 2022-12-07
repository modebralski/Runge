import numpy as np
import matplotlib.pyplot as plt

n = input("Podaj n: ")
n = int(n)

min_range = -1
max_range = 1


def function_to_interpolate(x):
    return 1 / (1 + 25 * x ** 2)


def calculate_table_of_difference_quotients(list):
    table = list
    for k in range(1, len(table[1])):
        row = []
        for i in range(0, len(table[k]) - 1):
            row.append((table[k][i + 1] - table[k][i]) / (table[0][i + k] - table[0][i]))
        table.append(row)
    return table


lista = []

x = np.linspace(min_range, max_range, n)
lista.append(x)

y = function_to_interpolate(x)
lista.append(y)

calculate_table_of_difference_quotients(lista)


def calculate_x_from_newton_polynomial(x, difference_quotients):
    result = difference_quotients[1][0]
    n = len(difference_quotients[0]) - 1
    for i in range(0, n):
        multiply_small_polynomials = [difference_quotients[i + 2][0]]
        for j in range(0, i + 1):
            multiply_small_polynomials.append(x - difference_quotients[0][j])
        multiplied_list = np.prod(multiply_small_polynomials)
        result += multiplied_list
    return result


range_to_interpolate = np.linspace(min_range, max_range, 10000)

y_calculated_by_function = []
for x in range_to_interpolate:
    y_calculated_by_function.append(function_to_interpolate(x))

y_calculated_by_newton_polymial = []
for x in range_to_interpolate:
    y_calculated_by_newton_polymial.append(calculate_x_from_newton_polynomial(x, lista))

error = [np.abs(x1 - x2) for (x1, x2) in zip(y_calculated_by_function, y_calculated_by_newton_polymial)]

print("Błąd maksymalny: ")
print(max(error))

plt.plot(range_to_interpolate, y_calculated_by_function, label='Original function')
plt.plot(range_to_interpolate, y_calculated_by_newton_polymial, label='Interpolated function')
plt.plot(range_to_interpolate, error, label='Error')
plt.legend()
plt.show()
