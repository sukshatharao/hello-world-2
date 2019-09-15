#!/usr/bin/env python
# coding: utf-8

# In[4]:


import csv
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
output_arr = set()
for row in calls:
    output_arr.add(row[0])
    output_arr.add(row[1])


with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
for row in texts:
    output_arr.add(row[0])
    output_arr.add(row[1])


#print(output_arr)
print("There are ",len(output_arr)," different telephone numbers in the call+text records.")     


# In[ ]:




