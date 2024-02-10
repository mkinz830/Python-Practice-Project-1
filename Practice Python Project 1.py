#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[9]:


get_ipython().system('head /Users/Bella/Downloads/sales_data.csv')


# In[11]:


#reading the file

sales = pd.read_csv(
    '/Users/Bella/Downloads/sales_data.csv',
    parse_dates=['Date'])


# In[12]:


#previewing the data

sales.head()


# In[13]:


#shape shows how many rows and columns are in the dataset

sales.shape


# In[14]:


sales.info()


# In[15]:


#shows the statistical properties of the dataset

sales.describe()


# # Numerical analysis & visualization

# In[16]:


sales['Unit_Cost'].describe()


# In[17]:


sales['Unit_Cost'].mean()


# In[18]:


sales['Unit_Cost'].median()


# In[19]:


sales['Unit_Cost'].plot(kind='box', vert=False, figsize=(14,6))


# In[21]:


sales['Unit_Cost'].plot(kind='density', figsize=(14,6))


# In[22]:


ax = sales['Unit_Cost'].plot(kind='density', figsize=(14,6))
ax.axvline(sales['Unit_Cost'].mean(), color='red')
ax.axvline(sales['Unit_Cost'].median(), color='green')


# In[23]:


ax = sales['Unit_Cost'].plot(kind='hist', figsize=(14,6))
ax.set_ylabel('Number of Sales')
ax.set_xlabel('Dollars')


# # Categorical Analysis & Visualization

# In[24]:


sales.head()


# In[25]:


sales['Age_Group'].value_counts()


# In[26]:


sales['Age_Group'].value_counts().plot(kind='pie', figsize=(6,6))


# In[29]:


ax = sales['Age_Group'].value_counts().plot(kind='bar', figsize=(14,6))
ax.set_ylabel('Number of Sales')


# # Relationship between the columns?

# In[33]:


corr = sales.corr()

corr


# In[35]:


fig = plt.figure(figsize=(8,8))
plt.matshow(corr, cmap='RdBu', fignum=fig.number)
plt.xticks(range(len(corr.columns)), corr.columns, rotation='vertical');
plt.yticks(range(len(corr.columns)), corr.columns);
    


# In[36]:


sales.plot(kind='scatter', x='Customer_Age', y='Revenue', figsize=(6,6))


# In[38]:


sales.plot(kind='scatter', x='Revenue', y='Profit', figsize=(6,6))


# In[40]:


ax = sales[['Profit', 'Age_Group']].boxplot(by='Age_Group', figsize=(10,6))
ax.set_ylabel('Profit')


# In[42]:


boxplot_cols = ['Year', 'Customer_Age', 'Order_Quantity', 'Unit_Cost', 'Unit_Price', 'Profit']

sales[boxplot_cols].plot(kind='box', subplots=True, layout=(2,3), figsize=(14,8))


# # Column Wrangling

# # Add & calculate a new Revenue_Per_Age column

# In[46]:


sales['Revenue_Per_Age'] = sales['Revenue'] / sales['Customer_Age']
sales['Revenue_Per_Age'].head()


# In[44]:


sales['Revenue_Per_Age'].plot(kind='density', figsize=(14,6))


# In[45]:


sales['Revenue_Per_Age'].plot(kind='hist', figsize=(14,6))


# # Adding a Calculated_Cost column

# In[66]:


sales['Calculated_Cost'] = sales['Order_Quantity'] * sales['Unit_Cost']

sales['Calculated_Cost'].head()


# In[61]:


(sales['Calculated_Cost'] != sales['Cost']).sum()


# In[55]:


sales.plot(kind='scatter', x='Calculated_Cost', y='Profit', figsize=(6,6))


# In[49]:


sales.head()


# In[ ]:




