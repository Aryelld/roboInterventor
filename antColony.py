import pants
import math
import random

mapa = [['R','0','0','0','0','0'],
        ['0','1','0','1','1','0'],
        ['0','0','0','0','1','-1']]
nodes = []
x,y = (0,0)
for line in mapa:
    for pos in line:
        nodes.append([x, y,pos])
        y += 1
    x += 1
    y = 0

def euclidean(a, b):
    return math.sqrt(pow(a[1] - b[1], 2) + pow(a[0] - b[0], 2))

world = pants.World(nodes, euclidean)

solver = pants.Solver()

solution = solver.solve(world)
# or
# solutions = solver.solutions(world)
print(solution.distance)
print(solution.tour)    # Nodes visited in order
print(solution.path)    # Edges taken in order
# or
# best = float("inf")
# for solution in solutions:
#   assert solution.distance < best
#   best = solution.distance