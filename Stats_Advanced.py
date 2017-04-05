__author__ = 'Jake'
#Grabs by game ID box score of games takes a while
import pandas
import nba_py
from nba_py.constants import CURRENT_SEASON
from nba_py import constants
from nba_py import game
print(constants.SeasonType.Regular)
print(CURRENT_SEASON)

'''
game_info()
game_summary()
inactive_players()
last_meeting()
line_score()
officials()
other_stats()
season_series()
'''
#last game of 2015 - 0021501229
#total games should be 2460
start_game_ID = 21600001
last_game_ID = 21601230 #feb 28

while(start_game_ID < last_game_ID+1):
    game_ID = '00' + str(start_game_ID)
    boxscore_summary = game.Boxscore(game_ID)
    team_stats = boxscore_summary.team_stats()
    boxscore_summary = game.BoxscoreSummary(game_ID)
    officials = boxscore_summary.officials()
    other_stats = boxscore_summary.other_stats()
    game_summary = boxscore_summary.game_summary()
    line_score = boxscore_summary.line_score()




    result = pandas.merge(team_stats, officials, left_index=True, right_index=True, how='outer')
    result = pandas.merge(result, other_stats, left_index=True, right_index=True, how='outer')
    result = pandas.merge(result, game_summary, left_index=True, right_index=True, how='outer')
    result = pandas.merge(result,line_score,left_index=True, right_index=True, how='outer')
    #away = result['TEAM_NAME'][0]
    #home = result['TEAM_NAME'][1]
    #date = result['GAME_DATE_EST'][0]
    #find = date.split('T')
    #date = find[0]
    #file_name = away + '@' + home+'-'+date+'.csv'
    #print(file_name)
    result.to_csv(r'C:\progData\NBA\2016\\' + str(start_game_ID)+'.csv')
    print(str(start_game_ID) + " added")
    start_game_ID = start_game_ID + 1

