#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd


# In[9]:


df = pd.read_excel(r"D:\Data sets\Customer Call List.xlsx")
df


# In[10]:


df=df.drop_duplicates()
df


# In[ ]:


df=df.drop(columns = "Not_Useful_Column")


# In[13]:


df["Last_Name"]=df["Last_Name"].str.lstrip("/")
df["Last_Name"]=df["Last_Name"].str.lstrip("...")
df["Last_Name"]=df["Last_Name"].str.rstrip("_")

df


# In[14]:


df["Phone_Number"]=df["Phone_Number"].str.replace('[^a-zA-Z0-9]','')

df["Phone_Number"] = df["Phone_Number"].apply(lambda x: str(x)) #lambda like the for loop, we can use the for loop too

df["Phone_Number"]=df["Phone_Number"].apply(lambda x:x[0:3] + '-' + x[3:6] + '-' + x[6:10])

df["Phone_Number"]= df["Phone_Number"].str.replace('nan','')
df["Phone_Number"]= df["Phone_Number"].str.replace('Na','')

df


# In[15]:


df[["Street_Address" , "State" , "Zip_code"]] = df["Address"].str.split(',' ,2,expand =True)
df


# In[18]:


df["Paying Customer"] = df["Paying Customer"].str.replace('Yes' , 'Y')
df["Paying Customer"] = df["Paying Customer"].str.replace('No' , 'N')
df


# In[21]:


df =df.fillna('')
df


# In[28]:


for x in df.index:
    if df.loc[x , "Do_Not_Contact"] == 'Y':
        df.drop(x , inplace=True)
df


# In[38]:


for x in df.index:
    if df.loc[x , "Phone_Number"] == '':
        df.drop(x , inplace=True)

df


# In[39]:


df =df.reset_index(drop=True)
df


# In[ ]:




