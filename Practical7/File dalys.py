import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
os.getcwd()
os.chdir("c:\\Users\\lenovo\\IBI1\\IBI1_2023-24\\IBI1_2023-24\\Practical7")
os.getcwd()
os.listdir()
dalys_data=pd.read_csv("dalys-rate-from-all-causes.csv")

print(dalys_data.iloc[0:100:10,3])   #show the fourth column (the DALYs) from every 10th row, starting from the first row, for the first 100 rows (inclusive)
print(dalys_data.loc[dalys_data["Entity"]=="Afghanistan"])  #show all rows corresponding to Afghanistan.
china_data=dalys_data.loc[dalys_data["Entity"]=="China",["Entity","Code","Year","DALYs"]]  #get data of china
china_mean=np.mean(china_data.iloc[:,3])   #get the mean of DALYs in china
china_2019=list(china_data.loc[china_data["Year"]==2019,"DALYs"])[0]   #get the DALYs in 2019 in china
print(china_mean)
if china_mean >china_2019:    # compare the mean with DALYS in 2019
    print("The DALYs in China in 2019 is smaller than the mean")
else:
    print("The DALYs in China in 2019 is larger than the mean")

plt.figure(1)  #draw a graph
plt.plot(china_data.Year, china_data.DALYs, 'r+')
plt.title("China DALYs")  # give it a title
plt.xticks(china_data.Year,rotation=-90) #give it xticks
plt.clf

#other question
data_2019=dalys_data.loc[dalys_data["Year"]==2019,"DALYs"]  #get the data in 2019
data_1990=dalys_data.loc[dalys_data["Year"]==1990,"DALYs"]   #get the data in 1990
data=[]
data.append(data_1990)
data.append(data_2019)
plt.figure(2)
plt.boxplot(data,patch_artist=True,zorder=0,positions=(1,1.4),labels=["1990","2019"])  #draw a boxpot of data in 1990 and 2019
plt.show()
plt.clf



