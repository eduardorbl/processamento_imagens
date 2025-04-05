import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img1 = np.array(Image.open('baboon_monocromatica.png').convert('L'))
img2 = np.array(Image.open('butterfly.png').convert('L'))

weights = np.linspace(0.1, 0.9, 9)
img_combinadas = np.add(np.multiply(img1[:, :, None], (1 - weights)), np.multiply(img2[:, :, None], weights))
img_combinadas = np.moveaxis(img_combinadas, -1, 0)

fig, axs = plt.subplots(3, 3, figsize=(10, 10))

for i, img in enumerate(img_combinadas):
    axs[i // 3, i % 3].imshow(img, cmap='gray')
    axs[i // 3, i % 3].set_title(f'Baboon: {1 - weights[i]:.1f}, Butterfly: {weights[i]:.1f}')
    axs[i // 3, i % 3].axis('off')
plt.tight_layout()
plt.show()
