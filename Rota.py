import numpy as np 
import Grafo as g
visitado = []

def listaAcoes(first, grafo):
    # nesse caso é por profundidade
    # pesquisar com mais cuidado se é adjacente ou incidente
    retorno = []
    if(first.tipo == '-1'):
        return ['chegada']
    elif(not first in visitado):
        adjacentes = grafo[first]
        visitado.append(first)
        for aresta in adjacentes:
            retornoAux = listaAcoes(aresta.vertice2, grafo)
            if(retornoAux[retornoAux.__len__()-1:] == ['chegada']):
                if((retorno == [] or retorno.__len__()>retornoAux.__len__()) and retornoAux != []):
                    retorno = [aresta.acao] + retornoAux   
    return retorno

def listaAcoesL(first, grafo):
    # nesse caso é por largura
    retorno = []
    if(first.tipo == '-1'):
        return ['chegada']
    elif(not first in visitado):
        visitar = []
        visitado.append(first)
        visitar.append(first)
        while visitar[0] in grafo.keys():
            for aresta in grafo[visitar[0]]:
                if(not aresta.vertice2 in visitado):
                    retorno.append(aresta.acao)
                    visitado.append(aresta.vertice2)
                    visitar.append(aresta.vertice2)
            visitar.remove(visitar[0])
            if(visitar.__len__() == 0):
                break
            print(visitar[0].tipo)
    return retorno