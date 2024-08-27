from PIL import Image, ImageFilter
# Carregar a imagem em escala de cinza
imagem = Image.open("imagens/ondas.jpeg").convert("L")

# filtro apicado na horizontal
sobel_h = imagem.filter(ImageFilter.Kernel(
    size=(3, 3),
    kernel=(-1, 0, 1,
            -2, 0, 2,
            -1, 0, 1),
    scale=1
))

# filtro aplicado na vertical
sobel_v = imagem.filter(ImageFilter.Kernel(
    size=(3, 3),
    kernel=(-1, -2, -1,
            0, 0, 0,
            1, 2, 1),
    scale=1
))

# combinação da horizontal e vertical  
sobel_combined = Image.blend(sobel_h, sobel_v, alpha=0.5)

sobel_h.show()# exibir filtro aplicado na horizontal
sobel_v.show()# exibir filtro aplicado na vertical
sobel_combined.show()# exibir filtro aplicado combinado
