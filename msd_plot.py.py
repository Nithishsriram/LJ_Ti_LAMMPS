import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("msd.dat", comments="#")

step = data[:, 0]
msd_x = data[:, 1]
msd_y = data[:, 2]
msd_z = data[:, 3]
msd_total = data[:, 4]

plt.figure(figsize=(7, 5))

plt.plot(step, msd_x, label="MSD x")
plt.plot(step, msd_y, label="MSD y")
plt.plot(step, msd_z, label="MSD z")
plt.plot(step, msd_total, label="Total MSD", linewidth=2)

plt.xlabel("Timestep")
plt.ylabel(r"Mean Squared Displacement ($\sigma^2$)")
plt.title("Mean Squared Displacement")
plt.legend()
plt.grid(alpha=0.3)

plt.tight_layout()
plt.savefig("msd.png", dpi=300)
plt.show()