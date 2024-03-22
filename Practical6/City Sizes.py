import matplotlib.pyplot as plt  #import matplotlib
uk_cities=[0.56,0.62,0.04,9.7]   
china_cities=[0.58,8.4,29.9,22.2]
uk_cities.sort()  #sort the data in uk_cities in ascending sort order
china_cities.sort()  #sort the data in china_cities in ascending sort order
print(uk_cities)
print(china_cities)
uk_city=["Stirling","Edinburgh","Glasgow","London"]
china_city=["Haining","Hangzhou","Beijing","Shanghai"]

plt.figure(1)
plt.bar(uk_city,uk_cities,color=["green","purple"]) #draw a gragh of uk cites'sizes
plt.ylabel("city size")  #give gragh a y label
plt.title("uk cities") #give gragh a title
for a,b in zip(uk_city,uk_cities):  #label the data on the top of bars
    plt.text(a,b,b)
plt.clf

plt.figure(2)
plt.bar(china_city,china_cities,color=["grey","pink"]) #draw a gragh of china cites'sizes
plt.ylabel("city size")  #give gragh a y label
plt.title("china cities")  #give gragh a title
for a,b in zip(china_city,china_cities):  #label the data on the top of bars
    plt.text(a,b,b)
plt.show()  # show the graghs
plt.clf