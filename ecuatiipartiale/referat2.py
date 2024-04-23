import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return y * (1 - x)

# metoda Euler
def euler(f, x0, y0, h, steps):
    x_values = [x0]
    y_values = [y0]
    x = x0
    y = y0
    for _ in range(steps):
        y += h * f(x, y)
        x += h
        x_values.append(x)
        y_values.append(y)
    return x_values, y_values

# metoda Runge-Kutta de ordinul 4
def runge_kutta(f, x0, y0, h, steps):
    x_values = [x0]
    y_values = [y0]
    x = x0
    y = y0
    for _ in range(steps):
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)
        y += (k1 + 2*k2 + 2*k3 + k4) / 6
        x += h
        x_values.append(x)
        y_values.append(y)
    return x_values, y_values

def exact_solution(x):
    return 0.1 * np.exp(-0.5 * x**2 + x)

x0 = 0
y0 = 0.1
h = 0.01  
x_max = 1.5  # Setăm valoarea maximă pentru x
steps = int((x_max - x0) / h)  

x_exact = np.linspace(x0, x_max, 1000)
y_exact = exact_solution(x_exact)

x_euler, y_euler = euler(f, x0, y0, h, steps)

x_rk4, y_rk4 = runge_kutta(f, x0, y0, h, steps)

fig, axs = plt.subplots(3, 1, figsize=(10, 18))

axs[0].plot(x_exact, y_exact, label='Solutia exacta')
axs[0].plot(x_euler, y_euler, label='Metoda lui Euler')
axs[0].set_xlabel('x')
axs[0].set_ylabel('y')
axs[0].set_title('Metoda lui Euler')
axs[0].legend()
axs[0].grid(True)

axs[1].plot(x_exact, y_exact, label='Solutia exacta')
axs[1].plot(x_rk4, y_rk4, label='Metoda Runge-Kutta de ordinul patru')
axs[1].set_xlabel('x')
axs[1].set_ylabel('y')
axs[1].set_title('Metoda Runge-Kutta de ordinul patru')
axs[1].legend()
axs[1].grid(True)

axs[2].plot(x_exact, y_exact, label='Solutia exacta')
axs[2].plot(x_euler, y_euler, label='Metoda lui Euler')
axs[2].plot(x_rk4, y_rk4, label='Metoda Runge-Kutta de ordinul patru')
axs[2].set_xlabel('x')
axs[2].set_ylabel('y')
axs[2].set_title('Comparatie intre metode')
axs[2].legend()
axs[2].grid(True)

plt.tight_layout()
plt.show()
