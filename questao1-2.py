'''
Aplicar a correção gama para ajustar o brilho de uma imagem monocromática A de entrada e gerar
uma imagem monocromática B de saída. A transformação pode ser realizada (i) convertendo
as intensidades dos pixels do intervalo [0, 255] para [0, 1], (ii) aplicando a equação
B = A^(1/γ) e (iii) convertendo os valores resultantes de volta para o intervalo [0, 255]. Realizar
a correção com diferentes valores de γ.
'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def correct_gamma(img, gamma):
    img = np.clip(img, 0, 1)
    img = img ** (1 / gamma)
    img = np.clip(img, 0, 255)
    return img

img = mpimg.imread('baboon_monocromatica.png')
fig, axs = plt.subplots(1, 5, figsize=(25, 5))

# Original image
axs[0].imshow(img, cmap=plt.get_cmap('gray'))
axs[0].set_title('Original')
axs[0].axis('off')

# Gamma corrected images
img1 = correct_gamma(img, 0.5)
img2 = correct_gamma(img, 1.0)
img3 = correct_gamma(img, 1.5)
img4 = correct_gamma(img, 2.0)

axs[1].imshow(img1, cmap=plt.get_cmap('gray'))
axs[1].set_title('γ = 0.5')
axs[1].axis('off')

axs[2].imshow(img2, cmap=plt.get_cmap('gray'))
axs[2].set_title('γ = 1.0')
axs[2].axis('off')

axs[3].imshow(img3, cmap=plt.get_cmap('gray'))
axs[3].set_title('γ = 1.5')
axs[3].axis('off')

axs[4].imshow(img4, cmap=plt.get_cmap('gray'))
axs[4].set_title('γ = 2.0')
axs[4].axis('off')

plt.tight_layout()
plt.show()
