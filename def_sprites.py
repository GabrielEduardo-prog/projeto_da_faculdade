import pygame as pg
from pygame.locals import *
pg.init()
janela=pg.display.set_mode((800,600))
sprite=pg.image.load("_Attack_recortado.png")
sair=False
x_sprite=0 # velociade
while not sair:
# Horiz,vertic,quanto pula, altura sprite, horiz sprite,por quanto tempo vai rolar a imagem
    janela.blit(sprite, (200,300), (x_sprite * 87, 0, 50,100))
    pg.time.Clock().tick(10)
    pg.display.flip()

    # EXCLUSIVAMENTE PRA ESSE CODIGO
    for e in pg.event.get():
        if e.type == pg.QUIT or e.type == KEYDOWN and e.key == K_ESCAPE:
            sair = True

    x_sprite+=1
    if x_sprite >4:
        x_sprite=0