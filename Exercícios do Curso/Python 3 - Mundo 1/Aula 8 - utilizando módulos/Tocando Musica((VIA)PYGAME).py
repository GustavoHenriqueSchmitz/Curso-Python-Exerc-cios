import pygame

pygame.mixer.init()
pygame.mixer.music.load('cyber.mp3')
pygame.mixer.music.play()
x = input('Digite algo para parar')