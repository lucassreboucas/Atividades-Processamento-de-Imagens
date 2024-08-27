from PIL import Image

img = Image.open('imagens/LagoTeste.jpg') # caminho da imagem

width, height = img.size # obter largura e altura da imagem

imgCinza = Image.new('L', (width, height))

# percorrer cada pixel da imagem
for y in range(height):
    for x in range(width):
        r, g, b = img.getpixel((x, y))

        luminance = int(0.299 * r + 0.587 * g + 0.114 * b) # fórmula da luminância

        imgCinza.putpixel((x, y), luminance)

imgCinza.save('imagens/LagoTesteCinza.jpg')

