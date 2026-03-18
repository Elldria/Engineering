import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Wire dimensions
L = 61.0        # metres
d = 140e-6      # diameter (metres)
A = np.pi * (d / 2)**2   # cross-sectional area (m²)

# Data filtered to 30–50°C: (Temp, Resistance, DeltaT)
data = [
    (30.6, 68.72,  0.6),
    (33.6, 69.50,  3.6),
    (35.6, 70.66,  5.6),
    (37.1, 70.41,  7.1),
    (38.4, 71.14,  8.4),
    (40.1, 71.16, 10.1),
    (40.2, 71.56, 10.2),
    (42.1, 72.00, 12.1),
    (43.0, 71.82, 13.0),
    (44.5, 72.58, 14.5),
    (45.3, 72.38, 15.3),
    (47.0, 73.20, 17.0),
    (49.5, 73.80, 19.5),
    (50.5, 73.20, 20.5),
]

temps  = np.array([row[0] for row in data])
R_vals = np.array([row[1] for row in data])
dT     = np.array([row[2] for row in data])  # ΔT in K (same as ΔT in °C)

# Calculate resistivity: rho = R * A / L
rho = (R_vals * A) / L

# rho(T0) at 30 degrees
idx_T0 = np.argmin(np.abs(temps - 30.0))
rho_T0 = rho[idx_T0]

# Linear regression to get slope
slope, intercept, r_value, _, _ = stats.linregress(dT, rho)

# alpha = slope / rho(T0)
alpha = slope / rho_T0
literature = 0.00404  # K⁻¹

print(f"Measured α  = {alpha:.5f} K⁻¹")
print(f"Literature α = {literature} K⁻¹")
print(f"Difference:  {abs(alpha - literature)/literature * 100:.1f}%")

# Plot
fig, ax = plt.subplots(figsize=(8, 6))

ax.scatter(dT, rho, color="#1a4f72", s=60, zorder=5, label="Measured data")

dT_fit = np.linspace(0, 22, 200)
ax.plot(dT_fit, slope * dT_fit + intercept,
        color="#e05c2a", linewidth=2,
        label="Best fit")

ax.text(0.03, 0.97,
        f"y = {slope:.4e}x + {intercept:.4e}\n"
        f"Measured α = {alpha:.5f} K⁻¹\n"
        f"Literature α = {literature} K⁻¹",
        transform=ax.transAxes, fontsize=9,
        verticalalignment="top", fontfamily="monospace",
        bbox=dict(boxstyle="round,pad=0.5", facecolor="lightyellow",
                  edgecolor="grey", alpha=0.9))

ax.set_xlabel("ΔT (K)", fontsize=12)
ax.set_ylabel("Resistivity ρ (Ω·m)", fontsize=12)
ax.set_title("Resistivity (Ω·m) vs ΔT (30–50 °C)", fontsize=13, fontweight="bold")
ax.legend(fontsize=10)
ax.grid(True, linestyle="--", alpha=0.4)
ax.set_xlim(0, 22)

plt.tight_layout()
plt.show()