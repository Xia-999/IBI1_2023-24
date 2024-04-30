import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


beta=0.3
N=10000
gamma=0.05
d=0         

population=np.zeros((100,100))
outbreak=np.random.choice(range(100),2)
population[outbreak[0],outbreak[1]]=1
plt.figure(figsize=(6,4),dpi=150)
plt.imshow(population,cmap="viridis",interpolation="nearest")
plt.show()

while d<100:
    for i in range(100):
        for j in range(100):
            if population[i,j]==1:
                population[i,j]=np.random.choice([1,2],1,p=[1-gamma,gamma])[0]
  
    # find infected points
    infectedIndex = np.where(population==1)
# loop through all infected points
    for i in range(len(infectedIndex[0])):
        # get x, y coordinates for each point
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        # infect each neighbour with probability beta
        # infect all 8 neighbours (this is a bit finicky, is there a better way?):
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,y+2):
                # don't infect yourself! (Is this strictly necessary?)
                if (xNeighbour,yNeighbour) != (x,y):
                    # make sure I don't fall off an edge
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                        # only infect neighbours that are not already infected!
                        if population[xNeighbour,yNeighbour]==0:
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
    
    plt.clf()
    plt.figure(figsize=(6,4),dpi=150)
    plt.imshow(population,cmap="viridis",interpolation="nearest")
    plt.show()
    d+=1
