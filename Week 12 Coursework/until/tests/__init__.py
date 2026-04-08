"""
Timing and plotting code for the until test subpackage.

When this subpackage is imported, it measures the average initialisation
time of Grid, UniformGrid, NTiL, and UNTiL on a collection of valid sample
occupancy lists, then displays the results on a log-log plot.

The sample data are taken from samples.py, and the side length n of each
grid is inferred from the fact that each sample contains exactly 2n
occupied cells.
"""

from timeit import timeit
import matplotlib.pyplot as plt

from .samples import until_occupancies
from ..grids import Grid, UniformGrid, NTiL, UNTiL

n_values = [len(occupancies) // 2 for occupancies in until_occupancies]

grid_times = []
uniform_times = []
ntil_times = []
until_times = []

num_runs = 100

for n, occupancies in zip(n_values, until_occupancies):
    grid_times.append(
    timeit(lambda: Grid(n, occupancies.copy()), number=num_runs) / num_runs
    )
    uniform_times.append(
        timeit(lambda: UniformGrid(n, occupancies.copy()), number=num_runs) / num_runs
    )
    ntil_times.append(
        timeit(lambda: NTiL(n, occupancies.copy()), number=num_runs) / num_runs
    )
    until_times.append(
        timeit(lambda: UNTiL(n, occupancies.copy()), number=num_runs) / num_runs
    )

plt.loglog(n_values, grid_times, marker="o", label="Grid: O(n^2)")
plt.loglog(n_values, uniform_times, marker="o", label="UniformGrid: O(n^2)")
plt.loglog(n_values, ntil_times, marker="o", label="NTiL: O(n^3)")
plt.loglog(n_values, until_times, marker="o", label="UNTiL: O(n^3)")

plt.xlabel("Side-length n")
plt.ylabel("Average initialisation time (seconds)")
plt.title("Initialisation runtimes for grid classes")
plt.legend()
plt.grid(True)
plt.show()