'''
1.1 Esboço a Lápis
Implementar um efeito de esboço a lápis em uma imagem por meio dos seguintes passos: 
(i) converter a imagem colorida para níveis de cinza, 
(ii) aplicar um filtro de desfoque gaussiano (por exemplo, com uma máscara de 21×21 pixels) para suavizar os detalhes da imagem e 
(iii) dividir a imagem em tons de cinza pela versão desfocada para realçar os contornos.
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.ndimage import gaussian_filter

img = mpimg.imread('watch.png')

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

gray = rgb2gray(img)
blurred = gaussian_filter(gray, sigma=20/3)

fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Subplot 1: Imagem em tons de cinza
axs[0].imshow(gray, cmap=plt.get_cmap('gray'))
axs[0].set_title('Tons de Cinza')
axs[0].axis('off')

# Subplot 2: Imagem desfocada
axs[1].imshow(blurred, cmap=plt.get_cmap('gray'))
axs[1].set_title('Imagem Desfocada')
axs[1].axis('off')

# Subplot 3: Imagem em tons de cinza dividida pela imagem desfocada
result = gray / blurred
result = np.clip(result, 0, 1)
axs[2].imshow(result, cmap=plt.get_cmap('gray'))
axs[2].set_title('Imagem em Tons de Cinza Dividida pela Imagem Desfocada')
axs[2].axis('off')

plt.tight_layout()
plt.show()