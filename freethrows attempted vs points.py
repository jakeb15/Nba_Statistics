__author__ = 'Jake'
import fuctions
import os
import csv
import pandas


file_list = os.listdir(r'C:\progData\NBA\All\\')
path = r'C:\progData\NBA\All\\'
games = []

count =0
for y in file_list:
            #open file and get info
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
            tot_PTS = int(data['PTS'][home]) + int(data['PTS'][away])
            #tot_FTA = int(data['FGM'][home]) + int(data['FGM'][away])
            tot_FTA = int(data['LEAD_CHANGES'][0])
            game = {"tot_FTA" : tot_FTA, 'tot_PTS' : tot_PTS}
            games.append(game)
            count +=1
            print("game " + str(count))


with open(r'C:\progData\NBA\Test\lead_changes.csv','w',newline='') as csvfile:
            fieldnames = ['tot_FTA' , 'tot_PTS']
            a = csv.DictWriter(csvfile,fieldnames=fieldnames)
            a.writeheader()
            for item in games:
                a.writerow(item)
