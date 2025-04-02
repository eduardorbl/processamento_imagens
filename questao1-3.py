import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Carrega a imagem em escala de cinza e converte para um array NumPy
img = np.array(Image.open('baboon_monocromatica.png').convert('L'))

# Obtém a altura e largura da imagem
altura, largura = img.shape3

# Calcula a altura e largura de cada bloco (dividindo a imagem em 4x4 blocos)
altura_bloco = altura // 4
largura_bloco = largura // 4

# Divide a imagem em blocos 4x4 e reorganiza as dimensões para facilitar o acesso
blocos = img.reshape(4, altura_bloco, 4, largura_bloco).transpose(0, 2, 1, 3)

# Define a nova ordem dos blocos (matriz 4x4 com os índices dos blocos)
nova_ordem = np.array([
    [6, 11, 13, 3],
    [8, 16, 1, 9],
    [12, 14, 2, 7],
    [4, 15, 10, 5]
])
# Ajusta os índices para começar de 0 (subtraindo 1)
nova_ordem = nova_ordem - 1

# Reorganiza os blocos de acordo com a nova ordem e reconstrói a imagem
mosaico = blocos[nova_ordem//4, nova_ordem%4].transpose(0, 2, 1, 3).reshape(altura, largura)

# Plota a imagem original e a imagem em mosaico lado a lado
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

# Exibe a imagem original
axs[0].imshow(img, cmap=plt.get_cmap('gray'))
axs[0].set_title('Original')
axs[0].axis('off')

# Exibe a imagem em mosaico
axs[1].imshow(mosaico, cmap=plt.get_cmap('gray'))
axs[1].set_title('Mosaico')
axs[1].axis('off')

# Ajusta o layout e exibe o gráfico
plt.tight_layout()
plt.show()
