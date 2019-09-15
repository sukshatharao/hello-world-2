#!/usr/bin/env python
# coding: utf-8

# # Task 2

# In[1]:


# arr_call-> distinct call numbers; call_calling-> calling numbers ; call_recieving-> recieving numbers;

import csv
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    
new_dict= dict()


#for calling numbers
for row in calls:
    if row[0] in new_dict:
        new_dict[row[0]] += int(row[3])
    else:
        new_dict[row[0]] = int(row[3])
        
# for recieving numbers 
for row in calls:
    if row[1] in new_dict:
        new_dict[row[1]] += int(row[3])
    else:
        new_dict[row[1]] = int(row[3])
        
#print(len(new_dict))

maximum= max(new_dict, key=new_dict.get)
print("phone number speaking for the longest time is", maximum,"and the total duration on call is ", new_dict[maximum],"seconds")


# In[ ]:




