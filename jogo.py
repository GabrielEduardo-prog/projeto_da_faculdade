import pygame
pygame.init()
pygame.display.set_caption("Run to the moon!")
vert_astr1=200
horiz_astr1=300
vel=5
gravidade=2.0
salto_astr1=15
salto_astr2=15
vert_astr2=200
horiz_astr2=200

janela=pygame.display.set_mode((1000,700))
background=pygame.image.load("terra4 700x700 (1).jpg")
astr1=pygame.image.load("astronauta_rosa-removebg-preview.png").convert_alpha()
astr2=pygame.image.load("astronauta branco.png").convert_alpha()
relogio = pygame.time.Clock()
janela_aberta=True

#Tela inicial antes de entrar no jogo 
def tela_inicial():
    fonte = pygame.font.SysFont("Arial", 60)
    fundo = background

    texto_botao = fonte.render("toque para começa", True, (0, 0, 0))
    botao_rect = pygame.Rect(250,300,500,100)  # posiçao: largura, altura proporçao: largura, altura

    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
              
                pygame.quit()
                exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_rect.collidepoint(evento.pos):
                    esperando = False

        janela.blit(fundo, (0, 0))

        # Efeito de passar o mouse em cima e trocar de cor
        cor_botao = (255,255,255)
        if botao_rect.collidepoint(pygame.mouse.get_pos()):
            cor_botao = (0, 0, 111)

        pygame.draw.rect(janela, cor_botao, botao_rect, border_radius=15)
        janela.blit(texto_botao, (botao_rect.x + 50, botao_rect.y + 20))
        pygame.display.update()
tela_inicial()
#Menu, no futuro da pra colocar mais coisa nele ate agora so fica no menu pra pausar msm
def menu_jogo():
    fonte = pygame.font.SysFont("Arial", 60)
    texto_pausa = fonte.render("PAUSADO", True, (255, 255, 0))
    texto_continuar = fonte.render("Continuar", True, (0, 0, 0))
    botao_continuar = pygame.Rect(350, 350, 300, 80)

    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
                #despausar apertando x ou clicando com o mouse achei que ficaria mais util
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_continuar.collidepoint(evento.pos):
                    esperando = False
            if evento.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                  esperando = False
        janela.blit(background, (0, 0))
        janela.blit(texto_pausa, (400, 200))

        cor_botao = (255, 255, 255)
        if botao_continuar.collidepoint(pygame.mouse.get_pos()):
            cor_botao = (0, 0, 110)

        pygame.draw.rect(janela, cor_botao, botao_continuar, border_radius=15)
        janela.blit(texto_continuar, (botao_continuar.x + 40, botao_continuar.y + 10))
        pygame.display.update()

# LOOP: tela simultania do jogo tudo que ta rodando em tempo real
while janela_aberta==True:
    relogio.tick(100) # o fps do jogo ja tinha colocado mas nao tinha explicado
    janela.blit(astr1,(horiz_astr1,vert_astr1))
    janela.blit(astr2,(horiz_astr2,vert_astr2))
    pygame.display.update()
    janela.blit(background,(0,0))
    
    for event in pygame.event.get():
        #fechamento
        if event.type == pygame.QUIT:
            janela_aberta = False

        if event.type == pygame.KEYDOWN:
               # Pausar o jogo permite que apertando x pause
            if event.key == pygame.K_x:
                menu_jogo()
# Movimentação dos astronautas 
            #pulo dos astronautas
            if event.key == pygame.K_UP and vert_astr1 > 0:
                  vert_astr1 -= salto_astr2 + 100
            if event.key == pygame.K_w and vert_astr2 > 0: 
                  vert_astr2 -= salto_astr1 + 100
    segurar=pygame.key.get_pressed()

    #astronauta 1
    #andar do personagem
    if segurar[pygame.K_LEFT] and horiz_astr1 > 0:
        horiz_astr1 -= vel
    if segurar[pygame.K_RIGHT] and horiz_astr1 < 950:
        horiz_astr1 += vel
    if segurar[pygame.K_DOWN] and vert_astr1 < 650:
        vert_astr1 += vel
    #para o astronauta 1 nao sair da tela
    if horiz_astr1 < 0:
        horiz_astr1 = 0
    if horiz_astr1 > 950:
        horiz_astr1 = 950
    if vert_astr1 < -10:
         vert_astr1 = -10
    if vert_astr1 > 635:
        vert_astr1 = 635

    #astronauta 2
    #andar do astronauta
    if segurar[pygame.K_a] and horiz_astr2 > 0:
        horiz_astr2 -= vel
    if segurar[pygame.K_d] and horiz_astr2 < 950:
        horiz_astr2 += vel
    if segurar[pygame.K_s] and vert_astr2 < 650:
        vert_astr2 += vel

   #pra o astronauta 2 nao sair da tela
    if horiz_astr2 < 0:
        horiz_astr2 = 0
    if horiz_astr2 > 950:
        horiz_astr2 = 950
    if vert_astr2 < -10:
        vert_astr2 = -10
    if vert_astr2 > 635:
        vert_astr2 = 635
    #A PARTE QUE EXPLICA PRO JOGADOR O BOTÃO DE PAUSE   
    botao_pausa = pygame.Rect(800,10, 200, 40)
    pygame.draw.rect(janela, (255, 0, 0), botao_pausa, border_radius=10)
    fonte_botao = pygame.font.SysFont("Arial", 24)
    texto_pause = fonte_botao.render("(X) PARA PAUSAR", True, (255, 255, 255))
    janela.blit(texto_pause, (botao_pausa.x + 10, botao_pausa.y + 5))

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


pygame.quit()