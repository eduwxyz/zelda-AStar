import pygame
from mapa import mapa_principal

# Define a largura e altura de cada célula
LARGURA = 42
ALTURA = 42

# Define o tamanho da janela

mapa = mapa_principal()
JANELA_LARGURA = len(mapa) * LARGURA
JANELA_ALTURA = len(mapa) * ALTURA

GREEN = (0, 255, 0)
LIGHT_GREEN = (144, 238, 144)
BLUE = (0, 0, 255)
LIGHT_BLUE = (173, 216, 230)
BROWN = (165, 42, 42)
LIGHT_BROWN = (244, 164, 96)
DARK_GREEN = (34, 139, 34)
# Define as constantes para os tipos de terreno e seus respectivos custos
GRAMA = 10
AREIA = 20
FLORESTA = 100
MONTANHA = 150
AGUA = 180

# Cria a janela
tela = pygame.display.set_mode((JANELA_LARGURA, JANELA_ALTURA))
# Define o título da janela
pygame.display.set_caption("Mapa de Hyrule")


def desenhar_celula(tela, cor, x, y):
            pygame.draw.rect(tela, cor, (x*LARGURA, y*ALTURA, LARGURA, ALTURA))

class Mapa:
    def __init__(self, mapa):
        self.mapa = mapa
        self.cores_celulas = {
            GRAMA: LIGHT_GREEN,
            AREIA: LIGHT_BROWN,
            FLORESTA: DARK_GREEN,
            MONTANHA: BROWN,
            AGUA: LIGHT_BLUE
        }
    

    def desenhar(self, tela):
        for y, linha in enumerate(self.mapa):
            for x, celula in enumerate(linha):
                cor = self.cores_celulas.get(celula)
                desenhar_celula(tela, cor, x, y)
                
        

mapa = Mapa(mapa)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            

    mapa.desenhar(tela)
    pygame.display.update()