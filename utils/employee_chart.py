import sqlite3 
from .attendance_hist import change_time
import datetime 
from matplotlib.figure import Figure
def get_user_teamtime(username):
    # Mean population time (user to be checked upon not included)
    today = datetime.date.today()
    days = datetime.timedelta(28)
    start_date = today-days
    connection = sqlite3.connect('models_and_pipelines\database\database.db')
    cur = connection.cursor()
    other_employee =' SELECT COUNT(*) FROM (SELECT DISTINCT name FROM employee_meetings) WHERE name<>?;'
    cur.execute(other_employee,(username,))
    total_num = cur.fetchone()[0]
    attendance_mean = 'SELECT duration FROM employee_meetings WHERE name<>? AND date>?'
    cur.execute(attendance_mean,(username,start_date))
    time = cur.fetchall()
    mean_time = 0 
    for element in time:
        mean_time+=change_time(element[0])
    mean_time  = mean_time//total_num
    ## User Time
    user_time = 'SELECT duration FROM employee_meetings WHERE name=? AND date>?' 
    cur.execute(user_time,(username,start_date))
    time = cur.fetchall()
    user_time = 0
    if time:
        for element in time:
            user_time+=change_time(element[0])

    return mean_time,user_time

def get_employee_review(username):
    connection = sqlite3.connect('models_and_pipelines\database\database.db')
    cur = connection.cursor()

    sql = 'SELECT date,review FROM employee_review WHERE name=? ORDER BY date'
    cur.execute(sql,(username,))
    result = cur.fetchall()
    if not result:
        return [1],["No Review Yet"]
    date,review = [],[[],[]]

    for element in result:
        date.append(str(element[0])[:-8])
        review[0].append(1)
        if element[1]=='Positive':
            review[1].append('green')
        elif element[1]=='Neutral':
            review[1].append('yellow')
        else:
            review[1].append('red')
    return date,review

def get_chart(username):
    mean_time , user_time = get_user_teamtime(username)
    date , review = get_employee_review(username)
    fig = Figure()
    axis = fig.add_subplot(2, 1, 1)
    axis.bar(['team_avg',username],[mean_time,user_time],color=['purple','green'])
    axis.set_ylabel('Minutes',fontweight ='bold')
    axis = fig.add_subplot(2, 1, 2)
    axis.bar(date,review[0],color=review[1])
    axis.set_ylabel('Review',fontweight ='bold')
    axis.set_yticklabels([0,None,None,None,None,1])
    for tick in axis.get_xticklabels():
        tick.set_rotation(-15)
    fig.tight_layout()
    return fig
    #plt.bar(frequency.keys(),frequency.values())

if __name__ == '__main__': 
    #get_user_chart('random')
    get_chart('ashwinkaurav07')