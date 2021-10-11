#!/usr/bin/env python
# coding: utf-8
1.Introduction
This assignment will help you to consolidate the concepts learnt in the session.
2.Problem Statement

1.1 Write a Python Program to implement your own myreduce() function which works exactly
like Python's built-in function reduce()

1.2 Write a Python program to implement your own myfilter() function which works exactly
like Python's built-in function filter()

2. Implement List comprehensions to produce the following lists.
Write List comprehensions to produce the following Lists
['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
[[2], [3], [4], [3], [4], [5], [4], [5], [6]] [[2, 3, 4, 5], [3, 4, 5, 6],
[4, 5, 6, 7], [5, 6, 7, 8]]
[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
# In[42]:


#my_reduce
def my_reduce_add(list_in):
    """Takes list as input and add all the values in a list and gives output as int"""
    list_add = 0
    for i in list_in:
        list_add = list_add+i
    return list_add 

def my_reduce_mul(list_in):
    """Takes list as input and multiply all the values in a list and gives output as int"""
    mul_out = 1
    for i in list_in:
        mul_out = i*mul_out
    return mul_out

def my_reduce_sub(list_in):
    sub_out = 0
    for i in list_in:
        sub_out = -(sub_out - i)
    return sub_out


# In[44]:


list_in = [6,55,43,78]
print(my_reduce_add(list_in))
print(my_reduce_mul(list_in))
print(my_reduce_sub(list_in))


# In[29]:


#####@@@@@@ my_filter #########################

def my_filter(list_in):
    filtered = []
    for i in list_in:
        if i%2 == 0:
            filtered.append(i)
    return filtered


# In[30]:


listin = [2,4,6,8,2222,3,5]
my_filter(listin)


# In[5]:


#########['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]###########
l = []
for i in "ACADGILD":
    l.append(i)
print(l)


# In[6]:


########################['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']######################
example = ["x", "y", "z"]
out = []

for i in example:
    for j in range(1,5):
        out.append(i * j)

print(out)
    


# In[7]:


#######################['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']##############
example = ["x", "y", "z"]
out = []

for i in range(1,5):
    for j in example:
        out.append(i * j)

print(out)


# In[8]:


############[[2], [3], [4], [3], [4], [5], [4], [5], [6]] [[2, 3, 4, 5], [3, 4, 5, 6],[4, 5, 6, 7], [5, 6, 7, 8]]############
example = [1,2,3,4]
out1 = []
out2 = []
out3 = []


for m in range(0,3):
    for i in range(1,4):
        for j in range(1,2):
            out1.append([j+i+m]) 

for i in range(1,5):
    l = []
    for j in example:
        l.append(i+j)
    out1.extend([l])

print(out1)
    


# In[9]:


##################[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]#######################
a = []
for i in range(0,3):
    for j in range(0,3):
        a.append(((j+1),(i+1)))
        
print(a)

