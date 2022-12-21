import matplotlib.pyplot as plt
import numpy as np
import random
from random import randint
from matplotlib.animation import FuncAnimation

Lenght = 8			# Size of lattice
p     = 0.9			# Probability 0 < p < 1
ConcentrationX = 0.0		# Density = Number of occupied cells / Total cells
ClustesSizeDistribution = 0.0 	# n_s(p) = average number of cluster of size *s* / Total cells
fig, Lattice = plt.subplots()

Lattice.grid(which = 'major', linestyle = '-', color = 'k', linewidth = 2)
Lattice.set_xticks(np.arange(0,Lenght,0.5)) 
Lattice.set_yticks(np.arange(0,Lenght,0.5)) 

XYPos  = np.zeros((Lenght,Lenght))						# Is necessary initialize the lattice only with zeros

def animate1(i):								# This walk one by one, just give it only one oportunity
    if (i == 0):								# Show the lattice just with zeros
        Lattice.imshow(XYPos)
    else:
        for j in range(Lenght):
            RandomNumber = random.random()
            if (RandomNumber < p):						# The condition to aplicate the percolation probability
                XYPos[i-1,j] = 1						# Show the lattice with the random numbers
                Lattice.imshow(XYPos)

def animate2(i):								# This not pass one by one, It choose random the cell and realice the conditional
    if (i == 0):								# Show the lattice just with zeros
        Lattice.imshow(XYPos)
    else:
        RandomNumber = random.random()
        if (RandomNumber < p):							# The condition to aplicate the percolation probability
            XYPos[randint(0,Lenght-1),randint(0,Lenght-1)] = 1			# Show the lattice with the random numbers
            Lattice.imshow(XYPos)
            print(i)
            
def Static():									# This walk one by one, just give it only one oportunity
    Lattice.imshow(XYPos)
    for i in range(Lenght):
        for j in range(Lenght):
            RandomNumber = random.random()
            if (RandomNumber < p):						# The condition to aplicate the percolation probability
                XYPos[i,j] = 1							# Show the lattice with the random numbers
                Lattice.imshow(XYPos)
    plt.title("Probabilidad :" + str(p))
    plt.show()

def Static2(Steps):								# This not pass one by one, It choose a random cell and realice the conditional
    Lattice.imshow(XYPos)
    NOpen = 0
    for i in range(0,Steps):
        RandomNumber = random.random()
        if (RandomNumber < p):
            i = randint(0,Lenght-1)
            j = randint(0,Lenght-1)
            if (XYPos[i,j] == 1):
                continue
            else:
                NOpen+= 1
                XYPos[i,j] = 1
                Lattice.imshow(XYPos)
    global ConcentrationX
    ConcentrationX = NOpen / pow(Lenght,2)
    plt.title("Probabilidad :" + str(p) +"\nDensidad :" + str(ConcentrationX))
    plt.show()
                
                
def dfs(grid,i,j,OldSpace,FillSpace):						# Oldspace is the yellow cell and Fillspace this one put with another color
    n = len(grid)								
    m = len(grid[0])
    if i < 0 or i >= n or j < 0 or j >= m or grid[i,j] != OldSpace:		
        return
    else:
        grid[i,j] = FillSpace
        dfs(grid,i+1,j,OldSpace,FillSpace)
        dfs(grid,i-1,j,OldSpace,FillSpace)
        dfs(grid,i,j+1,OldSpace,FillSpace)
        dfs(grid,i,j-1,OldSpace,FillSpace)
    return grid

def FloodFill(grid,OldSpace,FillSpace):
    for i in range(0,len(grid)):
        for j in range(0,len(grid[0])):
            if grid[i,j] != 1:
                continue
            else:
                dfs(grid,i,j,OldSpace,FillSpace)
    
def Animate(FuncionAnimate12, Frames = Lenght):
    ani = FuncAnimation(fig,FuncionAnimate12,frames=Frames+1,interval=1,repeat=False)
    plt.title("Probabilidad :" + str(p))
    plt.show()

Static2(20)
print(XYPos)
print("---------------------------")
FloodFill(XYPos,1,0.5)
print(XYPos)




# Links
#################################################################################
# 1) Stack Data Structure: https://www.geeksforgeeks.org/stack-data-structure/  #
# 2) Queue Data Structure: https://www.geeksforgeeks.org/queue-data-structure/  #
# 3) BFS and DFS: https://www.geeksforgeeks.org/difference-between-bfs-and-dfs/ #
#################################################################################
