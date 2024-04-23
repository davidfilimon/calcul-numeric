import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp

def equation(t, x, epsilon, mu):
    dx0 = x[1]  
    dx1 = (mu * x[1] - epsilon * x[0]**7 + np.sin(t) + np.cos(t)) / (-epsilon)  
    return np.vstack((dx0, dx1))

def equationc(t, x, epsilon, mu):
    dx0 = x[1]  
    ln = (np.sin(t)+np.cos(t))//7
    dx1 = (mu * x[1] - epsilon * x[0]**7 + ln**7) / (-epsilon)
    return np.vstack((dx0, dx1))

def boundary_conditions(xa, xb, epsilon, mu):
    return np.array([xa[0], xb[0]])  # modificam conditiile la limita ca sa ne asiguram ca sunt functiile ok

t_span = (0, np.pi) 
t_values = np.linspace(t_span[0], t_span[1], 100)

# Valori
cases = [
    (1, 1), # subpunctul a + b unde epsilon = mu = 1
    (1/100, 1), # subpunctul a
    (1, 1/100), # subpunctul b
    (1/100, 1/100)  # subpunctul c
]

plt.figure(figsize=(10, 7))

for i, (epsilon, mu) in enumerate(cases, start=1):
    if i == 4:  # pentru subpunctul c, folosim ecuatia equationc
        sol = solve_bvp(lambda t, x: equationc(t, x, epsilon, mu), 
                        lambda xa, xb: boundary_conditions(xa, xb, epsilon, mu), 
                        t_values, 
                        np.zeros((2, t_values.size)), 
                        verbose=2)
    else:
        sol = solve_bvp(lambda t, x: equation(t, x, epsilon, mu), 
                        lambda xa, xb: boundary_conditions(xa, xb, epsilon, mu), 
                        t_values, 
                        np.zeros((2, t_values.size)), 
                        verbose=2)
    
    plt.plot(sol.x, sol.y[0], label=f'$\\epsilon={epsilon}$, $\\mu={mu}$')

plt.xlabel('t') 
plt.ylabel('x(t)')
plt.legend()
plt.grid(True)
plt.title('Solutiile pentru toate subpunctele')
plt.show()
