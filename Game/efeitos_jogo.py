# coding : utf-8

import pygame, os, sys, time, random
from pygame import *
from faixa import *
from carro import *
from arvores import *
from menu import *
from objetos_pista import *
from combustivel import *

pygame.init()

som_carros_inimigos = pygame.mixer.Sound('sons' + os.sep + 'fast-car-effect.wav')
som_menu1 = pygame.mixer.Sound('sons' + os.sep + 'Blop-Mark.wav')
som_voltar = pygame.mixer.Sound('sons' + os.sep + 'spin_jump.wav')
som_bonus = pygame.mixer.Sound('sons' + os.sep + 'shells_falls.wav')
som_pausa = pygame.mixer.Sound('sons' + os.sep + 'Realistic_Punch.wav')
som_fuel = pygame.mixer.Sound('sons' + os.sep + 'Countdown-Me.wav')

lista_musicas = ['Track 01.mp3', 'Track 02.mp3', 'Track 03.mp3', 'Track 04.mp3']
