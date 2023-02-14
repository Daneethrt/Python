#!/usr/bin/env python
# coding: utf-8

# In[2]:


a = 1
b = 3

if a>b:
    print("a is grater  than b")
elif a<b:
    print("a is smaller than b")
else:
    print("b is smaller than a")


# In[3]:


#short hand if condition.
a=1
b=22
if a<b:print("this is short hand if")


# In[5]:


#Short hand if else
print("this is short hand if") if a>b else print("this is short hand else if")


# In[10]:


#logical operators

a=200
b=33
c=500

if a>b or c<b:
    print("or")
else:
    print('else')


# In[11]:


#pass
if b>a:
    pass


# In[1]:


Daneeth = []
print(Daneeth)


# In[2]:


Daneeth = [1,2.2,"Danny",True]
print(Daneeth)


# In[4]:


Daneeth = [1,2.2,"Danny",True]
Daneeth.append(1)
print(Daneeth)
print(type(Daneeth))


# In[7]:


Daneeth = [1,2.2,"Danny",True]
Daneeth.extend([1,3,5])
print(Daneeth)


# In[8]:


Daneeth = [1,2.2,"Danny",True]
Daneeth.insert(1,"Python")
print(Daneeth)


# In[11]:


Daneeth = [1,2.2,1,2,2,2,2,2,"Danny",True]
print(Daneeth.count(2))
print(len(Daneeth))


# In[12]:


Daneeth = [1,2.2,"Danny",True]
Daneeth.pop(1)
print(Daneeth)


# In[13]:


Daneeth = [1,2.2,"Danny",True]
Daneeth.reverse()
print(Daneeth)


# In[14]:


Daneeth = [1,2,3,4,5,6,7,10,9,8]
Daneeth.sort()
print(Daneeth)


# In[15]:


Daneeth = [1,2,3,[4,5,6,7],10,9,8]
print(Daneeth[3][1])


# In[16]:


for i in 'Daneeth':
    print(i)


# In[21]:


l = [1,2,3,4,5]
sum = 0
for i in l:
    sum = sum+i
    print(sum)
    
    


# In[22]:


for i in range(1,10,2):
    print(i)


# In[ ]:


mobiles = ['iphone','mi','realme','one plus']

for i in mobiles:
    if i=='iphone':
        print("This is iphone")
        #break
    else:
        print('This is not iphone')
    


# In[ ]:


c = 0

while c<3:
    c+=1
    print("c is",c)
else:
    print("completed")


# In[ ]:




