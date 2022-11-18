import matplotlib.pyplot as plt
import numpy as np

def complex_matrix(xmin, xmax, ymin, ymax, pixel_density):
    re = np.linspace(xmin, xmax, int((xmax - xmin) * pixel_density))
    im = np.linspace(ymin, ymax, int((ymax - ymin) * pixel_density))
    return re[np.newaxis, :] + im[:, np.newaxis] * 1j

def is_stable(z, num_iterations):
    c = -.4 + 0.6j
    for _ in range(num_iterations):
        z = z ** 2 + c
    return abs(z) <= 2

np.warnings.filterwarnings("ignore")

z = complex_matrix(-2, 2, -2, 2, pixel_density=512)
plt.imshow(is_stable(z, num_iterations=20), cmap="binary")
plt.show()