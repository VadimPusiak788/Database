DECLARE
    items_count int := 5;
BEGIN 
    for i in 1..items_count LOOP
    
        INSERT INTO player ( player_name, nationality, ht, wt)
            values ('player' || i, 'United States', '6-' || i, 200+i);
    end loop;
END;
    