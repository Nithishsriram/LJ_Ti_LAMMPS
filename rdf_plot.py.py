import numpy as np
import matplotlib.pyplot as plt

filename = "rdf.dat"

blocks = []

with open(filename, "r") as f:
    lines = f.readlines()

i = 0

while i < len(lines):

    line = lines[i].strip()

    # Ignore comments and empty lines
    if not line or line.startswith("#"):
        i += 1
        continue

    parts = line.split()

    # Header of each RDF block:
    # timestep number_of_rows
    if len(parts) == 2:
        try:
            timestep = int(parts[0])
            nrows = int(parts[1])

            block = []

            for j in range(i + 1, i + 1 + nrows):
                values = list(map(float, lines[j].split()))
                block.append(values)

            blocks.append((timestep, np.array(block)))

            i += nrows + 1
            continue

        except ValueError:
            pass

    i += 1


if len(blocks) == 0:
    raise RuntimeError("No RDF blocks found in rdf.dat")


# Select final RDF block
timestep, rdf = blocks[-1]

# Typical columns:
# 0 = bin number
# 1 = distance r
# 2 = g(r)
# 3 = coordination number

r = rdf[:, 1]
g_r = rdf[:, 2]


plt.figure(figsize=(7, 5))

plt.plot(r, g_r, linewidth=2)

plt.xlabel(r"Distance, $r/\sigma$")
plt.ylabel(r"$g(r)$")
plt.title(f"Radial Distribution Function - Step {timestep}")

plt.axhline(y=1.0, linestyle="--", linewidth=1)

plt.grid(alpha=0.3)
plt.tight_layout()

plt.savefig("rdf.png", dpi=300)
plt.show()