import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Beam parameters
# -----------------------------
L = 1.0                 # Beam length (m)
mass = 10               # Mass (kg)
g = 9.81
P = mass * g            # Load (N)

E = 200e9               # Young's modulus (Pa) - steel
I = 1.0e-6              # Second moment of area (m^4)

# -----------------------------
# Position along the beam
# -----------------------------
x = np.linspace(0, L, 500)

# -----------------------------
# Deflection equation
# -----------------------------
y = (P * x**2 / (6 * E * I)) * (3 * L - x)

# -----------------------------
# Plot deflection
# -----------------------------
plt.figure()
plt.plot(x, y)
plt.xlabel("Position along beam (m)")
plt.ylabel("Deflection (m)")
plt.title("Deflection of Cantilever Beam with 10 kg Load")
plt.grid(True)
plt.show()

# -----------------------------
# Maximum deflection
# -----------------------------
max_deflection = (P * L**3) / (3 * E * I)
print(f"Maximum deflection at free end: {max_deflection:.6e} m")
