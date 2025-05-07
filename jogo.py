from PIL import Image
import pygame
pygame.init()
pygame.display.set_caption("Run to the moon!")
horiz_astr1, vert_astr1 = 200, 500
horiz_astr2, vert_astr2 = 300, 500
vel = 5
gravidade = 1
pulo1, pulo2 = 15, 15
vel_Y1, vel_Y2 = pulo1, pulo2
pulando1, pulando2 = False, False
# ABRIR O GIF E PEGAR QUADROS 
gif = Image.open("beleza.gif")
quadros = []
try:
    while True:
        quadro = gif.copy()
        quadro = quadro.convert("RGBA")  # converte para fundo transparente
        quadro_pygame = pygame.image.fromstring(
            quadro.tobytes(), quadro.size, quadro.mode
        )
        quadro_pygame = pygame.transform.scale(quadro_pygame, (1000, 620))  # Redimensiona
        quadros.append(quadro_pygame)
        gif.seek(gif.tell() + 1)
except EOFError:
    pass  # Chegou no final dos quadros

# CONTROLE DE ANIMAÇÃO 
indice_quadro = 0
tempo_animacao = 100  # milissegundos entre quadros
ultimo_update = pygame.time.get_ticks()

janela=pygame.display.set_mode((1000,600))
background=pygame.image.load("beleza.gif")
background_remodelado=pygame.transform.scale(background,(1000,700))
fonte_m = pygame.font.SysFont("Arial", 20)

astronauta_normal_branco=pygame.image.load("astronauta branco.png").convert_alpha()
astronauta_normal_rosa=pygame.image.load("astronauta_rosa-removebg-preview.png").convert_alpha()
astr1=astronauta_normal_rosa
astr2=astronauta_normal_branco

relogio = pygame.time.Clock()
janela_aberta=True
#INTERFACE 
def tela_inicial():
    fonte = pygame.font.SysFont("arial", 60)
    texto = fonte.render("click para jogar", True, (0, 0, 0))
    botao = pygame.Rect(250, 300, 450, 100)

    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao.collidepoint(evento.pos):
                    esperando = False

        cor_botao = (255, 255, 255)
        if botao.collidepoint(pygame.mouse.get_pos()):
            cor_botao = (0, 0, 111)
        janela.blit(background, (0, 0))
        pygame.draw.rect(janela, cor_botao, botao, border_radius=15)
        janela.blit(texto, (botao.x + 50, botao.y + 20))
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
    relogio.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
            menu_jogo()

    segurar = pygame.key.get_pressed()

    #COLISÃO PIXEL POR PIXEL
    capa1 = pygame.mask.from_surface(astr1)
    capa2 = pygame.mask.from_surface(astr2)

    #MOVIMENTO ASTRONAUTA 1 (A-D-W) O ROSA
    if segurar[pygame.K_a] and horiz_astr1 > 0:
        offset = (horiz_astr2 - (horiz_astr1 - vel), vert_astr2 - vert_astr1)
        if not capa1.overlap(capa2, offset):
            horiz_astr1 -= vel
    if segurar[pygame.K_d] and horiz_astr1 < 950:
        offset = (horiz_astr2 - (horiz_astr1 + vel), vert_astr2 - vert_astr1)
        if not capa1.overlap(capa2, offset):
            horiz_astr1 += vel
    if segurar[pygame.K_w] and not pulando1:
        pulando1 = True
        vel_Y1 = pulo1

    if pulando1:
        nova_vert = vert_astr1 - vel_Y1
        offset = (horiz_astr2 - horiz_astr1, vert_astr2 - nova_vert)
        if not capa1.overlap(capa2, offset):
            vert_astr1 = nova_vert
        vel_Y1 -= gravidade
        if vel_Y1 < -pulo1:
            pulando1 = False

    elif vert_astr1 < 500:
        offset = (horiz_astr2 - horiz_astr1, vert_astr2 - (vert_astr1 + gravidade))
        if not capa1.overlap(capa2, offset):
            vert_astr1 += gravidade

    #MOVIMENTO ASTRONAUTA 2 (LEFT-RIGHT-UP) O BRANCO
    if segurar[pygame.K_LEFT] and horiz_astr2 > 0:
        offset = (horiz_astr1 - (horiz_astr2 - vel), vert_astr1 - vert_astr2)
        if not capa2.overlap(capa1, offset):
            horiz_astr2 -= vel
    if segurar[pygame.K_RIGHT] and horiz_astr2 < 950:
        offset = (horiz_astr1 - (horiz_astr2 + vel), vert_astr1 - vert_astr2)
        if not capa2.overlap(capa1, offset):
            horiz_astr2 += vel
    if segurar[pygame.K_UP] and not pulando2:
        pulando2 = True
        vel_Y2 = pulo2

    if pulando2:
        nova_vert = vert_astr2 - vel_Y2
        offset = (horiz_astr1 - horiz_astr2, vert_astr1 - nova_vert)
        if not capa2.overlap(capa1, offset):
            vert_astr2 = nova_vert
        vel_Y2 -= gravidade
        if vel_Y2 < -pulo2:
            pulando2 = False

    elif vert_astr2 < 500:
        offset = (horiz_astr1 - horiz_astr2, vert_astr1 - (vert_astr2 + gravidade))
        if not capa2.overlap(capa1, offset):
            vert_astr2 += gravidade

    # LIMITES DE TELA
    horiz_astr1 = max(0, min(horiz_astr1, 942))
    vert_astr1 = max(0, min(vert_astr1, 500))
    horiz_astr2 = max(0, min(horiz_astr2, 942))
    vert_astr2 = max(0, min(vert_astr2, 500))

    # Atualizar quadro do fundo 
    agora = pygame.time.get_ticks()
    if agora - ultimo_update > tempo_animacao:
        indice_quadro = (indice_quadro + 1) % len(quadros)
        ultimo_update = agora

    #Desenha o fundo animado
    janela.blit(quadros[indice_quadro], (0, 0))
    janela.blit(astr2, (horiz_astr2, vert_astr2))
    janela.blit(astr1, (horiz_astr1, vert_astr1))
        # Desenhar nomes dos astronautas
    nome1 = fonte_m.render("P1", True, (255, 0, 0))  # Rosa: rosa pink
    nome2 = fonte_m.render("P2", True, (250, 200,0))  # Branco: branco

    # Centralizar o texto em cima do personagem
    janela.blit(nome1, (horiz_astr1 + astr1.get_width()//2 - nome1.get_width()//2, vert_astr1 - 25))
    janela.blit(nome2, (horiz_astr2 + astr2.get_width()//2 - nome2.get_width()//2, vert_astr2 - 25))
    # Botão de pausa
    botao = pygame.Rect(800, 10, 200, 40)
    pygame.draw.rect(janela, (255, 0, 0), botao, border_radius=10)
    fonte = pygame.font.SysFont("Arial", 24)
    texto = fonte.render("(X) PARA PAUSAR", True, (255, 255, 255))
    janela.blit(texto, (botao.x + 10, botao.y + 5))

    pygame.display.update()

pygame.quit()