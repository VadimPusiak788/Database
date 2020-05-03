CREATE OR REPLACE VIEW NBA_star as 
    select player.player_name
    , years.position
    , years.year
    , teams.team
    from player
    join years on years.player_name = player.player_name
    join teams on teams.player_name = player.player_name;