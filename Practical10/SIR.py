import numpy as np
import matplotlib.pyplot as plt

N=10000  
s=9999
i=1   
r=0
beta=0.3
gamma=0.05
j=0

suscepeptical_num=[s]
infected_num=[i]
recovered_num=[r]
days=[j]

plt.figure(figsize=(10,6))
while j<1001:
    days.append(j+1)
    suscepeptical_num.append(s)
    infected_num.append(i)
    recovered_num.append(r)
    
    prob=i/N
    probability=prob*beta
   
    infected1=np.random.choice(range(2),s,p=[1-probability,probability])
    recovered1=np.random.choice(range(2),i,p=[gamma,1-gamma])
    add_infected=np.sum(infected1==1)

    add_recovered=np.sum(recovered1==0)
    
    s-=add_infected
    i=i+add_infected-add_recovered
    r+=add_recovered
    j+=1
   

plt.plot(days,suscepeptical_num,label="Susceptible")
plt.plot(days,infected_num,label="Infected")
plt.plot(days,recovered_num,label="Recovered")
plt.xlabel("time")
plt.ylabel("population")
plt.title("SIR model")
plt.legend()
plt.show()
plt.clf

