#!/usr/bin/env python
# coding: utf-8

# In[21]:


from bs4 import BeautifulSoup
import requests


# In[22]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)


soup = BeautifulSoup(page.text,'html')


# In[23]:


print(soup)


# In[24]:


soup.find('table',class_='wikitable sortable')


# In[29]:


table=soup.find_all('table')[1]


# In[30]:


print(table)


# In[37]:


world_titles=table.find_all('th')


# In[38]:


world_titles


# In[39]:


world_table_titles = [title.text.strip() for title in world_titles]

print(world_table_titles)


# In[40]:


import pandas as pd


# In[41]:


df= pd.DataFrame(columns=world_table_titles)
df


# In[54]:


column_data=table.find_all('tr')


# In[70]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    indvidual_row_data = [data.text.strip() for data in row_data]
    

    length = len(df)
    df.loc[length]= indvidual_row_data
    


# In[71]:


df


# In[74]:


df.to_csv(r'D:\Data sets\Companies.csv',index =False)


# In[ ]:




