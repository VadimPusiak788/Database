
select positions, count(player_name) as count_pos
from player
GROUP BY positions
order by count_pos DESC;

select  round((count(player.player_name)/14) * 100, 2) as rate
    --,teams.team
    ,NVL(teams.team, 0) as teams
from player
RIGHT join teams 
on teams.player_name = player.player_name
GROUP by NVL(teams.team, 0)
order by teams DESC;

select count(player.player_name) as count_player
            , years.star_years as all_years
            from player
            INNER JOIN years
            on years.player_name = player.player_name
            
GROUP by years.star_years
ORDER by count_player DESC;  
            



