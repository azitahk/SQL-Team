# https://datatofish.com/matplotlib-charts-tkinter-gui/
#from vscode terminal prompt >
#> python -m pip install pandas
#> python -m pip install matplotlib
#$sudo apt install python3-tk    # install for ubuntu only
import tkinter as tk
#from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#> python -m pip install mysql
#> python -m pip install mysql-connector
import mysql.connector
import pandas as pd

#need to set up remote connections in phpmyadmin for this to work
#check you are using the correct server IP address ie 
# host="10.0.0.49"
# host="10.0.0.60",
i40db = mysql.connector.connect(
  host="10.0.0.150",
  user="I40Remote",
  passwd="Password1",
  database="Industry40db",
  auth_plugin='mysql_native_password'
)

#read database data into a pandas DataFrame (df)
df = pd.read_sql('SELECT * FROM roomData', con=i40db)

#example of data in df
#   id	roomName  humidity  temperature	outsideTemp	CO2	  readDate
# 0	1	  E223	    47.63	    27.64	      None	      None	2020-03-13 12:46:06

#change humidity andf temperature columns values to numeric values
df['humidity'] = pd.to_numeric(df['humidity'])
df['temperature'] = pd.to_numeric(df['temperature'])

#drop unused columns in prototype (None values)
df.drop('outsideTemp', axis=1, inplace=True)
df.drop('CO2', axis=1, inplace=True)

#add extra columns for Date and Time from readDate
df['Date'] = df['readDate'].apply(lambda dt: dt.date())
df['Time'] = df['readDate'].apply(lambda dt: dt.time())

# set up tkinter main window
root= tk.Tk() 
  
#bar graph of Room temperature
figure1 = plt.Figure(figsize=(6,5), dpi=100)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, root)
bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
df1 = df[['Time','temperature']].groupby('Time').sum()   #required to label axes correctly
df1.plot(kind='bar', legend=True, ax=ax1)
ax1.set_title('Room temperature')

#df = df.set_index('id')
#line graph of temperature and humidity

figure2 = plt.Figure(figsize=(5,4), dpi=100)
ax2 = figure2.add_subplot(111)
line2 = FigureCanvasTkAgg(figure2, root)
line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
df2= df[['Time','temperature']].groupby('Time').sum() 
df2.plot(kind='line', legend=True, ax=ax2, color='r',marker='o', fontsize=10)
ax2.set_title('E223 hourly room temperature')

#run tkinter
root.mainloop()