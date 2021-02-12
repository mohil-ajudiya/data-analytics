#!/usr/bin/env python
# coding: utf-8

# In[1]:


#what we are going to achive from this datset analysis

#Q1 Who were the passengers on the titanic?                                                                                .
#Q2 What deck the passengers on and how does it relate to their class?                                                      .
#Q3 Where did passengers come from?                                                                                         .
#Q4 Who was alone and Who was with family?
#Q5 what helped surviving and sinking?


# In[2]:


import numpy as np
import pandas as pd
from numpy.random import randn
from pandas import Series, DataFrame
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


#importing the titanic data

titanic_data = pd.read_csv("E://data_set/titanic/train.csv")


# In[4]:


titanic_data


# In[5]:


titanic_data.info()


# In[6]:


#here we can see that cabin shows only 204 non null items else everything is close to th4e 891


# In[7]:


def child(Human):
    Age, Sex = Human
    if (Age<16):
        return 'child'
    else:
        return Sex


# In[8]:


titanic_data['Person'] = titanic_data[['Age','Sex']].apply(child, axis=1)


# In[ ]:





# In[9]:


titanic_data['Age'].hist()


# In[10]:


titanic_data['Age'].mean()


# In[11]:


child = titanic_data[titanic_data.Age <10]
child


# In[12]:


sns.relplot('Age','Survived',data=child)


# In[13]:


# this shows there are around 62 passenger who are childrens..


# In[14]:


adult = titanic_data.Age<40


# In[15]:


adult.value_counts()


# In[16]:


#551 - 62 = 490
#This shows that there are around 500 people from 890 are young passengers


# In[17]:


titanic_data['Person'].value_counts()


# In[18]:


fig = sns.FacetGrid(titanic_data,hue='Person', aspect=4)
fig.map(sns.kdeplot, 'Age', shade=True)
oldest = titanic_data['Age'].max()
fig.set(xlim=(0,oldest))
fig.add_legend()


# In[19]:


# this shows that most of the people on the titanic were adult


# In[20]:


fig = sns.FacetGrid(titanic_data, hue='Pclass',aspect=4)
fig.map(sns.kdeplot, 'Age', shade=True)
oldest = titanic_data['Age'].max()
fig.set(xlim=(0,oldest))
fig.add_legend()


# In[21]:


#This graph shows that most of the most person who aged greater than 40 are on the first class

#which defines that those must the successfull rich people on the board of journey in titanic


# In[22]:


titanic_data


# In[23]:


#cleaning data of the cabin column


# In[24]:


deck = titanic_data['Cabin'].dropna()


# In[25]:


deck


# In[26]:


levels = []

for level in deck:
    levels.append(level[0])
cabin_df = (levels)


# In[27]:


cabin_df


# In[28]:


sns.relplot('Pclass','Survived',data=titanic_data,kind='line')


# In[29]:


#this shows that most of the first class passenger was survived than the third class


# In[57]:


sns.catplot('Sex','Pclass',kind='point',data=titanic_data)


# In[ ]:


##this shows that there more no. of males than females.


# In[30]:


sns.relplot('Pclass','Survived',data=titanic_data,col='Person',kind='line')


# In[31]:


#First class children and the female passengers was survived the crash
#This shows that chance to seat in the rescue  boat was given first to the female and children in the boat


# In[32]:


sns.catplot('Survived','Pclass',col='Age',col_wrap=4,data=titanic_data)


# In[33]:


#moving on to the next question
# who were with the family


# In[34]:


titanic_data


# In[35]:


titanic_data['Alone'] = titanic_data.SibSp + titanic_data.Parch

# adding the sibling and the parent child if there


# In[36]:


titanic_data


# In[37]:


titanic_data.dropna()


# In[38]:


titanic_data


# In[39]:


titanic_data['Count'] = titanic_data.SibSp - titanic_data.Parch
titanic_data
titanic_data['Count'] = 1
titanic_data

#this will help to count the numbers accordingly when we want to categories the person with and without family


# In[40]:


sns.relplot('Pclass','Alone',hue='Survived',data=titanic_data)


# In[41]:


#so we can see clearly over here that first class passengers who were survived no matter with family or without family
#but the third class was not survived


# In[58]:


#now let us see the difference of survival eith class and age


# In[60]:


sns.lmplot('Age','Survived',hue='Pclass',data=titanic_data)


# In[61]:


#clearing the data for the age group


# In[62]:


generation = [10,20,40,60]
sns.lmplot('Age','Survived',hue='Pclass',data=titanic_data,x_bins=generation)


# In[63]:


#the first class and the second class childrens were high chances of being survived


# In[68]:


sns.lmplot('Age','Survived',hue='Sex',data=titanic_data,x_bins=generation)


# In[69]:


#this shows females saved in priority with the age and class


# In[70]:


titanic_data


# SO we came to know that passengers with upper class ws on the upper deck and thus their fare was also cost high then the lower classs.
# on the surviving instinct it showed that first class passengers was given priority and overall with sex females and children were saved first.
# the data showed if you were an female with older age you will be saved and with the class was like a golden priority, I dont know why according to me young generation should be saved regardless of the class

# In[ ]:




