# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 13:47:39 2020

@author: 91852
"""

#List
#Mutable 

L1 = [1,2,3,4,5]
L1
type(L1)

#indexed
L1
L1[0]
L1[1]
L1[0:4]

L1[6]

L1[4]

L1[1:4]

L1[:4]

L1[2:]

#Hetrog
L2=[1,"Kirat", 2.3, False, 2.66]
L2

L2[3]
L2[3:5]


#loop (assign variable one by one)
for i in L2:
    print(i)
    print(i)
    
    
#Mutable 
L2[2]=5.50
L2


L2[1].upper()

L2.count("Kirat")

len(L2)

L2.append("Khullar")
L2

L2.remove("Kirat")
L2

L2.remove("Khullar")
L2

L2.pop()
L2

L2.pop(1)
L2


L2=[1,"Kirat", 2.3, False, 2.66]

del L2[0]
L2

PopValue=L2.pop(1)
PopValue

L1.clear()
L1

#copy
L2=[1,"Kirat", 2.3, False, 2.66]
L2

L1 = L2

L1
L2

L1.pop()
L1
L2


L1 = L2.copy()
L1
L2

L1.pop()
L1
L2


Start = 0
End = 10
Jump = 1

range(End)

Start = 5
End = 100
Jump = 1

range(Start, End)

Start = 5
End = 100
Jump = 2

range(Start, End, Jump)

a=range(End)
a

list(a)

b=range(Start, End)
b
list(b)

c=range(Start, End, Jump)
c
list(c)

L3=[3,5,2,4,1]

L3.sort()
L3

L4=["Vikas","Aman", "Shubham"]
L4.sort()
L4

L4=["Vikas","Aman", "Shubham", str(1), str(5)]
L4.sort()
L4

L5=L3+L4
L5

L3.pop()
L5


#Set DataType 
set = {1, 2, 3, 4, 5}
type(set)
set


#union command combines to sets 
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

s1.union(s2)

#lsit allows assignment but not set
s1[0] = 1

s1.add(6)
s1

#will not add an item which is already there
s1.add(4)
s1

#set can hold hetrog items 
s1.add("Khullar")
s1

s1.update(["Khullar", 8])
s1

s1.add("Khullar")
s1


#set will not update items already there
s1.update(['Khullar', 9])
s1

#when we have set values with string type data it shows it in dictionary format
s1.update([4,5,9,10])
s1


#Ordered
s3 = {3,2,5,1,3}
s3

L3 = [3,2,5,1,3]
L3


#Round brackets with square brackets means 1 entry but without square brackets it means ech single letter is a different item
s1
s1.update(["kumar"])
s1

s1
s1.update("kumar")
s1

s4 = ["vikas", "vinay"]
s4


#remove commands
s1 = {1,2,3,4,5}
s1
s1.remove(5)
s1

s1 = {1,2,3,4,5,"vikas", "khullar"}
s1.remove("vikas")
s1

#difference between remove and discard, discard does not show any error if value does not exist, but remove command will raise an error
s1.remove(21)

s1.discard(21)

#pop operation removes the first item 
s1.pop()
s1

s1.pop()
s1

#del command deletes the set from entire sheet
del s1
s1


#intersection command gives only similar items in both sets
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

s1.intersection(s2)


#differnce command gives the items that are in first set but not in set 2
s1.difference(s2)

#Dict (dictionary command)(curly brackets used)

st = {'rollno': 1}
st
type(st)

st =  {'rollno': 1, 'Name': "Vikas", "Educ": "PhD"}
st

st =  {'rollno': 1, 'Name': "Vikas", "Name" : "Vinay", "Educ": "PhD"}
st

#can have hetrog items
car ={"brand":"Honda", "model": "Jazz", "year": 2020, "Purchased": True}
car

car["brand"]

car["year"]

car.get("brand")

#for loop can be used to fetch the keys
for i in car:
    print(i)
    
#for loop can also be used to fetch the values as under:
for i in car.values():
    print(i)
    
car.values()
len(car)


#to check the values in the dictionary 
car ={"brand":"Honda", "model": "Jazz", "year": 2020, "Purchased": True}

"Jazz" in car.values()
2020 in car.values()

"brand" in car

#dictionary is also mutable(you can change elements) 
car["year"] =2019
car


#use of pop on list, set and dict
pop_ele = car.pop("brand")
pop_ele

L1=[1,2,3]
L1.pop()
L1.pop(0)

S1={1,2,3}
S1.pop()
S1.pop(1)

car ={"brand":"Honda", "model": "Jazz", "year": 2020, "Purchased": True}
pop_ele = car.pop("year")
pop_ele


#fetching the items in different manners
car.keys()
car.values()
car.items()

for i in car.items():
    print(i)
    
for i,j in car.items():
    print("Key",i)
    print("Values",j)

#adding values in dictionary

car["Colour"] = "Black"
car    


#Tupple (tupple is not mutable)
t1 = (1,2,3,4)    

t1[0]
t1[0]=8

for i in t1:
    print(i)
    

#checking values in tupple
t1=("Vikas","Aman", "Harman")

"Aman" in t1

#use of if condition in tupple
if ("Aman" in t1):
    print("hi")

L1=list(t1)
type(t1)
type(L1)

#delete function with tupple
t1.remove()
del t1(1)
del t1
#no add, update, remove fucntion available in tupple

#Pending string Function
s1 = "Kirat Chhabra"
s1.replace("Chhabra", "Singh")

s2= "Kirat Chhabra"
s2.split(" ")

s3=s2.split(" ")
s3[0]

Fname=s3[0]
Lname=s3[1]

Fname
Lname


#Enumerate

L1 = ["Oranges", "Mangoes","Apples"]

obj1 = enumerate(L1)

obj1

list1=list(obj1)
list1

obj1 = enumerate(L1, start=100)

obj1

list1=list(obj1)
list1

print("Return type:", type(obj1))

print(list(enumerate(L1)))


#you need to initialize it again before changing its type 
obj1 = enumerate(L1, start=100)
list1= set(obj1)
list1

obj1 = enumerate(L1, start=100)
list1= dict(obj1)
list1

#you need to initialize it again because previous enumeration is exhausted already before fetching the items
obj1 = enumerate(L1, start=100)
for i,j in obj1:
    print(i,j)

print(i)

L1=list(range(100,200))
L1

obj1=enumerate(L1)
obj1

for i,j in obj1:
    print(i,j)
    if(i==50):
        break
    
#Frozenset"(this type of set is not mutable)
fs =frozenset([1,2,3])
fs
type(fs)

fs.add(2)

b= frozenset([3,4,5])
fs.add(b)

#operations can be applied but can't change the set 
fs.union(b)
fs.intersection(b)
fs.difference(b)

#zip

name = ["vikas", "Aman", "Ankit"]
roll_no = [1,2,3]
marks = [75,85,73]

z1 = zip(name, roll_no, marks)
z1

type(z1)

s1 = set(z1)
s1

z1 = zip(name, roll_no, marks)
l1= list(z1)
l1

z1 = zip(name, roll_no, marks)
for i,j,k in z1:
    print(i,j,k)