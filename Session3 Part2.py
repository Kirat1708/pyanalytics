# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 20:41:00 2020

@author: 91852
"""


import numpy
import numpy as np

np.random.randint(100, 1000)

np.random.randint(100)

#start and end can be mentioned
np.random.randint(10, 1000)

#multiple random nos. from same command
#this is the new dataset which "Array" and since it is array it can define only homogenous data only 
#this is restriction to use array
#it just have similar data i.e. homogenous data 
np.random.randint(10, 1000, size=10)

#it is also a type indexed datatype, accessible  
arr = np.random.randint(10, 1000, size=10)
arr[1]

#it can be updated anywhere i.e mutable 
arr[2] = 200
arr

#matrix formation or row and column format
arr = np.random.randint(10, 1000, size=(2,4))
arr

#to check the shape of error as in the no. of rows and columns
arr.shape

#fetch the individual elements from multidimensional array 
arr[0,0]
arr[0,1]
arr[0,2]
arr[0,3]

arr[1,0]
arr[1,1]
arr[1,2]
arr[1,3]

#fetch a set of elements together from a multidimensional array
arr[0,0:3]
arr[:, 0:2]
arr[:,2:4] / arr[:,2:]
arr[2:4,1:3]

arr = np.random.randint(1, 9, size=(5,4))
arr

arr[-1,:]
arr[-2,:]
arr[-2:,:]
arr[-2:,-2:]

#Range function of numpy is arange that can create a range to create even multidimensional range as well

np.arange(10)
np.arange(10, 20)
np.arange(10, 20, 2)

arr1= np.arange(10,20)
arr1.shape

arr1reshape= arr1.reshape(2,5)
arr1reshape
arr1reshape.shape

arr1reshape= arr1.reshape(10)
arr1reshape
arr1reshape.shape

arr2reshape= arr1.reshape(10,1)
arr2reshape
arr2reshape.shape

arr3reshape= arr1.reshape(1,10)
arr3reshape
arr3reshape.shape

arr2reshape= arr1.reshape(5,2)
arr2reshape
arr2reshape.shape

arr2reshape= arr1.reshape(2,5)
arr2reshape
arr2reshape.shape


#array of zeros and ones
#be default it creates an array of float type and thus there is a dot with values in the output
a = np.zeros((2,4))
a

b= np.ones((2,4))
b

c = np.ones((2,4), dtype="int32")
c

#algorithms in these library are very advanced and thus simple 
#mathematical calculations in not at all tough for this numpy library

b+c
b*c
b/c
b**c

#np.random.randint(10.0,100.0)
#np.random.random(10)

#creating empty arrays 
arr7= np.empty((4,5))
arr7

arr7= np.empty((4,5), dtype="int32")
arr7

#identity matrix/array
np.eye(3,3)

#linspace creates an array in a sequential manner or incremental manner with equal spaces
#in simple words it creates an arithmetic progression
np.linspace(0, 10, num=4)
np.linspace(0, 10, num=4, dtype="int32")
np.linspace(0, 48, num=4, dtype="int32")
np.linspace(10, 58, num=4, dtype="int32")
