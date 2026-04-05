import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

# create x values
x = np.linspace(-10, 10, 100)

# functions
def plot_sin():
    plt.plot(x, np.sin(x))
    plt.title("sin(x)")
    plt.grid()
    plt.show()

def plot_cos():
    plt.plot(x, np.cos(x))
    plt.title("cos(x)")
    plt.grid()
    plt.show()

def plot_square():
    plt.plot(x, x**2)
    plt.title("x^2")
    plt.grid()
    plt.show()

def plot_cube():
    plt.plot(x, x**3)
    plt.title("x^3")
    plt.grid()
    plt.show()

# create window
root = tk.Tk()
root.title("Math Graph Visualizer")

# buttons
tk.Button(root, text="sin(x)", command=plot_sin).pack()
tk.Button(root, text="cos(x)", command=plot_cos).pack()
tk.Button(root, text="x^2", command=plot_square).pack()
tk.Button(root, text="x^3", command=plot_cube).pack()

# run window
root.mainloop()
