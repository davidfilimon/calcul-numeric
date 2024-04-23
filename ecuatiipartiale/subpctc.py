import numpy as np
from scipy.integrate import solve_bvp
import matplotlib.pyplot as plt

def ode(t, x):
    return np.vstack((x[1], np.sin(t) + np.cos(t)))

def bc(xa, xb):
    return np.array([xa[0], xb[0] - 1])

# Alegem punctele pentru care calculăm soluția
t_values = np.linspace(0, 10, 100)

# Alegem o estimare inițială pentru soluție
x_guess = np.zeros((2, t_values.size))

# Rezolvăm problema BVP
sol = solve_bvp(ode, bc, t_values, x_guess)

# Rezultatele sunt stocate în sol.sol(t)
t_plot = np.linspace(0, 10, 1000)
x_plot = sol.sol(t_plot)

# Desenăm graficul soluției
plt.figure(figsize=(8, 6))
plt.plot(t_plot, x_plot[0], label='$x(t)$')
plt.xlabel('$t$')
plt.ylabel('$x(t)$')
plt.title('Solution of $\\frac{dx}{dt} = \sin(t) + \cos(t)$')
plt.legend()
plt.grid(True)
plt.show()
