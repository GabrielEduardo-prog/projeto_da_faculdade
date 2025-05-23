import pygame
pygame.init()
pygame.display.set_caption("Run to the moon!")
hp1, vp1 = 300, 450
hp2, vp2= 200, 500
vel = 15
gravidade = 1
pulo1, pulo2 = 12, 15
vel_Y1, vel_Y2 = 0, pulo2
pulando, pulando2 = False, False
x_sprite=0
pulando1 = False
chao=450
forca_pulo=15
#plataforma_x, plataforma_y = -10, 400 #posição




janela=pygame.display.set_mode((1000,600))
background=pygame.image.load("sdf3.jpg")
background_remodelado=pygame.transform.scale(background,(1000,600))
fonte_m = pygame.font.SysFont("Arial", 20)
sprite=pygame.image.load("sprites_parados.png")
# plataforma_img = pygame.image.load("plataforma.png").convert_alpha()
# plataforma_img = pygame.transform.scale(plataforma_img, (400, 50))#largura(400) altura(50)


Cavaleiro_UM=pygame.image.load("sprites_parados.png").convert_alpha()
Cavaleiro_DOIS=pygame.image.load("astronauta_rosa-removebg-preview.png").convert_alpha()
largura = Cavaleiro_UM.get_width()  *2
altura = Cavaleiro_UM.get_height() * 2
Cavaleiro_UM = pygame.transform.scale(Cavaleiro_UM, (largura, altura))
astr1=Cavaleiro_UM
astr2=Cavaleiro_DOIS
mask_astro1 = pygame.mask.from_surface(astr1)

relogio = pygame.time.Clock()
janela_aberta=True
#INTERFACE 
def tela_inicial():
    fonte = pygame.font.SysFont("arial", 60)
    esperando = True

    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao.collidepoint(evento.pos):
                    esperando = False

       
        botao = pygame.Rect(250, 300, 450, 100)

        
        if botao.collidepoint(pygame.mouse.get_pos()):
            texto = fonte.render("click para jogar", True, (0, 0, 200)) #azul escuro
        else:
            texto = fonte.render("click para jogar", True, (0, 0, 0)) #preto

        janela.blit(background, (0, 0))
        janela.blit(texto, (botao.x + 50, botao.y + 20)) #desenha o texto sem retângulo
        pygame.display.update()
def menu_jogo():
    fonte = pygame.font.SysFont("Arial", 60)
    texto = fonte.render("PAUSADO", True, (255, 255, 0))
    continuar = fonte.render("Continuar", True, (0, 0, 0))
    botao = pygame.Rect(350, 350, 300, 80)

    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao.collidepoint(evento.pos):
                    esperando = False
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_x:
                esperando = False

        cor = (255, 255, 255)
        if botao.collidepoint(pygame.mouse.get_pos()):
            cor = (0, 0, 110)
        janela.blit(background, (0, 0))
        janela.blit(texto, (400, 200))
        pygame.draw.rect(janela, cor, botao, border_radius=15)
        janela.blit(continuar, (botao.x + 40, botao.y + 10))
        pygame.display.update()

#TELA INICIAL PARA RODAR
tela_inicial()

#LOOP DO JOGO 
while janela_aberta:
    relogio.tick(30)
    # DESENHAR FUNDO E PERSONAGENS
    janela.blit(background_remodelado, (0, 0))
    # janela.blit(plataforma_img, (plataforma_x, plataforma_y)) 
    # janela.blit(plataforma_img, (plataforma_x, plataforma_y))    




    # janela.blit(astr2, (hp2, vp2))
    janela.blit(astr2, (hp2, vp2),(x_sprite*240,80,100,100))
    janela.blit(astr1,(hp1,vp1),(x_sprite*240,80,100,100)) 
    # pygame.time.Clock().tick(12)

    #máscaras de colisão pixel por pixel
    # mask_astro1 = pygame.mask.from_surface(astr1)
    # mask_plataforma = pygame.mask.from_surface(plataforma_img)
    # offset_plataforma = (int(plataforma_x - hp1), int(plataforma_y - vp1 + altura - 10))
    # colidindo = mask_astro1.overlap(mask_plataforma, offset_plataforma)

    # pygame.time.Clock().tick(12)


    x_sprite+=1
    if x_sprite > 9:
        x_sprite=0








    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
            menu_jogo()

    segurar = pygame.key.get_pressed()
    if segurar[pygame.K_a] and hp1 > 0:
        hp1 -= vel

    if segurar[pygame.K_d] and hp1 < 950:
        hp1 += vel
        # Iniciar pulo
    if segurar[pygame.K_w] and not pulando1 and vp1 >= chao:
        vel_Y1 = -forca_pulo
        pulando1 = True

    # # Atualizar física do pulo
    if pulando1:
        vp1 += vel_Y1
        vel_Y1 += gravidade
        if vp1 >=chao:
            vp1 = chao
            vel_Y1 = 0
            pulando1 = False
    # Física do pulo com colisão com plataforma
    # if pulando1:
    #     vp1 += vel_Y1
    #     vel_Y1 += gravidade
    #     offset_plataforma = (int(plataforma_x - hp1), int(plataforma_y - vp1 + altura - 10))
    #     colidindo = mask_astro1.overlap(mask_plataforma, offset_plataforma)
    
    #     if vel_Y1 > 0 and colidindo:  # Está descendo e colidiu
    #         vp1 = plataforma_y - altura + 10
    #         vel_Y1 = 0
    #         pulando1 = False
    #     elif vp1 >= chao and not colidindo:
    #         vp1 = chao
    #         vel_Y1 = 0
    #         pulando1 = False
    # else:
    # # Aplica gravidade quando não está pulando
    #     if vp1 < chao:
    #         vp1 += gravidade
    #         offset_plataforma = (int(plataforma_x - hp1), int(plataforma_y - vp1 + altura - 10))
    #         colidindo = mask_astro1.overlap(mask_plataforma, offset_plataforma)
    #         if colidindo:
    #             vp1 = plataforma_y - altura + 10




    


    # #COLISÃO PIXEL POR PIXEL
    # capa1 = pygame.mask.from_surface(astr1)
    # capa2 = pygame.mask.from_surface(astr2)

    # if segurar[pygame.K_d] and hp1 < 950:
    #     offset = (hp2 - (hp1 + vel), vp2 - vp1)
    # if not capa1.overlap(capa2, offset):
    #     hp1 += vel


    # #MOVIMENTO ASTRONAUTA 1 (A-D-W) O ROSA
    # if segurar[pygame.K_a] and hp1 > 0:
    #     offset = (hp2 - (hp1 - vel), vp2- vp1)
    #     if not capa1.overlap(capa2, offset):
    #         hp1 -= vel
    # if segurar[pygame.K_d] and hp1 < 950:
    #     offset = (hp2 - (hp1 + vel), vp2- vp1)
    #     if not capa1.overlap(capa2, offset):
    #         hp1 += vel
    # if segurar[pygame.K_w] and not pulando1:
    #     pulando1 = True
    #     vel_Y1 = pulo1

    # if pulando1:
    #     nova_vert = vp1 - vel_Y1
    #     offset = (hp2 - hp1, vp2- nova_vert)
    #     if not capa1.overlap(capa2, offset):
    #         vp1 = nova_vert
    #     vel_Y1 -= gravidade
    #     if vel_Y1 < -pulo1:
    #         pulando1 = False

    # elif vp1 < 500:
    #     offset = (hp2 - hp1, vp2- (vp1 + gravidade))
    #     if not capa1.overlap(capa2, offset):
    #         vp1 += gravidade

    # #MOVIMENTO ASTRONAUTA 2 (LEFT-RIGHT-UP) O BRANCO
    # if segurar[pygame.K_LEFT] and hp2 > 0:
    #     offset = (hp1 - (hp2 - vel), vp1 - vp2)
    #     if not capa2.overlap(capa1, offset):
    #         hp2 -= vel
    # if segurar[pygame.K_RIGHT] and hp2 < 950:
    #     offset = (hp1 - (hp2 + vel), vp1 - vp2)
    #     if not capa2.overlap(capa1, offset):
    #         hp2 += vel
    # if segurar[pygame.K_UP] and not pulando2:
    #     pulando2 = True
    #     vel_Y2 = pulo2

    # if pulando2:
    #     nova_vert = vp2- vel_Y2
    #     offset = (hp1 - hp2, vp1 - nova_vert)
    #     if not capa2.overlap(capa1, offset):
    #         vp2= nova_vert
    #     vel_Y2 -= gravidade
    #     if vel_Y2 < -pulo2:
    #         pulando2 = False

    # elif vp2< 500:
    #     offset = (hp1 - hp2, vp1 - (vp2+ gravidade))
    #     if not capa2.overlap(capa1, offset):
    #         vp2+= gravidade

    # LIMITES DE TELA
    vp1 = max(0, min(vp1, 500))
    hp2 = max(0, min(hp2, 942))
    vp2= max(0, min(vp2, 500))

    #nome em cima dos personagens
    nome1 = fonte_m.render("P1", True, (255, 0, 0))  # Rosa: rosa
    # nome2 = fonte_m.render("P2", True, (250, 200,0))  # Branco: branco

    # # Centralizar o texto em cima do personagem
    janela.blit(nome1, (hp1 + Cavaleiro_DOIS.get_width()//2 - nome1.get_width()//2, vp1 - 25))
    # janela.blit(nome2, (hp2 + astr2.get_width()//2 - nome2.get_width()//2, vp2- 25))
    # Botão de pausa
    botao = pygame.Rect(800, 10, 200, 40)
    pygame.draw.rect(janela, (255, 0, 0), botao, border_radius=10)
    fonte = pygame.font.SysFont("Arial", 24)
    texto = fonte.render("(X) PARA PAUSAR", True, (255, 255, 255))
    janela.blit(texto, (botao.x + 10, botao.y + 5))

    pygame.display.update()

pygame.quit()