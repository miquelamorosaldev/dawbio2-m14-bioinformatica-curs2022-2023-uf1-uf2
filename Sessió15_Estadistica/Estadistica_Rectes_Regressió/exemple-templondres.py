
# Original source:
# https://towardsdatascience.com/regression-plots-with-pandas-and-numpy-faf2edbfad4f

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the CSV file in a Panda Dataframe.
weather = pd.read_csv('https://raw.githubusercontent.com/alanjones2/dataviz/master/londonweather.csv')

#print(weather)
# Each line represents the temperature every month, 7 is july.
july = weather.query('Month == 7')

#Insert new column to make the plot
july.insert(0,'Yr',range(0,len(july)))
#print(july)

#Create basic plot, with max temperatures.
july.plot(y='Tmax',x='Yr',label = "{f}")

#Required to show the plot on screen.
# plt.show()


#In the graph we can't see trend, 
# temperatures do seem to be rising a little, over time.

#we'll show the linear regression to make sure if
#temperatures are rising every year.
#the third parameter is 1, if we want polinomical reg.
#should be 2, 3...

d = np.polyfit(july['Yr'],july['Tmax'],1)
f = np.poly1d(d)

#inserting that into a new column called Treg.
july.insert(6,'Treg',f(july['Yr']))
print(july)

# Next, we create a line plot of Yr against Tmax 
# (the wiggly plot we saw above) and 
# another of Yr against Treg which will be our straight 
# line regression plot. 
# We combine the two plot by assigning the first plot 
# to the variable ax and then passing that to the second plot 
# as an additional axis.

ax = july.plot(x = 'Yr',y='Tmax')
july.plot(x='Yr', y='Treg',color='Red',ax=ax)
plt.show()

#Anàlisi resultats
#És una barbaritat veure com ha pujat la temperatura el juliol Londres en des de fa 50 anys.