#!/usr/bin/env python
# coding: utf-8

# In[6]:


print("Pattern 1")
print()


n=6
for i in range(1, n+1):
    print("*"*n)   


# In[22]:


print("Pattern 2")
print()
n=6
for i in range(1,n+1):
    for j in range (1, n+1):
        print(i, end='') # i printed
    print()
    
print()


# In[13]:


print("Pattern 3")
print()

n=6
for i in range(1, n+1):
    for j in range(1,n+1):
        print(j, end='') # printed
    print()


# In[16]:


print("Pattern 4")
print()

n=6
for i in range(1,n+1):
    for j in range (1,n+1):
        print(chr(64+i),end='')
    print()


# In[21]:


print("Pattern 5")
print()

n=6
for i in range(1,n+1):
    for j in range(1, n+1):
        print(chr(64+i), end='')
    print()
    
print()
print("Pattern 5 Modified")
print()

n=6
for i in range(1,n+1):
    for j in range(1, n+1):
        print(chr(64+1), end='')
    print()


# In[24]:


print("Pattern 6")
print()

n=6
for i in range(1,n+1):
    for j in range(1, n+1):
        print(n+1-i, end="")
    print()


# In[25]:


print("Pattern 7")
print()

n=6
for i in range(1,n+1):
    for j in range(1,n+1):
        print(n+1-j, end='')
    print()


# In[ ]:




