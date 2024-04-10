def find_favorite_Bond(year):   #define a function
    actor={"Roger Moore":"1973-1986","Timothy Dalton":"1987-1994","Pierce Brosnon":"1995-2005","Daniel Craig":"2006-2021"}  #create a dictionary to contain acotrs' information
    year=year+18
    for i in actor.keys():   #search the right actor
        if year>=int(actor[i][0:4]) and year<=int(actor[i][5:9]):  
            return i
        
year=1990   #an example
favorite_actor=find_favorite_Bond(year)
print(favorite_actor)