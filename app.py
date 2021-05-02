from flask import Flask,render_template,request,redirect,url_for,session,flash,Response ,send_file,Response
import pandas as pd
from utils import preprocess_data,predict_,insert_attendance,attendance_hist
from datetime import date,datetime,timedelta
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from models_and_pipelines.gpt3.open_ai_model import return_feedback 
import random
import os
import io

app=Flask(__name__)
app.secret_key='asdkjfbaskdljfouaksdhfklsadhlfhsdlifhsk'

# Home Page
@app.route("/",methods=["POST","GET"])
def home():
    if request.method=="POST":
        csv = request.files['file']
        data = pd.read_csv(csv)
        user,user_data = preprocess_data.preprocess(data)
        burnout_predictions = predict_.predict_burnout(user_data)
        fatigue_predictions = predict_.predict_fatigue(user_data)
        today = datetime.now()
        today = today.strftime("%d_%m_%Y_%H_%M_%S")
        burnout = {'Name':user,'Burnout':burnout_predictions,'fatigue_predictions': fatigue_predictions}
    
        df = pd.DataFrame(burnout)
        name = today+'_burnout&fatigue.csv'
        df.to_csv('Reports\\burnout&fatigue\\'+name,index=False)
        return "Saved Report Successfully : {}".format(name)
        
    else:
        return render_template('base.html')

@app.route("/teams_insight",methods=["POST","GET"])
def teams_insight():
    if request.method=="POST":
        csv = request.files['file']
        csv.save('reports/attendence.csv')
        a = preprocess_data.preprocess_attendance('reports/attendence.csv')
        insert_attendance.insert_entry(a)
        return 'done'
    return render_template('attendance.html')

@app.route('/plot_attendance',methods=['POST'])
def plot_attendance():
    if request.method == "POST":
        #start_date = request.form['start_date']
        #end_date   = request.form['end_date']
        datetime.strptime('3/25/2021', '%m/%d/%Y')
        start_date =  datetime.strptime(request.form['start_date'], '%m/%d/%Y')
        end_date   =  request.form['end_date']
        if end_date=="To or None":
            end_date = None 
        else:
            end_date = datetime.strptime(end_date,'%m/%d/%Y')
        
        #end_date   = '04/29/2021'
        fig = attendance_hist.get_histogram(start_date,end_date)
        output = io.BytesIO()
        FigureCanvas(fig).print_png(output)
        return Response(output.getvalue(), mimetype='image/png')

@app.route('/manager_review',methods=['POST','GET'])
def review():
    if request.method=='POST':
        csv = pd.read_csv(request.files['file'])
        id_,review = preprocess_data.preprocess_reviews(csv)
        feedbacks = return_feedback(review)
        today = datetime.now()
        today = today.strftime("%d_%m_%Y_%H_%M_%S")
        df = pd.DataFrame({"Employee":id_[0],'Manager':id_[1],'Review':feedbacks})
        name = today+"Managers_review.csv"
        df.to_csv('Reports\\Manager Review\\'+name,index=False)
        negatives = [id_[0][index] for index in range(len(feedbacks)) if feedbacks[index]=='Negative']
        return 'File Saved in the review folder with name {} \n these emloyees need some attention {}'.format(name,negatives)
    return render_template('review.html')
if __name__=="__main__":
    app.run(debug=True)    