import Grafo as g
# onde R representa a localização atual do robo
# interventor
# mapa = [['R','0','0','0','0','0'],
#         ['0','1','0','1','1','1'],
#         ['0','0','0','0','1','-1']]
# o mapa terá partes inacessíveis marcadas,
# isoladas por 1s sempre, então é adequado
# analisar de uma forma que seja possível
# trilhar um caminho até locais mais próximos 
# ao local inacessível, uma solução é tornar também
# a vizinhança marcada como local inacessível (como usarei por hora):
mapa = [['R','0','0','0','0' , '0'],
        ['0','1','0','1','-1','-1'],
        ['0','0','0','0','-1','-1']]
grf = g.G(mapa)
grf.toString()
