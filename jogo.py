import pygame
from PIL import Image
pygame.init()
pygame.display.set_caption("Run to the moon!")
# cavaleiro1
hp1, vp1 = 300, 450
vel = 15
gravidade = 1
pulo1 = 12
vel_Y1= 0
pulando= False
caindo1=False
atacando1=False
x_sprite=0
pulando1 = False
chao=450
forca_pulo=15
Cavaleiro1_esquerda=False
cavaleiro1_direita=True
tempo_ataque=0
#plataforma_x, plataforma_y = -10, 400 #posição
# Cavaleiro DOIS; Player DOIS
hp2, vp2 = 500, 450
vel2 = 15
gravidade2 = 1
forca_pulo2 = 15
vel_Y2 = 0
pulando2 = False
caindo2 = False
atacando2 = False
x_sprite2 = 0
cavaleiro2_direita = True
cavaleiro2_esquerda = False

# SOM
Soundtrack= pygame.mixer.Sound("horror-background-atmosphere-156462.mp3")
Soundtrack.play(loops=-1)
andando_som=pygame.mixer.Sound("running-on-concrete-268478.mp3")
andando_canal=pygame.mixer.Channel(1)
andando_canal2=pygame.mixer.Channel(2)

# Display, blackground
janela=pygame.display.set_mode((1000,600))
background=pygame.image.load("sdf3.jpg")
background_remodelado=pygame.transform.scale(background,(1000,600))
fonte_m = pygame.font.SysFont("Arial", 20)
sprite2=pygame.image.load("_Idle_2_parado_recortado_esquerda.png")
sprite=pygame.image.load("sprites_parados.png")
filtro = pygame.Surface((1000, 600))

# Cavaleiro UM; Player UM
Cavaleiro_UM_parado_esquerda=pygame.image.load("sprite_parado_esquerdo.png")
Cavaleiro_UM_atacando_esquerda=pygame.image.load("_Attack_recortado_esquerda.png")
Cavaleiro_UM_atacando_direita=pygame.image.load("_Attack_recortado.png")
Cavaleiro_UM_correndo_direita=pygame.image.load("_Run_recortado.png").convert_alpha()
Cavaleiro_UM_correndo_esquerda=pygame.image.load("_Run_recortado_esquerda.png").convert_alpha()
Cavaleiro_UM_pulando_esquerda=pygame.image.load("_Jump_esquerda.png")
Cavaleiro_UM_pulando=pygame.image.load("_Jump.png")
Cavaleiro_UM_caindo=pygame.image.load("_Fall.png")
Cavaleiro_UM_caindo_esquerda=pygame.image.load("_Fall_PNG_esquerda.png")
Cavaleiro_UM_parado=pygame.image.load("sprites_parados.png").convert_alpha()
largura = Cavaleiro_UM_parado.get_width()  *2
altura = Cavaleiro_UM_parado.get_height() * 2
largura_pulando = Cavaleiro_UM_pulando.get_width()  *2
altura_pulando = Cavaleiro_UM_pulando.get_height() * 2
largura_pulando_esquerda = Cavaleiro_UM_pulando_esquerda.get_width()  *2
altura_pulando_esquerda = Cavaleiro_UM_pulando_esquerda.get_height() *2
largura_correndo_direita = Cavaleiro_UM_correndo_direita.get_width()  *2
altura_correndo_direita = Cavaleiro_UM_correndo_direita.get_height() * 2
largura_correndo_esquerda = Cavaleiro_UM_correndo_esquerda.get_width()  *2
altura_correndo_esquerda = Cavaleiro_UM_correndo_esquerda.get_height() * 2
largura_cavaleiro1_parado_esquerda=Cavaleiro_UM_parado_esquerda.get_width() * 2
altura_cavaleiro1_parado_esquerda=Cavaleiro_UM_parado_esquerda.get_height() * 2
largura_cavaleiro1_caindo=Cavaleiro_UM_caindo.get_width() * 2
altura_cavaleiro1_caindo=Cavaleiro_UM_caindo.get_height() * 2
largura_cavaleiro1_caindo_esquerda=Cavaleiro_UM_caindo_esquerda.get_width() * 2
altura_cavaleiro1_caindo_esquerda=Cavaleiro_UM_caindo_esquerda.get_height() * 2
altura_cavaleiro1_atacando_direita=Cavaleiro_UM_atacando_direita.get_width()*2
largura_cavaleiro1_atacando_direita=Cavaleiro_UM_atacando_direita.get_height()*2
altura_cavaleiro1_atacando_esquerda=Cavaleiro_UM_atacando_esquerda.get_width()*2
largura_cavaleiro1_atacando_esquerda=Cavaleiro_UM_atacando_esquerda.get_height()*2
Cavaleiro_UM_correndo_esquerda = pygame.transform.scale(Cavaleiro_UM_correndo_esquerda, (largura_correndo_esquerda, altura_correndo_esquerda))
Cavaleiro_UM_correndo_direita = pygame.transform.scale(Cavaleiro_UM_correndo_direita, (largura_correndo_direita, altura_correndo_direita))
Cavaleiro_UM_pulando = pygame.transform.scale(Cavaleiro_UM_pulando, (largura_pulando, altura_pulando))
Cavaleiro_UM_parado = pygame.transform.scale(Cavaleiro_UM_parado, (largura, altura))
Cavaleiro_UM_parado_esquerda= pygame.transform.scale(Cavaleiro_UM_parado_esquerda,(largura_cavaleiro1_parado_esquerda,altura_cavaleiro1_parado_esquerda))
Cavaleiro_UM_pulando_esquerda= pygame.transform.scale(Cavaleiro_UM_pulando_esquerda,(largura_pulando_esquerda, altura_pulando_esquerda))
Cavaleiro_UM_caindo=pygame.transform.scale(Cavaleiro_UM_caindo,(largura_cavaleiro1_caindo,altura_cavaleiro1_caindo))
Cavaleiro_UM_caindo_esquerda=pygame.transform.scale(Cavaleiro_UM_caindo_esquerda,(largura_cavaleiro1_caindo_esquerda, altura_cavaleiro1_caindo_esquerda))
Cavaleiro_UM_atacando_direita=pygame.transform.scale(Cavaleiro_UM_atacando_direita,(largura_cavaleiro1_atacando_direita,altura_cavaleiro1_atacando_direita))
Cavaleiro_UM_atacando_esquerda=pygame.transform.scale(Cavaleiro_UM_atacando_esquerda,(largura_cavaleiro1_atacando_esquerda,altura_cavaleiro1_atacando_esquerda))
astr1=Cavaleiro_UM_parado
mask_astro1 = pygame.mask.from_surface(astr1)

# Cavaleiro2
Cavaleiro_DOIS_parado_direita = pygame.image.load("_Idle_2_parado_recortado.png")
Cavaleiro_DOIS_parado_esquerda = pygame.image.load("_Idle_2_parado_recortado_esquerda.png")
Cavaleiro_DOIS_correndo_direita = pygame.image.load("_Run2_recortado.png")
Cavaleiro_DOIS_correndo_esquerda = pygame.image.load("_Run2_recortado_esquerda.png")
Cavaleiro_DOIS_pulando_direita = pygame.image.load("_Jump2.png")
Cavaleiro_DOIS_pulando_esquerda = pygame.image.load("_Jump2_esquerda.png")

# Dimensões do Cavaleiro 2
largura_cavaleiro2_parado = Cavaleiro_DOIS_parado_direita.get_width() * 2
altura_cavaleiro2_parado = Cavaleiro_DOIS_parado_direita.get_height() * 2
largura_cavaleiro2_parado_esquerda = Cavaleiro_DOIS_parado_esquerda.get_width() * 2
altura_cavaleiro2_parado_esquerda = Cavaleiro_DOIS_parado_esquerda.get_height() * 2
largura_cavaleiro2_pulando_direita = Cavaleiro_DOIS_pulando_direita.get_width() * 2
altura_cavaleiro2_pulando_direita = Cavaleiro_DOIS_pulando_direita.get_height() * 2
largura_cavaleiro2_pulando_esquerda = Cavaleiro_DOIS_pulando_esquerda.get_width() * 2
altura_cavaleiro2_pulando_esquerda = Cavaleiro_DOIS_pulando_esquerda.get_height() * 2
largura_cavaleiro2_correndo_direita = Cavaleiro_DOIS_correndo_direita.get_width() * 2
altura_cavaleiro2_correndo_direita = Cavaleiro_DOIS_correndo_direita.get_height() * 2
largura_cavaleiro2_correndo_esquerda = Cavaleiro_DOIS_correndo_esquerda.get_width() * 2
altura_cavaleiro2_correndo_esquerda = Cavaleiro_DOIS_correndo_esquerda.get_height() * 2

# Redimensionamento do cavaleiro2
Cavaleiro_DOIS_parado_direita = pygame.transform.scale(Cavaleiro_DOIS_parado_direita, (largura_cavaleiro2_parado, altura_cavaleiro2_parado))
Cavaleiro_DOIS_parado_esquerda = pygame.transform.scale(Cavaleiro_DOIS_parado_esquerda, (largura_cavaleiro2_parado_esquerda, altura_cavaleiro2_parado_esquerda))
Cavaleiro_DOIS_pulando_direita = pygame.transform.scale(Cavaleiro_DOIS_pulando_direita, (largura_cavaleiro2_pulando_direita, altura_cavaleiro2_pulando_direita))
Cavaleiro_DOIS_pulando_esquerda = pygame.transform.scale(Cavaleiro_DOIS_pulando_esquerda, (largura_cavaleiro2_pulando_esquerda, altura_cavaleiro2_pulando_esquerda))
Cavaleiro_DOIS_correndo_direita = pygame.transform.scale(Cavaleiro_DOIS_correndo_direita, (largura_cavaleiro2_correndo_direita, altura_cavaleiro2_correndo_direita))
Cavaleiro_DOIS_correndo_esquerda = pygame.transform.scale(Cavaleiro_DOIS_correndo_esquerda, (largura_cavaleiro2_correndo_esquerda, altura_cavaleiro2_correndo_esquerda))


relogio = pygame.time.Clock()
janela_aberta=True
#Carregar do Gif
def carregar_gif_para_frames(caveira):
    gif = Image.open(caveira)
    frames = []
    try:
        while True:
            frame = gif.convert("RGBA")
            modo = frame.mode
            tamanho = frame.size
            dados = frame.tobytes()
            py_image = pygame.image.fromstring(dados, tamanho, modo)
            frames.append(py_image)
            gif.seek(gif.tell() + 1)
    except EOFError:
        pass
    return frames

frames_gif = carregar_gif_para_frames("cov.gif")
#Tela inicial 
def tela_inicial():
    fonte = pygame.font.SysFont("arial", 60)
    esperando = True
    frame_atual = 0
    tempo_ultimo_frame = pygame.time.get_ticks()
    intervalo_frame = 50 

    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao.collidepoint(evento.pos):
                    esperando = False

        botao = pygame.Rect(25, 30, 450, 100)

        
        agora = pygame.time.get_ticks()
        if agora - tempo_ultimo_frame > intervalo_frame:
            frame_atual = (frame_atual + 1) % len(frames_gif)
            tempo_ultimo_frame = agora

        if botao.collidepoint(pygame.mouse.get_pos()):
            texto = fonte.render("New Game", True, (0, 0, 200))
        else:
            texto = fonte.render("New Game", True, (200, 0, 0))

        janela.blit(background, (0, 0))
        janela.blit(frames_gif[frame_atual], (0, 0))  
        janela.blit(texto, (botao.x + 5, botao.y + 2))
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

        
        if botao.collidepoint(pygame.mouse.get_pos()):
            continuar = fonte.render("Continuar", True, (0, 0,200))
        else:
            continuar = fonte.render("Continuar", True, (0, 0,0 ))
        
        janela.blit(background, (0, 0))
        janela.blit(texto, (400, 200))
        janela.blit(continuar, (botao.x + 40, botao.y + 10))
        pygame.display.update()
#RODAR
tela_inicial()

#LOOP DO JOGO 
while janela_aberta:
    relogio.tick(30)
    janela.blit(background_remodelado, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
            menu_jogo()

    segurar = pygame.key.get_pressed()

    # Movimento cavaleiro1
    if segurar[pygame.K_a] and hp1 > 0 and not(segurar[pygame.K_d]):
        hp1 -= vel
        x_sprite += 1
        if x_sprite > 9:
            x_sprite = 0

    if segurar[pygame.K_d] and hp1 < 950 and not(segurar[pygame.K_a]):
        hp1 += vel
        x_sprite += 1
        if x_sprite > 9:
            x_sprite = 0

    if segurar[pygame.K_w] and not(pulando1):
        vel_Y1 = -forca_pulo
        pulando1 = True

    #PULO ( se VARIAVEL DE CAIR= caindo1)
    if pulando1: 
        vp1 += vel_Y1
        vel_Y1 += gravidade
        x_sprite += 1
        if x_sprite > 2:
            x_sprite = 0
        if vp1 >= chao:
            vp1 = chao
            vel_Y1 = 0
            pulando1 = False

    # MOVIMENTO DO CAVALEIRO 2
    if segurar[pygame.K_LEFT] and hp2 > 0 and not(segurar[pygame.K_RIGHT]):
        hp2 -= vel2
        x_sprite2 += 1
        if x_sprite2 > 9:
            x_sprite2 = 0

    if segurar[pygame.K_RIGHT] and hp2 < 950 and not(segurar[pygame.K_LEFT]):
        hp2 += vel2
        x_sprite2 += 1
        if x_sprite2 > 9:
            x_sprite2 = 0

    if segurar[pygame.K_UP] and not pulando2 and vp2 >= chao:
        vel_Y2 = -forca_pulo2
        pulando2 = True

    # PULO DO CAVALEIRO 2
    if pulando2:
        vp2 += vel_Y2
        vel_Y2 += gravidade2
        x_sprite2 += 1
        if x_sprite2 > 2:
            x_sprite2 = 0
        if vp2 >= chao:
            vp2 = chao
            vel_Y2 = 0
            pulando2 = False

                
    # ESCOLHA DO SPRITE 
    if cavaleiro1_direita==True:
        sprite_atual = Cavaleiro_UM_parado
    if Cavaleiro1_esquerda==True:
        sprite_atual = Cavaleiro_UM_parado_esquerda 
    if pulando1:
        if cavaleiro1_direita:
            sprite_atual = Cavaleiro_UM_pulando
        if Cavaleiro1_esquerda:
            sprite_atual=Cavaleiro_UM_pulando_esquerda
    
    if pulando1:
        if segurar[pygame.K_a]:
            Cavaleiro1_esquerda = True
            cavaleiro1_direita = False
        elif segurar[pygame.K_d]:
            cavaleiro1_direita = True
            Cavaleiro1_esquerda = False

    elif segurar[pygame.K_a] and hp1 > 0 and not(segurar[pygame.K_d]):
        sprite_atual = Cavaleiro_UM_correndo_esquerda
        Cavaleiro1_esquerda=True
        cavaleiro1_direita=False



    elif segurar[pygame.K_d] and hp1 < 950 and not(segurar[pygame.K_a]):
        sprite_atual = Cavaleiro_UM_correndo_direita
        Cavaleiro1_esquerda=False
        cavaleiro1_direita=True


    elif atacando1==True:
        if cavaleiro1_direita:
            sprite_atual = Cavaleiro_UM_atacando_direita
        else:
            sprite_atual = Cavaleiro_UM_atacando_esquerda

    else:
        x_sprite += 1
        if x_sprite > 9:
            x_sprite = 0
            



        # ESCOLHA DO SPRITE DO CAVALEIRO 2
    if cavaleiro2_direita:
        sprite_atual2 = Cavaleiro_DOIS_parado_direita
    if cavaleiro2_esquerda:
        sprite_atual2 = Cavaleiro_DOIS_parado_esquerda
    if pulando2:
        if cavaleiro2_direita:
            sprite_atual2 = Cavaleiro_DOIS_pulando_direita
        if cavaleiro2_esquerda:
            sprite_atual2 = Cavaleiro_DOIS_pulando_esquerda
    
    if pulando2:
        if cavaleiro2_direita:
            sprite_atual2 = Cavaleiro_DOIS_pulando_direita
        elif cavaleiro2_esquerda:
            sprite_atual2 = Cavaleiro_DOIS_pulando_esquerda

    elif segurar[pygame.K_LEFT] and hp2 > 0 and not(segurar[pygame.K_RIGHT]):
        sprite_atual2 = Cavaleiro_DOIS_correndo_esquerda
        cavaleiro2_esquerda = True
        cavaleiro2_direita = False

    elif segurar[pygame.K_RIGHT] and hp2 < 950 and not(segurar[pygame.K_LEFT]):
        sprite_atual2 = Cavaleiro_DOIS_correndo_direita
        cavaleiro2_esquerda = False
        cavaleiro2_direita = True

    else:
        x_sprite2 += 1
        if x_sprite2 > 9:
            x_sprite2 = 0

     # Desenho do personagem 1/2
    janela.blit(sprite_atual, (hp1, vp1), (x_sprite*240, 80, 100, 100))
    janela.blit(sprite_atual2, (hp2, vp2), (x_sprite2*240, 80, 100, 100))

    # Sons do personagem 1
    teclas = pygame.key.get_pressed()

    andando = (teclas[pygame.K_a] and not teclas[pygame.K_d]) or (teclas[pygame.K_d] and not teclas[pygame.K_a]) 

    if andando:
        if not andando_canal.get_busy():
            andando_canal.play(andando_som, loops=-1)
    else:
        andando_canal.stop()

    # Som do personagem 1
    andando2 = (teclas[pygame.K_LEFT] and not teclas[pygame.K_RIGHT]) or (teclas[pygame.K_RIGHT] and not teclas[pygame.K_LEFT]) 

    if andando2:
        if not andando_canal2.get_busy():
            andando_canal2.play(andando_som, loops=-1)
    else:
        andando_canal2.stop()

    # LIMITES DE TELA
    vp1 = max(0, min(vp1, 500))
    hp2 = max(0, min(hp2, 942))
    vp2= max(0, min(vp2, 500))

    # Botão de pausa
    botao = pygame.Rect(30, 10, 200, 40)
    fonte = pygame.font.SysFont("Arial", 20)
    texto = fonte.render("(X) PARA PAUSAR", True, (255, 255, 255))
    janela.blit(texto, (botao.x + 10, botao.y + 5))

    filtro.fill((0, 0, 30))
    filtro.set_alpha(120)
    janela.blit(filtro, (0, 0))
    pygame.display.update()

pygame.quit()