#!/usr/bin/env python
# coding: utf-8

# In[97]:


import os , shutil


# In[94]:


path = "D:/sorter the project/"

# we changed the \ to /


# In[98]:


file_name = os.listdir(path)  

#showing us what files that we have 


# In[99]:


folder_names = ['csv file', 'image file' , 'Word file','Excel file']

for loop in range(0,4):
    if not os.path.exists(path + folder_names[loop]):
        print(path+folder_names[loop])
        os.makedirs(path+folder_names[loop])
    


# In[100]:


for file in file_name:
    if ".csv" in file and not os.path.exists(path+"csv file/" +file):
        shutil.move(path+file,path+ "csv file/" +file)
        
    elif ".xlsx" in file and not os.path.exists(path+"Excel file/" +file):
        shutil.move(path+file,path+ "Excel file/" +file)
        
    elif ".png" in file and not os.path.exists(path+"image file/" +file):
        shutil.move(path+file,path+ "image file/" +file) 
        
    elif ".docx" in file and not os.path.exists(path+"word file/" +file):
        shutil.move(path+file,path+ "Word file/" +file) 
    
    else:
        print("there are files that were not moved")
        
 
    
    


# In[ ]:




