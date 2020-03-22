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
    return render_template('html/dayattendance.html')
@APP.route('/assignteacher',methods=['GET'])
def subjectteacher_view():
    "url to add subject teacher"
    return render_template('html/subjectteacher.html')
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
    # response = dbop.update_faculty_details(data)
    response = {"msg" :"success"}
    return jsonify(response)

@APP.route('/login', methods = ['POST'])
def login_ajax():
    """This is the ajax endpoint for login"""
    data = request.get_json()
    print(data)
    response = dbop.validate_login(data)
    print(response)
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

if __name__ == '__main__':
    APP.run(debug=True, threaded=True)
    APP.run()
