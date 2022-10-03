import pygame
from pygame.locals import *
from sys import exit
from random import randint



pygame.init()
#area das variaveis
tela=pygame.display.set_mode((640,480))
pygame.display.set_caption('bob marley')
relogio= pygame.time.Clock()
x_cobra= 320
y_cobra= 240
x_maça=100
y_maça=100
pontos=0
pygame.mixer.music.set_volume(0.5)
musica_de_fundo= pygame.mixer.music.load('BoxCat Games - CPU Talk.mp3')
pygame.mixer.music.play(-1 )
barulho_colisao= pygame.mixer.Sound ('smw_fireball.wav')
fonte=pygame.font.SysFont('arial',40, True,True)
lista_cobra=[]
comprimento_inicial=5
velocidade= 5
x_controle=velocidade
y_controle=0
game_over= False
#abrir e fechar janela
def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0,255,0), (XeY[0], XeY[1],20,20))

def reiniciar():
    global pontos,comprimento_inicial,x_cobra,y_cobra,lista_cobra,lista_cabeça,x_maça,y_maça,game_over
    pontos=0
    comprimento_inicial= 5
    x_cobra = 320
    y_cobra = 240
    lista_cobra=[]
    lista_cabeça=[]
    x_maça = 100
    y_maça = 100
    game_over=False
while True:
    relogio.tick(50)
    tela.fill((0,0,0))
    #contagem de pontos
    mensagem = f'pontos: {pontos}'
    pontos_formatado=fonte.render(mensagem, True, (255,255,255  ))
    for event in pygame.event.get():
        if event.type== QUIT:
            pygame.quit()
            exit()
        #interaçoes com as teclas
        if event.type==KEYDOWN:
            if event.key== K_a:
                if x_controle==velocidade:
                    pass
                else:
                    x_controle=-velocidade
                    y_controle=0
            if event.key== K_d:
                if x_controle==- velocidade:
                    pass
                else:
                    x_controle=velocidade
                    y_controle=0
            if event.key== K_w:
                if y_controle==velocidade:
                    pass
                else:
                    y_controle=-velocidade
                    x_controle=0
            if event.key== K_s:
                if y_controle==-velocidade:
                    pass
                else:
                    y_controle=velocidade
                    x_controle=0
    #area da cobra e dos blocos
    x_cobra+=x_controle
    y_cobra+=y_controle
    cobra=pygame.draw.rect(tela, (0,255,0), (x_cobra,y_cobra,20,20))
    maça=pygame.draw.rect(tela, (255,0,0), (x_maça,y_maça,20,20))
    if cobra.colliderect(maça):
        x_maça= randint(0,590)
        y_maça= randint(0,430)
        pontos+=1
        barulho_colisao.play()
        comprimento_inicial+=1
    lista_cabeça=[]
    lista_cabeça.append(x_cobra)
    lista_cabeça.append(y_cobra)
    lista_cobra.append(lista_cabeça)
    if lista_cobra.count(lista_cabeça)>1 or x_cobra==0 or y_cobra==0 or x_cobra==640 or y_cobra==480:
        game_over= True
        while game_over:
            tela.fill((0,0,0))
            fonte2=pygame.font.SysFont('arial',30,True,True)
            mensagem = 'game over, press R para jogar novamente'
            texto_formatado= fonte2.render(mensagem,True, (255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type==KEYDOWN:
                    if event.key== K_r:
                        reiniciar()
            tela.blit(texto_formatado,(30,200))
            pygame.display.update()
    if len(lista_cobra)> comprimento_inicial:
        del lista_cobra[0]
    aumenta_cobra(lista_cobra)
    tela.blit(pontos_formatado, (430,30))
    pygame.display.update()