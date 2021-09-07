#Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import cm

#NBA stat database.
from nba_api.stats.static import players
from nba_api.stats.endpoints import shotchartdetail
from nba_api.stats.endpoints import playercareerstats

#Makes sure that the entire dataframe is displayed.
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

def draw_court(graphic):
    if graphic is None:
        graphic = plt.gca()
        graphic = plt.gcf()

    
    return graphic

if __name__ == "__main__":

    #Generates title.
    title = 'Test'

    draw_court(None)
    plt.show()
   