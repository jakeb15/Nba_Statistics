__author__ = 'Jake'
import os
import pandas
import fuctions

start_game_ID = 0
file_list = os.listdir(r'C:\progData\NBA\ALL_GAMES_BY_ID\\')
dir_size = len(file_list)
while(start_game_ID < dir_size):
    path = r'C:\progData\NBA\ALL_GAMES_BY_ID\\'
    original_file =  path + file_list[start_game_ID]
    print(original_file + '.....changing this games date')
    data = pandas.read_csv(path + file_list[start_game_ID])
    os.remove(path + file_list[start_game_ID])
    print("file deleted")
    #data['GAME_DATE_EST'][0] = fuctions.changeDate(data['GAME_DATE_EST'][0])
    data.loc[0,'GAME_DATE_EST'] = fuctions.changeDate(data['GAME_DATE_EST'][0])
    #rename column
    data = data.rename(columns={'GAME_ID_x': 'GAME_ID', 'TEAM_ID_x': 'TEAM_ID','TEAM_ABBREVIATION_x': 'TEAM_ABBREVIATION','TEAM_CITY_x': 'TEAM_CITY','GAME_DATE_EST' :'GAME_DATE'})
    #delete column in data frame
    data = data.drop('GAME_ID_y', 1)
    data = data.drop('TEAM_ID_y',1)
    data = data.drop('TEAM_ABBREVIATION_y',1)
    data = data.drop('TEAM_CITY_y',1)
    data.to_csv(path + file_list[start_game_ID],index =False,index_label=False)
    print("file changed")
    start_game_ID += 1


