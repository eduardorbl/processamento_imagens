'''
Dada uma imagem colorida no formato RGB, alterar a imagem conforme as seguintes
operacões

Dada uma imagem colorida no formato RGB, alterar a imagem tal que ela contenha apenas
uma banda de cor, cujos valores sao calculados pela média ponderada:
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('watch.png')

sepia_matrix = np.array([
    [0.393, 0.769, 0.189],
    [0.349, 0.686, 0.168],
    [0.272, 0.534, 0.131]
])

sepia_img = np.dot(img, sepia_matrix.T)  # shape (height, width, 3)

sepia_img = np.clip(sepia_img, 0, 255)

# Exibir a imagem
plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.imshow(img)
plt.title('Original')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(sepia_img)
plt.title('Efeito aplicado')
plt.axis('off')

gray = np.dot(img, [0.299, 0.587, 0.114])
gray = np.clip(gray, 0, 255)

plt.subplot(1, 3, 3)
plt.imshow(gray, cmap=plt.get_cmap('gray'))
plt.title('Escala de cinza')
plt.axis('off')

plt.tight_layout()
plt.show()