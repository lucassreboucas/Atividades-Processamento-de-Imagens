#Atividade disciplina Processamento de Imagens
from PIL import Image
#definir constantes para cada cor
BLACK = (0, 0, 0)
YELLOW = (253, 218, 36)
RED = (239, 51, 64)
#pedir ao usuário pára informar a largura da bandeira
width = (int(input("Informe a largura da bandeira: ")))

def bandeiraBelgica():
    high = 13 * width // 15 #proporção da imagem

    img = Image.new("RGB", (width, high), BLACK)#cria uma bandeira toda preta

    for x in range(img.width//3,img.width):#insere a faixa amarela
        for y in range(img.height):
            img.putpixel((x,y),YELLOW)
    
    for x in range(2 * img.width//3,img.width):#insere a faixa vermelha
        for y in range(img.height):
            img.putpixel((x,y),RED)

    return img

bandeiraBelgica().show()

