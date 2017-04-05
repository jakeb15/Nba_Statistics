__author__ = 'Jake'

import pandas
import nba_py
from nba_py.constants import CURRENT_SEASON
from nba_py import constants
from nba_py import player
import csv


player = player.PlayerGeneralSplits("201566")
wins_loses = player.win_losses()
rest = player.days_rest()
print(rest['W'][0])

rest.to_csv(r'C:\progData\NBA\Test\\' + 'experimental.csv')