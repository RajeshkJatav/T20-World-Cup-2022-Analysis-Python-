#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default = "plotly_white"


# In[7]:


data = pd.read_csv(r"C:\Users\WB96\Desktop\Projects\T20 World Cup 2022 Analysis\t20-world-cup-22.csv", encoding = "unicode_escape")


# In[8]:


print(data.head())


# In[9]:


data.head()


# In[10]:


data.describe()


# In[15]:


#Now look at the number of matches won by each team in the world cup:

figure = px.bar(data, 
                x=data["winner"],
                title="Number of Matches Won by teams in T20 World Cup 2022")
figure.show()


# In[ ]:


As England won the t20 world cup 2022, England won five matches. And Both Pakistan and India won 4 matches.


# In[17]:


# Now find the number of matches won by batting first and batting second in the T20 world cup 2022.

won_by = data["won by"].value_counts()
label = won_by.index
counts = won_by.values
colors = ['gold','lightgreen']

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Number of Matches Won By Runs Or Wickets')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# In[ ]:


#So in the T20 world cup 2022, 16 matches were won by batting first, and 13 matches were won by chasing.


# In[21]:


#Now, let’s have a look at the toss decisions by teams in the world cup:
won_by = data["toss decision"].value_counts()
label = won_by.index
counts = won_by.values
colors = ['blue','skyblue']

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Toss Decision in the T20 World Cup')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# In[ ]:


So in 17 matches, the teams decided to bat first, and in 13 matches, the teams chose to field first.


# In[26]:


#Now find the top scorers in the t20 world cup 2022:

figure = px.bar(data, 
                x=data["top scorer"], 
                y = data["highest score"], 
                color = data["highest score"],
                title="Top Scorers in t20 World Cup 2022")
figure.show()   


# In[ ]:


So,from the above graph we can see that Virat Kohli scored the highest in 3 matches. Undoubtedly, he was the best batsman in the t20 world cup 2022.


# In[29]:


#Now find the number of player of the match awards in the world cup:

figure = px.bar(data,
                x = data["player of the match"],
                title ="Player of the match award in T20 world cup 2022")
figure.show()


# In[ ]:


Virat Kohli, Sam Curran, Taskin Ahmed, Suryakumar Yadav, and Shadab Khan got the player of the match in 2 matches.
No player got the player of the match award in more than two matches.


# In[33]:


#Now let’s have a look at the bowlers with the best bowling figures at the end of the matches:

figure = px.bar(data, 
                x=data["best bowler"],
                title="Best Bowlers in t20 World Cup 2022")
figure.show()


# In[ ]:


Sam Curran was the only best bowler in 3 matches. Undoubtedly, he deserved to be the player of the tournament.


# In[35]:


#Now we will compare the runs scored in the first innings and second innings in every stadium of the t20 world cup 2022:

fig = go.Figure()
fig.add_trace(go.Bar(
    x=data["venue"],
    y=data["first innings score"],
    name='First Innings Runs',
    marker_color='blue'
))
fig.add_trace(go.Bar(
    x=data["venue"],
    y=data["second innings score"],
    name='Second Innings Runs',
    marker_color='red'
))
fig.update_layout(barmode='group', 
                  xaxis_tickangle=-45, 
                  title="Best Stadiums to Bat First or Chase")
fig.show()


# In[ ]:


So SCG was the only stadium in the world cup that was best for batting first. Other stadiums didn’t make much difference while batting first or chasing.


# In[36]:


#Now compare the number of wickets lost in the first innings and second innings in every stadium of the t20 world cup 2022:

fig = go.Figure()
fig.add_trace(go.Bar(
    x=data["venue"],
    y=data["first innings wickets"],
    name='First Innings Wickets',
    marker_color='blue'
))
fig.add_trace(go.Bar(
    x=data["venue"],
    y=data["second innings wickets"],
    name='Second Innings Wickets',
    marker_color='red'
))
fig.update_layout(barmode='group', 
                  xaxis_tickangle=-45, 
                  title="Best Statiums to Bowl First or Defend")
fig.show()


# In[ ]:


SCG was the best stadium to bowl while defending the target. While the Optus Stadium was the best stadium to bowl first.


# In[ ]:


#SUMMARY
So some highlights of the t20 world cup 2022 we found from our analysis are:

1.England won the most number of matches
2.Virat Kohli scored highest in the most number of matches
3.Sam Curran was the best bowler in the most number of matches
4.More teams won by batting first
5.More teams decided to bat first
6.SCG was the best stadium to bat first
7.SCG was the best stadium to defend the target in the World Cup
8.The Optus Stadium was the best stadium to bowl first

