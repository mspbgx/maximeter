import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()
# Test Data
cur.execute("INSERT INTO competitions (title, content, sporttype, shoton) VALUES (?, ?, ?, ?)",
            ('First competition', 'Content for the first note', 'training', '2021-08-19')
            )

cur.execute("INSERT INTO scores (competitionid, score, serie1, serie2, serie3, serie4) VALUES (?, ?, ?, ?, ?, ?)",
            (1, 394, 97, 98, 99 , 100)
            )

cur.execute("INSERT INTO shots (scoreid, shot1, shot2, shot3, shot4, shot5, shot6, shot7, shot8, shot9, shot10, shot11, shot12, shot13, shot14, shot15, shot16, shot17, shot18, shot19, shot20, shot21, shot22, shot23, shot24, shot25, shot26, shot27, shot28, shot29, shot30, shot31, shot32, shot33, shot34, shot35, shot36, shot37, shot38, shot39, shot40) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40)
            )
# Real Data
cur.execute("INSERT INTO competitions (title, content, sporttype, shoton) VALUES (?, ?, ?, ?)",
            ('Dez 2019', 'no content', 'training', '2019-12-03')
            )

cur.execute("INSERT INTO scores (competitionid, score, serie1, serie2, serie3, serie4) VALUES (?, ?, ?, ?, ?, ?)",
            (2, 367, 99, 85, 89 , 94)
            )

cur.execute("INSERT INTO shots (scoreid, shot1, shot2, shot3, shot4, shot5, shot6, shot7, shot8, shot9, shot10, shot11, shot12, shot13, shot14, shot15, shot16, shot17, shot18, shot19, shot20, shot21, shot22, shot23, shot24, shot25, shot26, shot27, shot28, shot29, shot30, shot31, shot32, shot33, shot34, shot35, shot36, shot37, shot38, shot39, shot40) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (2, 10.1, 10.1, 10.1, 10.1, 10.4, 10.3, 10.7, 10.2, 9.1, 10.6, 7.6, 10, 10.3, 7.6, 9.3, 9.9, 9.3, 7.5, 9.9, 8.4, 10.2, 9.4, 9.2, 9.6, 9.8, 9.9, 7, 8.3, 10.4, 9.1, 10.5, 8.9, 9.7, 8.4, 10.6, 10, 10, 9.3, 10.2, 10)
            )

connection.commit()
connection.close()