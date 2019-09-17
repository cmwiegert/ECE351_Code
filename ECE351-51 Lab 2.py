#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 14})

steps = 1e-5
t = np.arange(0,2+steps,steps)

print('# of elements: len(t) =',len(t), # notice this maybe one larger than expected since `t` starts at 0
 '\nFirst element: t[0] =',t[0], # index the first value of the array `t`
 '\nLast element: t[len(t)-1] =',t[len(t)-1]) # index the last value of the array `t`


# In[3]:


# --- User-Defined Function --- #
# Create the output `y(t)` using a for loop and if/else statements
def func1(t):
    y = np.zeros((len(t),1)) # initialize `y` as a numpy array (of zeros)

    for i in range(len(t)):
        y[i] = np.cos(t[i])
    return y


# In[4]:


y = func1(t) # function call using the user-defined function, shown in the above cell
myFigSize = (10,8)
plt.figure(figsize=myFigSize)
plt.subplot(2,1,1)
plt.plot(t,y)
plt.grid(True)
plt.ylabel('y(t) with Good Resolution')
plt.title('Background - Illustration of for Loops and if/else Statements') # `t` defined with poor resolution
plt.show() # this must be used for each figure


# $$y(t)=r(t)-r(t-3)+5u(t-3)-2u(t-6)-2r(t-6)$$

# In[5]:


def rampfunc(w):
    x=np.zeros((len(w),1))
    
    for i in range(len(w)):
        if w[i] >= 0:
            x[i] = w[i]
        else:
            x[i] = 0
    return x
    
steps = 1e-3
w = np.arange(-1,1+steps, steps)

plt.plot(w,rampfunc(w))
plt.grid(True)
plt.title('Ramp Function')
plt.show()


# In[6]:


def stepfunc(w):
    x=np.zeros((len(w),1))
    
    for i in range(len(w)):
        if w[i] >= 0:
            x[i] = 1
        else:
            x[i] = 0
            
    return x

steps = 1e-3
w = np.arange(-1,1+steps, steps)

plt.plot(w,stepfunc(w))
plt.grid(True)
plt.title('Step Function')
plt.show()


# In[8]:


def signalfunc(w):
    return (rampfunc(w) - rampfunc(w-3) + 5*stepfunc(w-3) - 2*stepfunc(w-6) - 2*rampfunc(w-6))

steps = 1e-3
w = np.arange(-5,10+steps, steps)
y = signalfunc(w)       

plt.title('Derived Function')
plt.plot(w,y)
plt.grid(True)
plt.ylabel('y(t)')
plt.xlabel('t')
plt.show()


# In[7]:


steps = 1e-3
w = np.arange(-10,5+steps, steps)
y = signalfunc(-w)      

plt.title('Derived Function With Time Reverse')
plt.plot(w,y)
plt.grid(True)
plt.ylabel('y(t)')
plt.xlabel('t')
plt.show()


# In[8]:


steps = 1e-3
w = np.arange(-20,20+steps, steps)
y = signalfunc(w-4)
x = signalfunc(-w-4)

plt.title('Altered Derived Functions ')
plt.plot(w,y,label='Original')
plt.plot(w,x,label='Time Shifted')
plt.grid(True)
plt.ylabel('y(t)')
plt.xlabel('t')
plt.legend()
plt.show()


# In[9]:


steps = 1e-3
w = np.arange(-1,20+steps, steps)
y = signalfunc(w/2,)
x = signalfunc(w*2,)

plt.title('Altered Derived Functions')
plt.plot(w,y,label='Lengthened')
plt.plot(w,x,label='Shortened')
plt.grid(True)
plt.ylim([-5,10])
plt.xlim([-5,20])
plt.legend()
plt.ylabel('y(t)')
plt.xlabel('t')
plt.show()


# In[17]:


y = signalfunc(w)
dt = np.diff(10*w)
dy = np.diff(y, axis=0)/dt

plt.plot(w,y,label='Original Function')
plt.plot(w[range(len(dy))],dy[:,0],label='Differentiated')
plt.ylim([-2,10])
plt.title('Differentiated Function Comparison')
plt.grid(True)
plt.legend()
plt.ylabel('y(t)')
plt.xlabel('t')
plt.show()


# In[ ]:




