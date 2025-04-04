import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
from PIL import Image

img = np.array(Image.open('watch.png').convert('RGB'))

def rgb2gray(rgb):
    rgb_img = np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])
    rgb_img = (rgb_img - rgb_img.min()) / (rgb_img.max() - rgb_img.min()) * 255
    rgb_img = rgb_img.astype(np.uint8)
    return rgb_img

gray = rgb2gray(img)
print(gray.max(), gray.min())
blurred = gaussian_filter(gray, sigma=21/6)
print(blurred.max(), blurred.min())

fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Subplot 1: Imagem em tons de cinza
axs[0].imshow(gray, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)
axs[0].set_title('Tons de Cinza')
axs[0].axis('off')

# Subplot 2: Imagem desfocada
axs[1].imshow(blurred, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)
axs[1].set_title('Imagem Desfocada')
axs[1].axis('off')

# Subplot 3: Imagem em tons de cinza dividida pela imagem desfocada
result = np.clip((gray / blurred) * 255, 0, 255).astype(np.uint8)

axs[2].imshow(result, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)
axs[2].set_title('Imagem em Tons de Cinza Dividida pela Imagem Desfocada')
axs[2].axis('off')

plt.tight_layout()
plt.show()