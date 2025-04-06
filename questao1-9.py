import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Carrega a imagem 'baboon_monocromatica.png', converte para escala de cinza ('L') e transforma em um array NumPy
img = np.array(Image.open('baboon_monocromatica.png').convert('L'))

# Define os níveis de quantização desejados
niveis = [64, 32, 16, 8, 4, 2]

# Define as máscaras binárias correspondentes para cada nível de quantização
mascaras = [0b11111100, 0b11111000, 0b11110000, 0b11100000, 0b11000000, 0b10000000]

# Cria uma grade de subplots (3x3) para exibir as imagens
fig, axs = plt.subplots(3, 3, figsize=(10, 6))

# Desativa os eixos dos subplots que não serão usados
axs[0,0].axis('off')
axs[0,2].axis('off')

# Exibe a imagem original no subplot central da primeira linha
axs[0,1].imshow(img, cmap='gray', vmin=0, vmax=255)
axs[0,1].set_title('Original: 256 níveis')  # Define o título para a imagem original
axs[0,1].axis('off')  # Desativa os eixos

# Loop para aplicar a quantização e exibir as imagens resultantes
for i, nivel in enumerate(niveis):
    # Aplica a máscara binária para reduzir os níveis de cinza
    img_quantizada = np.bitwise_and(img, mascaras[i])
    
    # Reescala os valores da imagem quantizada para o intervalo [0, 255]
    img_quantizada = np.interp(img_quantizada, (img_quantizada.min(), img_quantizada.max()), (0, 255))
    
    # Exibe a imagem quantizada no subplot correspondente
    axs[i//3 + 1, i%3].imshow(img_quantizada, cmap='gray', vmin=0, vmax=255)
    axs[i//3 + 1, i%3].set_title(f'{nivel} níveis')  # Define o título com o número de níveis
    axs[i//3 + 1, i%3].axis('off')  # Desativa os eixos

# Ajusta o layout para evitar sobreposição de elementos
plt.tight_layout()

# Exibe o gráfico com todas as imagens
plt.show()