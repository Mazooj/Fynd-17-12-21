from fastapi import FastAPI
import csv
from collections import Counter

app = FastAPI()

@app.get('/')
async def home_page():
    return {'Home':'Page'}


# List Battles
@app.get('/battles')
async def battles_page():
    battles = []
    with open('battles.csv','r') as file:
        data = csv.reader(file)
        for row in data:
            battles.append(row[0])
    return {'Battles': battles[1:]}


# Get Battle by ID
@app.get('/battle/{id}')
async def battles_page(id):
    local_dict = {}
    with open('battles.csv','r') as file:
        data = csv.reader(file)
        for rows in data:
            local_dict.update({rows[2]:rows[0]})
    return {'Battle':local_dict[id]}


# Count of battles per battle type
@app.get('/count_battles')
async def battles_page():
    battle_type_dict = {}
    with open('battles.csv', 'r') as file:
        data = csv.reader(file)

        list_of_battles = []
        battle_type = []
        for rows in data:
            list_of_battles.append(rows[0])
            battle_type.append(rows[14])
        battle_type.pop(0)
        count_dict = Counter(battle_type)

    return count_dict


# Most active attacker and defender kings in terms of battles they've fought
@app.get('/most_active_kings')
async def battles_page():
    with open('battles.csv', 'r') as file:
        data = csv.reader(file)
        attacker_kings = []
        defender_kings = []
        for rows in data:
            attacker_kings.append(rows[3])
            defender_kings.append(rows[4])
        attacker_kings.pop(0)
        defender_kings.pop(0)
        count_att = Counter(attacker_kings)
        count_def = Counter(defender_kings)
    return {'attacker kings': count_att,'defender kings':count_def}


# Min, Max, Average defender size
@app.get('/min_max_avg_defender_size')
async def battles_page():
    defender_size_list = []
    with open('battles.csv', 'r') as file:
        data = csv.reader(file)
        for rows in data:
            defender_size_list.append(rows[18])
        defender_size_list.pop(0)
        while "" in defender_size_list:
            defender_size_list.remove("")
        defender_size_list = list(map(int, defender_size_list))

    return {'Minimum defender size': min(defender_size_list),
            'Maximum defender size': max(defender_size_list),
            'Average defender size': sum(defender_size_list)/len(defender_size_list)}