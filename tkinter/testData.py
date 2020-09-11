# https://datatofish.com/matplotlib-charts-tkinter-gui/
#from vscode terminal prompt >
#> python -m pip install pandas
#> python -m pip install matplotlib
#$sudo apt install python3-tk
import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

roomTempData = {'Room': ['E222','E223','E208','E219','E216'],
         'Temperature': [23.3,22.1,20.6,21.1,19.8]
}
dfRoomTemp = DataFrame(roomTempData,columns=['Room','Temperature'])


e223tempData = {'Time': ['19:00','19:20','19:30','19:40','19:50','20:00'],
         'Temperature': [23.3,22.1,20.6,21.1,19.8,25.5]
        }
dfE223Temp = DataFrame(e223tempData,columns=['Time','Temperature'])

root= tk.Tk() 
  
figure1 = plt.Figure(figsize=(6,5), dpi=100)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, root)
bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
dfRoomTemp = dfRoomTemp[['Room','Temperature']].groupby('Room').sum()   #required to label axes correctly
dfRoomTemp.plot(kind='bar', legend=True, ax=ax1)
ax1.set_title('Room temperature')

figure2 = plt.Figure(figsize=(5,4), dpi=100)
ax2 = figure2.add_subplot(111)
line2 = FigureCanvasTkAgg(figure2, root)
line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
dfE223Temp = dfE223Temp[['Time','Temperature']].groupby('Time').sum()   #required to label axes correctly
dfE223Temp.plot(kind='line', legend=True, ax=ax2, color='r',marker='o', fontsize=10)
ax2.set_title('E223 hourly room temperature')

root.mainloop()