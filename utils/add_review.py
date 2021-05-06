import sqlite3 

def add_review(name,date,feedback):
    connection = sqlite3.connect("models_and_pipelines/database/database.db")
    cur = connection.cursor()
    for i in range(len(name)):
        check_sql = "SELECT * FROM employee_review WHERE name=? and date=?;"
        cur.execute(check_sql,(name[i],date[i]))
        result = cur.fetchone()
        if result:
            continue 
        sql = "INSERT INTO employee_review VALUES(?,?,?)"
        cur.execute(sql,(name[i],date[i],feedback[i]))
    connection.commit()
    connection.close()

