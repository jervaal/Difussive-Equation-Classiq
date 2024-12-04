import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

# Parámetros
L = 128.0           # Longitud del dominio
T = 20           # Tiempo total
v = 1.0           # Velocidad de advección
Nx = 128          # Número de puntos espaciales
Nt = 2000          # Número de pasos temporales
u_L, u_R = 0.0, 0.0  # Condiciones de Dirichlet

# Discretización
dx = L / (Nx - 1)
dt = T / Nt
c = v * dt / dx   # Número de Courant (debe cumplir c <= 1 para estabilidad)

# Condición inicial
x = np.linspace(0, L, Nx)
u = np.zeros(Nx)
u[int(0.25 * Nx):int(0.35 * Nx)] = 1.0  # Pulso inicial

# Resolver la ecuación
for n in tqdm(range(int(Nt))):
    with open("data_Euler_centered.txt", "a") as file:
        for i in range(len(x)):
            file.write(f"{x[i]}\t{u[i]}\n")
        file.write("\n")
    u_new = np.copy(u)
    for j in range(1, Nx-1):  # Esquema de diferencias finitas
        #u_new[j] = u[j] - c * (u[j] - u[j-1])         # Forward
        u_new[j] = u[j] - c * (u[j + 1] - u[j-1]) / 2   # Centered
    # Condiciones de Dirichlet
    u_new[0] = u_L
    u_new[-1] = u_R
    u = u_new