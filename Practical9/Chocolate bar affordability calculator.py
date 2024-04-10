def chocolate_bar_affordability(total_money,prize):  #define a function
    num=total_money//prize  #get the total number of chocolate bar user can afford
    change=total_money%prize  #get the change
    return str(num)+" "+str(change)

money=100
singleprize=7
number,change=chocolate_bar_affordability(money,singleprize).split()
print(number)
print(change)