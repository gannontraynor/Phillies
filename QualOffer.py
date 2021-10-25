#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import seaborn as sns
from re import sub
import matplotlib.pyplot as plt
import bs4


# In[6]:


temp = pd.read_html("https://questionnaire-148920.appspot.com/swe/data.html")
print(*temp)


# In[7]:


df = pd.DataFrame(*temp, columns = ["Player" , 'Salary', "Year", "Level"])
#prelace nulls with zero
df = df.fillna(0)
df


# In[8]:


# filter out anything that isnt a digit in salary, zeros are fine because we will only 
# be considereing the top 150 salries
i = 0
for sal in df["Salary"]:
    #convert everytyhing to string to remove non digit values
    sal = str(sal)
    sal = sub(r'[^\d.]', '', sal)
    #if the input was only text, it is now empyt change it to 0.
    if (sal == ""):
        sal = "0";
    sal = int(sal)
    #add new value to dataframe
    df.at[i , "Salary"] = sal
    i = i + 1
    #print(type(sal))


# In[9]:


df


# In[10]:


sort = df.sort_values(by = "Salary", ascending=False, ignore_index=True)
sort


# In[11]:


top = sort.head(150)


# In[12]:


top


# In[19]:


offer = top["Salary"].mean()
offer


# In[20]:


def getOffer():
    stroffer = "${:,.2f}".format(offer)
    return stroffer


# In[21]:


getOffer()


# In[49]:


def makeplot():
    plt.plot(top["Salary"])
    plt.title("The Value of the Qualifying Offer is " + getOffer())
    plt.ylabel("Salaries x 10^7")
    plt.axhline(y=offer, xmin=-1, xmax=1, color='r', linestyle='--')
    txt="The red line represents the values of the Qualifying Offer compared to the top 150 paid players."
    plt.figtext(0.5, 0.001, txt, wrap=True, horizontalalignment='center', fontsize=12)
    plt.savefig("QualifyingOffer_Traynor.png", dpi = 200, bbox_inches = "tight")
    plt.show()


# In[50]:


makeplot()


# In[15]:





# In[ ]:




