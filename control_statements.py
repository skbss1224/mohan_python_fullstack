#control statement
'''tamil=int(input("enter the tamil mark:"))
english=int(input("enter the english mark:"))
maths=int(input("enter the maths mark:"))
science=int(input("enter the science mark:"))
social=int(input("enter the social mark:"))
if(tamil<=english):
    print("english mark is big value")
elif(english<=maths):
    print("maths mark is big value")
elif(maths<=science):
    print("science mark is big value")
elif(science<=social):
    print("english mark is big value")
else:
    print("none of these")'''
    
    
#voter id apply
'''
nationality=input("enter the nationality:")
age=int(input("enter the age:"))
if(nationality=="indian"):
    print("you are selected indian")
    if(age>=18):
        print("you are apply for voter id")
    else:
        print("you are not elligible for voter id")
else:
    print("you are a not a indian")'''
    
#bus ticket reservation:


place=input("enter the place:")
if(place=="chennai"):
    print("you are selected ",place)
    bustype=input("enter the bus type:")
    if(bustype=="ordinary"):
        print("you are selected",bustype)
        amount=int(input("enter the amount:"))
        if(amount>=250):
            bal=amount-250
            print("your ticket reserved",place)
            print("your balance amount is",bal)
        else:
            print("insuffiecient amount")
    elif(bustype=="delux"):
        print("you are selected",bustype)
        amount=int(input("enter the amount:"))
        if(amount>=350):
            bal=amount-350
            print("your ticket reserved",place)
            print("your balance amount is",bal)
        else:
            print("insuffiecient amount")
    elif(bustype=="superdelux"):
        print("you are selected",bustype)
        amount=int(input("enter the amount:"))
        if(amount>=450):
            bal=amount-450
            print("your ticket reserved",place)
            print("your balance amount is",bal)
        else:
            print("insuffiecient amount")
    elif(bustype=="sleeper"):
        print("you are selected",bustype)
        amount=int(input("enter the amount:"))
        if(amount>=550):
            bal=amount-550
            print("your ticket reserved",place)
            print("your balance amount is",bal)
        else:
            print("insuffiecient amount")
    else:
        print("A/C bus not available")
elif(place=="madhurai"):
    print("you are selected ",place)
    bustype=input("enter the bus type:")
    if(bustype=="ordinary"):
        print("you are selected",bustype)
        amount=int(input("enter the amount:"))
        if(amount>=350):
            bal=amount-350
            print("your ticket reserved",place)
            print("your balance amount is",bal)
        else:
            print("insuffiecient amount")
    elif(bustype=="delux"):
        print("you are selected",bustype)
        amount=int(input("enter the amount:"))
        if(amount>=450):
            bal=amount-450
            print("your ticket reserved",place)
            print("your balance amount is",bal)
        else:
            print("insuffiecient amount")
    elif(bustype=="superdelux"):
        print("you are selected",bustype)
        amount=int(input("enter the amount:"))
        if(amount>=550):
            bal=amount-550
            print("your ticket reserved",place)
            print("your balance amount is",bal)
        else:
            print("insuffiecient amount")
    elif(bustype=="sleeper"):
        print("you are selected",bustype)
        amount=int(input("enter the amount:"))
        if(amount>=650):
            bal=amount-650
            print("your ticket reserved",place)
            print("your balance amount is",bal)
        else:
            print("insuffiecient amount")
    else:
        print("A/C bus not available")
else:
    print("only two place i will provide chennai and madhurai")

