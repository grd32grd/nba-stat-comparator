#Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from PIL import Image
import requests
from io import BytesIO

import tkinter as tk
from tkinter import *

#NBA API
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats

#Makes sure that the entire dataframe is displayed.
pd.set_option('display.max_rows',500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

def career_ppg_data(name,year,type):
    player_dict = [player for player in players.get_players() if player['full_name'] == name][0]

    #Multi-Dimensional Array that illustrates player's career stats.
    career = playercareerstats.PlayerCareerStats(player_id=player_dict['id'])
    career_array = np.array(career.get_data_frames()[0])

    #X Axis Data
    years = []
    #Y Axis Data
    yearly_ppg = []

    for i in range(len(career_array)):
        if ((int(career_array[i][1][5:]) - int(career_array[i-1][1][5:])) > 1):
            years.append(career_array[i-1][1][5:]+'-'+career_array[i][1][2:4])
        years.append(career_array[i][1][2:])

    for i in range(len(career_array)):
        if ((int(career_array[i][1][5:]) - int(career_array[i-1][1][5:])) > 1):
            yearly_ppg.append(0)
        yearly_ppg.append(career_array[i][26]/career_array[i][6]) 

    return years, yearly_ppg     

def graph(graphic, n1, i1, t1, n2, i2, t2):
    if graphic is None:
        graphic = plt.figure()
        ax = graphic.add_subplot()
        graphic.subplots_adjust(top=0.85)
    
    plt.plot(career_ppg_data(n1,i1,t1)[0], career_ppg_data(n1,i1,t1)[1], color='red', marker='o')
    plt.plot(career_ppg_data(n2,i2,t2)[0], career_ppg_data(n2,i2,t2)[1], color='blue', marker='o')
    plt.title(n1 + " VS " + n2 + " PPG Per Season", fontsize=10)
    plt.xlabel('Season', fontsize=14)
    plt.xticks(rotation=45)
    plt.ylabel('Season PPG', fontsize=14)
    plt.grid(True)
    return graphic

if __name__ == "__main__":

    name1 = ""
    name2 = ""

    def calculate():
        name1 = e1.get()
        name2 = e2.get()
        e1.delete(0, tk.END)
        e2.delete(0, tk.END)
        return name1, name2

    master = tk.Tk()
    tk.Label(master, text="Player 1 Full Name:").grid(row=0)
    tk.Label(master, text="Player 2 Full Name:").grid(row=1)

    e1 = tk.Entry(master)
    e2 = tk.Entry(master)
    e1.insert(10, "")
    e2.insert(10, "")

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    tk.Button(master, text='Calculate Stats', command=calculate).grid(row=3, column=0, sticky=tk.W, pady=4)
  

    master.mainloop()

    title = 'Test'

    name1 = calculate()[0]
    name2 = calculate()[1]
    graph(None, name1, '2020-21', 'Regular Season', name2, '2020-21', 'Regular Season')
    plt.show()
   