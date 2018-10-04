import Grafo as g
import Rota as r
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
mapa = [['0','0','0','0','0' , '0'],
        ['0','1','0','1','1','-1'],
        ['0','0','0','0','1','-1']]
grf = g.G(mapa)
# pega o termo inicial, no qual o robô interventor estará
for first in grf.grafo.keys():
        break
print(r.listaAcoes(first,grf.grafo))
# grf.toString()
