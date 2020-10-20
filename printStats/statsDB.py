import mysql.connector 
import pandas as pd
import time
#TODO:wailt for database creation since healthcheck didn't work and had to comment it
time.sleep(120)

mydb = mysql.connector.connect( 
  host = "db", 
  user = "root", 
  password = "example", 
  database = "futbolStats"
)  
print('-------------------------------------------------------------')
print('------- top ten mayores goleadas de argentina de local: -----')
print('-------------------------------------------------------------')
df = pd.read_sql('select m.date, t.name as local, m.homeScore, ta.name as visit, m.awayScore from futbolStats.match m inner join futbolStats.team t on m.homeTeamId = t.id inner join futbolStats.team ta on m.awayTeamId = ta.id where t.name = \'Argentina\' order by homeScore desc limit 10', mydb) 
pd.set_option('max_rows', None)
print(df)

print('-------------------------------------------------------')
print('-- ultimos diez encuentros entre Argentina y Brasil: --')
print('-------------------------------------------------------')
df = pd.read_sql('select * from (select m.date as matchDate, t.name as local, m.homeScore as hsc, ta.name as visit, m.awayScore as asco from futbolStats.match m inner join futbolStats.team t on m.homeTeamId = t.id inner join futbolStats.team ta on m.awayTeamId = ta.id where t.name = \'Argentina\' and ta.name = \'Brazil\' union select m.date as matchDate, t.name as local, m.homeScore as hsc, ta.name as visit, m.awayScore as asco from futbolStats.match m inner join futbolStats.team t on m.homeTeamId = t.id inner join futbolStats.team ta on m.awayTeamId = ta.id where ta.name = \'Argentina\' and t.name = \'Brazil\' ) a order by a.matchDate desc limit 10', mydb) 
print(df)


print('-----------------------------------------------------')
print('-- resumen de victorias de Argentina sobre Brasil: --')
print('-----------------------------------------------------')
df = pd.read_sql('select t.name as arg, \'local\' as condicion, count(distinct m.id) as victorias from futbolStats.match m inner join futbolStats.team t on m.homeTeamId = t.id inner join futbolStats.team ta on m.awayTeamId = ta.id where t.name = \'Argentina\' and ta.name = \'Brazil\' and m.homeScore > m.awayScore group by t.name  union select ta.name as arg, \'visitante\' as condicion, count(distinct m.id) as victorias from futbolStats.match m inner join futbolStats.team t on m.homeTeamId = t.id inner join futbolStats.team ta on m.awayTeamId = ta.id where ta.name = \'Argentina\' and t.name = \'Brazil\' and m.homeScore < m.awayScore group by t.name', mydb) 
print(df)

print('-----------------------------------------------------')
print('-- resumen de victorias de Brasil sobre Argentina: --')
print('-----------------------------------------------------')
df = pd.read_sql('select t.name as bra, \'local\' as condicion, count(distinct m.id) as victorias from futbolStats.match m inner join futbolStats.team t on m.homeTeamId = t.id  inner join futbolStats.team ta on m.awayTeamId = ta.id where ta.name = \'Argentina\' and t.name = \'Brazil\' and m.homeScore > m.awayScore group by t.name  union select ta.name as bra, \'visitante\' as condicion, count(distinct m.id) as victorias  from futbolStats.match m inner join futbolStats.team t on m.homeTeamId = t.id  inner join futbolStats.team ta on m.awayTeamId = ta.id  where t.name = \'Argentina\' and ta.name = \'Brazil\' and m.homeScore < m.awayScore group by t.name', mydb) 
print(df)

print('-------------------------------------------------------')
print('-- Como nos tiene de hijo Alemania en los mundiales: --')
print('-------------------------------------------------------')
df = pd.read_sql('select * from (select m.date as matchDate, t.name as localTeam, m.homeScore, ta.name as awayTeam, m.awayScore from futbolStats.match m inner join futbolStats.team t on m.homeTeamId = t.id inner join futbolStats.team ta on m.awayTeamId = ta.id inner join futbolStats.tournament tn on tn.id = m.tournamentId where t.name = \'Argentina\' and ta.name = \'Germany\' and tn.name = \'FIFA World Cup\'  union select m.date as matchDate, t.name as localTeam, m.homeScore, ta.name as awayTeam, m.awayScore from futbolStats.match m inner join futbolStats.team t on m.homeTeamId = t.id inner join futbolStats.team ta on m.awayTeamId = ta.id inner join futbolStats.tournament tn on tn.id  = m.tournamentId where ta.name = \'Argentina\' and t.name = \'Germany\' and tn.name = \'FIFA World Cup\') a order by a.matchDate desc', mydb) 

print(df)

mydb.close()
