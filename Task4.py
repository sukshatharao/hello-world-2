#!/usr/bin/env python
# coding: utf-8

# In[5]:


import re
import csv
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

with open('texts.csv', 'r') as f1:
    reader1 = csv.reader(f1)
    texts = list(reader1)

tele_list = []
for r1 in calls:
    if r1[0] not in tele_list :
        tele_list.append(r1[0])
    if r1[1] in tele_list:
        tele_list.remove(r1[1])

for r2 in texts:
    if r2[0] in tele_list :
        tele_list.remove(r2[0])
    if r2[1] in tele_list:
        tele_list.remove(r2[1])
print("\nThe list of telemarketers could be: " , tele_list)


# In[ ]:




