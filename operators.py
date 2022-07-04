#operators
#relational operator
# comparision property
'''
<-lessthan
>-greaterthan
<=lessthan equal
>=greatherthan equal
==-Assignment operator '''
from sqlalchemy import true


sasi=450
mohan=950
razzak=220

print('lesstan:',sasi<mohan)
print("greaterthan:",mohan>razzak)
print("greather than equal:",sasi>=mohan)
print("less than equal:",sasi<=mohan)
print("assignment:",sasi==mohan)

#datatypes
hari=6565454
mani=5000.00
basha='im new lerner001324#$%#'
hello=true
#print("int:",hari,"float",mani,"str:",basha,"boolean",hello)
print(type(hari),type(mani),type(basha),type(hello))

#string
alphabets="abcdefghijklnmopqrstuvwxyz"
print(alphabets)
print(alphabets[0])
print(alphabets[3])
print(alphabets[0:10])
print(alphabets.upper())
print(alphabets.lower())
print(alphabets[-1])
print(alphabets[0:20:3])
print(alphabets[0:20:-1])


sasi="my name is sasi"
print(sasi.title())

gully_boy=int(input("enter the gullyboy value:"))
print(gully_boy)
gully=float(input("enter the gully value:"))
print(gully)
mani=input("enter the gullyboy value:")
print(mani)

cent=float(input("enter the cent value:"))
acre=cent/100
print("cent value is",cent,"acre value is:",acre)


deposit=int(input("enter the amount:"))
intrest=6.8
profit=(deposit*intrest)/100
maturity=deposit+profit
print("meturity is ",maturity)
print("intrest yearly wise",profit)
print("yearly twise",maturity/2)
print("yearly month ",maturity/12)


