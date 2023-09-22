#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame

def reproduzir_mp3(caminho_do_arquivo):
                   pygame.init()
                   pygame.mixer.init()
                   pygame.mixer.music.load(caminho_do_arquivo)
                   pygame.mixer.music.play()
                   pygame.mixer.music.wait()
                   pygame.quit()
caminho_do_arquivo = 'C:\\Users\\arthu\\OneDrive\\Documentos\\Planet Hemp - Dig Dig Dig (Ao Vivo).mp3'
reproduzir_mp3(caminho_do_arquivo)
