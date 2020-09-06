# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 16:55:21 2020

@author: 91852
"""

#Conditions

#if

a=8

if (a<10):
    print("a is less than 10")

if (a>10):
    print("a is less than 10")

a=9
b=10

if (a<b):
    print("a is lesser than b")
    
#double equal to is used for similarity
#single equal to changes the value
a==b
a<b
a>b
a<=b
a>=b
a!=b

x=2
if (x==1):
    print("Right")
    
# if - else conditions  
if(x==1):
    print("Right")
else:
    print("Wrong")
    
x=10
y=20
if(x>y):
    print("X is greater")
else:
    print("Y is Greater")
    


#Multiple conditions
Marks = 50

if(Marks>80):
    print("A")
elif(Marks>70 and Marks<=80):
    print("B")
elif(Marks>60 and Marks<=70):
    print("C")
else:
    print("Fail")
    
    
Marks = 75

if(Marks>80):
    print("A")
elif(Marks>70 and Marks<=80):
    print("B")
elif(Marks>60 and Marks<=70):
    print("C")
else:
    print("Fail")
    
Marks = 85

if(Marks>80):
    print("A")
elif(Marks>70 and Marks<=80):
    print("B")
elif(Marks>60 and Marks<=70):
    print("C")
else:
    print("Fail")
    
#bullion conditions 
a=10
b=20    
c=30
a>b and c>b

a=10
b=20    
c=30
a<b and c>b

x=3
y=4
z=2
if ((x<y)or(y>z)) and (x>10):
    print("both conditions are true")
else:
    print("both conditions are not true")


#loops or iteration concepts
teamA = ["India", "Australia", "Pakistan", "England"]

teamA

teamA[0]
teamA[1]
teamA[2]
teamA[3]

#this is "for" looping
for var in teamA :
    print(var)

lenteamA= len(teamA)
lenteamA

#LT= range(LenteamA)
#LT

r1= range(10)
for i in r1:
    print(i)

r1 = range(1,11)
for i in r1:
    print(2*i)
    
lenteamA = len(teamA)
lenteamA
teamA
for i in range(lenteamA):
    print(teamA[i])
    
lenteamA = len(teamA)
lenteamA
teamA
teamB=[]
for i in range(lenteamA):
    teamB.append(teamA[i])
teamB


lenteamA = len(teamA)
lenteamA
teamA
teamB=[]

for i in range(lenteamA):
    teamB.append(teamA[i])
    teamA[i]=str(teamA[i])+ "_A"
teamA


for i in teamA:
    if i == "India" :
        print("India is in Team A", "\t", i)
    else:
        print("India is not in Team A")
        
        
for i in teamA:
    if i == "India" :
        print("India is in Team A", "\t", i)
        break
    else:
        print("India is not in Team A")
        
        
a=range(2,6)
La= list(a)
La
for x in range(2,6):
    print("x=", x, end = " ")
    
for x in range(2,6):
    print("x=", x)
    
for x in range(2,6):
    print("x=", x, end = "*****")
      
#while loop  
print("i=",1)
print("i=",2)
print("i=",3)
print("i=",4)
print("i=",5)
print("i=",6)
print("i=",7)
print("i=",8)
print("i=",9)

i = 1

while (i< 10):
    print("i=",i)
    i = i + 1    
    

#break the loop in between
i = 1
while (i < 10):
    
    if i == 5 : #end here
        print("exiting the loop at this point")
        break
    print(i, end = "\t")
    i = i + 1

#use of continue - continue with loop
i = 0 
while (i < 10):
    i+= 1
    if i == 5 : #continue with loop
        continue
    print(i, end = "\t")

i = 0 
while (i < 10):
    i+= 1
    if i == 5 : #continue with loop
        continue
    print(i)




