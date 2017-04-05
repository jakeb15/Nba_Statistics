__author__ = 'Jake'
import os
import pandas

start_game_ID = 0
file_list = os.listdir(r'C:\progData\NBA\ALL_GAMES_BY_ID\\')
dir_size = len(file_list)
while(start_game_ID < dir_size):
    path = r'C:\progData\NBA\ALL_GAMES_BY_ID\\'
    original_file =  path + file_list[start_game_ID]
    data = pandas.read_csv(path + file_list[start_game_ID])
    team1_name = data['TEAM_NAME'][0]
    team1_id = data['TEAM_ID_x'][0]
    team2_name = data['TEAM_NAME'][1]
    team2_id = data['TEAM_ID_x'][1]
    home_team_id = data['HOME_TEAM_ID'][0]
    nba_id = str(int(data['GAME_ID_x'][0]))
    home= ''
    away = ''
    if(team1_id == home_team_id):
        home = team1_name
        away = team2_name
    else:
        away = team1_name
        home = team2_name
    date = data['GAME_DATE_EST'][0]
    find = date.split('T')
    date = find[0]

    file_name = away + '@' + home+'-'+date+'['+nba_id+'].csv'
    file_name = path + file_name
    print(original_file + " changed to  " + file_name )
    os.rename(original_file,file_name)
    start_game_ID = start_game_ID + 1