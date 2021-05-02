import sqlite3 
import matplotlib.pyplot as plt 
from collections import defaultdict
from matplotlib.figure import Figure
from datetime import datetime

def change_time(string): #Changes time in X hours Y mins Z seconds to mins.
    time = string.split(' ')
    if len(time)==3:
        time =  int(time[0][:-1])*60+int(time[1][:-1])+int(time[2][:-1])/60 
        return round(time,1)
    if len(time)==2:
        time =   int(time[0][:-1])+int(time[1][:-1])/60  
        return round(time,1)
    time = int(time[0][:-1])/60
    return round(time,1)

def get_histogram(date_start,date_end = None): #returns bar plot for the total teams meeting time in a user defined range of Date 
    connection = sqlite3.connect('models_and_pipelines/database/database.db')
    cur = connection.cursor()
    if date_end is None:
        sql = 'SELECT name , duration FROM employee_meetings WHERE date>=?'
        cur.execute(sql,(date_start,))
        result = cur.fetchall()
    else:
        sql = 'SELECT name , duration FROM employee_meetings WHERE date>=? AND date<=?'
        cur.execute(sql,(date_start,date_end))
        result = cur.fetchall()
    if result:
        frequency = defaultdict(lambda : 0)
        for element in result:
            frequency[element[0]] += change_time(element[1])
        
        fig = Figure()
        axis = fig.add_subplot(1, 1, 1)
        axis.bar(frequency.keys(),frequency.values())
        axis.set_xlabel('Username', 
               fontweight ='bold')
        axis.set_ylabel('Minutes',fontweight ='bold')
        for tick in axis.get_xticklabels():
            tick.set_rotation(-45)
        #plt.bar(frequency.keys(),frequency.values())
        fig.tight_layout()
        return fig

## Testing code
if __name__ == '__main__':
    #get_histogram('4/25/2021','23/26/2021')
    #print('12/29/2021'>'4/28/2021')
    datetime_object = datetime.strptime('4/25/2021', '%m/%d/%Y')
    datetime_object2 = datetime.strptime('5/25/2021', '%m/%d/%Y')

    plot = get_histogram(datetime.strptime('3/25/2021', '%m/%d/%Y'))