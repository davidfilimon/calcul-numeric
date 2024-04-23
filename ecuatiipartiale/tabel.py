import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
import pandas as pd

def f(x, y):
    return y * (1 - x)

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
steps = int((3 - x0) / h)  

x_exact = np.linspace(x0, 3, 1000)
y_exact = exact_solution(x_exact)

x_euler, y_euler = euler(f, x0, y0, h, steps)

x_rk4, y_rk4 = runge_kutta(f, x0, y0, h, steps)

errors_euler = np.abs(exact_solution(np.array(x_euler)) - np.array(y_euler))

errors_rk4 = np.abs(exact_solution(np.array(x_rk4)) - np.array(y_rk4))

xn_values = np.arange(1, 1.6, 0.1)
euler_errors_df = pd.DataFrame({
    'Xn': xn_values,
    'Yn (Euler)': [y_euler[int((xn - x0) / h)] for xn in xn_values],
    'Valoarea exacta': [exact_solution(xn) for xn in xn_values],
    'Eroare absoluta (Euler)': [errors_euler[int((xn - x0) / h)] for xn in xn_values]
})

rk4_errors_df = pd.DataFrame({
    'Xn': xn_values,
    'Yn (Runge-Kutta)': [y_rk4[int((xn - x0) / h)] for xn in xn_values],
    'Valoarea exacta': [exact_solution(xn) for xn in xn_values],
    'Eroare absoluta (Runge-Kutta)': [errors_rk4[int((xn - x0) / h)] for xn in xn_values]
})

def display_table(df, title):
    root = tk.Tk()
    root.title(title)
    
    tree = ttk.Treeview(root, columns=list(df.columns), show='headings')
    for col in df.columns:
        tree.heading(col, text=col)
    for i, row in df.iterrows():
        tree.insert("", "end", values=list(row))
    tree.pack(expand=True, fill='both')
    
    root.mainloop()

display_table(euler_errors_df, "Erori absolute pentru metoda Euler")
display_table(rk4_errors_df, "Erori absolute pentru metoda Runge-Kutta de ordinul patru")
