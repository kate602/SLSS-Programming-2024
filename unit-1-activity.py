# Unit 1 Activity
# Kate Jiang
# 3/04/2024

# only for 2024
month = int(input("What month is it? (MM)"))
day = int(input("What day is it today? (DD)"))
    
def monthToDay(month):
    if month == 1:
        return 0
    elif month == 2:
        return 31
    else:
        return 0
    
days = day + (monthToDay(month))

# When it's past March
if month > 3:
    print("Spring break is over")

# When it's March
elif month == 3:
     if day >= 15:
        print("It's spring break!!")
     else:
        print(f"There are {15 - days} days left until spring break!!!")

# When it's before March     
else: 
     print(f"There are {75 - days} days left until spring break!!!")
 
