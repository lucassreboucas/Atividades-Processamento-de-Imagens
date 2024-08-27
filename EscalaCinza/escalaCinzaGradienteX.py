from PIL import Image

width = height = 600

imgCinzaGraX = Image.new('L', (width, height))

for y in range(height):
    for x in range(width):
        luminance = x

        imgCinzaGraX.putpixel((x, y), luminance)

imgCinzaGraX.save('imagens/escalaCinzaGradienteX.jpg')