#import metplotlib
import matplotlib.pyplot as plt
AD={"sleeping":8,"classes":6,"studying":3.5,"TV":2,"music":1,"other":3.5}  #create a dictionary of students' sactivities and their average spending time
print(AD)
activity_labels=AD.keys()  #get the keys of dictionary
time=AD.values()  #get the values of dictionary

plt.figure()  #draw a gragh 
plt.pie(time,labels=activity_labels,startangle=90)
plt.title("The average day of a nuiversity student")  #give the gragh a title
plt.show()  #show the gragh
plt.clf

activity="sleeping"  #one activity taken from the input	list'
t=AD[activity]
print(t)