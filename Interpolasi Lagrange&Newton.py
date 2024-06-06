import numpy as np
import matplotlib.pyplot as plt

# Data titik yang diberikan
x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# Fungsi untuk Polinom Lagrange
def lagrange_polynomial(x, y, x_new):
    total = 0
    n = len(x)
    for i in range(n):
        xi, yi = x[i], y[i]
        def L(i):
            terms = [((x_new - x[j]) / (xi - x[j])) for j in range(n) if j != i]
            return np.prod(terms, axis=0)
        total += yi * L(i)
    return total

# Fungsi untuk Polinom Newton
def newton_polynomial(x, y, x_new):
    def divided_diff(x, y):
        n = len(y)
        coef = np.zeros([n, n])
        coef[:,0] = y
        for j in range(1, n):
            for i in range(n-j):
                coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j] - x[i])
        return coef[0, :]
    
    def newton_poly(coef, x_data, x_new):
        n = len(x_data) - 1
        p = coef[n]
        for k in range(1, n+1):
            p = coef[n-k] + (x_new - x_data[n-k]) * p
        return p
    
    # Hitung koefisien beda terbagi
    coef = divided_diff(x, y)
    # Hitung nilai polinom di x_new
    return newton_poly(coef, x, x_new)

# Testing kode
x_new = np.linspace(5, 40, 100)
y_lagrange = lagrange_polynomial(x, y, x_new)
y_newton = newton_polynomial(x, y, x_new)

# Plot grafik hasil interpolasi
fig, axs = plt.subplots(1, 2, figsize=(15, 5))

# Grafik untuk Interpolasi Lagrange
axs[0].plot(x, y, 'ro', label='Data Asli')
axs[0].plot(x_new, y_lagrange, 'b-', label='Interpolasi Lagrange')
axs[0].set_title('Interpolasi Polinom Lagrange')
axs[0].set_xlabel('Tegangan (kg/mm^2)')
axs[0].set_ylabel('Waktu Patah (jam)')
axs[0].legend()

# Grafik untuk Interpolasi Newton
axs[1].plot(x, y, 'ro', label='Data Asli')
axs[1].plot(x_new, y_newton, 'g--', label='Interpolasi Newton')
axs[1].set_title('Interpolasi Polinom Newton')
axs[1].set_xlabel('Tegangan (kg/mm^2)')
axs[1].legend()

axs[1].text(1.01, 0.5, 'Adi Nur Fi Yan\n21120122120010', transform=axs[1].transAxes, ha='left', va='center')
plt.show()
