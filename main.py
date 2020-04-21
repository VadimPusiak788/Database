import cx_Oracle

username = "myonlineedu"

password = "oracle123"

database = "localhost/xe"

connection = cx_Oracle.connect(username, password, database)

print("#1 Вивести позицію гравця та скільки гравців на ній грають. Гравець - число")
query1 = """select positions, count(player_name) as count_pos
from player
GROUP BY positions
order by count_pos DESC
"""

cursor1 = connection.cursor()

cursor1.execute(query1)
result1  = cursor1.fetchall()

for i in result1:
	print(i)


print("#1 Вивести команду у якій відсоток гравців які є зірками є найбільший відносно решти команд.")
query1 = """select  round((count(player.player_name)/14) * 100, 2) as rate
    ,NVL(teams.team, 0) as teams
from player
RIGHT join teams 
on teams.player_name = player.player_name
GROUP by NVL(teams.team, 0)
order by teams DESC
"""

cursor2 = connection.cursor()

cursor2.execute(query1)
result2  = cursor2.fetchall()

for i in result2:
	print(i)

print("#1 Вивести динаміку кількості баскетбольних зірок по роках")
query3 = """select count(player.player_name) as count_player
            , years.star_years as all_years
            from player
            INNER JOIN years
            on years.player_name = player.player_name
            
GROUP by years.star_years
ORDER by count_player DESC
"""

cursor3 = connection.cursor()

cursor3.execute(query3)
result3  = cursor3.fetchall()

for i in result3:
	print(i)