DROP TABLE IF EXISTS competitions;
CREATE TABLE competitions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    content TEXT,
    sporttype TEXT NOT NULL,
    shoton DATE NOT NULL
);

DROP TABLE IF EXISTS scores;
CREATE TABLE scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    competitionid INT,
    score DOUBLE NOT NULL,
    serie1 DOUBLE NOT NULL,
    serie2 DOUBLE NOT NULL,
    serie3 DOUBLE NOT NULL,
    serie4 DOUBLE NOT NULL,
    CONSTRAINT fk_competitionid FOREIGN KEY(competitionid) REFERENCES competitions(id) ON DELETE SET NULL
);

DROP TABLE IF EXISTS shots;
CREATE TABLE shots (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    scoreid INT,
    shot1 DOUBLE,
    shot2 DOUBLE,
    shot3 DOUBLE,
    shot4 DOUBLE,
    shot5 DOUBLE,
    shot6 DOUBLE,
    shot7 DOUBLE,
    shot8 DOUBLE,
    shot9 DOUBLE,
    shot10 DOUBLE,
    shot11 DOUBLE,
    shot12 DOUBLE,
    shot13 DOUBLE,
    shot14 DOUBLE,
    shot15 DOUBLE,
    shot16 DOUBLE,
    shot17 DOUBLE,
    shot18 DOUBLE,
    shot19 DOUBLE,
    shot20 DOUBLE,
    shot21 DOUBLE,
    shot22 DOUBLE,
    shot23 DOUBLE,
    shot24 DOUBLE,
    shot25 DOUBLE,
    shot26 DOUBLE,
    shot27 DOUBLE,
    shot28 DOUBLE,
    shot29 DOUBLE,
    shot30 DOUBLE,
    shot31 DOUBLE,
    shot32 DOUBLE,
    shot33 DOUBLE,
    shot34 DOUBLE,
    shot35 DOUBLE,
    shot36 DOUBLE,
    shot37 DOUBLE,
    shot38 DOUBLE,
    shot39 DOUBLE,
    shot40 DOUBLE,
    CONSTRAINT fk_scoreid FOREIGN KEY(scoreid) REFERENCES scores(id) ON DELETE SET NULL
);