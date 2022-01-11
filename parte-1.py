import pygame
from random import randint
pygame.init()

def text (mensagem, cor, tamanho, x, y):
    font = pygame.font.SysFont(None,tamanho)
    texto1 = font.render(mensagem, True, cor)
    janela.blit(texto1)[x,y]

v1 = 12
v = 10
x = 350  #[165] [350] [445] 
y = 50
yy = 0

horizontal = 170
vertical = 800 
vertical_A = 1200 #carro do meio
vertical_B = 800
vertical_C = 800

janela_aberta = True

cenario = pygame.image.load(r'C:/Users/KAROL DINIZ/Desktop/Scripts PY/Jogo/img/pistacompleta.png')
carro = pygame.image.load(r'C:/Users/KAROL DINIZ/Desktop/Scripts PY/Jogo/img/carro.png')
carro1 = pygame.image.load(r'C:/Users/KAROL DINIZ/Desktop/Scripts PY/Jogo/img/carro1.png')
carro3 = pygame.image.load(r'C:/Users/KAROL DINIZ/Desktop/Scripts PY/Jogo/img/carro3.png')
carro4 = pygame.image.load(r'C:/Users/KAROL DINIZ/Desktop/Scripts PY/Jogo/img/carro4.png')
carro5 = pygame.image.load(r'C:/Users/KAROL DINIZ/Desktop/Scripts PY/Jogo/img/carro5.png')
nuvem = pygame.image.load(r'C:/Users/KAROL DINIZ/Desktop/Scripts PY/Jogo/img/Nuvem.png')

timer = 0
time = 0

font = pygame.font.SysFont('arial black',20) #Definir elemento da tabela de tempo.
texto = font.render("Time: ", True,(225,225,225),(0,0,0))
posição = texto.get_rect()
posição.center = (65,50)

pontos = 0
fonte = pygame.font.SysFont('arial black',20) #Definir elemento da tabela de tempo.
texto1 = fonte.render("Pontos: ", True,(225,225,225),(0,0,0))
posição1 = texto.get_rect()
posição1.center = (350,350)

W, H = 700, 535
janela = pygame.display.set_mode((W,H)) #Definir dimensões do display.
pygame.display.set_caption("CAR GAME")

while janela_aberta:
    pygame.time.delay(50) #Definir atualização a (x)ms.
    mensagem = f'Pontos:{pontos}'
    textof = fonte.render(mensagem,True,(255,255,255), (0,0,0))

    for event in pygame.event.get(): #Definir ação//evento.
        if event.type == pygame.QUIT:
            janela_aberta = False 

    controle = pygame.key.get_pressed() #Definir comandos de controle (SETAS).
    if controle [pygame.K_RIGHT] and x <= 445 :
        x += v
    if controle [pygame.K_LEFT] and x >= 165:
        x -= v    


    if x + 80 > horizontal + 285 and y + 160 > vertical_C: #Colisão da direita (carro vermelho).
        y = 1200
        ponto = 0
        fonte = pygame.font.SysFont('arial black',20)
        text = fonte.render("Fim de jogo! ", True,(225,225,225),(0,0,0))
    else: 
        pontos += 1

    if x - 80 < horizontal and y + 30 > vertical:
        y = 1200
        ponto = 0
    else: 
        pontos += 1
        
    if x - 80 < horizontal + 60 and y + 30 > vertical_B:
        y = 1200

    if x > horizontal + 120 and y + 50 > vertical_A or x > horizontal + 150 and y > vertical_A:
        y = 1200

    if vertical <= -80:
        vertical = randint(800,1000)

    if vertical_A <= -80:
        vertical_A = randint(1300,2000) #Carro Azul #330

    if vertical_B <= -80:
        vertical_B = randint(2200,2600) #Caminhão
    
    if vertical_C <= -80:
        vertical_C = randint(2900,3000) #Carro vermelho 


    if  timer <20:
        timer += 1
    else:
        time += 1
        texto = font.render("Time: " +str(time), True, (225,225,225), (0,0,0)) #Contador x 50MMS (Dentro do while).
        timer = 0


    vertical -= v1 + 2  #Decrementar a posição inicial.
    vertical_A -= v1 + 5
    vertical_B -= v1 + 12
    vertical_C -= v1 + 20


    relação = yy % cenario.get_rect().height
    janela.blit(cenario,(0,relação - cenario.get_rect().height)) #Definir imagens.
    if relação < W:
        janela.blit(cenario, (0, relação))
    yy += 15

    #pygame.draw.line(janela, (255, 0, 0),(0, relação),(H, relação),3) #Apenas para ver onde acaba a imagem.

    janela.blit(carro,(x,y))
    janela.blit(carro1,(horizontal,vertical))
    janela.blit(carro3,(horizontal + 160,vertical_A)) # Cordenada(H) = 330
    janela.blit(carro5,(horizontal + 80, vertical_B)) # Cordenada(H) = 250
    janela.blit(carro4,(horizontal + 250,vertical_C)) # Cordenada(H) = 420
    janela.blit(nuvem, (vertical, horizontal - 70))
    janela.blit(nuvem, (vertical - 200, horizontal))
    janela.blit(texto,posição)
    janela.blit(textof,(560,35))

    #pygame.draw.circle(janela,(12,238,238),(x,y),(50)) #Definir características do elemento(circle).
    pygame.display.update() #Definir atualização(x.pt2).

pygame.quit()
