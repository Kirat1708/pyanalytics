# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 18:58:48 2020

@author: 91852
"""


import numpy as np 

arr=np.linspace(1, 12, num=4, dtype="int32")
arr

l1=[1,2,3,4]
type(l1)

np.array(l1)
a = np.array(l1)

type(a)

a1 = np.array ([1,2,3,4,5])
a1

a1 = np.arange(10)
a1

a1 = np.array([2,3,1,4,5])
a1.sort()

a1

#reverse order

np.sort(a1)[::-1]
l1 = [1,2,3,4,5]

lR = l1[1::-1]
lR

np.sort(a1)

arr3 = np.random.randint(1,10, size=10)
arr3.sort()
arr3=arr3[::-1]
arr3

#normal distribution and calculation of statistical tools
np.random.normal(0,100,100)
np.random.normal(0,100,10)

a=np.random.normal(0,100,100)
a

a.mean()
a.std()

a=np.random.normal(100,10,2)
a
a.mean()
a.std()

#rounding off to two decimals or just removing them 
a.round (2)
np.floor([12.5, 67.8])

np.ceil([12.5,67.8])
np.trunc([12.5,67.8])


np.floor([-12.5, 67.8])
np.ceil([-12.5,67.8])
np.trunc([-12.5,67.8])

#String type array 
import numpy as np
names=np.array(["Vikas", "Aman", "Joseph"])
names

names.shape 

#np concatenates only those array where there is just row defined
x4= np.array([1,2,3,4])
x5= np.array([7,8,9,0])

x4a=np.concatenate([x4,x5])
x4a
x4a.shape

#reshaping the array
x= np.arange(6).reshape(2,3)
x

y=np.arange(6).reshape(2,3)
y
np.concatenate([x,y])
np.concatenate([x,y], axis=0)
np.concatenate([x,y], axis=1)

x.shape
y.shape


#Splitting up of arrays 
x=np.arange(10,22)
x

x1=np.split(x,2)
x1
x1[1]
x1[0]

#splitting out row related data(vsplit) or column way(hsplit)  
x2=x.reshape(4,3)
x2

x3= np.vsplit(x2,[3])
x3

x3= np.vsplit(x2,[2])
x3

x4=np.hsplit(x2,[3])
x4
x4=np.hsplit(x2,[2])
x4

#simple arithmetic functions
x2
x2+5

x2*5

np.add(x2, 5)
np.multiply(x2,5)

np.mean(x2)
np.median(x2)
np.sum(x2)
np.min(x2)
np.max(x2)


x=np.random.randint(30,50, size=200000)
x
np.median(x)

x=np.random.randint(30,50, size=20)
x
np.equal(x, 36)
np.equal(x,31)

import numpy as np
text = np.array(["Vikas","Aman","Amit"])
np.equal(text, "Vikas")

x
np.greater(x,36)
np.less(x,36)

np.greater_equal(x, 36)
np.less_equal(x, 36)

x
np.all(x>29)

x
x>35
np.sum(x>35)


import numpy as np

x = np.random.randint(12, size=(3,4))
x

np.sum(x>6, axis=0)
np.sum(x>6, axis=1)

np.sum(x>6)
