# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 18:50:31 2020

@author: 91852
"""

import pandas as pd
s = pd.Series(range(1001,1033))
df_mtcars = pd.read_csv("C:\\Analytics\\Projects\\mt.csv")
df_mtcars.head(2)
df_mtcars=df_mtcars.set_index(s)
df_mtcars.loc[1001:1009]
df_mtcars["mpg"]

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
df_mtcars.head()

course = pd.Series(["BTech", "MBA", "MTech"])
course

strength = pd.Series([100, 200, 250])
strength
fees = pd.Series([10000, 25000, 20000])
fees

pd1 = pd.DataFrame([course, strength, fees])
pd1

pd2 = pd.DataFrame({"course":course, "strength": strength,"fees" :fees})
pd2

#checking the entries under heads 
pd2["strength"]
pd2["course"]
pd2.course
pd2.strength

npd = pd2.keys
npd

pd2
pd2[1:2]
pd2[1:4]

pd2
pd2.count()

pd2.loc[1:2]
df_mtcars.count()

#changing columns
pd2.course="MBA"
pd2

pd3 = pd.DataFrame({"course":course, "strength":strength, "fees":fees})
pd3

pd2.course== "MBA"
pd3.loc[pd2.course== "MBA"]

pd3[pd3.fees==20000]
pd3.loc[pd3.fees==20000]

k = pd.Series(range(101,104))
pd3 = pd3.set_index(k)
pd3
pd3[1]
pd3.loc[1]
pd3.loc[101]
pd3.iloc[1]

pd2 #better way

pd2.index 
pd2.columns
pd2.values

#or
pd2
pd2.count()
pd2.course
pd2.strength
pd2.fees



#comparison
pd2 is pd2
pd2.course is pd2.fees
pd2.course is pd2["course"]

pd3=pd2
pd3.course is pd2.course

pd2[pd2.fees > 20000]


import pandas as pd
import numpy as np

placed = pd.Series([None,np.nan, 100, None])
placed
np.sum(placed) #not considering nan values

course = pd.Series(["BTech","MTech", "BBA", "MBA"])

strength = pd.Series([100, 50, 200,75])
fees = pd.Series([2.5, 3, 2, 4])

pd3 = pd.DataFrame({"course":course, "Strenth": strength, "fees": fees, "placed":placed})
pd3

pd3.placed.sum()
pd3.strength.sum()
pd3.placed.max()

placed
placed.isnull()
placed.notnull()

p2 = placed.dropna()
p2


import pandas as pd


#new dataframe from list values
pd4 = pd.DataFrame([['dhiraj', 50, 'M', 10000], ['kanika', 28, None, 5000], ['tanvi', 20, 'F', None], ['poonam',45,'F',None],['upen',None,'M',None]])
pd4
pd4.dropna()  #row with any an NA value / completecases
pd4.dropna(axis='columns')  #only those columns with NA
pd4.dropna(axis=1)
pd4.dropna(axis='rows')  #rows

pd4.dropna(axis="rows", how="all")
pd4.dropna(axis='columns', how='all')  #all None columns

pd4.dropna(axis='columns', how='any')  #all None columns

pd4.dropna(axis='columns', thresh=3)  #min non NA values in columns
pd4.dropna(axis='rows', thresh=3)  #min min NA values in rows

#filling na values
placed= pd.Series([1,2, None, 5, None, None, 8])
placed
placed.fillna(0)

placed.fillna(method='ffill')

placed.fillna(method='bfill')
#DF fill
pd4
pd4.fillna(method='ffill', axis=1)
pd4.fillna(method='ffill', axis=0)


#MultiIndex  - Later
#pag 130
x= [1,2,3]
y= [4,5,6]
z= [7,8,9]
x,y,z

np.concatenate([x,y,z])
np.concatenate([x,y,z], axis=0) #they are single dim arrays
#np.concatenate([x,y,z], axis=1)  #will not work

x=[[1,2,3],[4,5,6]]
y=[[10,11,12],[13,14,15]]
x
np.concatenate([x,y], axis=1) #cbind
np.concatenate([x,y], axis=0)  #rbind

#DF
grades1 = pd.DataFrame(['A','B1'])

grades1 = {'subject1': ['A1','B1','A2','A3'],'subject2': ['A2','A1','B2','B3']   }
grades1
df1 = pd.DataFrame(grades1,columns= ['subject1', 'subject2'])
df1

grades2 = {'subject3': ['A1','B1','A2','A3'],'subject4': ['A2','A1','B2','B3']   }
df2 = pd.DataFrame(grades2,columns= ['subject3', 'subject4'])
df2
#join
pd.concat([df1,df2])
pd.concat([df1,df2], axis=0)
pd.concat([df1,df2], axis=1)
pd.concat([df1,df2], ignore_index=True)  #index values in order
pd.concat([df1,df2], keys=['x','y'])  #adding multiple index


print (df)

import pandas as pd
#Join
rollno = pd.Series(range(1,11))
rollno
name = pd.Series(["student" + str(i) for i in range(1,11)])
name
genderlist  = ['M','F']
import random
gender = random.choices(genderlist, k=10)
gender


random.choices( population=genderlist,weights=[0.4, 0.6],k=10)
#numpy.random.choice(items, trials, p=probs)
np.random.choice(a=genderlist, size=10, p=[.2,.8])


import numpy as np
marks1 = np.random.randint(40,100,size=10)
marks1

pd5 = pd.DataFrame({'rollno':rollno, 'name':name, 'gender':gender, 'marks1':marks1})

pd5

#course = random.choices( population=['BBA','MBA','BTECH'] ,weights=[0.4, 0.3,0.3],k=10)
course = np.random.choice(a=['BBA','MBA','BTECH'], size=10)
course

marks2 = np.random.randint(40,100,size=10)

marks2

pd6 = pd.DataFrame({'rollno':rollno, 'course':course, 'marks2':marks2})
pd6

fees = pd.DataFrame({'course':['BBA','MBA','BTECH'], 'fees':[100000, 200000, 150000]})
fees

pd5.head(2)
pd6.head(2)

#1 to 1
pd7=pd.merge(pd5, pd6)
pd7
pd7.head(2)

pd8=pd.merge(pd5, pd6, on='rollno')
pd.concat([pd5, pd6], axis=1)
pd8.head(2)

#many to 1

pd6
fees
pd.merge(pd6, fees)

#
pd6b = pd.DataFrame({'rollno1':rollno, 'course':course, 'marks3':marks2})
pd6b
pd5

pdmerge= pd.merge(pd5, pd6b, left_on='rollno', right_on='rollno1')
pdmerge.head(2)

pdmerge
pd.merge(pd5, pd6b, left_on='rollno', right_on='rollno1').drop('rollno1', axis=1).head(2)  #drop redundant coln

#with indices defined
pd5a = pd5.set_index('rollno')

pd5a.head(1)


pd6a = pd6.set_index('rollno')
pd6a.head(1)


pd.merge(pd5a, pd6a, left_index=True, right_index=True)


pd5a
pd6a

#pd6a.join(pd5a)

pd5a
pd6

pd.merge(pd5a, pd6, left_index=True, right_on='rollno')


#set arithmetic
pd5
pd6

pd.merge(pd5, pd6, how='inner')

fees
pd6

pd.merge(pd6, fees, how='inner')


#two joins 
#left - combining on the basis of left df
#right -combining on the basis of right df

pd6
fees

pd.merge(pd6, fees, how='outer')

pd6

pd.merge(pd6, fees, how='left')

pd5
pd6

#replacing the column naming
pd4

pd4.columns

pd4.columns = ['name', 'age','gender','fees']
pd4

pd4.age

#select all from df where age>20
pd4.age > 20

pd4[pd4.age > 20]


#find out if any value in df.age is null then results True

pd4.age.isnull().any()

pd4
pd4.isnull()

pd4.isnull().any()

pd4.head(3)

pd4
pd4.dropna()

pd4
pd4.fillna(method='ffill')

pd4.fillna(method='bfill')



#pd4.dropna(inplace=True) #???? carefull it will make changes to original
pd4.sort_values(ascending=True, by='name')


pd4 = pd.DataFrame([['dhiraj', 50, 'M', 10000], ['kanika', 28, None, 5000], ['tanvi', 20, 'F', None], ['poonam',45,'F',None],['upen',None,'M',None]])
pd4

pd4.columns = ['name', 'age','gender','fees']
pd4.sort_values(ascending=False, by='name')
pd4
pd4.sort_values(ascending=False, by='name',inplace=True)
pd4 #change original DF
pd4.sort_values(ascending=False, by=['age'])
pd4.sort_values(ascending=False, by=['fees'], na_position='first')
pd4.sort_values(ascending=True, by=['fees','age'])
pd4.sort_values(ascending=[True,False], by=['gender','age'])
#pd4.sort() #depreciated

pd4.shape

#%%
#summary on DF: create fairly large data
import pandas as pd
import numpy as np

rollno = pd.Series(range(1,1001))

rollno

name = pd.Series(["student" + str(i) for i in range(1,1001)])
name

genderlist  = ['M','F']

import random
#gender = random.choices(genderlist, k=1000)
gender= np.random.choice(a=genderlist, size=1000,replace=True, p=[.6,.4])
gender


import collections

collections.Counter(gender)

marks1 = np.random.randint(40,100,size=1000)

marks2 = np.random.randint(40,100,size=1000)

fees = np.random.randint(50000,100000,size=1000)

fees.mean()

course = np.random.choice(a=['BBA','MBA','BTECH'], size=1000)

collections.Counter(course)

city = np.random.choice(a=['Delhi', 'Gurugram','Noida','Faridabad'], size=1000, replace=True, p=[.4,.2,.2,.2])

collections.Counter(city)


pd8 = pd.DataFrame({'rollno':rollno, 'name':name, 'course':course, 'gender':gender, 'marks1':marks1,'marks2':marks2, 'fees':fees,'city':city})
pd8

pd8.head()

#start

pd8.head()
pd8.tail()


pd8.describe()

pd8.count()
pd8['gender'].value_counts()  #if col has spaces


pd8.gender.value_counts()
#all columns


#pd8.apply(pd.value_counts)

#pd8.apply(pd.value_counts).fillna(0)

pd8.head(1)
pd8.groupby('course').size() #provides the average 

pd8.groupby('course').count() #count of every single column

#conver cat columns

pd8.columns

categ = ['course', 'gender','city']
categ

pd8.head(2)

pd9 = pd8[categ]
pd9.head()


pd9.describe()

pd8.groupby(['city','course', 'gender']).size()

pd8.groupby(['city','course', 'gender']).count()



pd8.pivot_table(index=['city','course'], columns='gender', aggfunc='size')

pd.crosstab([pd8.city, pd8.course], pd8.gender)


pd8.groupby(['city','course','gender'])['gender'].size().fillna(0).astype(int)

#aggregate, fileter, transform apply
pd8.columns

pd8
pd8.marks1.min()

pd8['marks1'].min()
pd8.groupby(['course']).size()

pd8.groupby(['course']).get_group('MBA')
pd8.groupby(['course']).get_group('MBA').count()

#Groupby('course').aggregate('min', np.median, max)
pd8.groupby(['course']).count()
pd8.groupby('course', as_index=False).agg({"marks1": "sum"})
pd8.groupby('course', as_index=True).agg({"marks1": "sum"}) #makes course as index

pd8.groupby(['course','gender']).agg({"marks1": [min, max, np.mean], "marks2": [min, max, np.median, 'first'], "gender": ['count']})  #np.mean - numpy object
pd8


def gthan(x): 
    return x > 70

pd8['marks1'].apply(gthan).value_counts()

pd8['marks1'].apply(gthan).value_counts().plot(kind='barh', stacked=True, figsize=[16,6], colormap='winter')










