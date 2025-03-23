'''
Construir um mosaico de 4 × 4 blocos a partir de uma imagem monocromática. A disposição dos
blocos deve seguir a numeração mostrada na figura (c).
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('baboon_monocromatica.png')
altura, largura = img.shape
altura_bloco = altura // 4
largura_bloco = largura // 4

blocos = img.reshape(4, altura_bloco, 4, largura_bloco).transpose(0, 2, 1, 3)

nova_ordem = np.array([
    [6, 11, 13, 3],
    [8, 16, 1, 9],
    [12, 14, 2, 7],
    [4, 15, 10, 5]
])
nova_ordem = nova_ordem - 1

mosaico = blocos[nova_ordem//4, nova_ordem%4].transpose(0, 2, 1, 3).reshape(altura, largura)

# Plot original e mosaico
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(img, cmap=plt.get_cmap('gray'))
axs[0].set_title('Original')
axs[0].axis('off')

axs[1].imshow(mosaico, cmap=plt.get_cmap('gray'))
axs[1].set_title('Mosaico')
axs[1].axis('off')

plt.tight_layout()
plt.show()


