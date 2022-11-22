import sqlite3


connection = sqlite3.connect("netflix.db")
cursor = connection.cursor()
sqlite_query = """
                    SELECT title
                    FROM netflix
                    WHERE release_year >= 2022
                """

cursor.execute(sqlite_query)
cursor.fetchall()

connection.close()

result = 

print(result)