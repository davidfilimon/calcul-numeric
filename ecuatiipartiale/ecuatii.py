import numpy as np
from scipy.integrate import solve_bvp
import matplotlib.pyplot as plt

def fun(t, x, epsilon, mu):
    dx0 = x[1]
    dx1 = (np.sin(t) + np.cos(t) - x[0]**7 - x[1] * mu) / (-epsilon)
    return np.vstack((dx0, dx1))

def fun_epsilon_zero(t, x):
    return np.vstack((x[1],(np.sin(t) + np.cos(t) - x[0]**7)))

def bc(xa, xb):
    return np.array([xa[0], xb[0]])

t_span = np.array([0, np.pi])
t_values = np.linspace(0, np.pi, 400)

def difference(t):
    return np.log(t) - (np.sin(t) + np.cos(t))**(1/7)

subpoints = [
    [{'epsilon': 0, 'mu': 1}, {'epsilon': 1/100, 'mu': 1}],
    [{'epsilon': 1, 'mu': 0}, {'epsilon': 1, 'mu': 1/100}],
    [{'epsilon': 1/100, 'mu': 1/100}]
]

fig, axs = plt.subplots(4, 1, figsize=(8, 16))

for i, subpoint_set in enumerate(subpoints, start=1):
    for j, subpoint in enumerate(subpoint_set, start=1):
        if subpoint['epsilon'] == 0:
            sol = solve_bvp(fun_epsilon_zero, bc, t_span, np.zeros((2, t_span.size)))
        else:
            sol = solve_bvp(lambda t, x: fun(t, x, subpoint['epsilon'], subpoint['mu']), bc, t_span, np.zeros((2, t_span.size)))
        t_plot = np.linspace(t_span[0], t_span[1], 100)
        x_plot = sol.sol(t_plot)[0]
        axs[i-1].plot(t_plot, x_plot, label=f'Setul {j}: epsilon={subpoint["epsilon"]}, mu={subpoint["mu"]}')
    axs[i-1].set_xlabel('t')
    axs[i-1].set_ylabel('x(t)')
    axs[i-1].set_title(f'Subpunctul {i}')
    axs[i-1].legend()
    axs[i-1].grid()

    def fundamental_solution(t, epsilon, mu):
        return np.sqrt((np.sin(t) + np.cos(t) - 1**7 - mu) / epsilon)

    fundamental_sol = fundamental_solution(t_values, subpoint['epsilon'], subpoint['mu'])

    axs[3].plot(t_values, fundamental_sol, label=f'Subpunctul {i}: epsilon={subpoint["epsilon"]}, mu={subpoint["mu"]}')

axs[3].set_xlabel('t')
axs[3].set_ylabel('Sistemul fundamental de soluții')
axs[3].set_title('Sistemul fundamental de soluții pentru primul set de subpuncte')
axs[3].legend()
axs[3].grid()

plt.tight_layout()
plt.show()
