import pygame
import random

pygame.init()
pygame.display.set_caption("O resgate de Marcelinho")
largura, altura = 600, 400
pygame.display.set_mode((largura,altura))
relogio = pygame.time.Clock()

def rodar_jogo():
    fim_jogo = False
    while not fim_jogo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True







rodar_jogo()