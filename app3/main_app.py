"""
This is the main application
"""
from flask import Flask, render_template, url_for, redirect, jsonify, request, Response, make_response
import database_operations as dbop
import json

APP = Flask(__name__)


@APP.route('/')
def homepage_view():
    """This is the homepage """
    return 'Hello World'


@APP.route('/createdatabase')
def create_database():
    """url to create new database """
    dbop.create_fresh_database()
    return redirect(url_for('homepage_view'))


@APP.route('/register', methods=['GET'])
def initial_register_view():
    """ url for initial register"""
    return render_template('html/register1.html')

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


if __name__ == '__main__':
    APP.run(debug=True)
    APP.run()
