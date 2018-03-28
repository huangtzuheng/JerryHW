
# coding: utf-8

# In[2]:


def cal(a, b, func):
    if func == "+":
        print(a,func,b,"=",plus(a,b))
    elif func == "-":
        print(a,func,b,"=",minus(a,b))
    elif func == "*":
        print(a,func,b,"=",multiply(a,b))
    elif func == "/":
        print(a,func,b,"=",devide(a,b))
def plus(n1,n2):
    return n1 + n2
def minus(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def devide(n1,n2):
    return n1 / n2

