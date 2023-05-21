import gspread
import Parser
import time

gc = gspread.service_account(filename='googleKeys.json')
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1WXli0D45kkwCV1fq2zB3WSkuzT0XPiMrhYDrk-zypQA/')
sh1 = sh.get_worksheet(0)
sh2 = sh.get_worksheet(1)

def checkPlayers(sh):
    currentMembers = Parser.GetCurrentMembers()
    playersTags = sh.col_values(2)[2:]

    for member in playersTags:
        time.sleep(2)

        result = sh.find(member)

        if member in currentMembers: # эти в клане есть
            sh.format("A" + str(result.row) + ":" + "B" + str(result.row), {
                "backgroundColor":  {
                        'red': 0.42,
                        'green': 0.8,
                        'blue': 0.41
                }
            })
        else: # этих в клане нет
            sh.format("A" + str(result.row) + ":" + "B" + str(result.row), {
                 "backgroundColor": {
                    "red": 0.95,
                    "green": 0.3,
                    "blue": 0.3
                }
            })

def setPlayerNames(sh, data):
    playersTags = sh.col_values(2)

    i = 1
    for member in data:
        if member[1] not in playersTags:
            print(member[1])
            time.sleep(2)

            sh.update('B' + str(len(playersTags) + i), member[1])
            sh.update('A' + str(len(playersTags) + i), member[0])
            i = i + 1

def setResults(sh, data):
    setPlayerNames(sh, data[1])
    startTimeRaids = sh.row_values(1)

    column = len(startTimeRaids) + 1
    if data[0] not in startTimeRaids:
        sh.update_cell(1, column, data[0])
    else:
        column = sh.find(data[0]).col

    for member in data[1]:
        time.sleep(2)

        result = sh.find(member[1])
        sh.update_cell(result.row, column, member[2])

    checkPlayers(sh)

def setRaidResults():
    data = Parser.GetRaidsInfo()
    setResults(sh1, data)

def setWarResults():
    data = Parser.GetCurrentWar()
    setResults(sh2, data)
