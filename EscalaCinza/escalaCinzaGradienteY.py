from PIL import Image

width = height = 600 #valores definidos para largura e altura

imgCinzaGradY = Image.new('L', (width, height))

# percorrer cada pixel da imagem
for y in range(height):
    for x in range(width):
        luminance = y

        imgCinzaGradY.putpixel((x, y), luminance)

imgCinzaGradY.save('imagens/escalaCinzaGradienteY.jpg')
