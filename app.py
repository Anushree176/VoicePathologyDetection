from unittest import result
from flask import *
import sys
import os
import sqlite3
from sqlite3 import Error
from detection import detect, compare

# def Onchange(self):
#     self.password = document.querySelector('input[name= reg_pass]'); 
#     self.confirm =   document.querySelector('input[name= reg_conpass]');
#     if (reg_conpass.value == reg_pass.value):
#         confirm.setCustomValidity('')
#     else:
#         confirm.setCustomValidity('Passwords do not match')
  

def sql_connection():
    try:
        conn = sqlite3.connect('database.db')
        print("Open database successfully..")
        
        return conn 
    
    except Error:
        print(Error)

def sql_table(conn):
    #conn = conn.cursor()
    conn.execute('''CREATE TABLE users (
            Userid INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT Not Null,
            Phone TEXT Not Null Unique,
            Email TEXT Not Null Unique,
            Password TEXT Not Null
            )''')
    conn.commit()
    print("Table created sucessfully..")


# conn = sql_connection()
# #sql_table(conn)
# cursor = conn.cursor()


# BASE_DIR = os.getcwd()
# STATIC_DIR = os.path.abspath('templates')
# TEMPLATE_DIR = os.path.abspath('static')
# print(STATIC_DIR, TEMPLATE_DIR)
curr_dir = os.getcwd()
static_folder = os.path.join(curr_dir, "static")
upload_folder= os.path.join(static_folder, 'uploads')
upload_extentions = {'wav'}
app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = "mynameisruchi"
app.config['UPLOAD_FOLDER'] = upload_folder
# app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def hello():
    return "Hello goorm!"

@app.route("/about")
def about_us():
    return render_template('about_us.html')

@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/more_info")
def more_info():
    return render_template('more_info.html')

@app.route("/info")
def info():
    return render_template('info.html')

@app.route("/insertion" , methods = ['POST', 'GET'])
def insertion():
    if request.method == 'POST':
        try:
            conn = sql_connection()
        # sql_table(conn)
            cursor = conn.cursor()

            name = request.form['reg_name']
            contact = request.form['reg_contact']
            email = request.form['reg_email']
            password = request.form['reg_pass']
            print(name,email)
            print(cursor)
            cursor.execute("INSERT INTO users (Name, Phone, Email, Password) VALUES(?,?,?,?)" ,(name, contact, email, password) )
            conn.commit()
            print("Record successfully added")
            
        except:
            conn.rollback()
            print("error in insert operation")
            
        finally:
             return render_template("output.html")
             conn.close()

@app.route("/contact")
def contact_us():
    return render_template('contact_us.html')


@app.route("/login", methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        conn = sql_connection()
        cursor = conn.cursor()
        login_email = request.form.get('useremail')
        login_pass = request.form.get('password')
        exist = cursor.execute("select email from users where email = ?", (login_email,)).fetchone()
        if exist is None:
            print("Doesn't exist")
            return render_template('home.html')
        else:
            print("Yep exists")
            name = cursor.execute("select name from users where email = ?", (login_email,)).fetchone()
            session["name"] = name[0]
            return render_template('login_page1.html')
    return render_template('home.html')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == "wav"

@app.route("/detector_upload", methods=["POST"])
def detector_upload():
    print(request.files)
    if 'formFile' not in request.files:
        # flash('No file part')
        return render_template('loginpage2.html')
    file = request.files['formFile']
    print(file)
    if file.filename.strip() == "":
        return redirect(request.url)
    if file and allowed_file(file.filename):
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        results = detect(file.filename)
        conf = results[0]
        if results[1] == 'Normal':
            conf = 1 - conf
        res_string = f"Your audio sample is detected as {results[1]}.\nThe confidence of the result is {conf * 100:.2f}%"
        return render_template('loginpage2.html', result=res_string)

@app.route("/comparator_upload", methods=["POST"])
def comparator_upload():
    print(request.files)
    if 'formFile1' not in request.files and 'formFile2' not in request.files:
        # flash('No file part')
        return render_template('loginpage2.html')
    file1 = request.files['formFile1']
    file2 = request.files['formFile2']
    print(file1)
    print(file2)
    if file1.filename.strip() == "":
        return redirect(request.url)
    if file1 and allowed_file(file1.filename):
        file1.save(os.path.join(app.config['UPLOAD_FOLDER'], file1.filename))
    if file2.filename.strip() == "":
        return redirect(request.url)
    if file2 and allowed_file(file2.filename):
        file2.save(os.path.join(app.config['UPLOAD_FOLDER'], file2.filename))
    results = compare(file1.filename, file2.filename)
    print(results)
    res_string = f"\nSimilarity = {results[0]*100:.2f}%.\nYour old audio sample is detected as {results[1][1]}.\nYour new audio sample is detected as {results[2][1]}."
    return render_template('loginpage2.html', result=res_string)

@app.route("/logout")
def logout():
    session.pop("name",None)
    return redirect(url_for("login"))
    
    
@app.route("/login_page1")
def login_page1():
    if 'name' in session:
        return render_template('login_page1.html')
    else:
        return render_template('home.html')
        

@app.route("/loginpage2")
def loginpage2():
    if 'name' in session:
        return render_template('loginpage2.html', result="")
    else:
        return render_template('home.html')
            
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8182, use_reloader=True, debug=True)
