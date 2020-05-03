import csv
import cx_Oracle

username = 'hr'
password = '11'
database = 'localhost/ORCL'


connection = cx_Oracle.connect(username, password, database)

cursor = connection.cursor()

players = []
teams = []
error = 1

with open('nba.csv', 'r') as file:
    csv_data = csv.DictReader(file)
    try:
        for row in csv_data:
            player = row['Player']
            national = row['Nationality']
            ht = row['HT']
            wt = int(row['WT'])
            year = int(row['Year'])
            pos = row['Pos']
            team = row['Team']
            if player not in players:

                players.append(player)
                insert_query1 = """insert into Player(player_name, nationality, HT, WT) VALUES( :player_name, :nationality, :HT, :WT)"""
                cursor.execute(insert_query1, player_name=player, nationality=national, HT=ht, WT=wt)

                insert_query2 = "insert into Years(player_name, year, position) VALUES( :player_name, :year, :position)"
                cursor.execute(insert_query2, player_name=player, year=year, position=pos)

            if team not in teams:
                teams.append(team)
                print(teams)
                for name in players:
                    insert_query3 = """insert into Teams(player_name, team) values( :player_name, :team)"""
                    cursor.execute(insert_query3, player_name=name, team=team)
            error += 1
    except:
        print(f"ERROR on the line {error}")

connection.commit()
cursor.close()
connection.close()