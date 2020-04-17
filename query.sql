-- Запит №1 Вивести кількість гравців на кожній позиції
select positions, count(player_name) as count_pos
from player
GROUP BY positions
order by count_pos DESC;

-- Запити №2 Вивести команди у яких відсоток баскетбольних зірок більший ніж в решти
select  round((count(player.player_name)/14) * 100, 2) as rate
    --,teams.team
    ,NVL(teams.team, 0) as teams
from player
RIGHT join teams 
on teams.player_name = player.player_name
GROUP by NVL(teams.team, 0)
order by teams DESC;

-- Запит №3 Вивести динаміку кількості баскетбольних зірок по роках.
select count(player.player_name) as count_player
            , years.star_years as all_years
            from player
            INNER JOIN years
            on years.player_name = player.player_name
            
GROUP by years.star_years
ORDER by count_player DESC;  
            



