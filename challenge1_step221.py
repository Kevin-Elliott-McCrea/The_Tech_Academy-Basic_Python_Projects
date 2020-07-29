import sqlite3

RosterValues = (('Jean-Baptiste Zorg', 'Human', 122), ('Korben Dallas', 'Meat Popsicle', 100), ('Ak\'not', 'Mangalore', -5))

with sqlite3.connect('challenge_database.db') as connection:
    c = connection.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS Roster(Name TEXT, Species TEXT, IQ INT)")
    c.executemany("INSERT INTO Roster VALUES(?, ?, ?)",
                  RosterValues)

c.execute('UPDATE Roster SET Species = "Human" WHERE Name = "Korben Dallas"')

c.execute('SELECT Name, IQ FROM Roster WHERE Species = "Human"')
while True:
    row = c.fetchone()
    if row is None:
        break
    print(row)
