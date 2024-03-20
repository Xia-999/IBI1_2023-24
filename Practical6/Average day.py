import matplotlib.pyplot as plt
AD={"sleeping":8,"classes":6,"studying":3.5,"TV":2,"music":1,"other":3.5}
print(AD)
activity_labels=AD.keys()
time=AD.values()

plt.figure()
plt.pie(time,labels=activity_labels,startangle=90)
plt.title("The average day of a nuiversity student")
plt.show()
plt.clf

activity="sleeping"  #one activity taken from the input	list
t=AD[activity]
print(t)