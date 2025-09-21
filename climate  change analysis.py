import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import filedialog , messagebox
import os
# global variable to store dataset
climate_df = None
# load csv file
def load_csv():
    global climate_df
    file_path = filedialog.askopenfilename(filetype =[("CSV FILES","*.csv")])
    if file_path:
        try:
            climate_df = pd.read_csv(file_path, parse_dates=["year"])
            climate_df.sort_values('year',inplace = True)
            messagebox.showinfo("sucess",f"Loaded data from {os.path.basement(file_path)}")
        except Exception as e:
            messagebox.showerror("error",f"failed to load file:\n{e}")
# SHOW TEMEPRATURE TREND
def show_temperature_trend():
    if climate_df is None or'temperature' not in climate_df.columns:
        messagebox.showwarning("no data","load CSV file with 'temperature' column.")
        return
    plt.figure(figsize=(10 , 5))
    plt.plot(climate_df['year'],climate_df['temperature'], marker ='o',color = 'red',label="temperature(c)")
    plt.title("temperature trend  over time")
    plt.xlabel("year")
    plt.ylabel("tempersture (c)")
    plt.grid(True)
    plt.legend()
    plt.show()
# show CO2 trend
def show_CO2_trend():
    if climate_df is None or'CO2' not in climate_df.columns:
        messagebox.showwarning("no data","load CSV file with 'CO2' column.")
        return
    plt.figure(figsize=(10 , 5))
    plt.plot(climate_df['year'],climate_df['CO2'], marker ='o',color = 'red',label="CO2(ppm)")
    plt.title("C02 Concentration over time")
    plt.xlabel("year")
    plt.ylabel("C02 (ppm)")
    plt.grid(True)
    plt.legend()
    plt.show()
# Correlation between temperature and C02
def show_correlation():
    if climate_df is None or not all(col in climate_df.columns for col in ['Tempature','CO2']):
        messagebox.showwarning("no data","load a dataset with'temperature' and 'CO2' columns.")
        return
    correlation = np.corrcoef(climate_df['temperature'], color = 'green')

    plt.figure(figsize=(8 , 5))
    plt.scatter(climate_df['CO2'],climate_df['Temparature'],color = 'green')
    plt.title(f"Temperature vs CO2 (correlation : {correlation:.2f})")
    plt.ylabel("temperature")
    plt.xlabel("C02 (ppm)")
    plt.grid(True)
    plt.show()    
#rainfall trend    
def rainfall_trend():
    if climate_df is None or "rainfall" not in climate_df.columns:
        messagebox.showwarning("no data","please load  a data with 'rainfall' columns.")
        return
    plt.figure(figsize=(10 , 5))
    plt.plot(climate_df['year'],climate_df['rainfall'], marker ='o',color = 'blue',label="rainfall (mm)")
    plt.title("rainfall trend over time")
    plt.xlabel("year")
    plt.ylabel("rainfall (mm)")
    plt.grid(True)
    plt.legend()
    plt.show()
#create Tkinter GUI
root = Tk()
root.title("climate change impact analysis")
root.geometry("450x380")

Label(root, text = "climate change impact analysis",font=("Arial",14,"bold")).pack(pady=10)
Button(root, text = "load csv",command= load_csv, width=30,bg="lightblue").pack(pady=5)
Button(root, text = "show temperature trend",command=show_temperature_trend , width=30,bg="lightgreen").pack(pady=5)
Button(root, text = "show CO2 trend",command=show_CO2_trend , width=30,bg="orange").pack(pady=5)
Button(root, text = "temperature vs CO2 correlation",command= show_correlation, width=30,bg="pink").pack(pady=5)
Button(root, text = "show rainfall trend",command= rainfall_trend, width=30,bg="yellow").pack(pady=5)
Button(root, text = "exit",command= load_csv, width=30,bg="lightblue").pack(pady=10)

root.mainloop()
# load csv file

import pandas as pd
df = pd.read_csv("sooraj_data.csv")


































