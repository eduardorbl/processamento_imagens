import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Carrega a imagem 'watch.png', converte para RGB e a transforma em um array NumPy
img = np.array(Image.open('watch.png').convert('RGB'))

# Define a matriz de transformação para o efeito sépia
sepia_matrix = np.array([
    [0.393, 0.769, 0.189],
    [0.349, 0.686, 0.168],
    [0.272, 0.534, 0.131]
])

# Aplica a matriz de transformação sépia à imagem original
sepia_img = np.dot(img, sepia_matrix.T)

# Normaliza os valores da imagem sépia para o intervalo de 0 a 255
sepia_img = np.interp(sepia_img, (sepia_img.min(), sepia_img.max()), (0, 255))
sepia_img = sepia_img.astype(np.uint8)  # Converte os valores para inteiros de 8 bits

# Exibe a imagem original e a imagem com efeito sépia lado a lado
plt.figure(figsize=(10, 5))

# Subplot para a imagem original
plt.subplot(1, 2, 1)
plt.imshow(img, vmin=0, vmax=255)  # Exibe a imagem original
plt.title('Original')  # Título do subplot
plt.axis('off')  # Remove os eixos

# Subplot para a imagem com efeito sépia
plt.subplot(1, 2, 2)
plt.imshow(sepia_img, vmax=255, vmin=0)  # Exibe a imagem sépia
plt.title('Efeito Sépiado')  # Título do subplot
plt.axis('off')  # Remove os eixos

# Ajusta o layout para evitar sobreposição
plt.tight_layout()

# Mostra as imagens na tela
plt.show()