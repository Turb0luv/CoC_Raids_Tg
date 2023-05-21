import pandas as pd
import clashAPI

def GetRaidsInfo():
    members = []

    Raids = clashAPI.getClashInfo('getRaidsData')
    Raids = Raids["items"]

    for Raid in Raids:
        parsed_dates = pd.to_datetime(Raid["startTime"]).date()
        startTime = parsed_dates.strftime('%d-%m-20%y')

        for Player in Raid["members"]:
            members.append([Player["name"], Player["tag"], Player["capitalResourcesLooted"]])

    return [startTime, members]

def GetRaidsTags(data):
    members = []
    for member in data:
        members.append(member[1])

    return members

def GetCurrentMembers():
    tags = []

    Members = clashAPI.getClashInfo('getClanMembers')
    Members = Members["items"]

    for member in Members:
        tags.append(member['tag'])

    return tags