'''
Dada (a) uma imagem monocromatica, transformar seu espaco de intensidades (niveis de cinza)
para (b) obter o negativo da imagem, ou seja, o nivel de cinza 0 sera convertido para 255, o nivel
1 para 254 e assim por diante, (c) converter o intervalo de intensidades para [100, 200], (d)
inverter os valores dos pixels das linhas pares da imagem, ou seja, os valores dos pixels da linha 0
serao posicionados da direita para esquerda, os valores dos pixels da linha 2 ser ao posicionados da
direita para a esquerda e assim por diante, (e) espelhar as linhas da metade superior da imagem
na parte inferior da imagem e (f) aplicar um espelhamento vertical na imagem levando-se em
conta todas as linhas da imagem.
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = (mpimg.imread('city.png') * 255).astype(np.uint8)

fig, axs = plt.subplots(2, 3, figsize=(10, 6))
axs[0, 0].imshow(img, cmap='gray')
axs[0, 0].set_title('Original')
axs[0, 0].axis('off')

img_negativo = np.subtract(255, img)
axs[0, 1].imshow(img_negativo, cmap='gray')
axs[0, 1].set_title('Negativo')
axs[0, 1].axis('off')

imagem_ajustada = np.clip(img, 100, 200)
axs[0, 2].imshow(imagem_ajustada, cmap='gray')
axs[0, 2].set_title('Transformada [100,200]')
axs[0, 2].axis('off')

img_invertida = img.copy()
img_invertida[::2, :] = img_invertida[::2, ::-1]
axs[1, 0].imshow(img_invertida, cmap='gray')
axs[1, 0].set_title('Invertida')
axs[1, 0].axis('off')

img_espelhada = img.copy()
img_espelhada[img.shape[0]//2:, :] = img_espelhada[img.shape[0]//2 - 1 :: -1, :]
axs[1, 1].imshow(img_espelhada, cmap='gray')
axs[1, 1].set_title('Espelhada')
axs[1, 1].axis('off')

img_espelhada_vertical = img.copy()
img_espelhada_vertical = img_espelhada_vertical[::-1, :]
axs[1, 2].imshow(img_espelhada_vertical, cmap='gray')
axs[1, 2].set_title('Espelhada Vertical')
axs[1, 2].axis('off')

plt.tight_layout()
plt.show()