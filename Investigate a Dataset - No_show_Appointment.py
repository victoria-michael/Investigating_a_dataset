#!/usr/bin/env python
# coding: utf-8

# # Victoria's Project: Investigate a Dataset - (No_show_Appointment)
# <br>
#     
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#quest">Questions</a></li>   
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusion">Conclusion</a></li>
# <li><a href="#limit">Limitations</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# 
# > This project is a cross-section of patients that were scheduled at the hospital and checks to see how many of these patients actually showed up for their appointments and how many didn't. It also checks to see their mean ages, and those that were awarded scholarships.
# 
# > I imported all necessary packages and used Pandas to read in the '.csv' file and also viewed the first five rows, Matplotlib and seaborn for visualisation.

# In[1]:


#import all packages necessary for the project.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


#read the file and print out first five rows
appointment = pd.read_csv('C://Users/victoria.udoh/Downloads/noshowappointments-kagglev2-may-2016.csv')
appointment.head()


# <a id='quest'></a>
# ## Questions
# 
# The project seeks to answer the following questions:
# 
# 1. What is the rate of patients' presence at scheduled appointments vs absence ?
# 2. What is the rate of absentees at appointments among those on scholarship vs self-sponsored?
# 3. What gender were more beneficiaries of the scholarship?
# 4. What was the age range for the women and men in this data?

# <a id='wrangling'></a>
# ## Data Wrangling
# 
# > I checked to the rows and columns count using the '.shape', the mean of the data columns and also checked for missing values in the data.

# In[3]:


#number of rows and columns
appointment.shape


# In[4]:


#returns useful descriptive statistics for each column of data
appointment.describe()


# In[5]:


appointment.rename(columns={'No-show':'No_show'}, inplace=True)


# I renamed the column "No-show" to "No_show" to avoid errors while plotting a graph

# In[6]:


#data types
appointment.dtypes


# In[7]:


#check for instances of missing or possibly errant data including the number of non-null values in each column
appointment.info()


# There are no missing data in the csv file, each column contains 110,527 rows; We also used the info to see the data types of each column and also the numbers of unique values in the dataset. Then, we proceed with the exploratory process. 

# In[8]:


appointment.nunique()


# <a id='eda'></a>
# ## Exploratory Data Analysis
# 
# > *What factors are important in order to predict if a patient will show up for their scheduled appointment? I made a histogram of all the collumns present in the dataset*
# 
# 
# 

# In[9]:


# explore data
appointment.hist(figsize=(10, 10));


# ### Question 1 
# 
# > What is the number of indiviuals that were given scholarship?

# In[10]:


#count of indiviuals that were given scholarship
appointment_totals = appointment.groupby('Gender').count()['Scholarship']
appointment_totals


# In[11]:


# select patients with ages less than 50
df_young = appointment.query('Age < 50')

# select patients with ages older than 50
df_old = appointment.query('Age > 50')

#num_samples = appointment.shape[0]
#num_samples == df_absent['No_show'].count() + df_present['No_show'].count()
df_young.head()


# In[12]:


# get total counts for each younger patients on scholarship
young_gender_totals = df_young.groupby('Gender').count()['Scholarship']
young_gender_totals


# In[13]:


# get total counts for older patients on scholarship
old_gender_totals = df_old.groupby('Gender').count()['Scholarship']
old_gender_totals


# ## What are the mean values for No_shows among the Patients?
# 

# In[14]:


appointment.groupby('No_show').mean()


# In[15]:


appointment.groupby('Gender').mean()


# ### Question 2
# 
# > *What is the rate of presence at scheduled appointments vs absence?*
# 
# From the graph below, it is deduced that there was a higher rate of presence at scheduled appointments compard to those that were a no_show

# In[16]:


show = ['Red', 'Green']
show_means = appointment.groupby('No_show')['Age'].mean()
show_means.plot(kind='bar', title='No Show vs Age', color=show, alpha=.7);
plt.xlabel('show', fontsize=12)
plt.ylabel('Age', fontsize=12)


# ### Question 3 
# 
# > *What is the rate of No_show of patients at appointments among those on scholarship vs self-sponsored?*
# 
# The graph below clearly shows that a higher number of patients on scholarship missed their appointments compared to those who were not on scholarship. 

# In[17]:


# plot relationship between Age and Scholarship
scholar = ['Red', 'Blue']
scholar_means = appointment.groupby('No_show')['Scholarship'].mean()
scholar_means.plot(kind='bar', title='Scholarship vs Appointment Graph', color=scholar, alpha=.7);
plt.xlabel('No_show', fontsize=12)
plt.ylabel('Scholarship', fontsize=12)


# ### Question 4
# 
# > *What gender were more beneficiaries of the scholarship?*
# 
# <br>
# 
# From our analysis, the graph shows women were more in the scholarship scheme than men.

# In[18]:


# plot relationship between Age and Scholarship
gendschol = ['Brown', 'Yellow']
scholar_means = appointment.groupby('Gender')['Scholarship'].mean()
scholar_means.plot(kind='bar', title='Scholarship vs Gender Graph', color=gendschol, alpha=.7);
plt.xlabel('Gender', fontsize=12)
plt.ylabel('Scholarship', fontsize=12)


# In[19]:


# what was the age range for the women and men in this data

sns.catplot(data=appointment, x="Gender", y="Age", kind='box')


# There were more older women and younger men in the dataset.

# In[20]:


#what is the age range for males and females that showed up for their appointment.
# I used .query to single out only females and only males to check out their appointment schedule and age

df_F = appointment.query('Gender == "F"')
sns.catplot(data=df_F, x="No_show", y="Age")

df_M = appointment.query('Gender == "M"')
sns.catplot(data=df_M, x="No_show", y="Age")


# <a id='conclusion'></a>
# ## Conclusion
# 
# In conclusion, the dataset shows that <br>
# 
# 1. There were more older patients in the hospital.
# 2. A higher number of the patients had hypertension and diabetes.
# 3. More of the patients that received SMS were absent at their appointment.
# 4. More women were given scholarship
# 5. There were older women in the project dataset

# <a id='limit'></a>
# ## Limitations
# 
# 1. The presence of categorical data in the dataset
# 2. Time Constraints for the project  

# In[ ]:




