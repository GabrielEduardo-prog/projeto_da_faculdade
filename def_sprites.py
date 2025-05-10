import pygame as pg
from pygame.locals import *
pg.init()
janela=pg.display.set_mode((800,600))
sprite=pg.image.load("sprites_parados.png")
sair=False
x_sprite=0 # velociade
while not sair:
# Horiz,vertic,quanto pula, altura sprite, horiz sprite,por quanto tempo vai rolar a imagem
    janela.blit(sprite,(100,200),(x_sprite*120,40,50,50)) 
    pg.time.Clock().tick(10)
    pg.display.flip()

    # EXCLUSIVAMENTE PRA ESSE CODIGO
    for e in pg.event.get():
        if e.type == pg.QUIT or e.type == KEYDOWN and e.key == K_ESCAPE:
            sair = True

    x_sprite+=1
    if x_sprite > 10:
        x_sprite=0