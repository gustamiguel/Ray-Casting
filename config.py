import math

# Configurações Gerais
LARGURA = 1200
ALTURA = 800
METADE_LARGURA =  LARGURA // 2
METADE_ALTURA = ALTURA // 2
FPS = 60
BLOCO = 50

# Configurações do Ray Casting
FOV = math.pi / 3
METADE_FOV = FOV / 2
NUM_RAIOS = 50     # DIMINUA SE ESTIVER LAGANDO
PROFUNDIDADE_MAX = 800        # TAMANHO DOS RAIOS
ANGULO_DELTA = FOV / NUM_RAIOS

# Configurações do Jogador

pos_player = (METADE_LARGURA, METADE_ALTURA)
ang_player = 0
vel_player = 2


# Cores

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (230, 0, 0)
VERDE = (0, 230, 0)
AZUL = (0, 0, 230)
CINZAESCURO = (110, 110, 110)
ROXO = (120, 0, 120)