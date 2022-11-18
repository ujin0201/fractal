import matplotlib.pyplot as plt
import numpy as np

def complex_matrix(xmin, xmax, ymin, ymax, pixel_density):
    re = np.linspace(xmin, xmax, int((xmax - xmin) * pixel_density)) # 2.5 * 512 
    im = np.linspace(ymin, ymax, int((ymax - ymin) * pixel_density)) # 3 * 512
    return re[np.newaxis, :] + im[:, np.newaxis] * 1j # 1j는 복소수 i의 python식 표현

def is_stable(c, num_iterations):
    z = 0
    for _ in range(num_iterations):
        z = z ** 2 + c
    return abs(z) <= 2

np.warnings.filterwarnings("ignore")

c = complex_matrix(-2, 0.5, -1.5, 1.5, pixel_density=512)
plt.imshow(is_stable(c, num_iterations=20), cmap="binary")
plt.show()