CREATE TABLE Player(
    Player_name VARCHAR(256) not Null,
    Positions VARCHAR(40) not NULL,
    Nationality VARCHAR(256) NOT NULL,
    HT VARCHAR(256) NOT NULL,
    WT NUMBER(4,2) NOT NULL,
    CONSTRAINT player_pk PRIMARY KEY (Player_name)
);
CREATE TABLE Years
(
    Player_name VARCHAR(256) NOT NULL,
    Star_years NUMBER(8) NOT NULL,
    CONSTRAINT year_pk FOREIGN KEY (Player_name) REFERENCES Player(Player_name)
);
CREATE TABLE Teams
(
    Player_name VARCHAR(256) NOT NULL,
    Team VARCHAR(256) NOT NULL,
    CONSTRAINT team_pk PRIMARY KEY (Team),
    CONSTRAINT games_team_pk FOREIGN KEY (Player_name) REFERENCES Player(Player_name)
);

CREATE TABLE Selection
(
    Team VARCHAR (256) NOT NULL,
    Selection_type VARCHAR(256) NOT NULL,
    Draw_status VARCHAR(256) NOT NULL,
    CONSTRAINT selection_pk FOREIGN KEY (Team) REFERENCES Teams(Team)
);

