# coding : utf-8

import pygame, os, sys, time
from pygame import *
from faixa import *
from carro import *
from arvores import *
from intro_menu import *
from objetos_pista import *
from combustivel import *

pygame.init()

# Carregando intro do jogo
#introducao_jogo(True)

# Menu Raiz
if menu_raiz(True):    
    tela =  pygame.display.set_mode((1024, 768))
    screen = pygame.display.get_surface()
    fundo = pygame.image.load('imagens' + os.sep + 'road3.png')
    pygame.display.set_caption('Need Py Speed - The Game')
        
    
    clock = pygame.time.Clock()

    comb = Combustivel(screen)
    carro = Carro(screen)
    faixas = [Faixa(screen)]
    objeto = Carro_inimigo(screen)
    arvores_direita = [Arvores(screen, 'direita')]
    arvores_esquerda = [Arvores(screen, 'esquerda')]
    pygame.key.set_repeat(1,1)
    i= 0
    combustivel = 1000
    
    while True:
        clock.tick(500)
        if combustivel <= 0:
            sys.exit()
        # Fechar o game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif pygame.key.get_pressed()[K_ESCAPE]:
                menu_raiz(True)
        ##
        
        tecla = pygame.key.get_pressed()
        carro.mover_carro(tecla)
    

        if i % 10 == 0 and len(arvores_direita) < 6:
            arvores_direita.append(Arvores(screen, 'direita'))
            arvores_esquerda.append(Arvores(screen, 'esquerda'))
            faixas.append(Faixa(screen))
        tela.blit(fundo, (0, 0))
      

        for j in range(len(arvores_direita)):
            faixas[j].print_faixa(screen)
            arvores_direita[j].print_arvore(screen)
            arvores_esquerda[j].print_arvore(screen)
            objeto.print_objeto(screen)
            comb.print_comb(screen)
        carro.print_carro(screen)
        pygame.display.update()



        for j in range(len(arvores_direita)):
            arvores_direita[j].mover_arvores('direita')
            arvores_esquerda[j].mover_arvores('esquerda')
            faixas[j].mover_faixa()
            objeto.mover_objeto()
            comb.mover_comb()


        ''' if carro.rect_carro.colliderect(objeto.rect_objeto):
                print 'Bateu'
                sys.exit()
        if comb.rect_comb.colliderect(carro.rect_carro):
                print "Bateu"   
        '''
        i += 1 
        combustivel -= 0 
