# Lennard-Jones Melting Simulation (lj_melt_lammps.ipynb)

A Lennard-Jones (LJ) system containing approximately 4,000 FCC atoms was simulated using LAMMPS to study the evolution of an initially ordered crystalline structure at high temperature.

# Simulation Details
- **Structure:** FCC
- **Number of atoms:** ~2,000
- **Initial temperature:** 3.0 LJ units
- **LJ potential:** lj/cut with cutoff = 2.5
- **Ensemble:** NVE
- **Simulation steps:** 1,000

# Analysis
The simulation output was used to analyze:

- **Thermodynamic properties:** Temperature, potential energy, total energy, and pressure.
- **Mean Squared Displacement (MSD):** Used to examine atomic mobility during the simulation.
- **Radial Distribution Function (RDF):** Used to analyze the structural arrangement and degree of order in the system.


