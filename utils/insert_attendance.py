import sqlite3 

## Function to enter microsoft teams meeting attendance 
def insert_entry(arr):
    connection = sqlite3.connect("models_and_pipelines/database/database.db")
    cur = connection.cursor()
    for entry in arr:
        check_query = "SELECT * FROM employee_meetings WHERE (name=? AND meeting_start=?)"
        cur.execute(check_query,(entry['name'],entry['meeting_start']))
    
        if cur.fetchall():
            print('already fed',entry['meeting_start'])
            continue
        sql_query = """INSERT INTO employee_meetings VALUES(?,?,?,?,?,?)"""
        cur.execute(sql_query,(entry['name'],entry['meeting_title'],entry['date'],entry['meeting_start'],entry['time_attended'],entry['role']))
    connection.commit()
    connection.close()

    