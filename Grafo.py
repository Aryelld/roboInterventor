import numpy as np
# classe Vertice
class V:
    # vertice "" esta vazio
    def __init__(self, tipo):
        self.visitado = tipo == "" or tipo == "1"
        self.tipo = tipo
    def toString(self):
        return self.tipo
# classe Aresta
class A:
    def __init__(self, vertice1, vertice2):
        self.vertice1 = vertice1
        self.vertice2 = vertice2
    def toString(self):
        return self.vertice1.toString() + "->" + self.vertice2.toString()
# classe Grafo
class G:
    def __init__(self,mapa):
        a = self.mpV(mapa)
        self.mapaVertice = a
        self.grafo = {}
        i = 0
        for linha in a:
            j = 0
            for pos in linha:
                self.grafo[pos] = [A(pos, adjacente) for adjacente in filter(lambda x : x.tipo != "",self.vizinhos(i,j))]
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
    def vizinhos(self,i,j):
        jMax = np.array(self.mapaVertice[0]).size 
        iMax = np.array(self.mapaVertice).size/jMax
        retorno = []
        if(i>0):
            retorno.append(self.mapaVertice[i-1][j])
        else:
            retorno.append(V(""))
        if(j>0):
            retorno.append(self.mapaVertice[i][j-1])
        else:
            retorno.append(V(""))
        if(j<jMax-1):
            retorno.append(self.mapaVertice[i][j+1])
        else:
            retorno.append(V(""))
        if(i<iMax-1):
            retorno.append(self.mapaVertice[i+1][j])
        else:
            retorno.append(V(""))
        # vizinho antes em i,j vizinho depois i,j
        return retorno
    def toString(self):
        for linha in self.mapaVertice:
            for vertice in linha:
                lista = []
                for aresta in self.grafo[vertice]:
                    lista.append(aresta.toString())
                print("{"+vertice.toString()+":"+lista.__str__()+"}")
    # def custo(self, i,j):