"""
This is the main application
"""
from flask import Flask, render_template, url_for, redirect, jsonify, request, Response, make_response
import database_operations as dbop
import json
import os

APP = Flask(__name__)
APP.config['UPLOAD_FOLDER'] = "upload"


@APP.route('/', methods=['GET'])
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


@APP.route('/assignteacher', methods=['GET'])
def subjectteacher_view():
    "url to add subject teacher"
    return render_template('html/subjectteacher.html')


@APP.route('/addstudent', methods=['GET'])
def add_student_view():
    """ URL to add or view students"""
    return render_template('html/studentbatch.html')


@APP.route('/iamarks', methods=['GET'])
def add_iamarks_view():
    """URL to add or view iamarks"""
    return render_template('html/iamarks.html')


@APP.route('/home', methods=['GET'])
def home_page_view():
    """URL for professor home page """
    return render_template('html/personalpage.html')


@APP.route('/teachers', methods=['GET'])
def all_teachers_view():
    """URL for all professors page """
    return render_template('html/allteachers.html')


@APP.route('/approval', methods=['GET'])
def approve_view():
    """This is the page to approve teachers """
    return render_template('html/approval.html')


@APP.route('/allstudents', methods=['GET'])
def all_students_view():
    """This is the page dispaly all student details """
    return render_template('html/viewallstudents.html')


@APP.route('/viewmarks', methods=['GET'])
def view_marks_view():
    """This is the page to view marks and send SMS"""
    return render_template('html/viewmarks.html')

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
    # print(data['teacher_picture'])
    response = dbop.update_faculty_details(data)
    # response = {"msg" :"success"}
    return jsonify(response)


@APP.route('/login', methods=['POST'])
def login_ajax():
    """This is the ajax endpoint for login"""
    data = request.get_json()

    response = dbop.validate_login(data)
    # print(response)
    return jsonify(response)


@APP.route('/getdetails', methods=['POST'])
def lget_details_ajax():
    """This is the ajax endpoint for login"""
    data = request.get_json()
    print(data)
    response = dbop.get_faculty_details(data)
    print(response)
    return jsonify(response)


@APP.route('/getclass', methods=['POST'])
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


@APP.route('/add_question_paper_pattern', methods=['POST'])
def add_question_paper_pattern_ajax():
    """This endpoint is to add qPattern"""
    data = request.get_json()
    print(data)
    response = dbop.add_question_paper_pattern(data)
    return jsonify(response)


@APP.route('/get_complete_faculty_details', methods=['POST'])
def get_faculty_details_view():
    """This endpoint is used tot get faculty details"""
    data = request.get_json()
    response = dbop.get_complete_faculty_details(data)
    return jsonify(response)


@APP.route('/add_student_res', methods=['POST'])
def add_student_res_ajax():
    """This endpoint is to add student result"""
    data = request.get_json()
    resonse = dbop.add_student_res(data)
    return jsonify(resonse)


@APP.route('/get_all_faculty', methods=['POST'])
def get_faculty_view():
    """This endpoint is used get  all faculty """
    data = request.get_json()
    response = dbop.get_complete_faculty(data)
    return jsonify(response)


@APP.route('/approve__decline', methods=['POST'])
def approve__decline__view():
    """This endpoint is approve or decline a faculty """
    data = request.get_json()
    response = dbop.approve__decline(data)
    return jsonify(response)


@APP.route('/get_class_marks', methods=['POST'])
def get_class_marks_ajax():
    """This endpoint is used to get marks classwise"""
    data = request.get_json()
    response = dbop.get_class_marks(data)
    return response


@APP.route('/resetpassword', methods=['POST'])
def reset__password__view():
    """This endpoint is reset password """
    data = request.get_json()
    response = dbop.reset__password(data)
    return jsonify(response)


@APP.route('/feedback', methods=['POST'])
def feedback__view():
    """This endpoint is submit feedback """
    data = request.get_json()
    response = dbop.submit__feedback(data)
    return jsonify(response)


@APP.route('/get_all_students_name', methods=['POST'])
def get_all_students_name_view():
    """This endpoint is to get all student details"""
    data = request.get_json()
    response = dbop.get_all_students(data)
    return jsonify(response)


@APP.route('/get_indivisual_student', methods=['POST'])
def get_indivisual_student_view():
    """This endpoint is to get indivisual studetn details"""
    data = request.get_json()
    response = dbop.get_indivisual_student(data)
    return jsonify(response)

@APP.route('/send_marks_sms', methods=['POST'])
def send_student_marks_ajax():
    """This endpoint is used to send marks SMS"""
    data = request.get_json()
    response = dbop.send_marks_sms(data)
    return jsonify(response)

# @APP.route('/get_class_details' , methods = ['POST'])
# def get_class_details_view():
#     """This endpoint is to get class details"""
#     data = request.get_json()
#     response = dbop.get_class_details(data)
#     return jsonify(response)

# FOR ALTERNATE ASSIGNCLASS PAGE <<IGNORE AS OF NOW>>

@APP.route('/submitfile' , methods = ['POST'])
def submit__file__view():
    """This endpoint is add student batch """
    data1 = request.files.get('batchdetails')
    data2 = request.files.get('batchpics')
    # print(data1.filename)
    # print(data2.filename)
    # print(data)
    data2.save(os.path.join(APP.config['UPLOAD_FOLDER'], data2.filename))
    data = {'file1': data1, 'file2': data2.filename}
    response = dbop.submit__batch(data)
    return jsonify(response)


if __name__ == '__main__':
    APP.run(debug=True, threaded=True)
    APP.run()
