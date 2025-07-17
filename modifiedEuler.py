import matplotlib.pyplot as plt

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

def plot_results(x_values, y_values):
    plt.plot(x_values, y_values, marker='o', linewidth=2)
    plt.title('Modified Euler Method Results')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.show()

x_results, y_results = modified_euler(lambda x, y: (y**2 - x**2) / (y**2 + x**2), 0, 1, 1, 20)

plot_results(x_results, y_results)
for x, y in zip(x_results, y_results):
    print(f"{x:.4f} \t {y:.4f}")