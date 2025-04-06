import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Carrega a imagem 'city.png', converte para escala de cinza e transforma em um array NumPy
img = np.array(Image.open('city.png').convert('L'))

# Cria uma figura com uma grade de subplots (2 linhas e 3 colunas)
fig, axs = plt.subplots(2, 3, figsize=(10, 6))

# Exibe a imagem original no primeiro subplot
axs[0, 0].imshow(img, cmap='gray', vmin=0, vmax=255)
axs[0, 0].set_title('Original')  # Define o título do subplot
axs[0, 0].axis('off')  # Remove os eixos

# Gera a imagem negativa (inversão de cores) e exibe no segundo subplot
img_negativo = np.subtract(255, img)
axs[0, 1].imshow(img_negativo, cmap='gray', vmin=0, vmax=255)
axs[0, 1].set_title('Negativo')
axs[0, 1].axis('off')

# Realiza uma transformação linear nos valores de pixel no intervalo [100, 200]
imagem_ajustada = np.interp(np.clip(img, 100, 200), (100, 200), (0, 255))
axs[0, 2].imshow(imagem_ajustada, cmap='gray', vmin=0, vmax=255)
axs[0, 2].set_title('Transformada [100, 200]')
axs[0, 2].axis('off')

# Inverte horizontalmente as linhas pares da imagem e exibe no quarto subplot
img_invertida = img.copy()
img_invertida[::2, :] = img_invertida[::2, ::-1]
axs[1, 0].imshow(img_invertida, cmap='gray')
axs[1, 0].set_title('Invertida')
axs[1, 0].axis('off')

# Espelha a metade inferior da imagem em relação à linha central horizontal
img_espelhada = img.copy()
img_espelhada[img.shape[0]//2:, :] = img_espelhada[img.shape[0]//2 - 1 :: -1, :]
axs[1, 1].imshow(img_espelhada, cmap='gray', vmin=0, vmax=255)
axs[1, 1].set_title('Espelhada')
axs[1, 1].axis('off')

# Espelha a imagem verticalmente (de cabeça para baixo) e exibe no último subplot
img_espelhada_vertical = img.copy()
img_espelhada_vertical = img_espelhada_vertical[::-1, :]
axs[1, 2].imshow(img_espelhada_vertical, cmap='gray', vmin=0, vmax=255)
axs[1, 2].set_title('Espelhada Vertical')
axs[1, 2].axis('off')

# Ajusta o layout para evitar sobreposição entre os subplots
plt.tight_layout()

# Exibe a figura com os subplots
plt.show()