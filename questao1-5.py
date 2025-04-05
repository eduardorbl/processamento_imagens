import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Carrega a imagem 'watch.png', converte para RGB e a transforma em um array NumPy
img = np.array(Image.open('watch.png').convert('RGB')) 

# Matriz de transformação para aplicar o efeito sépia
sepia_matrix = np.array([
    [0.393, 0.769, 0.189],
    [0.349, 0.686, 0.168],
    [0.272, 0.534, 0.131]
])

# Aplica a matriz de transformação sépia à imagem original
sepia_img = np.dot(img, sepia_matrix.T)

# Normaliza os valores da imagem sépia para o intervalo [0, 255]
sepia_img = np.interp(sepia_img, (sepia_img.min(), sepia_img.max()), (0, 255))
sepia_img = sepia_img.astype(np.uint8)  # Converte os valores para inteiros de 8 bits

# Configura o tamanho da figura para exibição
plt.figure(figsize=(10, 5))

# Exibe a imagem original
plt.subplot(1, 3, 1)
plt.imshow(img, vmin=0, vmax=255) 
plt.title('Original')  # Título da imagem original
plt.axis('off')  # Remove os eixos

# Exibe a imagem com o efeito sépia aplicado
plt.subplot(1, 3, 2)
plt.imshow(sepia_img, vmax=255, vmin=0)
plt.title('Efeito aplicado')  # Título da imagem com efeito sépia
plt.axis('off')  # Remove os eixos

# Converte a imagem original para escala de cinza
gray = np.dot(img, [0.299, 0.587, 0.114])  # Fórmula para conversão em escala de cinza
gray = np.interp(gray, (gray.min(), gray.max()), (0, 255))  # Normaliza os valores usando interp
gray = gray.astype(np.uint8)  # Converte os valores para inteiros de 8 bits

# Exibe a imagem em escala de cinza
plt.subplot(1, 3, 3)
plt.imshow(gray, cmap=plt.get_cmap('gray'))  # Define o mapa de cores como escala de cinza
plt.title('Escala de cinza')  # Título da imagem em escala de cinza
plt.axis('off')  # Remove os eixos

# Ajusta o layout para evitar sobreposição
plt.tight_layout()

# Mostra as imagens na tela
plt.show()