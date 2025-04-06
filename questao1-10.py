import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve
from PIL import Image

# Função para aplicar um filtro (máscara de convolução) em uma imagem monocromática
def aplicar_filtro(imagem, filtro):
    """Aplica um filtro (máscara de convolução) em uma imagem monocromática."""
    # Aplica a convolução da imagem com o filtro fornecido
    imagem_filtrada = convolve(imagem, filtro, mode='constant', cval=0.0)
    return imagem_filtrada

# Definição de vários filtros (máscaras de convolução) para diferentes propósitos
h1 = np.array([[0, 0, -1, 0, 0],
                [0, -1, -2, -1, 0],
                [-1, -2, 16, -2, -1],
                [0, -1, -2, -1, 0],
                [0, 0, -1, 0, 0]])

h2 = np.array([[1/256, 4/256, 6/256, 4/256, 1/256],
                [4/256, 16/256, 24/256, 16/256, 4/256],
                [6/256, 24/256, 36/256, 24/256, 6/256],
                [4/256, 16/256, 24/256, 16/256, 4/256],
                [1/256, 4/256, 6/256, 4/256, 1/256]])

h3 = np.array([[-1, 0, 1],
                [-2, 0, 2],
                [-1, 0, 1]])

h4 = np.array([[-1, -2, -1],
                [0, 0, 0],
                [1, 2, 1]])

h5 = np.array([[-1, -1, -1],
                [-1, 8, -1],
                [-1, -1, -1]])

h6 = np.array([[1/9, 1/9, 1/9],
                [1/9, 1/9, 1/9],
                [1/9, 1/9, 1/9]])

h7 = np.array([[-1, -1, 2],
                [-1, 2, -1],
                [2, -1, -1]])

h8 = np.array([[2, -1, -1],
                [-1, 2, -1],
                [-1, -1, 2]])

h9 = np.array([[1/9, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1/9, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1/9, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1/9, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1/9, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1/9, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1/9 ,0 ,0],
                [0, 0, 0, 0, 0, 0, 0, 1/9 ,0],
                [0, 0, 0, 0, 0, 0, 0, 0 ,1/9]])

h10 = np.array([[1/8, -1/8, -1/8, -1/8, -1/8],
                [-1/8, 2/8, 2/8, 2/8, -1/8],
                [-1/8, 2/8, 8/8, 2/8, -1/8],
                [-1/8, 2/8, 2/8, 2/8, -1/8],
                [-1/8, -1/8, -1/8, -1/8, -1/8]])

h11 = np.array([[-1, -1, 0],
                [-1, 0, 1],
                [0, 1, 1]])

# Carrega a imagem em escala de cinza
imagem = np.array(Image.open('watch.png').convert('L'))

# Dicionário para armazenar os resultados de cada filtro
resultados = {
    'Filtro h1': aplicar_filtro(imagem, h1),
    'Filtro h2': aplicar_filtro(imagem, h2),
    'Filtro h3': aplicar_filtro(imagem, h3),
    'Filtro h4': aplicar_filtro(imagem, h4),
    'Filtro h5': aplicar_filtro(imagem, h5),
    'Filtro h6': aplicar_filtro(imagem, h6),
    'Filtro h7': aplicar_filtro(imagem, h7),
    'Filtro h8': aplicar_filtro(imagem, h8),
    'Filtro h9': aplicar_filtro(imagem, h9),
    'Filtro h10': aplicar_filtro(imagem, h10),
    'Filtro h11': aplicar_filtro(imagem, h11),
    'Combinação sqrt(h3^2+h4^2)': np.zeros_like(imagem)  # Inicializa com zeros
}

# Calcula a combinação dos filtros h3 e h4
h3_result = aplicar_filtro(imagem, h3)
h4_result = aplicar_filtro(imagem, h4)
combinacao = np.sqrt(h3_result**2 + h4_result**2)  # Combinação pela raiz quadrada da soma dos quadrados
combinacao = np.interp(combinacao, (combinacao.min(), combinacao.max()), (0, 255))  # Normaliza para 0-255
resultados['Combinação sqrt(h3^2+h4^2)'] = combinacao

# Cria uma figura com subplots para exibir os resultados
fig, axs = plt.subplots(3, 4, figsize=(12, 12))

# Plota cada imagem filtrada
for idx, (titulo, img) in enumerate(resultados.items()):
    row = idx // 4  # Calcula a linha do subplot
    col = idx % 4   # Calcula a coluna do subplot
    axs[row, col].imshow(img, cmap='gray', vmin=0, vmax=255)  # Exibe a imagem em escala de cinza
    axs[row, col].set_title(titulo)  # Define o título do subplot
    axs[row, col].axis('off')  # Remove os eixos

# Ajusta o espaçamento entre os subplots
plt.subplots_adjust(wspace=0.5, hspace=0.5)
plt.show()  # Exibe a figura