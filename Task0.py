#!/usr/bin/env python
# coding: utf-8

# In[8]:


import csv
import csv
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    
print("calls last row", calls[-1]);

import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

print("texts first row",texts[0]);


# In[ ]:




