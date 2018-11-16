
import numpy as np
import matplotlib.pyplot as plt

class Mapa:
    # paredes devem estar do formato:
    # {
    #   'x':[
    #           (yPosition,xInit,xFin),
    #           (yPosition,xInit,xFin) 
    #       ],
    #   'y':[
    #           (xPosition,yInit,yFin),
    #           (xPosition,yInit,yFin) 
    #       ]
    # }
    # não é necessário colocar as paredes ao redor do mapa,
    # são adicionadas automaticamente
    # areas inacessiveis ficam do seguinte formato:
    # [
    #    (xInit, xFin, yInit, yFin) 
    # ]
    def __init__(self, paredes = [], areasInacessiveis = [], conhecido = 1 , xSize = 50, ySize = 50):
        self.xSize = xSize
        self.ySize = ySize
        self.mapa = [[4 if a != 0 and b != 0 and a != xSize-1 and b != ySize-1 else 1 for a in range(xSize)] for b in range(ySize)]
        for paredeHorizontal in paredes['x']:
            yPosition,xInit,xFin = paredeHorizontal
            for x in range(xSize):
                if(x>= xInit and x<= xFin):
                    self.mapa[yPosition][x] = 1
        for paredeVertical in paredes['y']:
            xPosition,yInit,yFin = paredeVertical
            for y in range(ySize):
                if(y>= yInit and y<= yFin):
                    self.mapa[y][xPosition] = 1
        for areaInacessivel in areasInacessiveis:
            xInit, xFin, yInit, yFin = areaInacessivel
            for x in range(xSize):
                for y in range(ySize):
                    if(x>= xInit and x<= xFin and y>= yInit and y<= yFin):
                        self.mapa[y][x] = -1
        self.mapa = [[self.mapa[y][x] if (x**2+y**2)**0.5 < ((xSize**2+ySize**2)**0.5)*conhecido else 0 for x in range(xSize)]for y in range(ySize)]
        # percorrido = 0
        # for y in range(ySize):
        #     for x in range(xSize):
        #         if(percorrido/2500 > conhecido):
        #             self.mapa[y][x] = 0
        #         percorrido += 1
    # funcao para extrapolar as áreas inacessíveis para sobre a parede
    def extInacessiveis(self, mapa):
        iControl = 0
        jControl = 0
        mapaRetorno = [[0 for x in range(self.xSize)] for y in range(self.ySize)]
        for i in range(self.ySize):
            for j in range(self.xSize):
                if(mapa[i][j] == -1 and i != 0 and j != 0 and i != self.ySize-1 and j != self.xSize-1):
                    mapaRetorno[i][j] = mapa[i][j]
                    mapaRetorno[i-1][j] = -1 if mapa[i-1][j] == 1 and i-1 != 0 else mapa[i-1][j] 
                    mapaRetorno[i][j-1] = -1 if mapa[i][j-1] == 1 and j-1 != 0 else mapa[i][j-1] 
                    mapaRetorno[i][j+1] = -1 if mapa[i][j+1] == 1 and j+1 != self.xSize-1 else mapa[i][j+1]
                    mapaRetorno[i+1][j] = -1 if mapa[i+1][j] == 1 and i+1 != self.ySize-1 else mapa[i][j+1] 
                    mapaRetorno[i-1][j-1] = -1 if mapa[i-1][j-1] == 1 and i-1 != 0  and j-1 != 0 else mapa[i-1][j-1]
                    mapaRetorno[i+1][j+1] = -1 if mapa[i+1][j+1] == 1 and j+1 != self.xSize-1 and i+1 != self.ySize-1 else mapa[i+1][j+1] 
                    mapaRetorno[i+1][j-1] = -1 if mapa[i+1][j-1] == 1 and i+1 != self.ySize-1 and j-1 != 0 else mapa[i+1][j-1] 
                    mapaRetorno[i-1][j+1] = -1 if mapa[i-1][j+1] == 1 and j+1 != self.xSize-1 and i-1 != 0 else mapa[i-1][j+1] 
                else:
                    mapaRetorno[i][j] = mapa[i][j] if mapaRetorno[i][j] == 0 else mapaRetorno[i][j]
        return mapaRetorno

    # gerando imagem do mapa
    def plotMap(self):
        data = np.array(self.extInacessiveis(self.mapa),dtype=np.uint8)+1
        plt.imshow(np.asarray(data))
        plt.show()