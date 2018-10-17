import numpy as np
# classe Vertice
class V:
    # pode ser adicionado feromonio 
    # quando se implementar o ACO
    def __init__(self, tipo):
        # onde R representa a localização do robo interventor
        self.visitado = tipo == "1"
        self.tipo = tipo
    def visitar(self):
        self.visitado = True
    def toString(self):
        return self.tipo
# classe Aresta
class A:
    def __init__(self, vertice1, vertice2, acao):
        self.vertice1 = vertice1
        self.vertice2 = vertice2
        self.acao = acao
    def toString(self):
        return self.vertice1.toString() + "->" + self.vertice2.toString()
# classe Grafo
class G:
    def __init__(self,mapa):
        self.mapaVertice = self.mpV(mapa)
        jMax = np.array(self.mapaVertice[0]).size 
        iMax = np.array(self.mapaVertice).size/jMax
        self.grafo = {}
        i = 0 
        for linha in self.mapaVertice:
            j = 0 
            for pos in linha:
                if(pos.tipo == '4'):
                    self.grafo[pos] = []
                    if(i>0):
                        aux = self.mapaVertice[i-1][j]
                        if(aux.tipo == '4' or aux.tipo == '-1'):
                            self.grafo[pos] += [A(pos, aux, 'acima')] 
                    if(j>0):
                        aux = self.mapaVertice[i][j-1]
                        if(aux.tipo == '4' or aux.tipo == '-1'):
                            self.grafo[pos] += [A(pos, aux, 'atras')]
                    if(i<iMax-1):
                        aux = self.mapaVertice[i+1][j]
                        if(aux.tipo == '4' or aux.tipo == '-1'):
                            self.grafo[pos] += [A(pos, aux, 'abaixo')]
                    if(j<jMax-1):
                        aux = self.mapaVertice[i][j+1]
                        if(aux.tipo == '4' or aux.tipo == '-1'):
                            self.grafo[pos] += [A(pos, aux, 'afrente')]
                j+=1
            i+=1     
    def mpV(self,mapa):
        retorno = []
        for line in mapa:
            linha = []
            for termo in line:
                linha.append(V(termo))
            retorno.append(linha)
        return retorno
    def toString(self):
        for vertice in self.grafo.keys():
            lista = []
            for aresta in self.grafo[vertice]:
                lista.append(aresta.toString())
            print("{"+vertice.toString()+":"+lista.__str__()+"}")
        