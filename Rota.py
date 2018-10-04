import numpy as np 
import Grafo as g
visitado = []

def listaAcoes(first, grafo):
    # nesse caso é por profundidade
    # pesquisar com mais cuidado se é adjacente ou incidente
    if(first.tipo == '-1'):
        return ['chegada']
    elif(not first in visitado):
        retorno = []
        adjacentes = grafo[first]
        visitado.append(first)
        for aresta in adjacentes:
            retorno += listaAcoes(aresta.vertice2, grafo)
            if(retorno[retorno.__len__()-1:] == ['chegada']):
                return [aresta.acao] + retorno
            else:
                retorno = []
    return ['404']