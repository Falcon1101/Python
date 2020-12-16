#!/usr/bin/env python
# coding: utf-8

# # Invoice data extraction scrpit
# The script is made to convert the old text or csv file invoice of a company to well organized database from which several studies can be mande in order to make business desicions
# 
# ## Why Invoice?
# It had a lot of information about the sales of the product(Supplier, customer address, amount, date of purchase etc.) it became the first steps stone towards building an enriching data for the study of future sales and market strategy.

# In[2]:


import glob
import pandas as pd

# get data file names
path = ('/Users/vagishmishra/Desktop/python')
ext = input('Enter the file extension: ')
filenames = glob.glob(path + "/*." +ext)
#filenames = glob.glob(path + "/*.txt")


# In[4]:


fr =list() #list for the full content in the files
fe = list()#list for splitting the content in small peices by \n
fs = list()
for m in filenames:
    fo = open(m)
    fd = fo.read().rstrip()
    fr.append(fd)
for n in fr:
    d= n.split('\n')
    fe.append(d)

        


# In[5]:


invoice_df = pd.DataFrame(fe, columns={'Invoice':0,'Amount':1,'Country':2})


# In[6]:


invoice_df


# In[7]:


#slicing the table to remove the prefix information from the text file
invoice_df['Country'] = invoice_df['Country'].str.slice(6,25)
if ext =='csv':
    invoice_df['Invoice'] = invoice_df['Invoice'].str.slice(9,25)
else:
    invoice_df['Invoice'] = invoice_df['Invoice'].str.slice(8,25)
invoice_df['Amount'] = invoice_df['Amount'].str.slice(7,25) 


# In[8]:


invoice_df


# In[9]:


invoice_df['Amount']


# In[10]:


invoice_data=invoice_df.astype({'Amount':'float32','Invoice':'int32'})


# In[11]:


print(invoice_data)


# In[12]:


invoice_data = invoice_df.drop_duplicates(subset=['Invoice'])


# In[13]:


group_country = invoice_data.groupby('Country')


# In[15]:


for x,group in group_country: # for randon var,gourp dataframe small in main dataframe
   print (x)
   print (group)


# In[ ]:




