# Employee-Burnout-Prediction
A project focused on the mental fatigue and burnout of the employee.

###  Installation Process. 
  1. Clone the repository.
  2. Use Python 3.9.5 
  3. Install the requirements.txt (pip -m install -r requirements.txt)
  4. Change your current working directory to the project folder.
  5. Run app.py.  

### Note : 
  1. Do not make any changes in the attendance file from the Microsoft Teams Apps.
  2. Fatigue and Burnout score data is assumed to not have "Fatigue" as a feature and is treated as a **Target Label**. 
  3. If during installation of requirements.txt 'can not import model named "wheel"' error occurs , install wheel first with pip -m install wheel
  
## **Description of functionalities**
  
### 1. Get Report on Burnout:
  This tab lets you get the fatigue and burnout score of your employees.   
  **Data used** - https://www.kaggle.com/redwankarimsony/hackerearth-employee-burnout-challenge   
  **Assumptions** - Fatigue score is treated as labeled target whereas it is a feature in the dataset.    
  **Preprocessing** - Remove the fatigue score column while giving input to the application.   
  
  ![alt text](https://github.com/ShadyAK/Employee_wellbeing/blob/main/static/images/report_tab.png "Logo Title Text 1")
  
  Upload your file in this tab and the processed report would be saved in *Reports* folder.
 
### 2. Team Meetings:
  **Add Attendance**  
  This tab lets you add the attendance of the teams meeting without manually doing it.  
  **Plot Attendance**  
  Also provides the feature where you can get the attendance chart between two dates.  
  
  **Database location** - models_and_pipelines/database 
  **Data Columns** - Name,Meeting Title,Date,Meeting_start_time,duration_attended,role
  
  ![alt text](https://github.com/ShadyAK/Employee_wellbeing/blob/main/static/images/teams_attendance_tab.png)  
  <br/>
  ![alt text](https://github.com/ShadyAK/Employee_wellbeing/blob/main/static/images/teams_time.png)
  
  ### 3. Manager Review 
   Here you can change the review of a Manager/collegue into classes Positive/Negative/Neutral
   Upload file with the same features as the file named **manager_reviews** in *Example Input Files* folder.  
   Result is saved in the *Reports* folder and in the database table employee_review.      
   ![alt text](https://github.com/ShadyAK/Employee_wellbeing/blob/main/static/images/manager_feedback_tab.png)  
 
 ### 4. Get User Report 
   This tab lets you get the report of an employee.  
   Shows chart of attendance of previous 2 weeks compared to others and past recent manager reviews. 
   
   ![alt text](https://github.com/ShadyAK/Employee_wellbeing/blob/main/static/images/employee_report_tab.png) 
   
   For employee named **Ashwin Kaurav**  
   ![alt text](https://github.com/ShadyAK/Employee_wellbeing/blob/main/static/images/userreport.png)  
   
### Extras:
   For extra insights the user can use the database and get the details according the requirements using SQL queries. 
    
    
    
    
