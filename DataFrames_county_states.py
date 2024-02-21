#!/usr/bin/env python
# coding: utf-8

# # DataFrames Basics

# In[1]:


import pandas as pd


# The `read_csv` method will read in a CSV file and returns to us a DataFrame

# In[5]:


states = pd.read_csv("data/states.csv")
states


# ## King County Home Sales Data Set
# This dataset includes the home sales from 2014-2015 in King County, WA (the county Seattle is located in)
# * `id` - house's unique id
# * `date` - sale date
# * `price` - sale price
# * `bedrooms` - number of bedrooms
# * `bathrooms` - numbers of bathrooms
# * `sqft_living` - living space square footage 
# * `sqft_lot` - total lot square footage
# * `floors` - numbers of floors
# * `waterfront` - is the house waterfront (1) or not (0)
# * `view` - rating from 0 to 4 of how good the view from the house is
# * `condition` - rating from 1 (poor) to 5 (very good) of the condition of the house
# * `grade` - rating from 1-13 representing the construction quality of improvements. 1-3 Falls short of minimum building standards (cabins, etc.) 7 is avg grade, 11-13 have high-quality design & construction
# * `sqft_above` - square footage of the interior that is above ground level
# * `sqft_basement` - square footage of the interior that is below ground level
# * `yr_built` - year the house was initially built
# * `yr_renovated` - The year of the house’s last renovation (if any)
# * `zipcode` - zipcode that the house is located in
# * `lat` - the property's latitude
# * `long` - the property's longitude
# * `sqft_living15` - average interior space square footage of the nearest 15 neighbors
# * `sqft_lot15` - average lot square footage of the nearest 15 neighbors

# In[6]:


houses = pd.read_csv("data/kc_house_data.csv")


# In[28]:


houses


# In[32]:


type(houses)


# In[33]:


houses.columns


# In[34]:


states.columns


# In[35]:


len(houses)


# In[37]:


houses.shape


# In[38]:


houses.size


# In[41]:


pd.options.display.min_rows = 15


# In[42]:


houses


# The `head()` method returns the first n rows in a NEW DataFrame

# In[45]:


first_5 = houses.head()
first_5


# In[46]:


type(first_5)


# In[48]:


houses.head(200)


# The `tail()` method is like `head()` but it works from the END of a DataFrame.  By default it returns the last 5 rows in a new DataFrame.

# In[49]:


houses.tail()


# In[50]:


houses.tail(9)


# In[52]:


houses.info()


# In[53]:


states.info()


# In[54]:


houses.dtypes


# ## Introducing The Titanic Dataset

# In[56]:


titanic = pd.read_csv("data/titanic.csv")
titanic.head()


# In[57]:


titanic.columns


# * `pclass` - Passenger Class (1 = 1st; 2 = 2nd; 3 = 3rd)
# * `survived` - Survival (0 = No; 1 = Yes)
# * `name` - Name
# * `sex` - Sex
# * `age` - Age
# * `sibsp` - Number of Siblings/Spouses Aboard
# * `parch` - Number of Parents/Children Aboard
# * `ticket` - Ticket Number
# * `fare` - Passenger Fare
# * `cabin` - Cabin
# * `embarked` - Port of Embarkation (C = Cherbourg; Q = Queenstown; S = Southampton)
# * `boat` - Lifeboat (if survived)
# * `body` - Body number (if did not survive and body was recovered)
# * `home.dest` - Home/Destination

# In[58]:


titanic.tail(10)


# In[59]:


titanic.info()


# In[60]:


titanic.head()


# ## read_csv with non-comma separators
# The `netflix_titles.csv` file is actually pipe (`|`) separated.  We can tell `read_csv` to expect this using the `sep="|"` option. 
# 
# Additionally, the netflix dataset includes an index column as the very first column.  We can let `read_csv` know using `index_col=0`

# In[68]:


netflix = pd.read_csv("data/netflix_titles.csv", sep="|", index_col=0)


# In[69]:


netflix.info()


# In[70]:


netflix.head()


# ## Proving Column Names
# 
# We can provide a list of custom column names to `read_csv` using the `names` parameter.  Additionally, we need to specify `header=0` to tell `read_csv` that the file still contains the original headers on the first line and that it should ignore them!

# In[80]:


names = ['sumlev', 'region', 'division', 'state', 'name', 'census2010pop', 'estimatesbase2010', 'popestimate2010', 'popestimate2011', 'popestimate2012', 'popestimate2013', 'popestimate2014', 'popestimate2015', 'popestimate2016', 'popestimate2017', 'popestimate2018', 'popestimate2019', 'popestimate042020', 'popestimate2020']
state_pops = pd.read_csv("data/nst-est2020.csv", names=names, header=0)
state_pops

