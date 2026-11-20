import matplotlib.pyplot as plt
import numpy as np

# Constantes físicas (mesmos valores do relatório em LaTeX)
k = 8.99e9    # N·m²/C²
q1 = 1e-6     # 1 µC (10^-6 C) para U(0,10 m) ≈ 0,09 J
q2 = 1e-6     # 1 µC (10^-6 C)

# Distâncias de 0,10 m até 1,00 m (passo de 0,01 m)
distancias = np.linspace(0.10, 1.00, 91)
energias = k * q1 * q2 / distancias

# Conferência r = 0,10 m
print(f"U(0,10 m) = {energias[0]:.6f} J")

plt.figure(figsize=(6, 4))
plt.plot(distancias, energias, color="tab:orange", linewidth=2, label=r"$q_1 = q_2 = 1\,\mu\mathrm{C}$")
plt.title("Energia Potencial Elétrica vs. Distância")
plt.xlabel("Distância r (m)")
plt.ylabel("Energia Potencial U (J)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("energia_potencial.png", dpi=150)
plt.close()
print("Gráfico salvo em energia_potencial.png!")