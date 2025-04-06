import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Carrega a imagem 'baboon_monocromatica.png', converte para escala de cinza e transforma em um array NumPy
img1 = np.array(Image.open('baboon_monocromatica.png').convert('L'))

# Carrega a imagem 'butterfly.png', converte para escala de cinza e transforma em um array NumPy
img2 = np.array(Image.open('butterfly.png').convert('L'))

# Cria uma lista de pesos igualmente espaçados entre 0.1 e 0.9 (9 valores)
weights = np.linspace(0.1, 0.9, 9)

# Combina as duas imagens usando os pesos
# Para cada peso, calcula uma combinação linear das imagens (img1 * (1 - peso) + img2 * peso)
# Adiciona uma nova dimensão para os pesos e realiza a operação em broadcast
img_combinadas = np.add(np.multiply(img1[:, :, None], (1 - weights)), np.multiply(img2[:, :, None], weights))

# Move o eixo dos pesos para o início, criando um array onde cada índice representa uma imagem combinada
img_combinadas = np.moveaxis(img_combinadas, -1, 0)

# Cria uma grade de subplots (3x3) para exibir as imagens combinadas
fig, axs = plt.subplots(3, 3, figsize=(10, 10))

# Itera sobre as imagens combinadas e exibe cada uma em um subplot
for i, img in enumerate(img_combinadas):
    axs[i // 3, i % 3].imshow(img, cmap='gray', vmin=0, vmax=255)  # Exibe a imagem em escala de cinza
    axs[i // 3, i % 3].set_title(f'Baboon: {1 - weights[i]:.1f}, Butterfly: {weights[i]:.1f}')  # Define o título com os pesos
    axs[i // 3, i % 3].axis('off')  # Remove os eixos para uma visualização limpa

# Ajusta o layout para evitar sobreposição
plt.tight_layout()

# Exibe o gráfico com as imagens combinadas
plt.show()
