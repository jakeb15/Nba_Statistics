__author__ = 'Jake'
import os
import pandas
import csv

'''
list of functions
unique_list : found on internet - use to get rid of duplicate words in a string - Dont think i ended up using it
Possession - statistical function to return the possessions of a nba basetball team
Pace = statistical function to return pace - uses the possesion stat
Team_to_Game_ID - used to get all the game_ids for each team and put them in a csv file

'''




def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist

def Possession(team_FGA,team_FTA,team_ORB,opponents_DRB,team_FG,team_TOV,opponents_FGA,opponenets_FTA,opponenets_ORB,team_DRB,opponents_FG,opponenets_TOV):
    team_possesion  = .5 * ((team_FGA + .4 * team_FTA - 1.07 * (team_ORB / (team_ORB + opponents_DRB)) * (team_FGA - team_FG) + team_TOV) + (opponents_FGA + .4 * opponenets_FTA  - 1.07 * (opponenets_ORB / (opponenets_ORB + team_DRB)) * (opponents_FGA - opponents_FG) + opponenets_TOV))
    return team_possesion

def Pace(team_possession,opponents_possession,team_minutes_played):
    team_poss = 48 * ((team_possession + opponents_possession) / (2 * (team_minutes_played / 5)))
    return team_poss

#makes a csv of all game_Ids that a team is part of
def Team_to_Game_ID(team):
    game_ids = []
    start = 0
    file_list = os.listdir(r'C:\progData\NBA\All\\')
    dir_size = len(file_list)
    end = dir_size
    path = r'C:\progData\NBA\All\\'
    while(start < end):
        data = pandas.read_csv(path + file_list[start])
        if(team == data['TEAM_NAME'][0]):
            game = {'Game_ID' : int(data['GAME_ID_x'][0])}
            #print("game: " + str(game['Game_ID']))
            game_ids.append(game)
        elif(team == data['TEAM_NAME'][1]):
            game = {'Game_ID' : int(data['GAME_ID_x'][0])}
            #print("game: " + str(game['Game_ID']))
            game_ids.append(game)


        start +=1

    with open(r'C:\progData\NBA\NBA_GAME_IDS\\' + team + '.csv','w', newline='') as csvfile:
            fieldnames = ['Game_ID']
            a = csv.DictWriter(csvfile,fieldnames=fieldnames)
            a.writeheader()
            for item in game_ids:
                a.writerow(item)
            csvfile.close()
    print(team + " added to game_id folder")
    return game_ids

#reads in a csv into a file specifically for individual NBA teams
def open_team_games(team):
    game_ids= []
    with open(r'C:\progData\NBA\NBA_GAME_IDS\\'+ team+'.csv', 'r') as f:
            reader = csv.DictReader(f)
            for item in reader:
                game_ids.append(item)
            f.close()
    return game_ids

def get_game_ID_from_file_name(file_name):
    file_string =  find_between(file_name,'[',']')
    return file_string

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""


def get_stats():
    team = ["76ers","Bobcats","Bucks","Bulls","Cavaliers","Celtics","Clippers","Grizzlies",
            "Hawks","Heat","Hornets","Jazz","Kings","Knicks","Lakers","Magic","Mavericks",
            "Nets","Nuggets","Pacers","Pelicans","Pistons","Raptors","Rockets","Spurs","Suns"
            ,"Thunder","Timberwolves","Trail Blazers","Warriors","Wizards"]

    #------------working----------------------
    #this is all game ids from bobcats
    test = open_team_games('Bulls')

    #gets all the files in the ALL directory and puts them in list
    file_list = os.listdir(r'C:\progData\NBA\All\\')
    path = r'C:\progData\NBA\All\\'
    games = []

    for x in test:
        x['Game_ID'] = x['Game_ID'][:len(x['Game_ID'])-2]
        print(x['Game_ID'])

    for item in test:
        print(item['Game_ID'])
        for y in file_list:
            #print('team to game id :' + str(get_game_ID_from_file_name(y)))
            if(item['Game_ID'] == get_game_ID_from_file_name(y)):
                #open file and get info
                print("inside")
                data = pandas.read_csv(path + y)
                home = 0
                home_team = ''
                away_team = ''
                away = 0
                home_id = data['HOME_TEAM_ID'][0]
                if(home_id == data['TEAM_ID_x'][0]):
                    home = 0
                    away = 1
                else:
                    away = 0
                    home = 1
                game = {'Game_ID' : data['GAME_ID_x'][0],'Home_Team' : data['TEAM_NAME'][home],'Away_Team' : data['TEAM_NAME'][away], 'Home_FTA' : data['FTA'][home],'Away_FTA' : data['FTA'][away],'Home_PF' : data['PF'][home],'Away_PF': data["PF"][away],
                        'Ref_1' : data['FIRST_NAME'][0] + " " + data['LAST_NAME'][0],'Ref_2' : data['FIRST_NAME'][1] + " " + data['LAST_NAME'][1], 'Ref_3' : data['FIRST_NAME'][2] + " " + data['LAST_NAME'][2], 'PTS_Away' : data['PTS'][away],'PTS_Home' : data['PTS'][home],
                        'Tot_PTS' : int(data['PTS'][away]) +  int(data['PTS'][home]),'FG3_PCT_Away' : data['FG3_PCT'][away], 'FG3_PCT_Home': data['FG3_PCT'][home] }
                games.append(game)


    with open(r'C:\progData\NBA\Test\Bulls_3pt.csv','w',newline='') as csvfile:
                fieldnames = ['Game_ID','Home_Team','Away_Team','Home_FTA','Away_FTA','Home_PF','Away_PF','Ref_1','Ref_2','Ref_3','Tot_PTS','PTS_Home', 'PTS_Away','FG3_PCT_Away','FG3_PCT_Home']
                a = csv.DictWriter(csvfile,fieldnames=fieldnames)
                a.writeheader()
                for item in games:
                    a.writerow(item)
                csvfile.close()


#for item in file_list:
#    print(fuctions.get_game_ID_from_file_name(item))

#returns a list of dictionaries: each dictionary has 3 refs and the stats
def parse_Refs(file):
    ref = []
    return ref



#gets all back to back games
def get_Connected_games(team):
    #gets all the files in the ALL directory and puts them in list
    connected_games = []
    games = open_team_games(team)
    previous_game = ''
    b2b_ID = []
    reg_game = []
    previous_game_ID = ''
    next_game_ID = ''
    count = 1
    b2b_count = 0
    path = r'C:\progData\NBA\ALL_GAMES_BY_ID\\'
    for y in games:
        #gets all team games in
        data = pandas.read_csv(path + y['Game_ID']+ '.csv')
        print("current Game: " + str(int(data['GAME_ID_x'][0])))
        date = data['GAME_DATE_EST'][0]#2012-11-30T00:00:00
        date = separate_date(date)
        next_game_ID = data['GAME_ID_x'][0]
        next_date = date
        if(previous_game != ''):
            if(is_B2B(previous_game,next_date) == True):
                print('b2b_game :' + str(int(next_game_ID)))
                b2b_count +=1
                b2b_dic = {'Game_ID' : str(int(next_game_ID))}
                b2b_ID.append(b2b_dic)
            else:
                nonB2B_dic = {'Game_ID' : str(int(next_game_ID))}
                reg_game.append(nonB2B_dic)
        previous_game = next_date
        previous_game_ID = next_game_ID
        count +=1
    print("Game count : "+ str(count))
    print("b2b count : "  + str(b2b_count))
    with open(r'C:\progData\NBA\Test\B2B_Games.csv','w',newline='') as csvfile:
                fieldnames = ['Game_ID']
                a = csv.DictWriter(csvfile,fieldnames=fieldnames)
                a.writeheader()
                for item in b2b_ID:
                    a.writerow(item)
                csvfile.close()
    with open(r'C:\progData\NBA\Test\nonB2B.csv','w',newline='') as csvfile:
                fieldnames = ['Game_ID']
                a = csv.DictWriter(csvfile,fieldnames=fieldnames)
                a.writeheader()
                for item in reg_game:
                    a.writerow(item)
                csvfile.close()

    return connected_games


def rename_file_to_id_Number():
    start_game_ID = 0
    file_list = os.listdir(r'C:\progData\NBA\ALL_GAMES_BY_ID\\')
    dir_size = len(file_list)
    while(start_game_ID < dir_size):
        path = r'C:\progData\NBA\ALL_GAMES_BY_ID\\'
        original_file =  path + file_list[start_game_ID]
        data = pandas.read_csv(path + file_list[start_game_ID]) #read from NBA\ALL
        nba_id = str(int(data['GAME_ID_x'][0]))
        new_file = path + nba_id + '.csv'
        os.rename(original_file,new_file)
        start_game_ID +=1

def separate_date(date):
    date_list = []
    year = date[:4]
    month  = date[5:7]
    day = date[8:10]
    date_list.append(year)
    date_list.append(month)
    date_list.append(day)
    return date_list

def is_B2B(date,next_game):
    if(date[0] != next_game[0]):
        #print('years dont match')
        return False
    if(date[1] == '01' or date[1] == '03' or date[1] == '05' or date[1] == '07' or date[1] == '08' or date[1] == '10' or date[1] == '12'):
        #print("inside 31")
        if(date[2] == '31' and next_game[2] == '01'):
            return True
        if(str(next_game[2]) == str((int(date[2])+1))):
            return True
        else:
            return False
    elif(date[1] == '04' or date[1] == '06' or date[1] == '09' or date[1] == '10'):
        #print('inside 30')
        if(date[2] == '30' and next_game[2] == '01'):
            return True
        if(str(next_game[2]) == str(int(date[2])+1)):
            return True
        else:
            return False
    elif(date[1]=='02'): # fe
        #print('inside 28')
        if(date[2] == '28' and next_game[2]=='01'):
            return True
        if(str(next_game[2]) == str(int(date[2])+1)):
            return True
        else:
            return False
    else:
        #print('exited out end')
        return False

#changes date from 2008-10-28T00:00:00 -----> 10/28/2008 and strips off the time
def changeDate(date):
    find = date.split('T')
    print(find[0])
    find = find[0].split('-')
    #month/day/year
    date = find[1] + '/' + find[2]+ '/'+find[0]
    return date
