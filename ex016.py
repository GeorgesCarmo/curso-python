# Faça um programa em Python que abra e reproduza um arquivo de áudio no formato mp3.
import pygame
pygame.init()
pygame.mixer.music.load('ex016.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()