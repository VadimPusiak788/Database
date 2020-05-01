CREATE TABLE Player(
    player_name VARCHAR(256) NOT NULL
    , Nationality VARCHAR(256) NOT NULL
    , HT VARCHAR(256) NOT NULL
    , WT NUMBER(4,0) NOT NULL
    , CONSTRAINT player_pk PRIMARY KEY (player_name)
);
CREATE TABLE Years
(
    player_name VARCHAR(256) NOT NULL
    ,year NUMBER(4,0) NOT NULL
    , position VARCHAR(100) NOT NULL
    , CONSTRAINT year_player_fk PRIMARY KEY (player_name)
    ,CONSTRAINT year_pk FOREIGN KEY (Player_name) REFERENCES Player(Player_name)
);
CREATE TABLE Teams
(
    player_name VARCHAR(256) NOT NULL,
    team VARCHAR(256) NOT NULL,
    CONSTRAINT team_pk PRIMARY KEY (team),
    CONSTRAINT games_team_pk FOREIGN KEY (player_name) REFERENCES Years(Player_name)
);
CREATE TABLE nba_status(
    nba_status VARCHAR(100) NOT NULL
    , CONSTRAINT nba_fk PRIMARY KEY (nba_status)
);

CREATE TABLE sel_type(
    selection_type VARCHAR(100) NOT NULL
    , CONSTRAINT type_fk PRIMARY KEY (selection_type)
);    


CREATE TABLE about_team
(
    team VARCHAR (256) NOT NULL
    , selection_type VARCHAR(256) NOT NULL
    , nba_status VARCHAR(256) NOT NULL
    ,CONSTRAINT about_all PRIMARY KEY (team, selection_type, nba_status)
    , CONSTRAINT teams_fk FOREIGN KEY (team) REFERENCES Teams(team)
    , CONSTRAINT selteam_fk FOREIGN KEY (selection_type) REFERENCES sel_type(selection_type)
    , CONSTRAINT nbateam_fk FOREIGN KEY (nba_status) REFERENCES nba_status(nba_status)
);