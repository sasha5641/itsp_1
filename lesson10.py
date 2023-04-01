import sqlite3

connection = sqlite3.connect('it_step_DB.sl3', 5)
cur = connection.cursor()

#cur.execute('CREATE TABLE first_table (name TEXT, surname TEXT, age INT);')
#cur.execute('INSERT INTO first_table (name, surname, age) VALUES ("Karina", "Shavshina", 14);')
cur.execute('SELECT name FROM first_table WHERE age < 55')  #rowid, * вибирає все можно подставить name
#cur.execute('SELECT name FROM first_table')
#cur.execute('SELECT surname FROM first_table WHERE name = "Evgen"')

connection.commit()
res = cur.fetchall() #Вигружає все що є в базі данних

for el in res:
    print(el)

connection.close()
