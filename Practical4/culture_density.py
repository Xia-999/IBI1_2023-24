#Function: calculate the culture density
  #if culture density<=90%:
    #day=day+1
  #if culture density>90%:
    #done
       
d=1
x=5
while x<=90:
    x*=2
    d+=1
print("on day "+str(d)+" the cell density goes over 90%.git ")
print("I can have "+str(d-1)+" days for holiday.")
    