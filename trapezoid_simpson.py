import numpy as np

# Function to be integrated
def func(x):
    return eval(user_function)

# Trapezoidal rule
def trapezoidal_rule(a, b, n):
    h = (b - a) / n
    integral = (func(a) + func(b)) / 2
    for i in range(1, n):
        integral += func(a + i * h)
    integral *= h
    return integral

# Simpson's 1/3 rule
def simpsons_one_third_rule(a, b, n):
    h = (b - a) / n
    integral = func(a) + func(b)
    for i in range(1, n, 2):
        integral += 4 * func(a + i * h)
    for i in range(2, n-1, 2):
        integral += 2 * func(a + i * h)
    integral *= h / 3
    return integral

# Simpson's 3/8 rule
def simpsons_three_eighth_rule(a, b, n):
    h = (b - a) / n
    integral = func(a) + func(b)
    for i in range(1, n):
        integral += 3 * func(a + i * h)
    integral *= 3 * h / 8
    return integral

# Get user input for function and integration limits
user_function = input("Enter the function to integrate (use 'np.' for numpy functions): ")
a = float(input("Enter the lower limit of integration: "))
b = float(input("Enter the upper limit of integration: "))
n = int(input("Enter the number of subintervals (even for Simpson's rules, multiple of 3 for 3/8 rule): "))

# Evaluate integrals using different rules
result_trapezoidal = trapezoidal_rule(a, b, n)
result_simpsons_one_third = simpsons_one_third_rule(a, b, n)
result_simpsons_three_eighth = simpsons_three_eighth_rule(a, b, n)

# Print the results
print("Trapezoidal Rule:", result_trapezoidal)
print("Simpson's 1/3 Rule:", result_simpsons_one_third)
print("Simpson's 3/8 Rule:", result_simpsons_three_eighth)
