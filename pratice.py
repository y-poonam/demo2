# a = 'hello\
# users'
# print(a)

# break statement
# a = [1,2,3,4,5,6,4]
# word = 4
# count = 0
# for i in a:
# 	if i  == word:
# 		count+=1
# 		break
# print(count)

# while loop
# i = 0
# while True:
# 	print(i,' ',end = '')
# 	i=i+1
# 	if  i == 5:
# 		break
# print('numbers are:',i)

# continue statement
# a = [1,2,3,4,5,6,7,8]
# num = 6
# for i in a:
# 	if (i == num):
# 		continue
# 	print(i)
# str1 = 'JAVATPOINT'
# str2 = 'T'
# for i in str1:
# 	if(i==str2):
# 		continue
# 	print(i,end = '')

# pass statement
# values = {'p','t','h','o','n'}
# for val in values:
# 	pass

# list Comprehension

# fruits = ["apple","apple", "banana", "cherry", "kiwi", "mango"]
# # a = [i for i in fruits if 'a' in i]
# b = []
# a = [i for i in range(10) if i%2!=0]
# print(a)

# matrix  = [[j for j in range(5)] for i in range(4)]
# print(matrix)
# number = [i*10 for i in range(1,6)]
# print(number)

# matrix = [[1,2],
#           [3,4],
#           [5,6]]
# result  = [row[i] for row in matrix for i in range(len(matrix[0]))]
# print(result)

# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]
# nums=[(x+y) for x in nums1 for y in nums2]
# print(nums)
# from functools import reduce
# a = [1,2,3,4,5,6,4]

# lst =list(map(lambda x:x*2,a))
# lst = reduce(lambda x:x,a)
# print(lst)

# l1=["   a","b  ","  c  "]
# l2=[i.strip() for i in l1]
# print (l2)

# l=[-2,-1,0,3,4]
# l3=[str(abs(i)) for i in l]
# print (l3)

# set comparhsion
# s = {(i,i*i)for i in range(1,10) if i%2==0}
# print(s)

# a = [1,2,3,4,5]
# b = ['red','yellow','green','white','black']
# dict1 = {k:v for k,v in zip(a,b)} 
# print(dict1)

# tup = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
# newset = list(filter(lambda x: x<=50 , tup)) 
# print(newset)
# tup = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
# newset = list(map(lambda x: x+3, tup)) 
# print(newset)

# from functools import reduce
# tup = [2,3,4,5]
# newset = reduce(lambda x,y:x+y, tup) 
# print(newset)

# import time 
# print(time.localtime(time.time()
# from datetime import datetime
# print(datetime.now())
# print(datetime.now().month)
# print(datetime.now().year)
# print(datetime.now().day)


# try:
# 	a = int(input('enter the number:'))
# 	b = int(input('enter the number:'))
# 	c = a/b
# 	print(c)
# except:
# 	print("Can't divide with zero")

# try:    
#     age = int(input("Enter the age:"))    
#     if(age<18):    
#         raise ValueError   
#     else:    
#         print("the age is valid")    
# except ValueError:    
#     print("The age is not valid")   


# try:    
#     a = int(input("Enter a:"))    
#     b = int(input("Enter b:"))    
#     if b is 0:    
#         raise ArithmeticError  
#     else:    
#         print("a/b = ",a/b)    
# except ArithmeticError:    
#     print("The value of b can't be 0")  


# class Student:
# 	def __init__(self,name,id,age):
# 		self.name = name
# 		self.id = id 
# 		self.age = age

# st = Student('john',22,23)





















































































()














































































































