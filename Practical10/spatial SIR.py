import numpy as np
import matplotlib.pyplot as plt

population=np.zeros((100,100))
outbreak=np.random.choice(range(100),2)
population[outbreak[0],outbreak[1]]=1   #choose one people to get infected

N=10000
beta=0.3
gamma=0.05

def plot(population):
    plt.figure(figsize=(6,4),dpi=150)
    plt.imshow(population,cmap="viridis",interpolation="nearest")
    plt.show()

for i in range(100):
    plot(population)
    infected=np.where(population==1)
    for j in range(len(infected[0])):
        x=infected[0][j]
        y=infected[1][j]
        for xneighbor in range(x-1,x+2):
            for yneighbor in range(y-1,y+2):
                if (xneighbor,yneighbor)!=(x,y):
                    if xneighbor!=-1 and yneighbor!=-1 and xneighbor!=100 and yneighbor!=100:
                        if population[xneighbor,yneighbor]==0:
                            population[xneighbor,yneighbor]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
    for z in range(len(infected[0])):
        x=infected[0][z]
        y=infected[1][z]
        population[x,y]=np.random.choice([1,2],1,p=[1-gamma,gamma])[0]

