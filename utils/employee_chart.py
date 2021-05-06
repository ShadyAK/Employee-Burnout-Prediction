import sqlite3 
from .attendance_hist import change_time
from datetime import datetime 
from matplotlib.figure import Figure
def get_user_teamtime(username):
    # Mean population time (user to be checked upon not included)
    connection = sqlite3.connect('models_and_pipelines\database\database.db')
    cur = connection.cursor()

    attendance_mean = 'SELECT duration FROM employee_meetings WHERE name<>? AND DATE'
    cur.execute(attendance_mean,(username,))
    time = cur.fetchall()
    mean_time = 0 
    for element in time:
        mean_time+=change_time(element[0])
    mean_time  = mean_time//len(time)
    ## User Time
    user_time = 'SELECT duration FROM employee_meetings WHERE name=?' 
    cur.execute(user_time,(username,))
    time = cur.fetchall()
    user_time = 0
    if time:
        for element in time:
            user_time+=change_time(element[0])
        user_time = user_time//len(time)

    return mean_time,user_time

def get_employee_review(username):
    connection = sqlite3.connect('models_and_pipelines\database\database.db')
    cur = connection.cursor()

    sql = 'SELECT date,review FROM employee_review WHERE name=? ORDER BY date'
    cur.execute(sql,(username,))
    result = cur.fetchall()
    if not result:
        return [1],["No Review Yet"]
    date,review = [],[]
    for element in result:
        date.append(element[0])
        if element[1]=='Positive':
            review.append(1)
        else:
            review.append(0)
    return date,review

def get_chart(username):
    mean_time , user_time = get_user_teamtime(username)
    date , review = get_employee_review(username)
    fig = Figure()
    axis = fig.add_subplot(2, 1, 1)
    axis.bar(['team_avg',username],[mean_time,user_time])
    axis.set_ylabel('Minutes',fontweight ='bold')
    for tick in axis.get_xticklabels():
        tick.set_rotation(-45)
    axis = fig.add_subplot(2, 1, 2)
    axis.bar(date,review)
    axis.set_ylabel('Review',fontweight ='bold')
    for tick in axis.get_xticklabels():
        tick.set_rotation(-15)
    fig.tight_layout()
    return fig
    #plt.bar(frequency.keys(),frequency.values())

if __name__ == '__main__': 
    #get_user_chart('random')
    get_chart('ashwinkaurav07')