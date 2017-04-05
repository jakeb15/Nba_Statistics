__author__ = 'Jake'
#Grabs by game ID box score of games takes a while
import pandas
import nba_py
from nba_py.constants import CURRENT_SEASON
from nba_py import constants
from nba_py import game

start = 21200001
stop = 21201230
while(start < stop):
    game_id = "00" + str(start)
    boxscore = game.Boxscore(game_id)
    result = boxscore.player_stats()
    result.to_csv(r'C:\progData\NBA\test\\' + game_id + '.csv')
    print(game_id + " saved")
    start += 1