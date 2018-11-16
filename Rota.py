import numpy as np 
import Grafo as g

def listaAcoes(first, grafo):
    # nesse caso é por profundidade
    # pesquisar com mais cuidado se é adjacente ou incidente
    visitado = []
    retorno = []
    if(first.tipo == -1):
        return []
    elif(not first in visitado):
        adjacentes = grafo[first]
        visitado.append(first)
        for aresta in adjacentes:
            retornoAux = listaAcoes(aresta.vertice2, grafo)
            if(retornoAux[retornoAux.__len__()-1:] == ['chegada']):
                if((retorno == [] or retorno.__len__()>retornoAux.__len__()) and retornoAux != []):
                    retorno = [aresta.acao] + retornoAux   
    return retorno

def passosLargura(origem, grafo):
    # nesse caso é por largura
    visitado=[]
    fila=[]
    retorno=[origem]
    vertices=[]
    daVez=origem
    found=False
    fila=fila+[origem]
    while(fila):
        daVez = fila[0]
        fila = fila[1:]
        vertices = [a.vertice2 for a in grafo[daVez]]
        while(vertices):
            v = vertices[0]
            vertices = vertices[1:]
            if(v not in visitado):
                if(v.tipo == -1):
                    found = True
                    break
                retorno += [v]
        if(found):
            break

    return retorno

def listaAcoesL(visit, grf):
    passos = passosLargura(visit,grf.grafo)
    acoes = []
    for i in range(passos.__len__()-1):
        print(grf.getAresta(passos[i],passos[i+1]))
        acoes.append(grf.getAresta(passos[i],passos[i+1]).acao)
    return acoes

def listaAcoesBreadthSearch(origem, grf):
    # niveis percorridos na "arvore" em largura
    niveis = breadthSearch(origem, grf.grafo)
    nNiveis = niveis.__len__()
    daVez = niveis[nNiveis-1][0]
    retorno = []
    for i in range(nNiveis-2):
        for vertice in niveis[nNiveis-2-i]:
            aresta = grf.getAresta(vertice, daVez)
            if(aresta):
                retorno += [aresta.acao]
                daVez = vertice  
                break      
    return retorno

def breadthSearch(origem, grafo):
    visitado = []
    fila = []
    descobertas = {}
    vertices = []
    if (origem != None):
    	fila += [origem]
    	visitado += [origem]
    	descobertas = {0:[origem]}
    ciclo = 1
    while (fila) :
        vertices = []
        for termo in fila: 
            if(termo in grafo.keys()):
                for aresta in grafo[termo]:
                    if not vertices.__contains__(aresta.vertice2):
                        vertices += [aresta.vertice2]
        fila = fila[1:]
        if ([a.tipo for a in vertices].__contains__(-1)):
            for a in vertices:
                if(a.tipo == -1):
                    visitado += [a]
                    descobertas[ciclo] = [a]
                    return descobertas
        for vertice in vertices:
            if (not vertice in visitado):
                visitado += [vertice]
                if(ciclo in descobertas.keys()):   
                    descobertas[ciclo] += [vertice]
                else:
                    descobertas[ciclo] = [vertice]
                fila += [vertice]
        ciclo += 1
    return []