from pprint import pprint

import sqlalchemy

dsn = 'postgresql://Anastasia:Anastasia@localhost:5432/task_3'
engine = sqlalchemy.create_engine(dsn)

connection = engine.connect()

pprint(connection.execute('''SELECT name, year FROM albums
WHERE year = 2018;
''').fetchall())

pprint(connection.execute('''SELECT name, lenght FROM tracks
ORDER BY lenght DESC;
''').fetchone())

pprint(connection.execute('''SELECT name FROM tracks
WHERE lenght >= 3.30;
''').fetchall())

pprint(connection.execute('''SELECT name FROM collections
WHERE year BETWEEN 2018 AND 2020;
''').fetchall())

pprint(connection.execute('''SELECT name FROM artists
WHERE name NOT LIKE '%% %%';
''').fetchall())

pprint(connection.execute('''SELECT name FROM tracks
WHERE name LIKE '%%My%%';
''').fetchall())