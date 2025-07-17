import matplotlib.pyplot as plt

def backward_euler(f, x0, y0, xn, n):
    x = x0
    y = y0
    h = (xn - x0) / n

    x_values = [x0]
    y_values = [y0]

    for i in range(n):
        y1 = y + h * (f(x, y))
        y = y + h * (f(x + h, y1))
        x = x + h
        x_values.append(x)
        y_values.append(y)

    return x_values, y_values

def modified_euler(f, x0, y0, xn, n):
    x = x0
    y = y0
    h = (xn - x0) / n

    x_values = [x0]
    y_values = [y0]

    for i in range(n):
        y1 = y + h * f(x, y)
        y = y + (h / 2) * (f(x, y) + f(x + h, y1))
        x = x + h
        x_values.append(x)
        y_values.append(y)

    return x_values, y_values

def plot_results(x1, y1, x2, y2):
    plt.plot(x1, y1, marker='o', linewidth=2, label='Backward Euler')
    plt.plot(x2, y2, marker='s', linewidth=2, label='Modified Euler')
    plt.title('Backward Euler vs Modified Euler')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.legend()
    plt.show()

x_results, y_results = backward_euler(lambda x, y: (y**2 - x**2) / (y**2 + x**2), 0, 1, 1, 20)
x_results_mod, y_results_mod = modified_euler(lambda x, y: (y**2 - x**2) / (y**2 + x**2), 0, 1, 1, 20)

plot_results(x_results, y_results, x_results_mod, y_results_mod)

for x, y in zip(x_results, y_results):
    print(f"Backward Euler: {x:.4f} \t {y:.4f}")

for x, y in zip(x_results_mod, y_results_mod):
    print(f"Modified Euler: {x:.4f} \t {y:.4f}")