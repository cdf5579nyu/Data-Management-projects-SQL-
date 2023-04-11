#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#decorators task 


# In[5]:


#this is the dummy function given in the exercise that takes a string and returns it
def dummy(s):
  return s

#this is the decorator function that will add the <> signs at the end of each sentence
def dec(f1, tag):

  #Inner function takes the string given for the tag
  def f2(s):
    return f"<{tag}>{f1(s)}</{tag}>\n"


  return f2


# In[6]:


#now, we create the other 5 functions that will use our initial dec function
#and the difference between each is the name of the tag
titleTagFunc = dec(dummy,'title')
pTagFunc = dec(dummy,'p')
headTagFunc = dec(dummy,'head')
bodyTagFunc = dec(dummy,'body')
htmlTagFunc = dec(dummy,'html')


# In[10]:


#now that we have such functions, we will overwrite them to set the specific tags on each

#since the first one is a title and head of the document we will use both
firstPhrase= headTagFunc(titleTagFunc('A page about rain in Spain'))

#and for the second phrase we have that is will be part of the body and will have the ptag
secondPhrase = bodyTagFunc(pTagFunc('The rain in Spain is mainly on the plane.'))

#and to finish we put both objects together to finally apply the html tag to both (since both need it)
output = firstPhrase + secondPhrase


# In[11]:


#we set a final string with the last decorator
finalString = htmlTagFunc(output)
print(finalString)


# In[12]:


#and to prove for the case in which we only put the word foo
print(pTagFunc("foo"))


# In[ ]:




