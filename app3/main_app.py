"""
This is the main application
"""
from flask import Flask, render_template, url_for, redirect, jsonify, request, Response, make_response
import database_operations as dbop
import json

APP = Flask(__name__)


@APP.route('/', methods = ['GET'])
def homepage_view():
    """This is the homepage """
    return render_template('html/login.html')


@APP.route('/createdatabase')
def create_database():
    """url to create new database """
    dbop.create_fresh_database()
    return redirect(url_for('homepage_view'))


@APP.route('/register', methods=['GET'])
def initial_register_view():
    """ url for initial register"""
    return render_template('html/register1.html')

@APP.route('/register2', methods=['GET'])
def final_register_view():
    """ url for Complete register"""
    return render_template('html/register2.html')

@APP.route('/assignclass', methods=['GET'])
def add_class_view():
    """ url to add class"""
    return render_template('html/assignclass.html')

@APP.route('/addattendance', methods=['GET'])
def attendance_view():
    """ url to attendance"""
    return render_template('html/attendancebatch.html')
@APP.route('/assignteacher',methods=['GET'])
def subjectteacher_view():
    "url to add subject teacher"
    return render_template('html/subjectteacher.html')

@APP.route('/addstudent', methods=['GET'])
def add_student_view():
    """ URL to add or view students"""
    return render_template('html/studentbatch.html')

@APP.route('/iamarks',methods = ['GET'])
def add_iamarks_view():
    """URL to add or view iamarks"""
    return render_template('html/iamarks.html')

@APP.route('/home',methods = ['GET'])
def home_page_view():
    """URL for professor home page """
    return render_template('html/personalpage.html')
# Endpoints


@APP.route('/initialregister', methods=['POST'])
def initial_register_ajax():
    """This is the ajax endpoint for initial registeration"""
    data = request.get_json()
    print(type(data))
    data['type_description'] = data['faculty_type'][0]['type_description']
    response = dbop.add_initial_faculty(data)
    print(response)
    return jsonify(response)

@APP.route('/finalregister', methods=['POST'])
def final_register_ajax():
    """This endpoint is to add all the faculty details"""
    data = request.get_json()
    print(data)
    print(data['teacher_picture'])
    response = dbop.update_faculty_details(data)
    # response = {"msg" :"success"}
    return jsonify(response)

@APP.route('/login', methods = ['POST'])
def login_ajax():
    """This is the ajax endpoint for login"""
    data = request.get_json()
    print(data)
    response = dbop.validate_login(data)
    print(response)
    print("hello tresting")
    return jsonify(response)

@APP.route('/getdetails', methods = ['POST'])
def lget_details_ajax():
    """This is the ajax endpoint for login"""
    data = request.get_json()
    print(data)
    response = dbop.get_faculty_details(data)
    print(response)
    return jsonify(response)

@APP.route('/getclass', methods = ['POST'])
def class_details_ajax():
    """This is the ajax endpoint for login"""
    data = request.get_json()
    print(data)
    response = dbop.get_class_details(data)
    print(response)
    return jsonify(response)

@APP.route('/getclassdetails', methods=['POST'])
def get_all_class_details_ajax():
    """This endpoint is to get all details"""
    data = request.get_json()
    print(data)
    response = dbop.get_all_class_details(data)
    print(response)
    return jsonify(response)

@APP.route('/addclass', methods=['POST'])
def add_class_ajax():
    """This endpoint is to add new class into the database"""
    data = request.get_json()
    print(data)
    response = dbop.add_class(data)
    print(response)
    return jsonify(response)

@APP.route('/getfcs', methods=['POST'])
def get_subjectteacher_details_ajax():
    """This endpoint is to add new class into the database"""
    data = request.get_json()
    print(data)
    response = dbop.get_subjectteacher_details(data)
    print(response)
    return jsonify(response)

@APP.route('/addsubject', methods=['POST'])
def add_subject_ajax():
    """This endpoint is to add new subject into the database"""
    data = request.get_json()
    print(data)
    response = dbop.add_subject(data)
    print(response)
    return jsonify(response)

@APP.route('/get_year_sem_sec', methods=['POST'])
def get_year_sem_sec():
    """This endpoint is to get all class information accordingly"""
    data = request.get_json()
    print(data)
    response = dbop.get_year_sem_sec(data)
    print(response)
    return jsonify(response)

@APP.route('/get_student_details', methods=['POST'])
def get_student_details_ajax():
    """This endpoint is to get list of student, in a particular class"""
    data = request.get_json()
    print(data)
    response = dbop.get_student_details(data)
    print(response)
    return jsonify(response)

@APP.route('/addstudent', methods=['POST'])
def add_student_ajax():
    """This endpoint is used to add new student data"""
    data = request.get_json()
    print(data)
    response = dbop.add_student(data)
    print(response)
    return jsonify(response)

@APP.route('/get_student_attendance_details', methods=['POST'])
def get_student_attendance_details_ajax():
    """This endpoint get stusdents details based on subject"""
    data = request.get_json()
    print(data)
    response = dbop.get_student_attendance_details(data)
    return jsonify(response)

@APP.route('/get_student_marks_details', methods=['POST'])
def get_student_marks_details_ajax():
    """This endpoint get stusdents details based on subject"""
    data = request.get_json()
    print(data)
    response = dbop.get_student_marks_details(data)
    return jsonify(response)

@APP.route('/add_student_attendance', methods=['POST'])
def add_student_attendance_ajax():
    """This endpoint is used to add student attendance"""
    data = request.get_json()
    print(data)
    response = dbop.add_student_attendance(data)
    return jsonify(response)

@APP.route('/get_attendance_details', methods=['POST'])
def get_attendance_details_ajax():
    """This endpoint is used to get student attendance"""
    data = request.get_json()
    print(data)
    response = dbop.get_attendance_details(data)
    return jsonify(response)

<<<<<<< HEAD
@APP.route('/add_question_paper_pattern', methods = ['POST'])
def add_question_paper_pattern_ajax():
    """This endpoint is to add qPattern"""
    data = request.get_json()
    print(data)
    response = dbop.add_question_paper_pattern(data)
    return jsonify(response)
=======
@APP.route('/get_complete_faculty_details' , methods = ['POST'])
def get_faculty_details_view():
    """This endpoint is used tot get faculty details"""
    data = request.get_json()
    response = dbop.get_complete_faculty_details(data)
    return jsonify(response)

>>>>>>> 1c7fd311f2d70b1858458ade337e76c80d1b669c
if __name__ == '__main__':
    APP.run(debug=True, threaded=True)
    APP.run()
