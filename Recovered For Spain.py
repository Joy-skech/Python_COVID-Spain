# The Course - PROG8420 (PROGRAMMING FOR BIG DATA)
# Quiz - Quiz 05
# Creation date : 24th April 2020
# Author's Name: Joy Obisesan


# importing libraries
import pandas as pd
import matplotlib.pyplot as plt 


#Read the data
data = pd.read_csv ('C:\\Users\\hp\\Documents\\Data\\covid_19_data.csv') 


data_Spain = data[data['Country/Region']=='Spain']


fig, ax = plt.subplots()
data_Spain.plot(x = "ObservationDate", y = "Recovered", figsize=(10,5), kind = 'line',ax=ax)
plt.xlabel('Date Observed')
plt.ylabel('Recovered')
plt.title('COVID-19 Recovered for Spain')

#display gridlines
ax.grid()
plt.show()