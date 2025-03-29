'''
Quantização refere-se ao número de níveis de cinza usados para representar uma 
imagem monocromática. A quantização está relacionada à profundidade de uma imagem,
a qual corresponde ao número de bits necessários para armazenar a imagem.
Representar uma imagem com diferentes níveis de quantização.
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Carrega a imagem e converte para uint8 (0-255)
img = (mpimg.imread('baboon_monocromatica.png') * 255).astype(np.uint8)

# Níveis de quantização e bits correspondentes
niveis = [64, 32, 16, 8, 4, 2]
mascaras = [0b11111100, 0b11111000, 0b11110000, 0b11100000, 0b11000000, 0b10000000]

fig, axs = plt.subplots(3, 3, figsize=(10, 6))
axs[0,0].axis('off')
axs[0,2].axis('off')
axs[0,1].imshow(img, cmap='gray')
axs[0,1].set_title('Original: 256 níveis')
axs[0,1].axis('off')

for i, nivel in enumerate(niveis):
    # Aplica a máscara de quantização e ajusta os níveis de cinza usando numpy
    img_quantizada = np.bitwise_and(img, mascaras[i])
    img_quantizada = np.uint8(img_quantizada * (255 / mascaras[i]))
    
    axs[i//3 + 1, i%3].imshow(img_quantizada, cmap='gray')
    axs[i//3 + 1, i%3].set_title(f'{nivel} níveis')
    axs[i//3 + 1, i%3].axis('off')
plt.tight_layout()
plt.show()