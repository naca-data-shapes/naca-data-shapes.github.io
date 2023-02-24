#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install shexviz')


# # Production Shape
# * OBJECTID
# * Date of planting
# * Date of harvest
# * SeedingRatePerAcre
# * PercentBallOpened
# 

# In[2]:


from shexviz import shex2dot
f = open("cotton/productionShape.shex", "r")
shex = f.read()

shex2dot.shex2dot(shex, "test")


# In[ ]:


OBJECTID
Date of planting
Date of harvest
ValuePerac
SeedingRatePerAcre
PercentBallOpened

