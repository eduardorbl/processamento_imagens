import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Função para corrigir o gamma de uma imagem
def correct_gamma(img, gamma):
    # Aplica a correção de gamma na imagem
    img_corrected = (img / 255) ** (1 / gamma)
    return (img_corrected * 255).astype(np.uint8)

# Carrega a imagem em escala de cinza
img = np.array(Image.open('baboon_monocromatica.png').convert('L'))

# Cria uma figura com 1 linha e 5 colunas para exibir as imagens
fig, axs = plt.subplots(1, 5, figsize=(25, 5))

# Exibe a imagem original
axs[0].imshow(img, cmap=plt.get_cmap('gray'))
axs[0].set_title('Original')
axs[0].axis('off')

# Aplica a correção de gamma com diferentes valores
img1 = correct_gamma(img, 0.5)
img2 = correct_gamma(img, 1.0)
img3 = correct_gamma(img, 1.5)
img4 = correct_gamma(img, 2.0)

# Exibe a imagem com gamma = 0.5
axs[1].imshow(img1, cmap=plt.get_cmap('gray'))
axs[1].set_title('γ = 0.5')
axs[1].axis('off')

# Exibe a imagem com gamma = 1.0
axs[2].imshow(img2, cmap=plt.get_cmap('gray'))
axs[2].set_title('γ = 1.0')
axs[2].axis('off')

# Exibe a imagem com gamma = 1.5
axs[3].imshow(img3, cmap=plt.get_cmap('gray'))
axs[3].set_title('γ = 1.5')
axs[3].axis('off')

# Exibe a imagem com gamma = 2.0
axs[4].imshow(img4, cmap=plt.get_cmap('gray'))
axs[4].set_title('γ = 2.0')
axs[4].axis('off')

# Ajusta o layout para evitar sobreposição
plt.tight_layout()
plt.show()
