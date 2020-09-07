# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 18:51:51 2020

@author: 91852
"""









a=10
b=20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)

a=20
b=30
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)

a=50
b=60
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)

a=70
b=40
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)


#user defined functions
def oper(a,b):
    print("Sum",a+b)
    print("Sub",a-b)
    print("Mul",a*b)
    print("Div",a/b)
    print("Pow",a**b)
    
oper(10,20)
oper(20,30)
oper(50,60)
oper(40,70)

i = 0
j = 10
while(i<10):
    oper(i,j)
    i = i+1
    j = j+1
    
i = 0
j = 10
while(i<10):
    print("Oper Call")
    oper(i,j)
    i = i+1
    j = j+1
    
def oper(a,b):
    Sum= a+b
    Sub= a-b
    return(Sum, Sub)


#individual elements are integers 
oper(10,20)
     
     
#when fetching it is tuple
c= oper(10,20)
c
type(c)

def printhello(fname):
    print("Hello", fname,"      welcome")

printhello("Aman")
printhello("Sushant")

#inputs are needed because no default input has been provided
def totalsale(x, y):
    return(x+y)

totalsale()

#no inputs put so default inputs used
def totalsale(x=0, y=0):
    return(x+y)

totalsale()
totalsale(10,20)


def totalsale(x=0, y=0):
    c=x+y
    return(c)


#random numbers
import random

#random integers every single time you run it till the time you store that
random.randint(1,10)

x = random.randint(100, 1000)
x

#choose an element from the list on random basis 
list = [11,12,13,14,15,16]
random.choice (list)

#4 groups of 5 random numbers 

list1 = []
list2 = []
list3 = []
list4 = []

i=0
while(i<4):
    list1.append(random.randint(100,1000))
    list2.append(random.randint(100,1000))
    list3.append(random.randint(100,1000))
    list4.append(random.randint(100,1000))
    i = i+1
list1
list2
list3
list4

#Use of choice command with string
import random
st = "abcdef"
st
random.choice(st)

names=["vikas", "Aman", "Simar", "Sirat"]
random.choice(names)

#random.choices returns you "n" no of random items
random.choices (names, k=3)
random.choices(list1, k=3)

#creating a random sample 
import random
sample = random.choices (names, k=2)

sample

#working these random codes on dictionary

d1 = {"Name": "vikas", "RollNo": 111, "Class" : "ML"}
type(d1)
random.choices(d1)

#it does not work on dict or set and has to converted to list or tuple
c = random.choices(list(d1), k=3)
c

d1 = {"Name": "vikas", "RollNo": 111, "Class" : "ML"}
type(d1)
s1 ={20,30,40,50}
c= random.choices(list(d1), k=3)
c
c= random.choices(tuple(s1), k=3)
c

#this word random can be replaced with other name
import random as rd
rd.choices(list(s1), k=3)


#randrange usuage
movie_list = ["The Godfather", "The Wizard of Oz", "Citizen Kane", "The shawkerliners", " Fast and Furious"]

random_ndex = rd.randrange(9)
random_ndex

Random_index = rd.randrange(len(movie_list))
Random_index 

item = movie_list[Random_index]
print("Randomly selected item and its index is - ", item, "Index - ", Random_index)

import random as rd
s1={1,2,3,4}
l1=list(s1)
l1[2]

t=(1,2,3,4)
t=[1]

#seed function- used to state of the random number, the same data can be called randomly again and again 
#don't want to change samples frequently

import random
for i in range(5):
    #any number can be used in the place of "0"
    random.seed(0)
    #generated random number will be between 1 to 1000
    print(random.randint(1, 1000))

random.seed(100)
random.randint(1, 1000)


#highly required and important library in Python, it can hold any array related object
import numpy
