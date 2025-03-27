'''
Combinar duas imagens monocromaticas de mesmo tamanho por meio da media ponderada de
seus niveis de cinza.
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img1 = mpimg.imread('baboon_monocromatica.png')
img2 = mpimg.imread('butterfly.png')


weights = np.linspace(0.1, 0.9, 9)
img_combinadas = img1[:, :, None] * (1 - weights) + img2[:, :, None] * weights
img_combinadas = np.moveaxis(img_combinadas, -1, 0)

fig, axs = plt.subplots(3, 3, figsize=(10, 10))

for i, img in enumerate(img_combinadas):
    axs[i // 3, i % 3].imshow(img, cmap='gray')
    axs[i // 3, i % 3].set_title(f'Baboon: {1 - weights[i]:.1f}, Butterfly: {weights[i]:.1f}')
    axs[i // 3, i % 3].axis('off')
plt.tight_layout()
plt.show()
