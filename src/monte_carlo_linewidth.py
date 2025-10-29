import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

n = 10000
mod_freq = 110  # Hz
base_delta_lambda = 0.1  # nm
gain = 1e5  # Q-analog

time = np.linspace(0, 0.1, n)
linewidth = base_delta_lambda / gain * (1 + 0.01 * np.sin(2*np.pi*mod_freq*time) + norm.rvs(0, 0.001, n))
flux = 1e18 * (1 + 0.002 * np.sin(2*np.pi*mod_freq*time) + norm.rvs(0, 0.0001, n))
tau_proxy = 1 / np.mean(np.abs(np.diff(linewidth))) * 1e6  # μs

print(f"Mean linewidth: {np.mean(linewidth):.4f} nm (std {np.std(linewidth):.4f})")
print(f"Flux mean: {np.mean(flux):.2e} photons/s (std {np.std(flux):.2e})")
print(f"τ proxy: {tau_proxy:.2f} μs")

# Plot
fig, ax1 = plt.subplots()
ax1.plot(time, linewidth * 1e3, 'b-', label='Linewidth (pm)')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Linewidth (pm)', color='b')
ax1.tick_params(axis='y', labelcolor='b')

ax2 = ax1.twinx()
ax2.plot(time, flux / 1e18, 'r-', label='Flux (norm)')
ax2.set_ylabel('Flux (normalized)', color='r')
ax2.tick_params(axis='y', labelcolor='r')

plt.title('Linewidth Narrowing Simulation')
plt.savefig('outputs/linewidth.png')
plt.show()
