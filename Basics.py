#!/usr/bin/env python
# coding: utf-8

# ## Tuple

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





# In[ ]:





# In[ ]:


daneeth = ()
print(type(daneeth))


# In[3]:


daneeth = (1,3,3.3,"danny")
print(daneeth)
print(daneeth[3])


# In[4]:


#Repetations
daneeth = (1,3,3.3,"danny")
a=(1,2,4,5)
print(daneeth*2)


# In[5]:


#conecdination
daneeth = (1,3,3.3,"danny")
a=(1,2,4,5)
print(daneeth+a)


# In[7]:


#memberships
daneeth = (1,3,3.3,"danny")
a=(1,2,4,5)
print(2 in a )
print(3 in a)


# In[9]:


#iternation 
daneeth = (1,3,3.3,"danny")
a=(1,2,4,5)
for i in a:
    print(i)


# In[12]:


daneeth = (1,3,3.3)
print(min(daneeth))
print(max(daneeth))


# ## Break and contintue statment

# In[14]:


for val in "daneeth":
    if val=='e':
        break
    print(val)
print("the end")
    


# In[16]:


for val in "daneeth":
    if val=='t':
        continue
    print(val)
print("the end")
    


# ## String

# In[17]:


s = "daneeth"
s1 = "reddy"
s2 ='''
daneeth
reddy
tadiparthi
'''

print(type(s))
print(type(s1))
print(type(s2))


# In[19]:


h = s2.replace('daneeth','danny')
print(h)


# In[20]:


h = s2.upper()
print(h)


# In[21]:


h= s2.lower()
print(h)


# In[24]:


s2 ='''
   daneeth
reddy
tadiparthi  
'''
print(s2)

h = s2.strip()
print(h)


# In[25]:


h = s1.split()
print(h)


# In[28]:


h = s1.startswith('d')
print(h)

h = s1.endswith('y')
print(h)


# In[29]:


print("my name is {}".format('daneeth'))


# print(s2.count("e"))
# print(len(s2))

#  ## Set

# In[1]:


s={}
print(type(s))


# In[2]:


s={1,2,3}
print(type(s))


# In[5]:


s={1,2.2,"danny"}
s.add('reddy')
print(s)


# In[6]:


s={1,2.2,"danny"}
s.update(['reddy'])
print(s)


# In[8]:


s={1,2.2,"danny"}
s.remove('danny')
print(s)


# In[9]:


s={1,2.2,"danny"}
s.add('reddy')
print(len(s))


# In[10]:


s={1,2.2,"danny",1,2.2,3,4,5}
print(s)


# In[11]:


s1={1,2,3,4,5,6}
s2={5,6,7,8,9,100}
print(s1.union(s2)) #print(s1|s2)


# In[12]:


s1={1,2,3,4,5,6}
s2={5,6,7,8,9,100}
print(s1.intersection(s2))


# In[17]:


s1={1,2,3,4,5,6}
s2={1,2,3,4,5,6}
print(s1.issubset(s2))


# ## Dictionary

# In[1]:


dic = {}
print(type(dic))


# In[3]:


dic = {"name":"Daneeth","Age":24}
print(dic)
print(dic["name"])


# In[5]:


dic = {"name":"Daneeth","Age":24,"address":"272 Manning Blvd"}
dic.pop("address")
print(dic)


# In[6]:


dic = {"name":"Daneeth","Age":24,"address":"272 Manning Blvd"}
dic.update({"Phno":5189618423})
print(dic)


# In[7]:


dic = {"name":"Daneeth","Age":24,"address":"272 Manning Blvd"}
dic.clear()
print(dic)


# In[10]:


dic = {"name":"Daneeth","Age":24,"address":"272 Manning Blvd"}
print(dic.keys())
print(dic.values())


# ## Functions

# In[11]:


def function_name():
    print("This is Function")

function_name()


# In[15]:


def function_name(name,age):
    print("This is Function",name,"and age is",age)

function_name("Daneeth",24)


# In[16]:


def function(a,b):
    return a+b

w=function(3,4)
print(w)


# In[17]:


def function(a):
    for i in a:
        print(i)
function([1,2,3,4])


# In[18]:


def function(*a):
    print(a)
function(1,3,4,5,6,6,76)


# In[19]:


def function(**a):
    print(a)

function(name ="Daneeth", age=24)


# ## File Handling

# In[21]:


f = open('danny.txt','r')
c = f.read()
print(c)
f.close()


# In[23]:


'''
f = open('danny.txt','w')
c = f.write("This is Write")
print(c)
f.close()
f = open('danny.txt','r')
c = f.read()
print(c)
f.close()
'''


# In[29]:


f = open('danny.txt','a')
c = f.write("This is Daneeth")
print(c)
f.close()
f = open('danny.txt','r')
c = f.read()
print(c)
f.close()


# ## Error Handling

# In[35]:


try:
    print(s)
except:
    print("Except")
finally:
    print("end")


# In[36]:


try:
    print(s)
except Exception as e:
    print(e)
finally:
    print("end")


# In[37]:


s = "danny"
d=1

try:
    print(s/d)
except Exception as e:
    print(e)
finally:
    print("end")


# In[40]:


x=-1
if x<0:
    print("correct")
    #raise Exception("the is raise")


# ## Class and Object

# In[41]:


class Daneeth:
    print("This is Class")


# In[45]:


class Daneeth:
    print("This is Class")
    def display(self):
        a = 10
        b = 12
        print(a,b)
        
obj = Daneeth()
obj.display()


# In[46]:


class Daneeth:
    d=15
    def display(self):
        a = 10
        b = 12
        print(a,b)
        
obj = Daneeth()
obj.display()
print(obj.d)


# In[54]:


class Mobile:
    def __init__(self,brand,battery,ram,camera,price):
        self.brand = brand
        self.battery = battery
        self.ram = ram
        self.camera = camera
        self.price =  price
    def display(self):
        print("brand:",self.brand)
        print("battery:",self.battery)
        print("ram:",self.ram)
        print("camera:",self.camera)
        print("price:",self.price)
        print("_________________")
        
obj = Mobile("apple","4000mah","8Gb","48MP","90000")
obj.display()
obj2 = Mobile("Oneplus","5000mah","8Gb","48MP","90000")
obj.display()


# In[57]:


class mobile:
    def __init__(self):
        print("This is init")
    def display(self):
        print("This is Method")
obj = mobile()
obj.display()


# ## Inheritance

# In[61]:


#single Inheritance
class parent:
    def function(self):
        print("This is Parent class")
class child(parent):
    def fun1(self):
        print("this is child class")

obj = child()
obj.fun1()
obj.function()


# In[63]:


#multilevel inheritance
class parent:
    def function(self):
        print("This is Parent class")
class child(parent):
    def fun1(self):
        print("this is child class")
class grandchild(child):
    def fun2(self):
        print("This is grandchild")
        
obj = grandchild()
obj.function()
obj.fun1()
obj.fun1()
    
 
    


# In[66]:


#Hierachical inheritance
class parent:
    def function(self):
        print("This is Parent class")
class child1(parent):
    def fun1(self):
        print("this is child class")
class child2(parent):
    def fun2(self):
        print("This is grandchild")
        
obj = child2()
obj.function()
#obj.fun1()
obj.fun2()


# In[68]:


#multiple inheritance
class father:
    def function(self):
        print("This is father class")
class mother:
    def fun1(self):
        print("this is mother class")
class child(father,mother):
    def fun2(self):
        print("This is child class")
        
obj =child()
obj.function()
obj.fun1()
obj.fun2()


# In[72]:


#Super keyword
class A:
    def __init__(self):
        print("This is class A")
        
class B(A):
    def __init__(self):
        print("This is class B")
        super().__init__()
        
obj = B() 


# ## Ploymorphism

# In[75]:


#Over-loading
#same class and function names but different parameter's
class A:
    def sum(self,a,b):
        return a+b
    def sum(self,a,b,c=1):
        return a+b+c

obj = A()
print(obj.sum(1,2,5))

#To get rid of overloading we can give defaul arguments.


# In[78]:


# Over-riding 
#Different class but same function name and parameter's

class A:
    def display(self):
        print("This is Class A")
class B(A):
    def display(self):
        print("This is class B")
        super().display()
        
obj = B()
obj.display()


# In[ ]:


#Abstraction 
#hiding of Data, we will get only output, we cannot see data


# In[ ]:


#Encapsulation
#Binding of Data members and member functions

