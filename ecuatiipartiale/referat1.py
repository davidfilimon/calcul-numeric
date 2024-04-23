import numpy as np
import matplotlib.pyplot as plt

# Subpunctul a
def diff_eq(T, t, r):
    return r * T

# Subpunctul b
def euler_method(T0, r, dt, num_years):
    T_values = [T0]
    t_values = [0]
    for i in range(int(num_years / dt)):
        T = T_values[-1]
        dT = diff_eq(T, t_values[-1], r) * dt
        T_values.append(T + dT)
        t_values.append(t_values[-1] + dt)
    return t_values, T_values

# Subpunctul c
def plot_population(t_values, T_values, title):
    plt.plot(t_values, T_values, label='Numar de tigri')
    plt.xlabel('Timp (ani)')
    plt.ylabel('Numar de tigri')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

# Subpunctul d
def find_time_for_population(t_values, T_values, target_population):
    for t, T in zip(t_values, T_values):
        if T >= target_population:
            return t

# Setarea datelor inițiale
T0 = 50  # numar initial de tigri
dt = 1    # pasul de timp (ani)
num_years = 20  # intervalul de timp pentru care vom calcula evolutia populatiei
target_population = 100  # populatia tinta

# Subpunctul e
r1 = 0.07  # rata 1 de crestere
r2 = 0.1   # rata 2 de crestere

t_values1, T_values1 = euler_method(T0, r1, dt, num_years)
plot_population(t_values1, T_values1, 'Evolutia populatiei de tigri (7% crestere pe an)')

time_to_target1 = find_time_for_population(t_values1, T_values1, target_population)
print(f"Populatia de tigri ajunge la {target_population} de indivizi dupa aproximativ {time_to_target1:.2f} ani pentru rata de crestere de 7% pe an.")

t_values2, T_values2 = euler_method(T0, r2, dt, num_years)
plot_population(t_values2, T_values2, 'Evolutia populatiei de tigri (10% crestere pe an)')

time_to_target2 = find_time_for_population(t_values2, T_values2, target_population)
print(f"Populatia de tigri ajunge la {target_population} de indivizi dupa aproximativ {time_to_target2:.2f} ani pentru rata de crestere de 10% pe an.")

print("Concluzie:")
if time_to_target1 < time_to_target2:
    print("Rata de crestere de 7% pe an duce la atingerea populatiei tinta mai repede decat rata de crestere de 10% pe an.")
elif time_to_target1 > time_to_target2:
    print("Rata de crestere de 10% pe an duce la atingerea populatiei tinta mai repede decat rata de crestere de 7% pe an.")
else:
    print("Ambele rate de crestere duc la atingerea populatiei tinta in acelasi timp.")
