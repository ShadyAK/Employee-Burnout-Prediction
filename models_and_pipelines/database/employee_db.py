import sqlite3 
from datetime import datetime
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

review_table = """CREATE TABLE IF NOT EXISTS employee_review (  
name VARCHAR(20),
date timestamp,
review TEXT
);"""
cur.execute(review_table)
connection.commit()
def add_entries():
    review_entry = "INSERT INTO employee_review VALUES('Ashwin Kaurav',?,'Negative')"
    date1 = datetime.strptime('4/25/2021', '%m/%d/%Y')
    date2 = datetime.strptime('4/30/2021', '%m/%d/%Y')
    date3 = datetime.strptime('5/04/2021', '%m/%d/%Y')
    cur.execute(review_entry,(date1,))
    #cur.execute(review_entry,(date2,))
    #cur.execute(review_entry,(date3,))
    connection.commit()
add_entries()