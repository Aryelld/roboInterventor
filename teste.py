import Grafo as g
# onde R representa a localização atual do robo
# interventor
mapa = [['R','0','0','0','0','0'],
        ['0','1','0','1','1','0'],
        ['0','0','0','0','1','-1']]
grafo = g.G(mapa)
print(grafo.toString())
