#!/usr/bin/env python
# coding: utf-8

# # Example (synthetic) data sets
# For the purpose of this effort to create a common data shape on Glioblastoma, two synthetic data sets were provided. Synthetic datasets contain fabricated data that is represtable of actual data on the topic. 
# 
# In this chapter we will inspect the provided datasets and prepare them to by converted into linked data. As described earlier, linked data is data that follows a linked-data format consisting of triples where the individual parts consists of either values or identifiers (IRIs) pointing to concept definitions. 
# 
# The proces of converting data to linked data is rather straightforwards and can be summed up as follows:
# 1. Inspect the data
# 2. Clean the data headers
# 3. Align the data with common controlled vocabularies or ontologies
# 4. Design linked-data shapes using the IRIs from the controlled vocabularies and ontologies
# 5. Transform the data into RDF
# 
# In this chapter we will focus on the first two steps.

# ## Dataset 1 on Cotton
# The first dataset is a provided csv file (Legacy_Cotton_VT_data.csv) ## TODO add a link.
# It contains legacy data on cotton harvests.

# In[1]:


import pandas as pd
gdb1 = pd.read_csv("data/Legacy_Cotton_VT_data.csv",index_col=False)
gdb1


# In[2]:


set(gdb1.LintFraction.tolist())


# In[3]:


gdb1.info()


# This dataset contains 26 fields of various datatypes. In one of the next steps this field names will be alligned with various controlled vocabularies and ontologies. For this to be succesful the fieldnames need to be as expressive as it can be. 

# In[4]:


def show_difference(row):
    highlight = 'background-color: yellow;'
    default = ''
    if row['original_field'] != row['prepared_field']:
        return [default, highlight]
    else:
        return [default, default]
    
def strip_check(row):
    if row['original_field'] != row['prepared_field']:
        row["change"] = "remove trailing spaces"
        
def abbreviations(row):
    if row['original_field'] != row['prepared_field']:
        if row["change"] == "":
            row["change"] = "resolved abbreviations"
            
def removechoices(row):
    if row['original_field'] != row['prepared_field']:
        if row["change"] == "":
            row["change"] = "removed choices"

df = pd.DataFrame(columns=["original_field", "prepared_field", "change"])
for column in gdb1.columns: 
    df.loc[len(df.index)] = [column, column.strip(), ""]
    
df.apply(strip_check, axis=1)
    
df['prepared_field'] = df['prepared_field'].str.replace('adj','adjuvant')
df['prepared_field'] = df['prepared_field'].str.replace('months OS','months overall survival')
df['prepared_field'] = df['prepared_field'].str.replace('PP','pseudo-progression')
df['prepared_field'] = df['prepared_field'].str.replace('PFS','progression-free survival')

df.apply(abbreviations, axis=1)
         
df['prepared_field'] = df['prepared_field'].str.replace('(1=yes 0=no)','', regex=False)
df.apply(removechoices, axis=1)
 
df.style.set_properties(**{'text-align': 'left'})
df.style.apply(show_difference, subset=['original_field', 'prepared_field'], axis=1)


# In this chapter we have reviewed and possibly cleaned the source data. In the next chapter these terms will be use to identify IRIs that unambiguously point to the definitions of these field labels. In this stage of the project we need to be a bit creative here. Some crucial information such as conditionals or units have been removed, but these are needed in the semantic models that will be derived.
# 
# Moving forward the project should design a common tabular format that, next to field labels, also captures these conditionals, units and cardinality. 
# 
# Eventually this book should contain a chapter that describes this tabular format. 
# 
# Eventually the steps described in this chapter will be redundant. Moving forward performers in the different PDAs, ideally will build on a predefined tabular format where the field names are selected from the provided codebook. 
# 
# ## NALT shapes and  codebook
# The DT codebook will be a listing of selected field names. Data curators will be able to select field names from this codebook. Non-existing field names can be requested. 
# 
