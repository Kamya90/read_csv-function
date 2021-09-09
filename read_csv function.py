#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os


# In[2]:


os.getcwd()


# In[4]:


os.listdir('.')


# In[7]:


os.mkdir('./data')


# In[9]:


'data' in os.listdir('.')


# In[10]:


os.listdir('./data')


# In[11]:


url1 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans1.txt'
url2 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans2.txt'
url3 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans3.txt'


# In[12]:


import urllib.request


# In[18]:


urllib.request.urlretrieve(url1,'./data/loans1.txt')


# In[19]:


urllib.request.urlretrieve(url2,'./data/loans2.txt')


# In[20]:


urllib.request.urlretrieve(url3,'./data/loans3.txt')


# In[21]:


os.listdir('./data')


# In[23]:


file1=open('./data/loans1.txt',mode='r')


# In[24]:


file1_contents=file1.read()


# In[26]:


print(file1_contents)


# In[27]:


file1.close()


# In[28]:


with open('./data/loans2.txt','r') as file2:
    file2_contents=file2.read()
    print(file2_contents)


# In[32]:


with open('./data/loans3.txt','r') as file3:
    file3_contents=file3.readlines()
    print(file3_contents)


# In[43]:


file3_contents[0].strip()


# In[44]:


print(file2_contents)


# In[45]:


def parse_headers(header_line):
    return header_line.strip().split(',')


# In[46]:


headers=parse_headers(file3_contents[0])


# In[47]:


headers


# In[65]:


def parse_values(values):
    value_list=[]
    for item in values.strip().split(','):
        if item=='':
            value_list.append(0.0)
        else:   
            value_list.append(float(item))
    return value_list    


# In[66]:


parse_values(file3_contents[2])


# In[67]:


def create_dict(values,keys):
    result={}
    for values,keys in zip(values,keys):
        result[keys]=values
        
    return result


# In[68]:


create_dict(parse_values(file3_contents[2]),headers)


# In[69]:


with open('./data/loans2.txt','r') as file2:
    file2_contents=file2.read()
    print(file2_contents)


# In[72]:


def read_csv(path):
    final=[]
    with open ('./data/loans2.txt','r') as f:
        lines=f.readlines()
        headers=parse_headers(lines[0])
        for data in lines[1:]:
            values=parse_values(data)
            item_dict=create_dict(values,headers)
            final.append(item_dict)
        return final


# In[73]:


read_csv('./data/loans2.txt')


# In[ ]:




