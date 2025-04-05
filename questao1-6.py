import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Carrega a imagem em escala de cinza e converte para um array NumPy de 8 bits
img = np.array(Image.open('baboon_monocromatica.png').convert('L')).astype(np.uint8)

# Define máscaras binárias para cada bit da imagem
bin0 = 0b00000001  # Máscara para o bit menos significativo (LSB)
bin1 = 0b00000010
bin2 = 0b00000100
bin3 = 0b00001000
bin4 = 0b00010000
bin5 = 0b00100000
bin6 = 0b01000000
bin7 = 0b10000000  # Máscara para o bit mais significativo (MSB)

# Função para normalizar os valores para o intervalo [0, 255]
def normalize(img):
    return np.interp(img, (img.min(), img.max()), (0, 255))

# Extrai e normaliza o bit 0 da imagem
img0 = normalize(np.bitwise_and(img, bin0))

# Extrai e normaliza o bit 1 da imagem
img1 = normalize(np.bitwise_and(img, bin1))

# Extrai e normaliza o bit 2 da imagem
img2 = normalize(np.bitwise_and(img, bin2))

# Extrai e normaliza o bit 3 da imagem
img3 = normalize(np.bitwise_and(img, bin3))

# Extrai e normaliza o bit 4 da imagem
img4 = normalize(np.bitwise_and(img, bin4))

# Extrai e normaliza o bit 5 da imagem
img5 = normalize(np.bitwise_and(img, bin5))

# Extrai e normaliza o bit 6 da imagem
img6 = normalize(np.bitwise_and(img, bin6))

# Extrai e normaliza o bit 7 da imagem
img7 = normalize(np.bitwise_and(img, bin7))

# Cria uma grade de subplots para exibir as imagens
fig, axs = plt.subplots(3, 3, figsize=(10, 10))

# Exibe a imagem correspondente ao bit 0
axs[0, 0].imshow(img0, cmap='gray', vmin=0, vmax=255)
axs[0, 0].set_title('0 bit')  # Título do subplot
axs[0, 0].axis('off')  # Remove os eixos

# Exibe a imagem correspondente ao bit 1
axs[0, 1].imshow(img1, cmap='gray', vmin=0, vmax=255)
axs[0, 1].set_title('1 bits')
axs[0, 1].axis('off')

# Exibe a imagem correspondente ao bit 2
axs[0, 2].imshow(img2, cmap='gray', vmin=0, vmax=255)
axs[0, 2].set_title('2 bits')
axs[0, 2].axis('off')

# Exibe a imagem correspondente ao bit 3
axs[1, 0].imshow(img3, cmap='gray', vmin=0, vmax=255)
axs[1, 0].set_title('3 bits')
axs[1, 0].axis('off')

# Exibe a imagem correspondente ao bit 4
axs[1, 1].imshow(img4, cmap='gray', vmin=0, vmax=255)
axs[1, 1].set_title('4 bits')
axs[1, 1].axis('off')

# Exibe a imagem correspondente ao bit 5
axs[1, 2].imshow(img5, cmap='gray', vmin=0, vmax=255)
axs[1, 2].set_title('5 bits')
axs[1, 2].axis('off')

# Exibe a imagem correspondente ao bit 6
axs[2, 0].imshow(img6, cmap='gray', vmin=0, vmax=255)
axs[2, 0].set_title('6 bits')
axs[2, 0].axis('off')

# Exibe a imagem correspondente ao bit 7
axs[2, 1].imshow(img7, cmap='gray', vmin=0, vmax=255)
axs[2, 1].set_title('7 bits')
axs[2, 1].axis('off')

# Exibe a imagem original
axs[2, 2].imshow(img, cmap='gray', vmin=0, vmax=255)
axs[2, 2].set_title('Original')
axs[2, 2].axis('off')

# Ajusta o layout para evitar sobreposição
plt.tight_layout()

# Mostra o gráfico com todas as imagens
plt.show()