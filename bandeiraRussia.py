#Atividade disciplina Processamento de Imagens
from PIL import Image
#definir constantes para cada cor
WHITE = (255, 255, 255)
BLUE = (0, 50, 160)
RED = (218, 41, 28)
#pedir ao usuário pára informar a largura da bandeira
width = (int(input("Informe a largura da bandeira: ")))

def bandeiraRussia():
    high = 2 * width // 3 #proporção da imagem

    img = Image.new("RGB", (width, high), WHITE)#cria uma bandeira toda branca

    for x in range(0, img.width):#insere a faixa azul
        for y in range(img.height//3,img.height):
            img.putpixel((x,y),BLUE)
    
    for x in range(0, img.width):#insere a faixa vermelha
        for y in range(2 * img.height//3,img.height):
            img.putpixel((x,y),RED)
    
    return img
            

bandeiraRussia().show()
