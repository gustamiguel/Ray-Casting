from config import *

mapa = [
     '########################',
     '#                      #',
     '#                      #',
     '#   ######    #  ###   #',
     '#   #         #    #   #',
     '#   #    ######    #   #',
     '#                  #   #',
     '#                      #',
     '#   ##  ##   #         #',
     '#   #    #   ###  ##   #',
     '#   #        #     #   #',
     '#   #        #     #   #',
     '#   ######   ###   #   #',
     '#                      #',
     '#                      #',
     '########################'
]

mapa_mundo = set()

for j, linha in enumerate(mapa):
    for i, letra in enumerate(linha):
        if letra == '#':
            mapa_mundo.add((i * BLOCO, j * BLOCO))