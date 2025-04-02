import pygame
pygame.init()
pygame.display.set_caption("Run to the moon!")
vert_astr1=200
horiz_astr1=300
vel=30
gravidade=0.5
salto_astr1=15
salto_astr2=15
vert_astr2=300
horiz_astr2=200

janela=pygame.display.set_mode((1000,700))
background=pygame.image.load("terra4 700x700 (1).jpg")
astr1=pygame.image.load("astronauta_rosa-removebg-preview.png").convert()
astr2=pygame.image.load("astronauta branco.png").convert()
relogio = pygame.time.Clock()
janela_aberta=True

while janela_aberta==True:
    relogio.tick(100)
    janela.blit(astr1,(horiz_astr1,vert_astr1))
    janela.blit(astr2,(horiz_astr2,vert_astr2))
    pygame.display.update()
    janela.blit(background,(0,0))
    
    for event in pygame.event.get():

            # para o astronauta1
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP and vert_astr1>0:
                    vert_astr1=vert_astr1-salto_astr2-100

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_DOWN  and vert_astr1<650:
                    vert_astr1=vert_astr1+vel

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT and horiz_astr1>0:
                    horiz_astr1=horiz_astr1-vel

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT and horiz_astr1<950:
                    horiz_astr1=horiz_astr1+vel

        
                # TALVEZ PARA FAZER PULAR APENAS UMA VEZ, COLOCAR A CONDIÇÃO DE ESTAR TOCANDO UMA HITBOX? PODE GERAR ALGUNS BUGS
                # PARABOLA NA HORA DE PULAR E CAIR
            # para o astronauta 2
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_w and vert_astr2>0:
                    vert_astr2=vert_astr2-salto_astr1-100

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_s and vert_astr2<650:
                    vert_astr2=vert_astr2+vel

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_a and horiz_astr2>0:
                    horiz_astr2=horiz_astr2-vel

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_d and horiz_astr2<950:
                    horiz_astr2=horiz_astr2+vel

            

# para para a gente pode colocar um and nao tocando uma hitbox de uma pltaforma
    if vert_astr2<600:
        vert_astr2=vert_astr2+gravidade
    if vert_astr1<600:
        vert_astr1=vert_astr1+gravidade

# OQUE PRECISA FAZER: HITBOX
# OQUE PRECISA FAZER: HITBOX
# OQUE PRECISA FAZER: HITBOX
# OQUE PRECISA FAZER: HITBOX
# OQUE PRECISA FAZER: HITBOX
# OQUE PRECISA FAZER: HITBOX
# OQUE PRECISA FAZER: HITBOX









    if event.type==pygame.QUIT:
        janela_aberta=False
pygame.quit()