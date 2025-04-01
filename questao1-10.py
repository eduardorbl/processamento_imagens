import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve
import matplotlib.image as mpimg

def aplicar_filtro(imagem, filtro):
    """Aplica um filtro (máscara de convolução) em uma imagem monocromática."""
    # Normaliza a imagem para 0-1 se estiver em 0-255
    if imagem.max() > 1:
        imagem = imagem / 255.0
    
    # Aplica a convolução
    imagem_filtrada = convolve(imagem, filtro, mode='constant', cval=0.0)
    
    # Garante que os valores permaneçam no intervalo [0, 1]
    imagem_filtrada = np.clip(imagem_filtrada, 0, 1)
    
    return imagem_filtrada

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

h7 = np.array([[-1, -2, -1],
                [0, 0, 0],
                [1, 2, 1]])

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

def main():
    # Carrega a imagem
    imagem = mpimg.imread('baboon_monocromatica.png')
    
    # Aplica todos os filtros
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
        'Combinação sqrt(h3^2+h4^2)': np.zeros_like(imagem)  # Placeholder, será substituído abaixo
    }
    
    # Calcula a combinação de h3 e h4
    h3_result = aplicar_filtro(imagem, h3)
    h4_result = aplicar_filtro(imagem, h4)
    combinacao = np.sqrt(h3_result**2 + h4_result**2)
    combinacao = np.clip(combinacao, 0, 1)  # Garante que está no intervalo [0,1]
    resultados['Combinação sqrt(h3^2+h4^2)'] = combinacao
    
    # Configuração da figura
    fig, axs = plt.subplots(3, 4, figsize=(12, 12))
    
    # Plota cada imagem
    for idx, (titulo, img) in enumerate(resultados.items()):
        row = idx // 4
        col = idx % 4
        axs[row, col].imshow(img, cmap='gray', vmin=0, vmax=1)
        axs[row, col].set_title(titulo)
        axs[row, col].axis('off')
    
    # Ajusta o espaçamento entre os subplots
    plt.subplots_adjust(wspace=0.5, hspace=0.5)
    plt.show()

if __name__ == "__main__":
    main()