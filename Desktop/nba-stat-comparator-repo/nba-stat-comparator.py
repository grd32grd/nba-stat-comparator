#Imports
from nba_api.stats.library.parameters import NumberOfGames
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.patches import Circle, Rectangle, Arc, Polygon
import seaborn as sns
from matplotlib import cm
from PIL import Image
import requests
from io import BytesIO

#NBA stat database.
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats

#Makes sure that the entire dataframe is displayed.
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# def ppg(name,year,type):
#     player_dict = [player for player in players.get_players() if player['full_name'] == name][0]

#     #Multi-Dimensional Array that illustrates player's career stats.
#     career = playercareerstats.PlayerCareerStats(player_id=player_dict['id'])
#     career_array = np.array(career.get_data_frames()[0])

#     #Calculates the PPG by dividing total points by games played and returns the stat (returns 0 if player missed entire season)
#     for i in range(len(career_array)):
#         if (str(year) in career_array[i]):
#             return career_array[i][26]/career_array[i][6]
#     return 0

def career_ppg(name,year,type):
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

# def rpg(name,year,type):
#     player_dict = [player for player in players.get_players() if player['full_name'] == name][0]

#     #Multi-Dimensional Array that illustrates player's career stats.
#     career = playercareerstats.PlayerCareerStats(player_id=player_dict['id'])
#     career_array = np.array(career.get_data_frames()[0])

#     #Calculates the PPG by dividing total points by games played and returns the stat (returns 0 if player missed entire season)
#     for i in range(len(career_array)):
#         if (str(year) in career_array[i]):
#             return career_array[i][20]/career_array[i][6]
#     return 0

# def apg(name,year,type):
#     player_dict = [player for player in players.get_players() if player['full_name'] == name][0]

#     #Multi-Dimensional Array that illustrates player's career stats.
#     career = playercareerstats.PlayerCareerStats(player_id=player_dict['id'])
#     career_array = np.array(career.get_data_frames()[0])

#     #Calculates the PPG by dividing total points by games played and returns the stat (returns 0 if player missed entire season)
#     for i in range(len(career_array)):
#         if (str(year) in career_array[i]):
#             return career_array[i][21]/career_array[i][6]
#    return 0

# def player_codes(name,year,type):
#     player_dict = [player for player in players.get_players() if player['full_name'] == name][0]

#     #Multi-Dimensional Array that illustrates player's career stats.
#     career = playercareerstats.PlayerCareerStats(player_id=player_dict['id'])
#     career_array = np.array(career.get_data_frames()[0])

#     #Return player's code
#     return career_array[0][0]


def draw(graphic, n1, i1, t1, n2, i2, t2):
    if graphic is None:
        graphic = plt.figure()
        ax = graphic.add_subplot()
        graphic.subplots_adjust(top=0.85)
          
    # #Player 1
    # ax.text(0, 0.95, n1, transform=ax.transAxes, color='black', fontsize=12)
    # ax.text(0, 0.90, i1, transform=ax.transAxes, color='black', fontsize=9)
    # ax.text(0, 0.85, t1 + ' PPG: ' + "{:.2f}".format(ppg(n1,i1,t1)), transform=ax.transAxes, color='black', fontsize=9)
    # ax.text(0, 0.80, t1 + ' RPG: ' + "{:.2f}".format(rpg(n1,i1,t1)), transform=ax.transAxes, color='black', fontsize=9)
    # ax.text(0, 0.75, t1 + ' APG: ' + "{:.2f}".format(apg(n1,i1,t1)), transform=ax.transAxes, color='black', fontsize=9)

    # #Player 2
    # ax.text(1, 0.95, n2, transform=ax.transAxes, horizontalalignment='right', color='black', fontsize=12)
    # ax.text(1, 0.90, i2, transform=ax.transAxes, horizontalalignment='right', color='black', fontsize=9)
    # ax.text(1, 0.85, t2 + ' PPG: ' + "{:.2f}".format(ppg(n2,i2,t2)), horizontalalignment='right', transform=ax.transAxes, color='black', fontsize=9)
    # ax.text(1, 0.80, t2 + ' RPG: ' + "{:.2f}".format(rpg(n2,i2,t2)), horizontalalignment='right', transform=ax.transAxes, color='black', fontsize=9)
    # ax.text(1, 0.75, t2 + ' APG: ' + "{:.2f}".format(apg(n2,i2,t2)), horizontalalignment='right', transform=ax.transAxes, color='black', fontsize=9)
    
    # response1 = requests.get('https://ak-static.cms.nba.com/wp-content/uploads/headshots/nba/latest/260x190/' + str(player_codes(n1,i1,t1)) + '.png')
    # response2 = requests.get('https://ak-static.cms.nba.com/wp-content/uploads/headshots/nba/latest/260x190/' + str(player_codes(n2,i2,t2)) + '.png')
    # img1 = Image.open(BytesIO(response1.content))
    # img2 = Image.open(BytesIO(response2.content))
    
    plt.plot(career_ppg(n1,i1,t1)[0], career_ppg(n1,i1,t1)[1], color='red', marker='o')
    plt.plot(career_ppg(n2,i2,t2)[0], career_ppg(n2,i2,t2)[1], color='blue', marker='o')
    plt.title(n1 + " VS " + n2 + " PPG Per Season", fontsize=10)
    plt.xlabel('Year', fontsize=14)
    plt.xticks(rotation=45)
    plt.ylabel('Season PPG', fontsize=14)
    plt.grid(True)
    return graphic

if __name__ == "__main__":

    #Generates title.
    title = 'Test'

    #Asks user for the two players' general info.
    # player_name1 = input ("Enter player 1's full name: ")
    # season_id1 = input ("Input season in format (####-##): ")
    # season_type1 = input ("Regular Season (R) or Playoffs (P): ")
    # if season_type1 == 'R':
    #     season_type1 = 'Regular Season'
    # elif season_type1 == 'P':
    #     season_type1 = 'Playoffs'

    # player_name2 = input ("Enter player 2's full name: ")
    # season_id2 = input ("Input season in format (####-##): ")
    # season_type2 = input ("Regular Season (R) or Playoffs (P): ")
    # if season_type2 == 'R':
    #     season_type2 = 'Regular Season'
    # elif season_type2 == 'P':
    #     season_type2 = 'Playoffs'    
    
    #Default, for testing.
    #draw(None, player_name1, season_id1, season_type1, player_name2, season_id2, season_type2)  
    draw(None, 'Kevin Durant','2020-21','Regular Season','James Harden','2020-21','Regular Season')
    plt.show()
   