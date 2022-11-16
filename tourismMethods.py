import pandas as pd
import requests
import matplotlib.pyplot as plt

""" Reading data and fill in the data to variable df """
df = pd.read_csv('https://raw.githubusercontent.com/andrzejmp/some_codes/main/python/tourism/data.csv')

year = df["YEAR"]
'''tourismForTurkey(): This fuction generate a chart with data from Turkey
- Country data are taken from the column " TK"'''
def tourismForTurkey():
    tk = df[" TK"]

    plt.bar(year,tk,color="red")
    plt.title('Tourism Income of Turkey')
    plt.xlabel('Years')
    plt.ylabel('Income')
    
    plt.show()


'''tourismForPoland(): This fuction generate a chart with data from Poland
- Country data are taken from the column " PL"'''

def tourismForPoland():
    country = df[" PL"]

    plt.bar(year,country, color="pink")
    plt.title("Tourism Income of Poland")
    plt.xlabel("Years")
    plt.ylabel("Income")
    plt.show()   


'''tourismForSpain(): This fuction generate a chart with data from Spain
- Country data are taken from the column " SP"'''
def tourismForSpain():
    country = df[" SP"]

    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.bar(year, country, color="yellow")
    ax.set_title("Data on tourism in Spain by year", fontsize=24)
    ax.set_xlabel('Years', fontsize=16)
    ax.set_ylabel("Number of people", fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)
    plt.show() 



def allcountries():

  """
  
  This method shows tourism income of all 3 countries.
 and if input is
   t, it shows Turkey income
   p, it shows poland income
   s, it shows spain income
   a, it shows all of 3 countries income
  """
  year = df["YEAR"]
  spain = df[" SP"]
  turkey = df[" TK"]
  poland = df[" PL"]
  
  plt.style.use('seaborn')
  fig, ax = plt.subplots()
  ax.plot(year, spain, c='yellow')
  ax.plot(year, turkey, c='red')
  ax.plot(year, poland, c='pink')
  
  
  ax.set_title("Tourism in last decade, 2010-2020", fontsize=24)
  ax.set_xlabel('Income', fontsize=16) 
  ax.set_ylabel("Years", fontsize=16)
  ax.tick_params(axis='both', which='major', labelsize=16)
  
  plt.show() 