'''
Extrair os planos de bits de uma imagem monocromatica. Os niveis de cinza de uma imagem
monocromatica com m bits podem ser representados na forma de um polinomio de base 2
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Carrega a imagem
img = mpimg.imread('baboon_monocromatica.png')

# Define os números binários
bin0 = 0b00000001
bin1 = 0b00000010
bin2 = 0b00000100
bin3 = 0b00001000
bin4 = 0b00010000
bin5 = 0b00100000
bin6 = 0b01000000
bin7 = 0b10000000
bin8 = 0b10000000

# Aplica a operação AND bit a bit
img = img * 255
img = img.astype(np.uint8)
img0 = np.bitwise_and(img, bin0)
img1 = np.bitwise_and(img, bin1)
img2 = np.bitwise_and(img, bin2)
img3 = np.bitwise_and(img, bin3)
img4 = np.bitwise_and(img, bin4)
img5 = np.bitwise_and(img, bin5)
img6 = np.bitwise_and(img, bin6)
img7 = np.bitwise_and(img, bin7)


# Configura a exibição das imagens
fig, axs = plt.subplots(3, 3, figsize=(10, 10))

axs[0, 0].imshow(img0, cmap='gray')
axs[0, 0].set_title('0 bit')
axs[0, 0].axis('off')

axs[0, 1].imshow(img1, cmap='gray')
axs[0, 1].set_title('1 bits')
axs[0, 1].axis('off')

axs[0, 2].imshow(img2, cmap='gray')
axs[0, 2].set_title('2 bits')
axs[0, 2].axis('off')

axs[1, 0].imshow(img3, cmap='gray')
axs[1, 0].set_title('3 bits')
axs[1, 0].axis('off')

axs[1, 1].imshow(img4, cmap='gray')
axs[1, 1].set_title('4 bits')
axs[1, 1].axis('off')

axs[1, 2].imshow(img5, cmap='gray')
axs[1, 2].set_title('5 bits')
axs[1, 2].axis('off')

axs[2, 0].imshow(img6, cmap='gray')
axs[2, 0].set_title('6 bits')
axs[2, 0].axis('off')

axs[2, 1].imshow(img7, cmap='gray')
axs[2, 1].set_title('7 bits')
axs[2, 1].axis('off')

axs[2, 2].axis('off')  # Espaço vazio no canto inferior direito
plt.tight_layout()
plt.show()