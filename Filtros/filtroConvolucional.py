from PIL import Image, ImageFilter
import numpy as np

img = Image.open("imagens/ondas.jpeg").convert("L")# carregar imagem e converter para cinza

kernel = [
    [0, -1, 0],
    [-1, 5,-1],
    [0, -1, 0]
]

kernel = np.array(kernel) #converter para array numpy
kernel = kernel.flatten()
convertKernel = ImageFilter.Kernel(size=(3, 3), kernel=kernel, scale=np.sum(kernel)) # cria filtro de convolução

imgFiltro = img.filter(convertKernel) # aplicação do filtro

imgFiltro.show()