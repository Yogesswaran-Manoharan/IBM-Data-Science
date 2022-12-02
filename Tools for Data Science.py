#!/usr/bin/env python
# coding: utf-8

# # My Jupyter Notebook on IBM Watson Studio

# **Yogesswaran Manoharan**

# *I am interested in Data Science because of its cores principal to identify detailed information from the data to answer questions*

# ### Rock, Paper & Scissors

# In[7]:


import random

def play():
    user = input("What's your choice ?\n\nr' for rock,'p' for papers,'s' for scissors\n\n")
    computer = random.choice(['r','p','s'])
    
    if user == computer:
        return 'Its a Ties'
    
    if is_win(user,computer):
        return 'You won !'
    
    return 'You lost !'
    
    # r>s, s>p, p>r
    
def is_win(player,component):
    if (player == 'r' and component == 's') or (player == 's' and component == 'p') or (player == 'p' and component == 'r'):
        return True

print(play())


# **Markdown experiment**
# 
# Blocked quote
# 
# >Hi everyone how you doing !
# 
# Numbered list
# 
# 1. Rock
# 2. Paper
# 3. Scissors
# 
# Bulleted list
# 
# * google
# * netflix
# 
# Table
# 
# | S.No | Name | Age |
# | --- | --- | --- |
# | 1 | Yogi | ** |
