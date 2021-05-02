import numpy as np 
import pandas as pd 
from datetime import datetime
def preprocess(df):
    user_id = list(df['Employee ID'])
    df.drop(['Date of Joining','Employee ID'],axis=1,inplace=True)
    return user_id,pd.get_dummies(df)


def preprocess_reviews(df):
    employee_id = list(df['Employee ID'])
    manager_id  = list(df['Manager ID'])
    review      = list(df['Review'])
    print(employee_id,manager_id,review)
    return [employee_id,manager_id],review
def preprocess_attendance(csv):
    text = []
    with open(csv, "r") as my_input_file:
            for line in my_input_file:
                
                line = line.split(",", 2)
                string = " ".join(line)
                string = string.replace('\t',' ')

                if len(string)>0:
                    text.append(string.replace('  ', '   ')[1::2])
    text = text[1:]
    while True:
        try:
            text.remove('\n')
        except:
            break 
    while True:
        try:
            text.remove('')
        except:
            break 
    
    total_participants = int(text[0].split(' ')[4][:-1])
    meeting_title = text[1].split(' ')[2][:-1]
    meeting_date  = datetime.strptime(text[2].split(' ')[3], '%m/%d/%Y')
    ## Done until here
    users = [] 
    for i in range(5,len(text)):
        this = {}
        split = text[i].split(' ')
        start =  len(split)-12
        this['name'] = []
        curr = 0
        value = 1
        while value:
            try:
                value=0
                a = int(split[curr][0])
            except:
                value=1
                this['name'].append(split[curr])
                curr+=1
        this['name']=" ".join(this['name'])
        this['time_attended'] = ' '.join(split[curr+8:-2])
        this['meeting_start'] = " ".join(split[curr:curr+4]) 
        this['role'] = split[-1][:-1]
        this['meeting_title'] = meeting_title 
        this['date']   = meeting_date
        #print(this)
        users.append(this)
    return users
    #for element in text:

if __name__=='__main__':
    txt1=preprocess_attendance('models_and_pipelines\database\meetingAttendanceReport(General) (1).csv')
    #txt2=preprocess_attendance('models_and_pipelines\database\meetingAttendanceReport(General) (2).csv')
    #txt3=preprocess_attendance('models_and_pipelines\database\meetingAttendanceReport(General) (3).csv')
    print(txt1)