from datetime import *; 
from dateutil.parser import *
import sys
import mysql.connector 
import time
#TODO:wailt for database creation since healthcheck didn't work and had to comment it
time.sleep(60)

def addItems(itemList, tableName, mycursor) :
    for item in itemList :
        sql = f"INSERT INTO {tableName} (name, id) VALUES (%s, %s)"
        val = (item, itemList.index(item) + 1)
        mycursor.execute(sql, val)

countryList = []
tournamentList = []
teamList = []
matchInserts = []
#first iterate all to create satellite tables
with open(sys.argv[1], 'r') as inputFile :
    for l in inputFile.readlines() :
        cols = l.split(",")
          #date,home_team,away_team,home_score,away_score,tournament,city,country,neutral
        date = cols[0]
        country = cols[7]
        # wont migrate cities city = row[6] IS VERY DIFFICULT!!! (vago mode ON)
        tournament = cols[5]
        homeTeam = cols[1]
        awayTeam = cols[2]
        homeScore = cols[3]
        awayScore = cols[4]

        if  country not in countryList :
          countryList.append(country)
        country = countryList.index(country) +1

        if tournament not in tournamentList :
          tournamentList.append(tournament)
        tournament = tournamentList.index(tournament) +1

        if homeTeam not in teamList :
          teamList.append(homeTeam)
        homeTeam = teamList.index(homeTeam) + 1

        if awayTeam not in teamList :
          teamList.append(awayTeam)
        awayTeam = teamList.index(awayTeam) +1

        matchInserts.append(f'INSERT INTO futbolStats.match (date, homeTeamId, awayTeamId, homeScore, awayScore, tournamentId, countryId) values (\'{date}\', {homeTeam},  {awayTeam}, {homeScore}, {awayScore}, {tournament}, {country})')
        
    print(teamList)
    print(tournamentList)
inputFile.close()
mydb = mysql.connector.connect( 
  host = "db", 
  user = "root", 
  password = "example", 
  database = "futbolStats"
)  
mycursor = mydb.cursor() 

addItems(teamList, "team", mycursor)
addItems(countryList, "country", mycursor)
addItems(tournamentList, "tournament", mycursor)

for query in matchInserts :
    mycursor.execute(query)

mydb.commit() 
mydb.close()

