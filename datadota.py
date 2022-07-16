import pandas as pd
import json
from urllib.request import urlretrieve
import time
import random
import sqlite3 as sql
import requests



def listofplayers():
    url = 'https://api.opendota.com/api/proPlayers'
    r = requests.get(url)
    with open('JSON_DATA/pro_players_list.json', 'wb') as outfile:
        outfile.write(r.content)





def playersgames(players_list):
    for player in players_list:
        check = False
        while check == False:
            try:
                accaunt_id = str(player['account_id'])
                url = 'https://api.opendota.com/api/players/' + accaunt_id+ '/matches'
                r = requests.get(url)
                with open('JSON_DATA/'+ accaunt_id + '.json', 'wb') as outfile:
                    outfile.write(r.content)
                time.sleep(1)
                print('.', end=' ')
                check = True
            except: time.sleep(2)