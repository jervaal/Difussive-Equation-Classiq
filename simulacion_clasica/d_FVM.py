import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

def solve_advection_fvm_central(x, u, Nx, Nt, dx, dt, a, uL, uR, filename):
    for n in tqdm(range(Nt)):
        with open(f"{filename}_FVM.txt", "a") as file:
            for i in range(len(x)):
                file.write(f"{x[i]}\t{u[i]}\n")
            file.write("\n")
        u_next = np.copy(u)
        for i in range(1, Nx - 1):  # Iterar sobre las celdas (excepto en los bordes)
            flux_left = 0.5 * a * (u[i - 1]  + u[i]) # Flujo en el borde izquierdo
            flux_right = 0.5 * a * (u[i] + u[i + 1])    # Flujo en el borde derecho
            u_next[i] = u[i] - dt / dx * (flux_right - flux_left) 
        
        # Condiciones de borde
        u_next[0] = uL
        u_next[-1] = uR

        u = u_next

def solve_advection_fvm_upwind(x, u, Nx, Nt, dx, dt, a, uL, uR, filename):
    for n in tqdm(range(Nt)):
        with open(f"{filename}_FVM.txt", "a") as file:
            for i in range(len(x)):
                file.write(f"{x[i]}\t{u[i]}\n")
            file.write("\n")
        u_next = np.copy(u)
        for i in range(1, Nx - 1):  # Iterar sobre las celdas (excepto en los bordes)
            flux_left = a * u[i - 1] # Flujo en el borde izquierdo
            flux_right = a * u[i]  # Flujo en el borde derecho
            u_next[i] = u[i] - dt / dx * (flux_right - flux_left) 
        
        # Condiciones de borde
        u_next[0] = uL
        u_next[-1] = uR

        u = u_next

def main():
    # Parámetros
    L = 128.0          # Longitud del dominio
    T = 20.0          # Tiempo total 
    dt = 0.01
    Nx = 128         # Número de celdas espaciales
    v = 10.0          # Velocidad de advección
    dx = L / Nx      # Tamaño de celda
    Nt = int(T / dt)    # Paso de tiempo
    x = np.linspace(0, L, Nx)  # Puntos del centro de cada celda
    # Discretización
    dx = L / (Nx - 1)
    dt = T / Nt
    c = v * dt / dx   # Número de Courant (debe cumplir c <= 1 para estabilidad)
    # Verificación de estabilidad CFL
    CFL = v * dt / dx
    if CFL > 1:
        raise ValueError("El número de Courant debe ser ≤ 1 para estabilidad.")
    # Condición de borde de Dirichlet
    uL, uR = 0.0, 0.0
    u = np.where((x > 0.01 * Nx) & (x < 0.11 * Nx), 1.0, 0.0) # Perfil Inicial

    central_fn = "centered"
    upwind_fn = "forward"
    solve_advection_fvm_central(x, u, Nx, Nt, dx, dt, v, uL, uR, central_fn)
    solve_advection_fvm_upwind(x, u, Nx, Nt, dx, dt, v, uL, uR, upwind_fn)

main()