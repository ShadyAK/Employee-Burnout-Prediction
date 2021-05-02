import sqlite3 

connection = sqlite3.connect("models_and_pipelines/database/database.db")
cur = connection.cursor()

sql_command = """CREATE TABLE IF NOT EXISTS employee_meetings (  
name VARCHAR(13),  
meeting_title VARCHAR(30),  
date timestamp,
meeting_start TEXT,
duration TEXT,
role VARCHAR(30));"""

cur.execute(sql_command)
connection.commit()

