__author__ = 'Jake'
import os
import pandas
import fuctions
import csv
import math
'''
Put all Files of a directory in a list
    - Create an Official Class
        - Games
        - PFs
        - Guys He officiated with
Put all Players in its own Directory with stats
    - Create a Player Class
        - Games
        - PF
        - Minutes
        - ability to draw Fouls
'''
officials = []
#puts all files in a list that are in a directory
file_list = os.listdir(r'C:\progData\NBA\All\\')
dir_size = len(file_list)
print(dir_size)
print(file_list[0])
#print("Directory size: " + str(dir_size)+ ' Games')
path = r'C:\progData\NBA\All\\'
# colum names to use "TEAM_NAME" "OFFICIAL_ID" "FIRST_NAME" "LAST_NAME" "PF"
data = pandas.read_csv(path + file_list[0])
#print(path+file_list[0])
PLUS_MINUS = 0
if(data["PLUS_MINUS"][0] > 0):
    PLUS_MINUS = 0
else:
    PLUS_MINUS = 1

home_PF = 0
away_PF = 0
home_FTA = 0
away_FTA = 0
if(data['HOME_TEAM_ID'][0] == data['TEAM_ID_x'][0]):
    home_PF =  data['PF'][0]
    home_FTA = data['FTA'][0]
    away_FTA = data['FTA'][1]
    away_PF = data['PF'][1]
else:
    home_PF =  data['PF'][1]
    home_FTA = data['FTA'][1]
    away_FTA = data['FTA'][0]
    away_PF = data['PF'][0]

ref = {'OFFICIAL_ID': data['OFFICIAL_ID'][0],'Name' : str(data['FIRST_NAME'][0]) + " " + str(data['LAST_NAME'][0]),'PF_AWAY' : away_PF,'PF_HOME': home_PF,'Games' : 1,"PLUS_MINUS" : data['PLUS_MINUS'][PLUS_MINUS],"FTA_AWAY" : away_FTA,"FTA_HOME":home_FTA}
officials.append(ref)
ref = {'OFFICIAL_ID': data['OFFICIAL_ID'][1],'Name' : str(data['FIRST_NAME'][1]) + " " + str(data['LAST_NAME'][1]),'PF_AWAY' : away_PF,'PF_HOME': home_PF,'Games' : 1,"PLUS_MINUS" : data['PLUS_MINUS'][PLUS_MINUS],"FTA_AWAY" : away_FTA,"FTA_HOME": home_FTA}
officials.append(ref)
ref = {'OFFICIAL_ID': data['OFFICIAL_ID'][2],'Name' : str(data['FIRST_NAME'][2]) + " " + str(data['LAST_NAME'][2]),'PF_AWAY' : away_PF,'PF_HOME': home_PF,'Games' : 1,"PLUS_MINUS" : data['PLUS_MINUS'][PLUS_MINUS],"FTA_AWAY" : away_FTA,"FTA_HOME": home_FTA}
officials.append(ref)


for item in officials:
    print(item['FTA_AWAY'])
    print(item['FTA_HOME'])


start = 1
end = dir_size
while(start < end):
    data = pandas.read_csv(path + file_list[start])
    print(path + file_list[start])
    #------------Check whatever stats here that might show up in a game---------------#
    f = open('Game_Log', 'a')
    '''
    if(int(data['FTA'][0]) > 50):
        f.write(path+file_list[start]+ '\n')
    if(int(data['FTA'][1]) > 50):
        f.write(path+file_list[start]+ "\n")
     '''
    #difference of fouls between 2 teams
    foul_diff = abs(int(data['PF'][0]) - int(data['PF'][1]))
    if(abs(int(data['PF'][0]) - int(data['PF'][1])) > 15 ):
        f.write(path+file_list[start]+" **" + str(foul_diff) + "**" +str(data['GAME_ID_x'][0])+"\n")
    '''
    if(data['FIRST_NAME'][0]=='Lauren'):
        f.write(path+file_list[start]+ "\n")
    if(data['FIRST_NAME'][1]=='Lauren'):
        f.write(path+file_list[start]+ "\n")
    if(data['FIRST_NAME'][2]=='Lauren'):
        f.write(path+file_list[start]+ "\n")
    '''
    f.close()
    #=================================================================================+#
    ref_num = 0
    PLUS_MINUS = 0
    if(data["PLUS_MINUS"][0] > 0):
        PLUS_MINUS = 0
    else:
        PLUS_MINUS = 1

    if(data['HOME_TEAM_ID'][0] == data['TEAM_ID_x'][0]):
        home_PF =  data['PF'][0]
        home_FTA = data['FTA'][0]
        away_FTA = data['FTA'][1]
        away_PF = data['PF'][1]
    else:
        home_PF =  data['PF'][1]
        home_FTA = data['FTA'][1]
        away_FTA = data['FTA'][0]
        away_PF = data['PF'][0]
    #ref_is_HERE = False
    #Friends = ''
    while(ref_num < 3):
        ref_is_HERE = False
        #print(data['OFFICIAL_ID'][0])
        for item in officials:
            if(str(item['OFFICIAL_ID']) == str(data['OFFICIAL_ID'][ref_num])):
                #print('Match - ref data updated')
                '''
                if(ref_num == 0):
                    Friends = str(data['OFFICIAL_ID'][1]) + " " + str(data['OFFICIAL_ID'][2]) + " "
                elif(ref_num == 1):
                    Friends = str(data['OFFICIAL_ID'][0]) + " " +  str(data['OFFICIAL_ID'][2])+ " "
                else:
                    Friends = str(data['OFFICIAL_ID'][0]) + " " + str(data['OFFICIAL_ID'][1])+ " "
                '''
                item['PF_AWAY'] += away_PF
                item["PF_HOME"] += home_PF
                item['PLUS_MINUS'] += data['PLUS_MINUS'][PLUS_MINUS]
                item['FTA_AWAY'] += away_FTA
                item['FTA_HOME'] += home_FTA
                item['Games'] += 1
                #item['FRIENDS'] += Friends
                item['PF/Games'] = 0
                item['PF_Away/Game'] = 0
                item['PF_Home/Game'] = 0
                item['AVG_PLUS_MINUS'] = 0
                item['AWAY/HOME_PF_RATIO'] = 0
                item['FTA_AWAY/GAME'] = 0
                item['FTA_HOME/GAME'] = 0
                ref_is_HERE = True
        if(ref_is_HERE == False):
            '''
            if(ref_num == 0):
                Friends = str(data['OFFICIAL_ID'][1]) + " " + str(data['OFFICIAL_ID'][2]) +  ' '
            elif(ref_num == 1):
                Friends = str(data['OFFICIAL_ID'][0]) + " " +  str(data['OFFICIAL_ID'][2])+ ' '
            else:
                Friends = str(data['OFFICIAL_ID'][0]) + " " + str(data['OFFICIAL_ID'][1]) + ' '
            '''
            ref = {'OFFICIAL_ID': data['OFFICIAL_ID'][ref_num],'Name' : str(data['FIRST_NAME'][ref_num]) + " " + str(data['LAST_NAME'][ref_num]),'PF_AWAY' : away_PF,'PF_HOME': home_PF,'Games' : 1, "PF_Away/Game" : 0, "PF_Home/Game" : 0, "PF/Games" : 0,"PLUS_MINUS" : data['PLUS_MINUS'][PLUS_MINUS],"AVG_PLUS_MINUS" : 0,'AWAY/HOME_PF_RATIO':0,"FTA_AWAY" : away_FTA,"FTA_HOME": home_FTA}
            officials.append(ref)
            #print("new ref added")
        ref_num +=1
        #print(data['PLUS_MINUS'][PLUS_MINUS])
    start += 1
print("-----------------Data_COMPLETE-----------------")
for x in officials:
    x['PF/Games'] = (float(x['PF_AWAY']) + float(x['PF_HOME']))/ float(x['Games'])
    x['PF_Away/Game'] = float(x['PF_AWAY']) / float(x['Games'])
    x['PF_Home/Game'] = float(x['PF_HOME']) / float(x['Games'])
    x['AVG_PLUS_MINUS'] = float(x['PLUS_MINUS']) / float(x['Games'])
    x['AWAY/HOME_PF_RATIO'] = float(x['PF_AWAY']) / float(x['PF_HOME'])
    x['FTA/GAME'] = (float(x['FTA_AWAY']) + float(x['FTA_HOME'])) / float(x['Games'])
    x['FTA_AWAY/GAME'] = float(x['FTA_AWAY']) / float(x['Games'])
    x['FTA_HOME/GAME'] = float(x['FTA_HOME']) / float(x['Games'])
    x['FTA_Difference_AWAY'] = float(x['FTA_AWAY']) - float(x['FTA_HOME'])
    x['FTA_Difference_HOME'] = float(x['FTA_HOME']) - float(x['FTA_AWAY'])
    x['FTA_Difference_ABSOLUTE'] = abs(float(x['FTA_HOME']) - float(x['FTA_AWAY']))

for i in officials:
    print(str(i['OFFICIAL_ID']) + " " + str(i['Name'])+ ' ' +  str(i['PF_HOME']) + ' ' + str(i["PF_AWAY"]) + ' ' + str(i['Games']))

with open(r'C:\progData\NBA\Referee.csv','w',newline='') as csvfile:
            fieldnames = ['OFFICIAL_ID','Name','PF/Games','PF_Away/Game','PF_Home/Game','AWAY/HOME_PF_RATIO','AVG_PLUS_MINUS','FTA_AWAY/GAME','FTA_HOME/GAME','FTA/GAME','PLUS_MINUS','PF_AWAY','PF_HOME','Games','FTA_HOME', 'FTA_AWAY','FTA_Difference_AWAY','FTA_Difference_HOME','FTA_Difference_ABSOLUTE']
            a = csv.DictWriter(csvfile,fieldnames=fieldnames)
            a.writeheader()
            for item in officials:
                a.writerow(item)
            csvfile.close()
