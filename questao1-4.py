'''
Implementar um filtro para simular o efeito de fotografias antigas por meio da aplicação de uma 
transformacão linear nas cores da imagem.
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('watch.png')

# Matriz de transformação sépia (valores originais)
sepia_matrix = np.array([
    [0.393, 0.769, 0.189],
    [0.349, 0.686, 0.168],
    [0.272, 0.534, 0.131]
])

# Aplicar a transformação: multiplicação matricial vetorizada
sepia_img = np.dot(img, sepia_matrix.T)  # shape (height, width, 3)

sepia_img = np.clip(sepia_img, 0, 255)

# Exibir a imagem
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(sepia_img)
plt.title('Efeito Sépiado')
plt.axis('off')

plt.tight_layout()
plt.show()