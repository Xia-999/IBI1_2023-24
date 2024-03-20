import matplotlib.pyplot as plt
uk_cities=[0.56,0.62,0.04,9.7]
china_cities=[0.58,8.4,29.9,22.2]
uk_cities.sort()
china_cities.sort()
print(uk_cities)
print(china_cities)
uk_city=["Stirling","Edinburgh","Glasgow","London"]
china_city=["Haining","Hangzhou","Beijing","Shanghai"]

plt.figure(1)
plt.bar(uk_city,uk_cities,color=["green","purple"])
plt.ylabel("city size")
plt.title("uk cities")
for a,b in zip(uk_city,uk_cities):
    plt.text(a,b,b)
plt.clf

plt.figure(2)
plt.bar(china_city,china_cities,color=["grey","pink"])
plt.ylabel("city size")
plt.title("china cities")
for a,b in zip(china_city,china_cities):
    plt.text(a,b,b)
plt.show()
plt.clf