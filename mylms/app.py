from flask import Flask, render_template, url_for, request, session, redirect,send_file,make_response
from flask.ext.pymongo import PyMongo
import bcrypt
from flask import jsonify
import os
from uuid import uuid4
from gridfs import GridFS
import pdfkit
from werkzeug.datastructures import FileStorage

from werkzeug.utils import secure_filename
from flask import send_from_directory
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path_wkthmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = ''
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['MONGO_DBNAME'] = 'mongologinexample'
app.config['MONGO_URI'] = 'mongodb://Aakanksha:lms123@ds111618.mlab.com:11618/mysite'

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

mongo = PyMongo(app)

@app.route('/')
def index():
    #if 'username' in session:
    return render_template('index.html')
    #return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        users = mongo.db.users
        login_user = users.find_one({'name' : request.form['username']})

        if request.form['username'] == "vidya" :
            return render_template('InstructorHomePage.html')

        if login_user:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            if bcrypt.hashpw(bytes(request.form['pass'], 'utf-8'), hashpass) == hashpass:
                session['username'] = request.form['username']
                return render_template('CourseHomePage.html')
        return 'Invalid username/password combination'

    else:
        return render_template('login.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return render_template('mypage.html')
        return 'That username already exists!'
    return render_template('register.html')

@app.route('/course_request', methods=['POST', 'GET'])
def course_request():
    if request.method == 'POST':
        #users = mongo.db.users
        cr = mongo.db.courseRequests
        existing_user = cr.find_one({"name" : "sush"})
        existing_user['send_request'] = '1'
        cr.save(existing_user)
        return render_template('ML_RequestStatus.html',result = existing_user)

@app.route('/course_status', methods=['POST', 'GET'])
def course_status():
    cr = mongo.db.courseRequests
    existing_user = cr.find_one({"name" : "sush"})

    return render_template('CourseStatus.html',student = existing_user)
    #return render_template('course_status.html')

@app.route('/course_accept', methods=['POST', 'GET'])
def course_accept():
    if request.method == 'POST':
        #users = mongo.db.users
        cr = mongo.db.courseRequests
        existing_user = cr.find_one({"name" : "sush"})
        existing_user['accept_request'] = "1"
        cr.save(existing_user)

        if existing_user['accept_request'] == "1" :
            return render_template('StudentAccepted.html',student_status = existing_user)
    #return render_template('course_status.html')

@app.route('/makequizz', methods=['POST', 'GET'])
def makequizz():
    if request.method == 'POST':
        quiz = mongo.db.instructorMLQuiz
        existing_user = quiz.find_one({'name' : "vidya"})
        existing_user['Q1'] = request.form['1']
        existing_user['1a'] = request.form['1a']
        existing_user['1b'] = request.form['1b']
        existing_user['1c'] = request.form['1c']
        existing_user['1d'] = request.form['1d']
        existing_user['Q1ans'] = request.form['1ans']
        existing_user['Q2'] = request.form['2']
        existing_user['2a'] = request.form['2a']
        existing_user['2b'] = request.form['2b']
        existing_user['2c'] = request.form['2c']
        existing_user['2d'] = request.form['2d']
        existing_user['Q2ans'] = request.form['2ans']
        existing_user['Q3'] = request.form['3']
        existing_user['3a'] = request.form['3a']
        existing_user['3b'] = request.form['3b']
        existing_user['3c'] = request.form['3c']
        existing_user['3d'] = request.form['3d']
        existing_user['Q3ans'] = request.form['3ans']
        existing_user['Q4'] = request.form['4']
        existing_user['4a'] = request.form['4a']
        existing_user['4b'] = request.form['4b']
        existing_user['4c'] = request.form['4c']
        existing_user['4d'] = request.form['4d']
        existing_user['Q4ans'] = request.form['4ans']
        existing_user['Q5'] = request.form['5']
        existing_user['5a'] = request.form['5a']
        existing_user['5b'] = request.form['5b']
        existing_user['5c'] = request.form['5c']
        existing_user['5d'] = request.form['5d']
        existing_user['Q5ans'] = request.form['5ans']
        existing_user['Q6'] = request.form['6']
        existing_user['6a'] = request.form['6a']
        existing_user['6b'] = request.form['6b']
        existing_user['6c'] = request.form['6c']
        existing_user['6d'] = request.form['6d']
        existing_user['Q6ans'] = request.form['6ans']
        existing_user['Q7'] = request.form['7']
        existing_user['7a'] = request.form['7a']
        existing_user['7b'] = request.form['7b']
        existing_user['7c'] = request.form['7c']
        existing_user['7d'] = request.form['7d']
        existing_user['Q7ans'] = request.form['7ans']
        existing_user['Q8'] = request.form['8']
        existing_user['8a'] = request.form['8a']
        existing_user['8b'] = request.form['8b']
        existing_user['8c'] = request.form['8c']
        existing_user['8d'] = request.form['8d']
        existing_user['Q8ans'] = request.form['8ans']
        existing_user['Q9'] = request.form['9']
        existing_user['9a'] = request.form['9a']
        existing_user['9b'] = request.form['9b']
        existing_user['9c'] = request.form['9c']
        existing_user['9d'] = request.form['9d']
        existing_user['Q9ans'] = request.form['9ans']
        existing_user['Q10'] = request.form['10']
        existing_user['10a'] = request.form['10a']
        existing_user['10b'] = request.form['10b']
        existing_user['10c'] = request.form['10c']
        existing_user['10d'] = request.form['10d']
        existing_user['Q10ans'] = request.form['10ans']

        quiz.save(existing_user)

    return render_template('FinalQuiz.html',q = existing_user)

@app.route('/myprofile')
def myprofile():
    users = mongo.db.users
    existing_user = users.find_one({'name' : request.form['username']})
    return render_template('myprofile.html',existing_user=existing_user)

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/PrepareQuizz',methods=['POST', 'GET'])
def PrepareQuizz():
    return render_template('MakeQuiz.html')

@app.route('/TakeQuizz',methods=['POST', 'GET'])
def TakeQuizz():
    if request.method == 'POST':
        quiz = mongo.db.instructorMLQuiz
        existing_user = quiz.find_one({'name' : "vidya"})
        return render_template('TakeQuizz.html',qt = existing_user)

@app.route('/sendquizz',methods=['POST', 'GET'])
def sendquizz():
    if request.method == 'POST':
        quiz = mongo.db.instructorMLQuiz
        existing_user = quiz.find_one({'name' : "vidya"})
        existing_user['Send_Quizz'] = "1"
        quiz.save(existing_user)
        return ("Quizz uploaded successfully")

@app.route('/submitquizz',methods=['POST', 'GET'])
def submitquizz():
    if request.method == 'POST':
        correct = 0
        wrong = 0
        quiz = mongo.db.instructorMLQuiz
        instructor = quiz.find_one({'name' : "vidya"})
        stu_quiz = mongo.db.StudentMLQuiz
        student = stu_quiz.find_one({'name' : "sush"})
        student['Submit_Quizz'] = "1"
        if student['Submit_Quizz'] == "1":
            student['Q1ans'] = request.form['1option']
            student['Q2ans'] = request.form['2option']
            student['Q3ans'] = request.form['3option']
            student['Q4ans'] = request.form['4option']
            student['Q5ans'] = request.form['5option']
            student['Q6ans'] = request.form['6option']
            student['Q7ans'] = request.form['7option']
            student['Q8ans'] = request.form['8option']
            student['Q9ans'] = request.form['9option']
            student['Q10ans'] = request.form['10option']
            stu_quiz.save(student)
            if instructor['Q1ans'] == student['Q1ans']:
                correct = correct + 1
            if instructor['Q2ans'] == student['Q2ans']:
                correct = correct + 1
            if instructor['Q3ans'] == student['Q3ans']:
                correct = correct + 1
            if instructor['Q4ans'] == student['Q4ans']:
                correct = correct + 1
            if instructor['Q5ans'] == student['Q5ans']:
                correct = correct + 1
            if instructor['Q6ans'] == student['Q6ans']:
                correct = correct + 1
            if instructor['Q7ans'] == student['Q7ans']:
                correct = correct + 1
            if instructor['Q8ans'] == student['Q8ans']:
                correct = correct + 1
            if instructor['Q9ans'] == student['Q9ans']:
                correct = correct + 1
            if instructor['Q10ans'] == student['Q10ans']:
                correct = correct + 1

            student['Correct'] = correct
            student['Wrong'] = 10 - correct

            stu_quiz.save(student)

        return render_template('CalculateScore.html',st = student)

@app.route('/FinalQuiz')
def FinalQuiz():
    return render_template('FinalQuiz.html')

@app.route('/StudentCourses')
def StudentCourses():
    return render_template('StudentCourses.html')

@app.route('/um',methods=['POST', 'GET'])
def um():
    if request.method == 'POST':
        return render_template('uf.html')

@app.route('/upload_quiz',methods=['POST', 'GET'])
def upload_quiz():
    if request.method == 'POST':
        f1  = mongo.db.fileUpload
        existing_course = f1.find_one({'name' : 'xyz'})
        existing_course['File_Uploaded'] = "1"
        file = request.files['file']
        filename = secure_filename(file.filename)
        existing_course['File_Name'] = filename

        f1.save(existing_course)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        with open(filename,"r") as f:
            reader = csv.reader(f,delimiter = ",")
            data = list(reader)
            row_count = len(data)
        df = pd.read_csv(filename)
        count = 0
        with open(filename) as f:
            for i, line in enumerate(f, 1):
                count += 1
        l = len(df.columns)
        len1 = count
        res = []
        for i in range(0,row_count):
        	for j in range(0,l):
        		res.append(data[i][j])
        quiz = mongo.db.instructorMLQuiz
        existing_user = quiz.find_one({'name' : "vidya"})
        existing_user['Q1'] = res[6]
        existing_user['1a'] = res[7]
        existing_user['1b'] = res[8]
        existing_user['1c'] = res[9]
        existing_user['1d'] = res[10]
        existing_user['Q1ans'] = res[11]
        existing_user['Q2'] = res[12]
        existing_user['2a'] = res[13]
        existing_user['2b'] = res[14]
        existing_user['2c'] = res[15]
        existing_user['2d'] = res[16]
        existing_user['Q2ans'] = res[17]
        existing_user['Q3'] = res[18]
        existing_user['3a'] = res[19]
        existing_user['3b'] = res[20]
        existing_user['3c'] = res[21]
        existing_user['3d'] = res[22]
        existing_user['Q3ans'] = res[23]
        existing_user['Q4'] = res[24]
        existing_user['4a'] = res[25]
        existing_user['4b'] = res[26]
        existing_user['4c'] = res[27]
        existing_user['4d'] = res[28]
        existing_user['Q4ans'] = res[29]
        existing_user['Q5'] = res[30]
        existing_user['5a'] = res[31]
        existing_user['5b'] = res[32]
        existing_user['5c'] = res[33]
        existing_user['5d'] = res[34]
        existing_user['Q5ans'] = res[35]
        existing_user['Q6'] = res[36]
        existing_user['6a'] = res[37]
        existing_user['6b'] = res[38]
        existing_user['6c'] = res[39]
        existing_user['6d'] = res[40]
        existing_user['Q6ans'] = res[41]
        existing_user['Q7'] = res[41]
        existing_user['7a'] = res[43]
        existing_user['7b'] = res[44]
        existing_user['7c'] = res[45]
        existing_user['7d'] = res[46]
        existing_user['Q7ans'] = res[47]
        existing_user['Q8'] = res[48]
        existing_user['8a'] = res[49]
        existing_user['8b'] = res[50]
        existing_user['8c'] = res[51]
        existing_user['8d'] = res[52]
        existing_user['Q8ans'] = res[53]
        existing_user['Q9'] = res[54]
        existing_user['9a'] = res[55]
        existing_user['9b'] = res[56]
        existing_user['9c'] = res[57]
        existing_user['9d'] = res[58]
        existing_user['Q9ans'] = res[59]
        existing_user['Q10'] = res[60]
        existing_user['10a'] = res[61]
        existing_user['10b'] = res[62]
        existing_user['10c'] = res[63]
        existing_user['10d'] = res[64]
        existing_user['Q10ans'] = res[65]

        quiz.save(existing_user)

    return render_template('FinalQuiz.html',q = existing_user)

@app.route("/upm", methods=["POST"])
def upm():
    f = request.files['file']
    f1  = mongo.db.fileUpload
    existing_course = f1.find_one({'name' : 'xyz'})
    existing_course['File_Name'] = f.filename
    existing_course['File_Uploaded'] = "1"
    f1.save(existing_course)
    return render_template('downloads.html')

@app.route("/UploadQuizz", methods=["POST"])
def UploadQuizz():
    if request.method == 'POST':
        return render_template('UploadQuizz.html')

@app.route('/filedownloads')
def filedownloads():
	try:
		return render_template('downloads.html')
	except Exception as e:
		return str(e)
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/returnfile',methods=['POST', 'GET'])
def returnfile():
    if request.method == 'POST':
        f1  = mongo.db.fileUpload
        existing_course = f1.find_one({'name' : 'xyz'})
        file.filename = existing_course['File_Name']
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',filename=filename))
'''
    f1  = mongo.db.fileUpload
    existing_course = f1.find_one({'name' : 'xyz'})
    r = existing_course['material']
    css = ['static/css/style.css']
    pdf = pdfkit.from_string(r,False,css=css)
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment;filename=material.pdf'

    return response

    target = os.path.join(APP_ROOT,'Files/')
    if not os.path.isdir(target):
        os.mkdir(target)
    for file in request.files.getlist("file"):
        filename = file.filename
        destination = "/".join([target, filename])

    return send_file('static\images', attachment_filename='1.jpeg')'''

@app.route('/uploadmaterial', methods=['GET', 'POST'])
def uploadmaterial():
    return render_template('uploadmaterial.html')
@app.route('/uploadvideo', methods=['GET', 'POST'])
def uploadvideo():
    return render_template('uploadvideo.html')
@app.route('/upload1', methods=['GET', 'POST'])
def upload1():
    return render_template('upload.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f1  = mongo.db.fileUpload
        existing_course = f1.find_one({'name' : 'xyz'})
        existing_course['File_Uploaded'] = "1"
        #existing_course['File_Name'] = request.files['file']
        #f1.save(existing_course)
        file = request.files['file']
        filename = secure_filename(file.filename)
        existing_course['File_Name'] = filename
        f1.save(existing_course)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return ("File uploaded successfully")

@app.route('/returnfilematerial', methods=['GET', 'POST'])
def returnfilematerial():
    if request.method == 'POST':
        f1  = mongo.db.fileUpload
        existing_course = f1.find_one({'name' : 'xyz'})
        if existing_course['Material_Uploaded'] == "1":
            #path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'index.php')
            filename = existing_course['Material_Name']
            return redirect(url_for('uploaded_file',filename=filename))
        else:
            return redirect(url_for('uploaded_file',filename=filename))

@app.route('/returnfilevideo', methods=['GET', 'POST'])
def returnfilevideo():
    if request.method == 'POST':
        f1  = mongo.db.fileUpload
        existing_course = f1.find_one({'name' : 'xyz'})
        if existing_course['Video_Uploaded'] == "1":
            #path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'index.php')
            filename = existing_course['Video_Name']
            return redirect(url_for('uploaded_file',filename=filename))
        else:
            return redirect(url_for('uploaded_file',filename=filename))

@app.route('/tq1', methods=['GET', 'POST'])
def tq1():
    if request.method == 'POST':
        quiz = mongo.db.instructorMLQuiz
        existing_user = quiz.find_one({'name' : "vidya"})
        return render_template('TakeQuizz.html',q = existing_user)


@app.route('/tq2', methods=['GET', 'POST'])
def tq2():
    if request.method == 'POST':
        quiz = mongo.db.instructorMLQuiz
        existing_user = quiz.find_one({'name' : "vidya"})
        return render_template('TakeQuizz.html',qt = existing_user)

@app.route('/progress', methods=['GET', 'POST'])
def progress():
    if request.method == 'POST':
        return render_template('QuizzStatus.html')


@app.route('/uploadm', methods=['GET', 'POST'])
def uploadm():
    if request.method == 'POST':
        f1  = mongo.db.fileUpload
        existing_course = f1.find_one({'name' : 'xyz'})
        existing_course['Material_Uploaded'] = "1"
        #existing_course['File_Name'] = request.files['file']
        #f1.save(existing_course)
        file = request.files['file']
        filename = secure_filename(file.filename)
        existing_course['Material_Name'] = filename
        f1.save(existing_course)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return ("Material uploaded successfully")

@app.route('/uploadv', methods=['GET', 'POST'])
def uploadv():
    if request.method == 'POST':
        f1  = mongo.db.fileUpload
        existing_course = f1.find_one({'name' : 'xyz'})
        existing_course['Video_Uploaded'] = "1"
        #existing_course['File_Name'] = request.files['file']
        #f1.save(existing_course)
        file = request.files['file']
        filename = secure_filename(file.filename)
        existing_course['Video_Name'] = filename
        f1.save(existing_course)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return ("Video uploaded successfully")

@app.route('/InstructorHomepage')
def InstructorHomePage():
    return render_template('InstructorHomePage.html')

@app.route('/ViewProgress')
def ViewProgress():
    return render_template('ViewProgress.html')


@app.route('/WebTechnologies')
def WebTechnologies():
    return render_template('WebTechnologies.html')

@app.route('/MachineLearning')
def MachineLearning():
    return render_template('MachineLearning.html')

@app.route('/ml',methods=['POST', 'GET'])
def ml():
    if request.method == 'POST':
        quiz = mongo.db.instructorMLQuiz
        existing_user = quiz.find_one({'name' : "vidya"})
        if existing_user['Send_Quizz'] == "1":
            return render_template('ml.html',tq = existing_user)
        return render_template('ml.html')

@app.route('/QuizzStatus',methods=['POST', 'GET'])
def QuizzStatus():
    if request.method == 'POST':
        return render_template('QuizzStatus.html')

@app.route('/Python')
def Python():
    return render_template('Python.html')

@app.route('/ArtificialIntelligence')
def ArtificialIntelligence():
    return render_template('ArtificialIntelligence.html')



@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('index'))
if __name__ == '__main__':
    app.secret_key = 'mysecret'
app.run(debug=True)
