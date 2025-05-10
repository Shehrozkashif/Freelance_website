from django.shortcuts import redirect, render
from django.contrib import messages
import mysql.connector as sql
from django.shortcuts import render, redirect
from django.contrib import messages


email = None
password = None
pk = None
# Create your views here.
def signup(request):
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="password123A$", database='freelance_table')
        cursor = m.cursor()

        fname = request.POST.get("fname", "")
        lname = request.POST.get("lname", "")
        gender = request.POST.get("gender", "")
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")
        user_type = request.POST.get("userType", "")

        c = "INSERT INTO users1 (firstname, lastname, gender, email, password, user_type) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(c, (fname, lname, gender, email, password, user_type))
        m.commit()
        messages.success(request, 'You are registered successfully!')


    return render(request, 'SignUp.html', {'messages': messages.get_messages(request)})

# creating for login page 
def login(request):
    global email, password, pk,user_id
    if request.method == 'POST':
        email = request.POST.get('username', '')  # Assuming your login form uses 'username' for email input
        password = request.POST.get('password', '')
        
        m = sql.connect(host="localhost", user="root", passwd="password123A$", database='freelance_table')
        cursor = m.cursor()
        
        # Adjust the query based on your table structure and fields
        query = "SELECT * FROM users1 WHERE email = %s AND password = %s"
        cursor.execute(query, (email, password))
        user = cursor.fetchone()

        if user:
           
            # Assuming the 'username' is at index 1 and 'password' is at index 2 in the tuple
            user_id = user[0]
            username = user[1]
            password = user[2]
            pk = user[0]
            u_type =user[6]
            
            if u_type =="freelancer":
                # Add a welcome message to the context
                welcome_message = f"Welcome, {username}!"

                # You can pass the welcome message to the template using the context dictionary
                return render(request, 'Freelancer_Dashboard.html', {'welcome_message': welcome_message})
            else:
                # Add a welcome message to the context
                welcome_message = f"Welcome, {username}!"

                # You can pass the welcome message to the template using the context dictionary
                return render(request, 'Client_Dashboard.html', {'welcome_message': welcome_message})

        else:
            # Authentication failed, you might want to display an error message
            return render(request, 'Login.html', {'error_message': 'Invalid credentials'})

    return render(request, 'Login.html')




# creating views of freelance dashbaord
def freelance_dashbaord(request):
    return render(request, 'Freelancer_Dashboard.html')

# Import the MySQL connector

# Creating views for the Client dashboard


def Client_dashboard(request):
    global jobtitle, jobd, jobr, budget, sdate, edate, userid
    
    if request.method == 'POST':
        # Assuming you have a session variable named 'user_id' that holds the user's ID
        user_id = request.session.get('userid')

        m =sql.connector.connect(host="localhost", user="root", passwd="password123A$", database='freelance_table')
        cursor = m.cursor()
        
        query = "SELECT * FROM clientjob,user1 WHERE clientjob.userid = user1.userid"
        cursor.execute(query, (user_id,))
        user_data = cursor.fetchall()
        user_id = request.session.get('userid')
        print(f"User ID from session: {user_id}")
        if user_data:
            jobtitle = user_data[0][1]
            jobd = user_data[0][2]
            jobr = user_data[0][3]
            budget = user_data[0][4]
            sdate = user_data[0][5]
            edate = user_data[0][7]
            userid = user_data[0][8]
            print(userid) 

            # Pass the retrieved data to the template context
            context = {
                'jobtitle': jobtitle,
                'jobd': jobd,
                'jobr': jobr,
                'budget': budget,
                'sdate': sdate,
                'edate': edate,
                'userid': userid,
            }

            return render(request, 'Client_Dashboard.html', context)

    # Return a response for the GET request when the form is not submitted
    return render(request, 'Client_Dashboard.html')



#creating viwes for home page 
def home_page(request):
    return render(request, 'Home.html')

def dashboard(request):
    return render(request,"Freelancer_Dashboard")




def post_job(request):
    global email, password, pk

    if email is not None and password is not None and request.method == 'GET':
        return render(request, "Post_Job.html")

    if request.method == 'POST':
        # Retrieve form data
        job_title = request.POST.get("jobTitle", "")
        job_description = request.POST.get("jobDescription", "")
        job_requirements = request.POST.get("jobRequirements", "")
        budget = request.POST.get("budget", "")
        start_date = request.POST.get("startDate", "")
        end_date = request.POST.get("endDate", "")
        
        connection = sql.connect(host="localhost", user="root", passwd="password123A$", database='freelance_table')
        cursor = connection.cursor()

        # Insert data into the MySQL table
        query = "INSERT INTO clientjob (job_title, job_description, job_requirements, budget, start_date, end_date, userid,jobstatus) " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"  # Replace 'some_column_name' with the actual column name

        # Assuming '1' is the value you want to insert into the 'some_column_name'
        cursor.execute(query, (job_title, job_description, job_requirements, budget, start_date, end_date, pk, 1))

        # Commit changes and close connection
        connection.commit()

        messages.success(request, 'Job posted successfully!')
        return render(request, 'Post_Job.html', {'messages': messages.get_messages(request)})

    # Return a response for the GET request
    return render(request, 'Post_Job.html')

def clientjob(request):
    # sql ->  datas = cursor.fetchall()
    datas = None
    return render(request, 'clientjob.html',{'datas':datas})    

def find_work(request):
    global pk
    # SELECT * FROM freelance_table.Job where client_id =pk;
    # search client pk
    return render(request, 'find_work.html')

def Freelancer_edit(request):
    return render(request, 'Freelancer_edit.html')


