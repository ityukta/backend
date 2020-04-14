"""
contains functions to perform all database operations
"""
import sqlite3 as sql
import string
import random
import datetime
import itertools
import calendar
import helper
import pickle
import pprint

p = pprint.PrettyPrinter(1)
import pandas as pd


def create_fresh_database():
    """functions to create a fresh database """
    conn = sql.connect('database.db')

    create_faculty_table = """
        CREATE TABLE IF NOT EXISTS Faculty(
            faculty_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email_id TEXT NOT NULL,
            password TEXT NOT NULL,
            department TEXT NOT NULL,
            phone TEXT NULL,
            date_of_joining DATE NULL,
            experience INTEGER NULL,
            date_of_birth DATE NULL,
            gender TEXT NULL,
            marital_status TEXT NULL,
            address TEXT NULL,
            teacher_picture TEXT NULL,
            designation TEXT NULL,
            association_with_institution TEXT NULL,
            deleted BOOLEAN DEFAULT(FALSE),
            approved BOOLEAN DEFAULT(FALSE),
            first_login BOOLEAN DEFAULT(TRUE)
        )
    """

    create_faculty_type__table = """
        CREATE TABLE IF NOT EXISTS Type(
            type_id INTEGER PRIMARY KEY AUTOINCREMENT,
            type_description TEXT NOT NULL,
            faculty_id INTEGER NOT NULL,
            FOREIGN KEY(faculty_id) REFERENCES Faculty(faculty_id) ON DELETE CASCADE
        )
    """
    create_publications_table = """
        CREATE TABLE IF NOT EXISTS Publications(
            publication_id INTEGER PRIMARY KEY AUTOINCREMENT,
            publication_details TEXT NOT NULL,
            faculty_id INTEGER NOT NULL,
            FOREIGN KEY(faculty_id) REFERENCES Faculty(faculty_id) ON DELETE CASCADE
        )
    """
    create_invited_talks_table = """
        CREATE TABLE IF NOT EXISTS InvitedTalks(
            invited_talk_id INTEGER PRIMARY KEY AUTOINCREMENT,
            invited_talk_details TEXT NOT NULL,
            faculty_id INTEGER NOT NULL,
            FOREIGN KEY(faculty_id) REFERENCES Faculty(faculty_id) ON DELETE CASCADE
        )
    """
    create_workshops_table = """
        CREATE TABLE IF NOT EXISTS Workshops(
            workshop_id INTEGER PRIMARY KEY AUTOINCREMENT,
            workshop_type TEXT NOT NULL,
            workshop_details TEXT NOT NULL,
            faculty_id INTEGER NOT NULL,
            FOREIGN KEY(faculty_id) REFERENCES Faculty(faculty_id) ON DELETE CASCADE
        )
    """

    create_faculty_qualification_table = """
        CREATE TABLE IF NOT EXISTS FacultyQualification(
            qualification_id INTEGER PRIMARY KEY AUTOINCREMENT,
            degree TEXT NOT NULL,
            branch TEXT NOT NULL,
            institution TEXT NOT NULL,
            percentage REAL NOT NULL,
            graduation_year INTEGER NOT NULL,
            university TEXT NOT NULL,
            faculty_id INTEGER NOT NULL,
            FOREIGN KEY(faculty_id) REFERENCES Faculty(faculty_id) ON DELETE CASCADE
        )
    """

    create_research_paper_table = """
        CREATE TABLE IF NOT EXISTS ResearchPaper(
            research_paper_id INTEGER PRIMARY KEY AUTOINCREMENT,
            research_paper_details TEXT NOT NULL,
            faculty_id INTEGER NOT NULL,
            FOREIGN KEY(faculty_id) REFERENCES Faculty(faculty_id) ON DELETE CASCADE
        )
    """

    create_session_chair_table = """
        CREATE TABLE IF NOT EXISTS SessionChair(
            session_chair_id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_chair_details TEXT NOT NULL,
            faculty_id INTEGER NOT NULL,
            FOREIGN KEY(faculty_id) REFERENCES Faculty(faculty_id) ON DELETE CASCADE
        )
    """

    create_work_experience_table = """
        CREATE TABLE IF NOT EXISTS WorkExperience(
            work_experience_id INTEGER PRIMARY KEY AUTOINCREMENT,
            designation TEXT NOT NULL,
            organzation TEXT NOT NULL,
            duration REAL NOT NULL,
            faculty_id INTEGER NOT NULL,
            FOREIGN KEY(faculty_id) REFERENCES Faculty(faculty_id) ON DELETE CASCADE
        )
    """

    create_area_of_specialisation_table = """
        CREATE TABLE IF NOT EXISTS AreaOfSpecialisation(
            specialisation_id INTEGER PRIMARY KEY AUTOINCREMENT,
            specialisation_details TEXT NOT NULL,
            faculty_id INTEGER NOT NULL,
            FOREIGN KEY(faculty_id) REFERENCES Faculty(faculty_id) ON DELETE CASCADE
        )
    """

    create_academic_role_table = """
        CREATE TABLE IF NOT EXISTS AcademicRole(
            academic_role_id INTEGER PRIMARY KEY AUTOINCREMENT,
            academic_role_details TEXT NOT NULL,
            faculty_id INTEGER NOT NULL,
            FOREIGN KEY(faculty_id) REFERENCES Faculty(faculty_id) ON DELETE CASCADE
        )
    """

    create_login_auth_key_table = """
        CREATE TABLE IF NOT EXISTS LoginAuthKey(
            login_authkey_id INTEGER PRIMARY KEY AUTOINCREMENT,
            authkey TEXT NOT NULL,
            deleted BOOLEAN DEFAULT(FALSE),
            faculty_id INTEGER NOT NULL,
            FOREIGN KEY(faculty_id) REFERENCES Faculty(faculty_id) ON DELETE CASCADE
        )
    """
    create_class_table = """
        CREATE TABLE IF NOT EXISTS Class(
            class_id INTEGER PRIMARY KEY AUTOINCREMENT,
            sem INTEGER NOT NULL,
            sec TEXT NOT NULL,
            graduation_year INTEGER NOT NULL,
            department TEXT NOT NULL,
            classteacher_id INTEGER NOT NULL,
            FOREIGN KEY(classteacher_id) REFERENCES Faculty(faculty_id) ON DELETE SET NULL
        )
    """

    create_student_table = """
        CREATE TABLE IF NOT EXISTS Student(
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            usn TEXT NOT NULL,
            batch TEXT NOT NULL,
            class_id INTEGER NOT NULL,
            blood_group TEXT NOT NULL,
            father_name TEXT NOT NULL,
            phone_no TEXT NOT NULL,
            parent_mail TEXT NOT NULL,
            permanent_address TEXT NOT NULL,
            current_address TEXT NOT NULL,
            c10th_res REAL NOT NULL,
            c12th_res REAL NOT NULL,
            student_picture BLOB ,
            deleted BOOLEAN DEFAULT(FALSE),
            FOREIGN KEY(class_id) REFERENCES Class(class_id) ON DELETE SET NULL
        )
    """

    create_subject_table = """
        CREATE TABLE IF NOT EXISTS Subject(
            subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject_name TEXT NOT NULL,
            subject_code TEXT NOT NULL,
            credits INTEGER NOT NULL
        )
    """

    create_fcs_table = """
        CREATE TABLE IF NOT EXISTS Fcs(
            fcs_id INTEGER PRIMARY KEY AUTOINCREMENT,
            faculty_id INTEGER NOT NULL,
            class_id INTEGER NOT NULL,
            subject_id INTEGER NOT NULL,
            section TEXT NOT NULL ,
            FOREIGN KEY(faculty_id) REFERENCES Faculty(faculty_id) ON DELETE SET NULL,
            FOREIGN KEY(class_id) REFERENCES Class(class_id) ON DELETE SET NULL,
            FOREIGN KEY(subject_id) REFERENCES Subject(subject_id) ON DELETE SET NULL
        )
    """

    create_fcss_table = """
        CREATE TABLE IF NOT EXISTS Fcss(
            fcss_id INTEGER PRIMARY KEY AUTOINCREMENT,
            fcs_id INTEGER NOT NULL,
            student_id INTEGER NOT NULL,
            FOREIGN KEY(fcs_id) REFERENCES Fcs(fcs_id) ON DELETE SET NULL,
            FOREIGN KEY(student_id) REFERENCES Student(student_id) ON DELETE SET NULL
        )
    """

    create_attendance_table = """
        CREATE TABLE IF NOT EXISTS Attendance(
            attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
            fcss_id INTEGER NOT NULL,
            hour INTEGER NOT NULL,
            date DATE NOT NULL,
            status BOOLEAN NOT NULL,
            FOREIGN KEY(fcss_id) REFERENCES Fcss(fcss_id) ON DELETE SET NULL
        )
    """
    create_tests_table = """
        CREATE TABLE IF NOT EXISTS Tests(
            test_id INTEGER PRIMARY KEY AUTOINCREMENT,
            fcs_id INTEGER NOT NULL,
            test_no INTEGER NOT NULL,
            qp_pattern BLOB NOT NULL,
            FOREIGN KEY(fcs_id) REFERENCES Fcs(fcs_id) ON DELETE SET NULL
        )
    """

    create_test_res_table = """
        CREATE TABLE IF NOT EXISTS Test_res(
            testres_id INTEGER PRIMARY KEY AUTOINCREMENT,
            fcss_id INTEGER NOT NULL,
            test_id INTEGER NOT NULL,
            marks BLOB NOT NULL,
            FOREIGN KEY(fcss_id) REFERENCES Fcss(fcss_id) ON DELETE SET NULL,
            FOREIGN KEY(test_id) REFERENCES Tests(test_id) ON DELETE SET NULL
        )
    """
    create_otp_table = """
        CREATE TABLE IF NOT EXISTS OTP(
            email_id TEXT PRIMARY KEY ,
            otp TEXT ,
            FOREIGN KEY(email_id) REFERENCES Faculty(email_id) ON DELETE CASCADE
        )
    """
    conn.execute(create_faculty_table)
    conn.execute(create_faculty_type__table)
    conn.execute(create_publications_table)
    conn.execute(create_workshops_table)
    conn.execute(create_faculty_qualification_table)
    conn.execute(create_research_paper_table)
    conn.execute(create_session_chair_table)
    conn.execute(create_work_experience_table)
    conn.execute(create_area_of_specialisation_table)
    conn.execute(create_academic_role_table)
    conn.execute(create_login_auth_key_table)
    conn.execute(create_class_table)
    conn.execute(create_student_table)
    conn.execute(create_subject_table)
    conn.execute(create_invited_talks_table)
    conn.execute(create_fcs_table)
    conn.execute(create_fcss_table)
    conn.execute(create_attendance_table)
    conn.execute(create_tests_table)
    conn.execute(create_test_res_table)
    print("tables created successfully")
    conn.close()


def add_initial_faculty(data):
    """Initial registration insert query"""
    try:
        conn = sql.connect('database.db')
        insert_faculty_query = """
            INSERT INTO Faculty(name, email_id, password, department) VALUES (?, ?, ?, ?)
        """
        insert_faculty_type_query = """
            INSERT INTO Type(type_description, faculty_id) VALUES (? , ?)
        """
        c = conn.cursor()
        c.execute(insert_faculty_query,
                  (data['name'], data['email_id'], data['password'], data['department']))
        faculty_id = c.lastrowid
        if data['type_description'] != 'P':
            c.execute(insert_faculty_type_query,
                      (data['type_description'], faculty_id))
        c.execute(insert_faculty_type_query,
                  ('P', faculty_id))
        conn.commit()
        conn.close()
        response = {"status_message": "successful",
                    "status_code": 200, "data": data}
    except Exception as E:
        response = {"status_message": "Unsuccessful",
                    "status_code": 301, "data": str(E)}
    return response


def update_faculty_details(data):
    conn = sql.connect('database.db')
    check_authkey_query = """
        SELECT *FROM LoginAuthKey WHERE authkey = ? AND faculty_id = ? AND DELETED = 0
    """
    update_first_login_query = """
        UPDATE Faculty SET first_login = 0 
    """
    c = conn.cursor()
    _ = c.execute(check_authkey_query,
                  (data['authkey'], data['faculty_id'])).fetchone()
    if _ is None:
        response = {"status_message": "Unauthorized access",
                    "status_code": 404, "data": "Invalid Authkey provided"}
        return response
    del data['authkey']
    inp_faculty_id = data['faculty_id']
    del data['faculty_id']
    attributes = []
    other_attributes = []
    for key, value in data.items():
        if type(value) is list:
            other_attributes.append(key)
        else:
            attributes.append(key)
    update_query_values = " = ?, ".join(attributes) + " = ?"
    update_faculty_details_query = f"""
        UPDATE Faculty SET {update_query_values} WHERE faculty_id = ?
    """
    values_to_update_list = [data[key] for key in attributes]
    values_to_update_list.append(inp_faculty_id)
    values_to_update_list = tuple(values_to_update_list)
    c.execute(update_faculty_details_query, values_to_update_list)

    for attrs in other_attributes:
        if attrs == 'education':
            education_data = data[attrs]
            for each_education_data in education_data:
                degree = each_education_data['degree']
                educational_institution = each_education_data['educational_institution']
                branch = each_education_data['branch']
                percentage = each_education_data['percentage']
                year_of_passing = each_education_data['year_of_passing']
                university = each_education_data['university']
                insert_education_details_query = """
                    INSERT INTO FacultyQualification(degree, branch, institution, percentage, graduation_year, university, faculty_id) VALUES(?, ?, ?, ?, ?, ?, ?)
                """
                c.execute(insert_education_details_query, (degree, branch, educational_institution,
                                                           percentage, year_of_passing, university, inp_faculty_id))
        elif attrs == 'work_experience':
            work_experience_data = data[attrs]
            for each_work_experience in work_experience_data:
                designation = each_work_experience['designation']
                organization = each_work_experience['organization']
                duration = each_work_experience['duration']
                insert_work_experience_details_query = """
                    INSERT INTO WorkExperience(designation, organzation, duration, faculty_id) VALUES (?, ?, ?, ?)
                """
                c.execute(insert_work_experience_details_query,
                          (designation, organization, duration, inp_faculty_id))
        elif attrs == "publications":
            publication_data = data[attrs]
            for each_publication in publication_data:
                pub_details = each_publication['publication_details']
                insert_publication_details_query = """
                    INSERT INTO Publications(publication_details, faculty_id) VALUES (?, ?)
                """
                c.execute(insert_publication_details_query,
                          (pub_details, inp_faculty_id))
        elif attrs == "papers":
            papers_data = data[attrs]
            for each_paper in papers_data:
                paper_details = each_paper['paper_details']
                insert_paper_details_query = """
                    INSERT INTO ResearchPaper(research_paper_details, faculty_id) VALUES (?, ?)
                """
                c.execute(insert_paper_details_query,
                          (paper_details, inp_faculty_id))
        elif attrs == "invitedtalks":
            invitedtalks_data = data[attrs]
            for each_invited_talk in invitedtalks_data:
                invited_talk_details = each_invited_talk['invited_talk_details']
                insert_into_invited_talks_query = """
                    INSERT INTO InvitedTalks(invited_talk_details, faculty_id) VALUES (? ,?)
                """
                c.execute(insert_into_invited_talks_query,
                          (invited_talk_details, inp_faculty_id))
        elif attrs == "sessions":
            session_chair_data = data[attrs]
            for each_session_chair in session_chair_data:
                session_chair_details = each_session_chair['session_details']
                insert_into_session_query = """
                    INSERT INTO SessionChair(session_chair_details, faculty_id) VALUES (?, ?)
                """
                c.execute(insert_into_session_query,
                          (session_chair_details, inp_faculty_id))
        elif attrs == "workshops":
            workshop_data = data[attrs]
            for each_workshop in workshop_data:
                workshop_type = each_workshop['workshop_type']
                workshop_details = each_workshop['workshop_description']
                insert_workshop_details_query = """
                    INSERT INTO Workshops(workshop_type, workshop_details, faculty_id) VALUES (?, ?, ?)
                """
                c.execute(insert_workshop_details_query,
                          (workshop_type, workshop_details, inp_faculty_id))
        elif attrs == "area_of_specialisation":
            specialisation_data = data[attrs]
            for each_specialisation in specialisation_data:
                specialisation_details = each_specialisation['specialisation_details']
                insert_specialisation_details_query = """
                    INSERT INTO AreaOfSpecialisation(specialisation_details, faculty_id) VALUES (?, ?)
                """
                c.execute(insert_specialisation_details_query,
                          (specialisation_details, inp_faculty_id))
        c.execute(update_first_login_query, (data['faculty_id'],))
    conn.commit()
    response = {"msg": "successful"}
    return response


def validate_login(data):
    """ Function to validate initial register"""
    conn = sql.connect('database.db')
    get_login_credentials_query = """
        SELECT *FROM Faculty WHERE email_id = ? AND password = ?
    """
    get_type_query = """
        SELECT type_description FROM Type WHERE faculty_id = ?
    """
    c = conn.cursor()
    c.execute(get_login_credentials_query, (data['emailid'], data['password']))
    faculty_details = c.fetchone()
    if faculty_details is None:
        response = {"status_message": "Unsuccessful", "status_code": 301,
                    "data": "Incorrect username and password"}
    else:
        faculty_details = dict(
            zip([cur[0] for cur in c.description], faculty_details))
        # print("facultydet", faculty_details)
        if(faculty_details['approved'] == 0):
            response = {"status_message": "Unsuccessful", "status_code": 301,
                        "data": "User Still not approved, contact admin"}
        else:
            insert_login_authkey_query = """
                INSERT INTO LoginAuthKey(authkey, faculty_id) VALUES (? , ?)
            """
            random_authkey = ''.join(random.SystemRandom().choice(
                string.ascii_uppercase + string.digits) for _ in range(16))
            c.execute(insert_login_authkey_query,
                      (random_authkey, faculty_details['faculty_id']))
            conn.commit()
            faculty_type = c.execute(
                get_type_query, (faculty_details['faculty_id'],)).fetchall()
            faculty_type = [i[0] for i in faculty_type]
            print(faculty_type)
            conn.close()
            if 'H' in faculty_type:
                f_type = 3
            elif 'C' in faculty_type:
                f_type = 2
            else:
                f_type = 1
            faculty_details['faculty_type'] = f_type
            response = {"status_message": "Successful",
                        "status_code": 200, "authkey": random_authkey, 'faculty_type': f_type, "data": faculty_details}

    # except Exception as E:
    #     response = {"status_message": "Unsuccessful", "status_code": 301,
    #                 "data": "The following error occured" + str(E)}
    return response


def get_faculty_details(data):
    """function to get one faculty data using id and authkey"""
    conn = sql.connect('database.db')
    check_authkey_query = """
        SELECT *FROM LoginAuthKey WHERE authkey = ? AND faculty_id = ? AND DELETED = 0
    """
    c = conn.cursor()
    _ = c.execute(check_authkey_query,
                  (data['authkey'], data['faculty_id'])).fetchone()
    if _ is None:
        response = {"status_message": "Unauthorized access",
                    "status_code": 404, "data": "Invalid Authkey provided"}
        return response
    request_params = list(data.keys())
    if 'faculty_id' in request_params and 'department' not in request_params:
        get_data_query = """
            SELECT *FROM Faculty WHERE faculty_id = ?
        """
        f_data = c.execute(get_data_query, (data['faculty_id'], )).fetchone()
        if f_data is not None:
            f_data = dict(
                zip([cur[0] for cur in c.description], f_data))
            response = {"statusmessage": "Successful",
                        "status_code": 200, "data": f_data}
            return response
        else:
            response = {"status_message": "Unsuccessful",
                        "status_code": 301, "data": "data not available"}
    elif 'department' in request_params:
        get_faculty_query = """
            SELECT faculty_id, name FROM faculty WHERE department = ?
        """
        c_data = c.execute(get_faculty_query,
                           (data['department'], )).fetchall()
        print(c_data)
        for i in range(len(c_data)):
            c_data[i] = dict(
                zip([cur[0] for cur in c.description], c_data[i]))
        response = {"statusmessage": "Successful",
                    "status_code": 200, "data": c_data}
        return response
    response = {"statusmessage": "Unsuccessful",
                "status_code": 501, "data": "bad Request"}
    return response


def get_class_details(data):
    conn = sql.connect('database.db')
    check_authkey_query = """
        SELECT *FROM LoginAuthKey WHERE authkey = ? AND faculty_id = ? AND DELETED = 0
    """
    c = conn.cursor()
    _ = c.execute(check_authkey_query,
                  (data['authkey'], data['faculty_id'])).fetchone()
    if _ is None:
        response = {"status_message": "Unauthorized access",
                    "status_code": 404, "data": "Invalid Authkey provided"}
        return response
    get_data_query = """
        SELECT *FROM class WHERE classteacher_id = ?
    """
    c_data = c.execute(get_data_query, (data['faculty_id'])).fetchone()
    if c_data is not None:
        c_data = dict(
            zip([cur[0] for cur in c.description], c_data))
        response = {"statusmessage": "Successful",
                    "status_code": 200, "data": c_data}
        return response


def get_all_class_details(data):
    conn = sql.connect('database.db')
    check_authkey_query = """
        SELECT *FROM LoginAuthKey WHERE authkey = ? AND faculty_id = ? AND DELETED = 0
    """
    c = conn.cursor()
    _ = c.execute(check_authkey_query,
                  (data['authkey'], data['faculty_id'])).fetchone()
    if _ is None:
        response = {"status_message": "Unauthorized access",
                    "status_code": 404, "data": "Invalid Authkey provided"}
        return response
    current_year = datetime.datetime.now().year
    get_class_details_query = """
        SELECT *FROM Class WHERE graduation_year IN (? , ? , ?)
    """
    c_data = c.execute(get_class_details_query, (current_year+1,
                                                 current_year+2, current_year+3)).fetchall()
    print(c_data)
    c_data_keys = c.description
    for i in range(len(c_data)):
        c_data[i] = dict(
            zip([cur[0] for cur in c_data_keys], c_data[i]))
        teacher_id = c_data[i]['classteacher_id']
        get_teacher_data = """
            SELECT name, teacher_picture FROM faculty WHERE faculty_id = ?
        """
        f_data = c.execute(get_teacher_data, (teacher_id, )).fetchone()
        print(teacher_id)
        f_data = dict(
            zip([cur[0] for cur in c.description], f_data))
        c_data[i]['details'] = f_data
    response = {"statusmessage": "Successful",
                "status_code": 200, "data": c_data}
    return response


def add_class(data):
    conn = sql.connect('database.db')
    check_authkey_query = """
        SELECT *FROM LoginAuthKey WHERE authkey = ? AND faculty_id = ? AND DELETED = 0
    """
    c = conn.cursor()
    _ = c.execute(check_authkey_query,
                  (data['authkey'], data['faculty_id'])).fetchone()
    if _ is None:
        response = {"status_message": "Unauthorized access",
                    "status_code": 404, "data": "Invalid Authkey provided"}
        return response
    current_year = datetime.datetime.now().year
    if data['sem'] in ['2', '1']:
        current_year += 3
    elif data['sem'] in ['3', '4']:
        current_year += 2
    elif data['sem'] in ['5', '6']:
        current_year += 1
    get_faculty_id_query = """
        SELECT faculty_id FROM faculty WHERE faculty_id = ? AND name = ?
    """
    f_data = c.execute(get_faculty_id_query,
                       (data['c_id'], data['c_teacher'])).fetchone()
    if f_data is None:
        response = {"status_message": "Incorrect data",
                    "status_code": 501, "data": "Invalid faculty for class teacher"}
        return response
    create_new_class_query = """
        INSERT INTO Class(sem, sec, graduation_year, department, classteacher_id) VALUES(
            ?, ?, ?, ?, ?
        )
    """
    add_faculty_type_query = """
        INSERT INTO Type(type_description, faculty_id) VALUES (? ,?)
    """
    print(f_data)
    try:
        c.execute(create_new_class_query,
                  (data['sem'], data['sec'], current_year, data['department'], f_data[0]))
        c.execute(add_faculty_type_query, ("C", f_data[0]))
        conn.commit()
        response = {"status_message": "successful",
                    "status_code": 200, "data": data}
    except Exception as E:
        response = {"status_message": "Unsuccessful",
                    "status_code": 301, "data": str(E)}
    return response


def get_subjectteacher_details(data):
    conn = sql.connect('database.db')
    check_authkey_query = """
        SELECT *FROM LoginAuthKey WHERE authkey = ? AND faculty_id = ? AND DELETED = 0
    """
    c = conn.cursor()
    _ = c.execute(check_authkey_query,
                  (data['authkey'], data['faculty_id'])).fetchone()
    if _ is None:
        response = {"status_message": "Unauthorized access",
                    "status_code": 404, "data": "Invalid Authkey provided"}
        return response
    get_class_id_query = """
        SELECT *FROM Class WHERE department = ? and sec = ? and graduation_year =? and sem = ?

    """
    class_id_details = c.execute(
        get_class_id_query, (data['dept'], data['sec'], data['graduation_year'], data['sem'])).fetchone()
    if class_id_details is None:
        response = {"statusmessage": "Error",
                    "status_code": 501, "data": "class not found"}
        return response
    get_fcs_details_query = """ 
        SELECT *FROM Fcs WHERE class_id= ?
    """
    print(class_id_details)

    fcs_data = c.execute(get_fcs_details_query,
                         (class_id_details[0],)).fetchall()
    if fcs_data is None:
        response = {"statusmessage": "Error",
                    "status_code": 501, "data": "class not found"}
        return response

    print(fcs_data)
    get_faculty_query = """ 
            SELECT name,teacher_picture FROM Faculty WHERE faculty_id =?
        """
    get_subject_details_query = """
            SELECT *FROM Subject WHERE subject_id = ?
        """
    res = []
    for fcs in fcs_data:
        faculty_name = c.execute(get_faculty_query, (fcs[1],)).fetchone()
        print(faculty_name)

        subject_details = c.execute(
            get_subject_details_query, (fcs[3],)).fetchone()
        print(subject_details)
        if faculty_name is None or subject_details is None:
            response = {"statusmessage": "Error",
                        "status_code": 501, "data": "class not found"}
            return response
        res.append({
            'sem': class_id_details[1], 'name': faculty_name[0], 'subject_name': subject_details[1],
            'subject_code': subject_details[2], 'credits': subject_details[3], 'teacher_picture': faculty_name[1],
            'faculty_id': fcs[1]
        })
    response = {"status_message": "successful",
                "status_code": 200, "data": res}
    return response


def add_subject(data):
    conn = sql.connect('database.db')
    check_authkey_query = """
        SELECT *FROM LoginAuthKey WHERE authkey = ? AND faculty_id = ? AND DELETED = 0
    """
    c = conn.cursor()
    _ = c.execute(check_authkey_query,
                  (data['authkey'], data['faculty_id'])).fetchone()
    if _ is None:
        response = {"status_message": "Unauthorized access",
                    "status_code": 404, "data": "Invalid Authkey provided"}
        return response

    get_class_id_query = """
            SELECT class_id FROM Class WHERE sem = ? and sec = ? and graduation_year=? and department = ?
        """
    add_subject_details = """
        INSERT INTO Subject(subject_name,subject_code,credits) VALUES(?,?,?)
    """
    get_subject_id_query = """
        SELECT subject_id FROM Subject WHERE subject_code = ?
    """
    add_fcs_query = """
            INSERT INTO Fcs(faculty_id,class_id,subject_id, section) VALUES(?,?,?, ?)
    """
    c_id = c.execute(get_class_id_query,
                     (data['sem'], data['sec'], data['year'], data['dept'])).fetchone()
    print(c_id)

    c.execute(add_subject_details,
              (data['subject_name'], data['subjectcode'], data['credits']))
    conn.commit()

    s_id = c.execute(get_subject_id_query, (data['subjectcode'],)).fetchone()
    print(s_id)
    if c_id is None or s_id is None:
        response = {"statusmessage": "Error",
                    "status_code": 501, "data": "class not found"}
        return response
    c.execute(add_fcs_query,
              (data['subjectteacher'], c_id[0], s_id[0], data['sec']))
    conn.commit()
    response = {"status_message": "successful",
                "status_code": 200, "data": "successfully added"}
    return response


def get_year_sem_sec(data):
    conn = sql.connect('database.db')
    print(data)
    check_authkey_query = """
        SELECT *FROM LoginAuthKey WHERE authkey = ? AND faculty_id = ? AND DELETED = 0
    """
    c = conn.cursor()
    _ = c.execute(check_authkey_query,
                  (data['authkey'], data['faculty_id'])).fetchone()
    if _ is None:
        response = {"status_message": "Unauthorized access",
                    "status_code": 404, "data": "Invalid Authkey provided"}
        return response
    param = list(data.keys())

    if 'department' in param and 'year' not in param and 'sem' not in param:
        get_all_year = """ 
            SELECT DISTINCT(graduation_year) FROM Class WHERE department = ?
        """
        year = c.execute(get_all_year, (data['department'],)).fetchall()
        # print(year,"year")
        response = {"status_message": "successful",
                    "status_code": 200, "data": year}
        return response
    elif 'department' in param and 'year' in param and 'sem' not in param:
        get_all_sem = """ 
            SELECT DISTINCT(sem) FROM Class WHERE department = ? and graduation_year = ?
        """
        sem = c.execute(
            get_all_sem, (data['department'], data['year'])).fetchall()
        # print(sem,"sem")
        response = {"status_message": "successful",
                    "status_code": 200, "data": sem}
        return response
    elif 'department' in param and 'year' in param and 'sem' in param and 'sec' not in param:
        get_all_sec = """ 
            SELECT DISTINCT(sec) FROM Class WHERE department = ? and graduation_year = ? and sem = ?
        """
        sec = c.execute(
            get_all_sec, (data['department'], data['year'], data['sem'])).fetchall()
        # print(sec,"section")
        response = {"status_message": "successful",
                    "status_code": 200, "data": sec}
        return response
    elif 'department' in param and 'year' in param and 'sem' in param and 'sec' in param:
        get_class_id = """
            SELECT class_id FROM Class WHERE department = ? AND graduation_year = ? AND sem = ? AND sec = ?
        """
        class_id = c.execute(
            get_class_id, (data['department'], data['year'], data['sem'], data['sec'])).fetchone()
        if class_id is None:
            response = {"statusmessage": "Error",
                        "status_code": 501, "data": "class not found"}
            return response
        class_id = class_id[0]
        get_subjects_query = """
            SELECT Fcs.subject_id, subject_name FROM Fcs, Subject WHERE Fcs.subject_id = Subject.subject_id AND class_id = ?
            AND Fcs.faculty_id = ?
        """
        subjects_data = c.execute(
            get_subjects_query, (class_id, data['faculty_id'])).fetchall()
        print(subjects_data)
        for i in range(len(subjects_data)):
            subjects_data[i] = dict(
                zip([cur[0] for cur in c.description], subjects_data[i]))
        print(subjects_data)
        response = {"status_code": 200,
                    "status_message": "successful", "data": subjects_data}
        return response


def get_student_details(data):
    conn = sql.connect('database.db')
    print(data)
    check_authkey_query = """
        SELECT *FROM LoginAuthKey WHERE authkey = ? AND faculty_id = ? AND DELETED = 0
    """
    c = conn.cursor()
    _ = c.execute(check_authkey_query,
                  (data['authkey'], data['faculty_id'])).fetchone()
    if _ is None:
        response = {"status_message": "Unauthorized access",
                    "status_code": 404, "data": "Invalid Authkey provided"}
        return response
    get_class_id_query = """
            SELECT class_id FROM Class WHERE sem = ? and sec = ? and graduation_year=? and department = ?
        """
    class_data = c.execute(
        get_class_id_query, (data['sem'], data['sec'], data['year'], data['department'])).fetchone()

    if class_data is None:
        response = {"statusmessage": "Error",
                    "status_code": 501, "data": "class not found"}
        return response
    class_id = class_data[0]
    get_fcs_ids_query = """
        SELECT Fcs.fcs_id, subject_name, Fcs.subject_id FROM Fcs, Subject WHERE class_id = ? AND Fcs.subject_id = Subject.subject_id
    """

    fcs_details = c.execute(get_fcs_ids_query, (class_id, )).fetchall()
    subject_details = [{"subject_id": i[2], "subject_name": i[1]}
                       for i in fcs_details]
    for i in range(len(fcs_details)):
        fcs_details[i] = dict(
            zip([cur[0] for cur in c.description], fcs_details[i]))
    print("FCS details", fcs_details)

    student_details_query = """
        SELECT Fcss.student_id, name, usn, Subject.subject_id, subject_name FROM Fcss, Student, Fcs, Subject WHERE Fcss.student_id = Student.student_id AND Fcs.fcs_id = Fcss.fcs_id AND Fcs.subject_id = Subject.subject_id AND Fcss.fcs_id IN (""" + ", ".join(['?' for i in subject_details]) + """ ) """
    student_details = c.execute(student_details_query, [
                                i['fcs_id'] for i in fcs_details]).fetchall()
    print("Student", student_details)
    final_student_details = []
    for student_id, order_iter in itertools.groupby(sorted(student_details, key=lambda x: x[0]), lambda x: x[0]):
        each_student_detail = list(order_iter)
        print(each_student_detail)
        enrolled_subjects = list()
        for i in each_student_detail:
            enrolled_subjects.append(
                {"subject_id": i[3], "subject_name": i[4]})
        student_data = {
            "student_id": student_id,
            "student_name": each_student_detail[0][1],
            "student_usn": each_student_detail[0][2],
            "subjects_enrolled": enrolled_subjects
        }
        final_student_details.append(student_data)
    print()
    print("final details", final_student_details)
    return {"status_message": "success", "status_code": 200, "data": {"student_details": final_student_details, "subject_details": subject_details}}

    # student_details_query = """
    #     SELECT Fcss.student_id, name, usn FROM Fcss, Student WHERE fcs_id = ? AND Fcss.student_id = Student.student_id
    # """
    # complete_student_details = []
    # for each_fcs_detail in fcs_details:
    #     fcs_id = each_fcs_detail['fcs_id']
    #     student_details = c.execute(student_details_query, (fcs_id, )).fetchall()


def add_student(data):
    """function to add student"""
    conn = sql.connect('database.db')
    print(data)
    check_authkey_query = """
        SELECT *FROM LoginAuthKey WHERE authkey = ? AND faculty_id = ? AND DELETED = 0
    """
    c = conn.cursor()
    _ = c.execute(check_authkey_query,
                  (data['authkey'], data['faculty_id'])).fetchone()
    if _ is None:
        response = {"status_message": "Unauthorized access",
                    "status_code": 404, "data": "Invalid Authkey provided"}
        return response
    get_class_id_query = """
            SELECT class_id FROM Class WHERE sem = ? and sec = ? and graduation_year=? and department = ?
        """
    class_data = c.execute(
        get_class_id_query, (data['sem'], data['sec'], data['year'], data['department'])).fetchone()
    if class_data is None:
        response = {"statusmessage": "Error",
                    "status_code": 501, "data": "class not found"}
        return response
    class_id = class_data[0]
    get_fcs_id_query = """
        SELECT fcs_id FROM Fcs WHERE class_id = ? AND subject_id = ?
    """
    fcs_ids = []
    for each_subject_id in data['enrolled_subjects']:
        fcs_id_res = c.execute(
            get_fcs_id_query, (class_id, each_subject_id)).fetchone()
        if fcs_id_res is None:
            response = {"statusmessage": "Error",
                        "status_code": 501, "data": "subject and class IDs invalid"}
            return response
        fcs_ids.append(fcs_id_res[0])
    insert_student_query = """
        INSERT INTO Student(name, usn, batch, class_id, blood_group, father_name, phone_no, parent_mail, permanent_address, current_address, c10th_res, c12th_res, student_picture) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    c.execute(insert_student_query, (data['name'], data['usn'], data['year'], class_id, data['blood_group'], data['fathername'], data['contact_no'],
                                     data['email_id'], data['permanent_address'], data['current_address'], data['c10_res'], data['c12_res'], data['picture']))

    student_id = c.lastrowid

    insert_fcss_query = """
        INSERT INTO Fcss(fcs_id, student_id) VALUES (?, ?)
    """
    for fcs_id in fcs_ids:
        c.execute(insert_fcss_query, (fcs_id, student_id))
    conn.commit()

    return {"msg": "success"}


def get_student_attendance_details(data):
    conn = sql.connect('database.db')
    print(data)
    check_authkey_query = """
        SELECT *FROM LoginAuthKey WHERE authkey = ? AND faculty_id = ? AND DELETED = 0
    """
    c = conn.cursor()
    _ = c.execute(check_authkey_query,
                  (data['authkey'], data['faculty_id'])).fetchone()
    if _ is None:
        response = {"status_message": "Unauthorized access",
                    "status_code": 404, "data": "Invalid Authkey provided"}
        return response
    get_class_id_query = """
            SELECT class_id FROM Class WHERE sem = ? and sec = ? and graduation_year=? and department = ?
        """
    class_data = c.execute(
        get_class_id_query, (data['sem'], data['sec'], data['year'], data['department'])).fetchone()

    if class_data is None:
        response = {"statusmessage": "Error",
                    "status_code": 501, "data": "class not found"}
        return response
    class_id = class_data[0]
    get_fcs_ids_query = """
        SELECT Fcs.fcs_id FROM Fcs WHERE class_id = ? AND subject_id = ?
    """

    fcs_details = c.execute(
        get_fcs_ids_query, (class_id, data['subject_id'])).fetchone()
    if fcs_details is None:
        response = {"statusmessage": "Error",
                    "status_code": 501, "data": "fcs not found"}
        return response
    fcs_details = fcs_details[0]
    get_student_details_from_fcss_query = """
        SELECT Fcss.student_id, Student.name, Student.usn FROM Fcss, Student WHERE Fcss.student_id = Student.student_id AND fcs_id = ?
    """
    student_data = c.execute(
        get_student_details_from_fcss_query, (fcs_details, )).fetchall()
    for i in range(len(student_data)):
        student_data[i] = dict(
            zip([cur[0] for cur in c.description], student_data[i]))
    print(student_data)
    response = {"status_code": 200,
                "status_message": "successful", "data": student_data}
    return response


def add_student_attendance(data):
    conn = sql.connect('database.db')
    print(data)
    check_authkey_query = """
        SELECT *FROM LoginAuthKey WHERE authkey = ? AND faculty_id = ? AND DELETED = 0
    """
    c = conn.cursor()
    _ = c.execute(check_authkey_query,
                  (data['authkey'], data['faculty_id'])).fetchone()
    if _ is None:
        response = {"status_message": "Unauthorized access",
                    "status_code": 404, "data": "Invalid Authkey provided"}
        return response
    get_class_id_query = """
            SELECT class_id FROM Class WHERE sem = ? and sec = ? and graduation_year=? and department = ?
        """
    class_data = c.execute(
        get_class_id_query, (data['data']['sem'], data['data']['sec'], data['data']['year'], data['data']['department'])).fetchone()

    if class_data is None:
        response = {"statusmessage": "Error",
                    "status_code": 501, "data": "class not found"}
        return response
    class_id = class_data[0]
    get_fcs_ids_query = """
        SELECT Fcs.fcs_id FROM Fcs WHERE class_id = ? AND subject_id = ?
    """

    fcs_details = c.execute(
        get_fcs_ids_query, (class_id, data['data']['subject_id'])).fetchone()
    if fcs_details is None:
        response = {"statusmessage": "Error",
                    "status_code": 501, "data": "fcs not found"}
        return response
    fcs_details = fcs_details[0]
    student_data = data['data']['student_data']
    for i in range(len(student_data)):
        get_fcss_id_query = """
            SELECT fcss_id FROM Fcss WHERE fcs_id = ? AND student_id = ?
        """
        fcss_id = c.execute(get_fcss_id_query, (fcs_details,
                                                student_data[i]['student_id'])).fetchone()
        if fcss_id is None:
            response = {"statusmessage": "Error",
                        "status_code": 501, "data": "fcss not found"}
            return response
        fcss_id = fcss_id[0]
        student_data[i]['fcss_id'] = fcss_id
    todays_date = datetime.date.today()
    add_attendance_query = """
            INSERT INTO Attendance(fcss_id, hour, date, status) VALUES (?, ?, ? , ?)
        """
    for each_student in student_data:
        c.execute(add_attendance_query,
                  (each_student['fcss_id'], data['data']['hour_no'], todays_date, each_student['attendance']))
        if not each_student['attendance']:
            get_phoneno_mail_query = """
                SELECT Student.phone_no, Student.parent_mail FROM Student, Fcss WHERE Fcss.fcss_id = ? AND Fcss.student_id = Student.student_id
            """
            st_data = c.execute(get_phoneno_mail_query,
                                (each_student['fcss_id'], )).fetchone()
            phone_no, emailid = st_data
            helper.sendsms(phone_no, data['data']['hour_no'])
            helper.main(emailid, data['data']['hour_no'])
    conn.commit()
    response = {"msg": "success"}
    return response


def get_attendance_details(data):
    conn = sql.connect('database.db')
    print(data)
    check_authkey_query = """
        SELECT *FROM LoginAuthKey WHERE authkey = ? AND faculty_id = ? AND DELETED = 0
    """
    c = conn.cursor()
    _ = c.execute(check_authkey_query,
                  (data['authkey'], data['faculty_id'])).fetchone()
    if _ is None:
        response = {"status_message": "Unauthorized access",
                    "status_code": 404, "data": "Invalid Authkey provided"}
        return response
    params = data.keys()
    find_month = None
    if 'attendance_month' in params:
        find_month = data['attendance_month']
    else:
        find_month = datetime.date.today().month
    get_class_id_query = """
            SELECT class_id FROM Class WHERE sem = ? and sec = ? and graduation_year=? and department = ?
        """
    class_data = c.execute(
        get_class_id_query, (data['sem'], data['sec'], data['year'], data['department'])).fetchone()

    if class_data is None:
        response = {"statusmessage": "Error",
                    "status_code": 501, "data": "class not found"}
        return response
    class_id = class_data[0]
    get_fcs_ids_query = """
        SELECT Fcs.fcs_id FROM Fcs WHERE class_id = ? AND subject_id = ?
    """

    fcs_details = c.execute(
        get_fcs_ids_query, (class_id, data['subject_id'])).fetchone()
    if fcs_details is None:
        response = {"statusmessage": "Error",
                    "status_code": 501, "data": "fcs not found"}
        return response
    fcs_details = fcs_details[0]
    get_attendance_detail = """
        SELECT Student.name, Student.usn, Attendance.status, strftime('%d', Attendance.date) FROM Fcss, Student, Attendance WHERE Student.student_id = Fcss.student_id AND Attendance.fcss_id = Fcss.fcss_id AND Fcss.fcs_id = ? AND strftime('%m', Attendance.date) = ?
    """
    attendance_data = c.execute(
        get_attendance_detail, (fcs_details, str(find_month).zfill(2))).fetchall()
    print(attendance_data)
    now = datetime.datetime.now()
    no_of_days = calendar.monthrange(now.year, find_month)[1]
    usn_hash_map = sorted(list(set([(i[1], i[0]) for i in attendance_data])))
    no_of_rows = len(usn_hash_map)
    attendance_matrix = [
        [-1 for i in range(no_of_days)] for j in range(no_of_rows)]
    print(no_of_days, no_of_rows)
    for i in range(len(attendance_data)):
        print(int(attendance_data[i][3]))
        if attendance_data[i][2] == 1:
            attendance_matrix[usn_hash_map.index(
                (attendance_data[i][1], attendance_data[i][0]))][int(attendance_data[i][3])-1] = 1
        else:
            attendance_matrix[usn_hash_map.index(
                (attendance_data[i][1], attendance_data[i][0]))][int(attendance_data[i][3])-1] = 0
    for i in attendance_matrix:
        print(i)
    return_data = {
        "student_details": usn_hash_map,
        "no_of_days": no_of_days,
        "attendance_matrix": attendance_matrix
    }
    response = {"msg": "success", 'data': return_data}
    return response


def add_question_paper_pattern(data):
    conn = sql.connect('database.db')
    print(data)
    check_authkey_query = """
        SELECT *FROM LoginAuthKey WHERE authkey = ? AND faculty_id = ? AND DELETED = 0
    """
    c = conn.cursor()
    _ = c.execute(check_authkey_query,
                  (data['authkey'], data['faculty_id'])).fetchone()
    if _ is None:
        response = {"status_message": "Unauthorized access",
                    "status_code": 404, "data": "Invalid Authkey provided"}
        return response
    get_class_id_query = """
            SELECT class_id FROM Class WHERE sem = ? and sec = ? and graduation_year=? and department = ?
        """
    class_data = c.execute(
        get_class_id_query, (data['sem'], data['sec'], data['year'], data['department'])).fetchone()

    if class_data is None:
        response = {"statusmessage": "Error",
                    "status_code": 501, "data": "class not found"}
        return response
    class_id = class_data[0]
    get_fcs_ids_query = """
        SELECT Fcs.fcs_id FROM Fcs WHERE class_id = ? AND subject_id = ?
    """

    fcs_details = c.execute(
        get_fcs_ids_query, (class_id, data['subject_id'])).fetchone()
    if fcs_details is None:
        response = {"statusmessage": "Error",
                    "status_code": 501, "data": "fcs not found"}
        return response
    fcs_id = fcs_details[0]
    all_counter = 0
    get_no_of_tests = "SELECT COUNT(*) AS num FROM Tests WHERE fcs_id = ? AND test_no <> -1"
    current_test_data = c.execute(get_no_of_tests, (fcs_id, )).fetchone()
    all_counter = current_test_data[0]
    if data['for'] == 'all':
        test_no_updated = int(all_counter) + 1
        test_name = f"Assessment {test_no_updated}"
    else:
        test_no_updated = -1
        test_name = f"Assessment n"
    add_test_details_query = """
        INSERT INTO Tests(fcs_id, test_no, qp_pattern) VALUES(?, ?, ?)
    """
    test_data = {
        "for_whom": data['for'],
        "name": test_name,
        "details": data['q_pattern_data']
    }
    binary_test_set_obj = pickle.dumps(test_data)
    c.execute(add_test_details_query,
              (fcs_id, test_no_updated, binary_test_set_obj))
    conn.commit()
    response = {"status_message": "success", "status_code": 200}
    return response


def get_student_marks_details(data):
    conn = sql.connect('database.db')
    print(data)
    check_authkey_query = """
        SELECT *FROM LoginAuthKey WHERE authkey = ? AND faculty_id = ? AND DELETED = 0
    """
    c = conn.cursor()
    _ = c.execute(check_authkey_query,
                  (data['authkey'], data['faculty_id'])).fetchone()
    if _ is None:
        response = {"status_message": "Unauthorized access",
                    "status_code": 404, "data": "Invalid Authkey provided"}
        return response
    get_class_id_query = """
            SELECT class_id FROM Class WHERE sem = ? and sec = ? and graduation_year=? and department = ?
        """
    class_data = c.execute(
        get_class_id_query, (data['sem'], data['sec'], data['year'], data['department'])).fetchone()

    if class_data is None:
        response = {"statusmessage": "Error",
                    "status_code": 501, "data": "class not found"}
        return response
    class_id = class_data[0]
    get_fcs_ids_query = """
        SELECT Fcs.fcs_id FROM Fcs WHERE class_id = ? AND subject_id = ?
    """

    fcs_details = c.execute(
        get_fcs_ids_query, (class_id, data['subject_id'])).fetchone()
    if fcs_details is None:
        response = {"statusmessage": "Error",
                    "status_code": 501, "data": "fcs not found"}
        return response
    fcs_details = fcs_details[0]
    get_student_details_from_fcss_query = """
        SELECT Fcss.fcss_id, Fcss.student_id, Student.name, Student.usn FROM Fcss, Student WHERE Fcss.student_id = Student.student_id AND fcs_id = ?
    """
    student_data = c.execute(
        get_student_details_from_fcss_query, (fcs_details, )).fetchall()
    for i in range(len(student_data)):
        student_data[i] = dict(
            zip([cur[0] for cur in c.description], student_data[i]))
        student_data[i]['assessments'] = []
    get_tests_data_query = """
        SELECT *FROM tests WHERE fcs_id = ?
    """
    tests_data = c.execute(get_tests_data_query, (fcs_details, )).fetchall()
    get_student_results_query = """
        SELECT *FROM Test_res WHERE fcss_id = ? AND test_id = ?
    """
    for i in range(len(tests_data)):
        tests_data[i] = dict(
            zip([cur[0] for cur in c.description], tests_data[i]))
    count_of_for_all = sum(
        [1 for i in range(len(tests_data)) if int(tests_data[i]['test_no']) != -1])
    assessment_counter = 1
    temp2 = dict()
    for each_test_details in tests_data:
        q_pattern = each_test_details['qp_pattern']
        q_pattern = pickle.loads(q_pattern)
        for_whom = q_pattern['for_whom']
        print(for_whom)
        print()
        for each_student in student_data:
            temp = temp2.get(each_student['student_id'], [])
            fcss_id = each_student['fcss_id']
            student_marks = c.execute(
                get_student_results_query, (fcss_id, each_test_details['test_id'])).fetchone()
            if for_whom == 'all' or for_whom == each_student['student_id']:
                if for_whom == 'all':
                    assessment_name = q_pattern['name']
                else:
                    assessment_name = f"Assessment {count_of_for_all + 1}"
                if student_marks is None:
                    each_student['assessments'] = each_student.get(
                        'assessments', [])
                    # each_student['assessments'][q_pattern['details']['assessment_name']] = None
                    if for_whom == "all":
                        each_student['assessments'].append({
                            "fcss_id": fcss_id,
                            "data_found": False,
                            "name": assessment_name,
                            "test_id": each_test_details['test_id'],
                            "q_pattern": q_pattern['details']
                        })
                    else:
                        temp.append({
                            "fcss_id": fcss_id,
                            "data_found": False,
                            "name": assessment_name,
                            "test_id": each_test_details['test_id'],
                            "q_pattern": q_pattern['details']
                        })

                else:
                    student_marks = dict(
                        zip([cur[0] for cur in c.description], student_marks))
                    student_marks['marks'] = pickle.loads(
                        student_marks['marks'])
                    each_student['assessments'] = each_student.get(
                        'assessments', [])
                    if for_whom == "all":
                        each_student['assessments'].append({
                            "fcss_id": fcss_id,
                            "data_found": True,
                            "name": assessment_name,
                            "test_id": each_test_details['test_id'],
                            "marks": student_marks['marks']
                        })
                    else:
                        temp.append({
                            "fcss_id": fcss_id,
                            "data_found": True,
                            "name": assessment_name,
                            "test_id": each_test_details['test_id'],
                            "marks": student_marks['marks']
                        })
            temp2[each_student['student_id']] = temp
        assessment_counter += 1
    print(temp2)
    for i in range(len(student_data)):
        student_data[i]['assessments'].extend(
            temp2.get(student_data[i]['student_id'], []))
    print(student_data)
    final_data = dict()
    final_data['student_data'] = student_data
    response = {"status_code": 200,
                "status_message": "successful", "data": final_data}
    return response


def add_student_res(data):
    conn = sql.connect('database.db')
    print(data)
    check_authkey_query = """
        SELECT *FROM LoginAuthKey WHERE authkey = ? AND faculty_id = ? AND DELETED = 0
    """
    c = conn.cursor()
    _ = c.execute(check_authkey_query,
                  (data['authkey'], data['faculty_id'])).fetchone()
    if _ is None:
        response = {"status_message": "Unauthorized access",
                    "status_code": 404, "data": "Invalid Authkey provided"}
        return response
    insert_student_result_query = """
        INSERT INTO Test_res(fcss_id, test_id, marks) VALUES(?, ?, ?)
    """
    marks_object = pickle.dumps(data['result_data'])
    c.execute(insert_student_result_query,
              (data['fcss_id'], data['test_id'], marks_object))
    conn.commit()
    response = {"status_message": "successful", "status_code": 200}
    return response


def get_complete_faculty_details(data):
    conn = sql.connect('database.db')
    print(data)
    check_authkey_query = """
        SELECT *FROM LoginAuthKey WHERE authkey = ? AND faculty_id = ? AND DELETED = 0
    """
    c = conn.cursor()
    _ = c.execute(check_authkey_query,
                  (data['authkey'], data['faculty_id'])).fetchone()
    if _ is None:
        response = {"status_message": "Unauthorized access",
                    "status_code": 404, "data": "Invalid Authkey provided"}
        return response
    if 'f_id' in data.keys():
        data['faculty_id'] = data['f_id']
    get_complete_faculty_details_query = """
        SELECT * FROM Faculty WHERE faculty_id = ? 
    """
    get_area_of_specialisation_query = """
        SELECT specialisation_details FROM AreaOfSpecialisation Where faculty_id = ?
    """
    get_qualification_query = """
        SELECT * FROM FacultyQualification WHERE faculty_id = ?
    """
    get_experience_query = """
        SELECT * FROM WorkExperience WHERE faculty_id = ?
    """
    get_publication_query = """
        SELECT publication_details FROM Publications WHERE faculty_id = ?
    """
    get_paper_query = """
        SELECT research_paper_details FROM ResearchPaper WHERE faculty_id = ?
    """
    get_invited_talk_query = """
        SELECT invited_talk_details FROM InvitedTalks WHERE  faculty_id = ?
    """
    get_session_query = """
        SELECT session_chair_details FROM SessionChair WHERE faculty_id = ?
    """
    get_workshop_details_query = """
        SELECT workshop_type , workshop_details FROM Workshops WHERE faculty_id = ? 
    """
    faculty_details = c.execute(
        get_complete_faculty_details_query, (data['faculty_id'],)).fetchone()
    area_of_spec = c.execute(
        get_area_of_specialisation_query, (data['faculty_id'],)).fetchall()
    qualification = c.execute(get_qualification_query,
                              (data['faculty_id'],)).fetchall()
    experience = c.execute(get_experience_query,
                           (data['faculty_id'],)).fetchall()
    publication = c.execute(get_publication_query,
                            (data['faculty_id'],)).fetchall()
    paper = c.execute(get_paper_query, (data['faculty_id'],)).fetchall()
    invited_talks = c.execute(get_invited_talk_query,
                              (data['faculty_id'],)).fetchall()
    sessions = c.execute(get_session_query, (data['faculty_id'],)).fetchall()
    workshops = c.execute(get_workshop_details_query,
                          (data['faculty_id'],)).fetchall()
    area = " ".join([i[0] for i in area_of_spec])
    paper = [i[0] for i in paper]
    publication = [i[0] for i in publication]
    invited_talks = [i[0] for i in invited_talks]
    sessions = [i[0] for i in sessions]
    print(faculty_details)

    response = {
        'status_code': 200,
        'status_message': 'successfull',
        'data': {
            'name': faculty_details[1],
            'dept': faculty_details[4],
            'date_of_joining': faculty_details[6],
            'dob': faculty_details[8],
            'phone': faculty_details[5],
            'email': faculty_details[2],
            'marital_status': faculty_details[10],
            'gender': faculty_details[9],
            'address': faculty_details[11],
            'designation': faculty_details[13],
            'association_with_institute': faculty_details[14], 'experience_in_years': faculty_details[7],
            'area_of_spec': area,
            'qualification': qualification,
            'experience': experience,
            'paper': paper,
            'publications': publication,
            'invitedtalks': invited_talks,
            'sessions': sessions,
            "workshops": workshops,
            'image': faculty_details[12]
        }
    }
    return response


def get_complete_faculty(data):
    conn = sql.connect('database.db')
    # print(data)
    check_authkey_query = """
        SELECT *FROM LoginAuthKey WHERE authkey = ? AND faculty_id = ? AND DELETED = 0
    """
    c = conn.cursor()
    _ = c.execute(check_authkey_query,
                  (data['authkey'], data['faculty_id'])).fetchone()
    if _ is None:
        response = {"status_message": "Unauthorized access",
                    "status_code": 404, "data": "Invalid Authkey provided"}
        return response

    params = data.keys()

    if 'check_approval' in params:
        faculty_details_query = """
        SELECT F.faculty_id , name , department, teacher_picture , email_id , t.type_description FROM Faculty F , Type t WHERE approved = 0 
        AND F.faculty_id = t.faculty_id
        """
        faculty_details = c.execute(faculty_details_query).fetchall()
    else:
        faculty_details_query = """
            SELECT faculty_id , name , department, teacher_picture FROM Faculty 
        """
        faculty_details = c.execute(faculty_details_query).fetchall()
    print(faculty_details)
    response = {
        "statusmessage": "Successfull",
        "status_code": 200, "data": faculty_details
    }
    return response


def approve__decline(data):
    conn = sql.connect('database.db')
    # print(data)
    check_authkey_query = """
        SELECT *FROM LoginAuthKey WHERE authkey = ? AND faculty_id = ? AND DELETED = 0
    """
    c = conn.cursor()
    _ = c.execute(check_authkey_query,
                  (data['authkey'], data['faculty_id'])).fetchone()
    if _ is None:
        response = {"status_message": "Unauthorized access",
                    "status_code": 404, "data": "Invalid Authkey provided"}
        return response

    if data['status'] == 1:
        approve_query = """
        UPDATE Faculty SET approved = 1 WHERE faculty_id = ?
        """
        c.execute(approve_query, (data['f_id'],))
        message = "approved"
        conn.commit()
    elif data['status'] == 0:
        decline_query = """
            DELETE FROM Faculty WHERE faculty_id = ?
        """
        c.execute(decline_query, (data['f_id'],))
        conn.commit()
        message = "Declined"
    response = {
        "statusmessage": "Successfull",
        "status_code": 200, "data": message
    }
    return response


def get_class_marks(data):
    conn = sql.connect('database.db')
    check_authkey_query = """
        SELECT *FROM LoginAuthKey WHERE authkey = ? AND faculty_id = ? AND DELETED = 0
    """
    c = conn.cursor()
    _ = c.execute(check_authkey_query,
                  (data['authkey'], data['faculty_id'])).fetchone()
    if _ is None:
        response = {"status_message": "Unauthorized access",
                    "status_code": 404, "data": "Invalid Authkey provided"}
        return response
    get_class_id_query = """
            SELECT class_id FROM Class WHERE sem = ? and sec = ? and graduation_year=? and department = ?
        """
    class_data = c.execute(
        get_class_id_query, (data['sem'], data['sec'], data['graduation_year'], data['dept'])).fetchone()

    if class_data is None:
        response = {"statusmessage": "Error",
                    "status_code": 501, "data": "class not found"}
        return response
    class_id = class_data[0]
    get_all_subjects_query = """
        SELECT Fcs.fcs_id, Subject.subject_id, subject_name FROM Subject, Fcs WHERE Fcs.subject_id = Subject.subject_id AND class_id = ? ORDER BY 2
    """
    get_test_details_query = """
        SELECT Tests.test_id, qp_pattern FROM Tests WHERE fcs_id = ? AND test_no <> -1 ORDER BY 1
    """
    get_students_from_fcs_id = """
        SELECT fcss_id, Student.student_id, Student.name, Student.usn FROM Fcss, Student WHERE Fcss.student_id = Student.student_id AND fcs_id = ? ORDER BY 4 ASC
    """
    get_student_marks_query = """ 
        SELECT marks FROM Test_res WHERE test_id = ? AND fcss_id = ?
    """
    final_student_data = dict()
    subject_dict = dict()
    get_all_subjects_data = c.execute(
        get_all_subjects_query, (class_id, )).fetchall()
    print(get_all_subjects_data)
    for fcs_id, sub_id, sub_name in get_all_subjects_data:
        co = 0
        student_data = c.execute(
            get_students_from_fcs_id, (fcs_id, )).fetchall()
        assessments_data = c.execute(
            get_test_details_query, (fcs_id, )).fetchall()
        for test_id, qp_pattern in assessments_data:
            unserialised_pattern = pickle.loads(qp_pattern)
            test_name = unserialised_pattern['name']
            sub_tests_data = []
            max_marks_dict = dict()
            for each_sub_test in unserialised_pattern['details']:
                sub_test_type = each_sub_test['test_set_type']
                if each_sub_test['test_set_eval_type'] == 'Descriptive':
                    max_marks = (int(each_sub_test['questions_details']['no_of_questions'])//2) * int(
                        each_sub_test['questions_details']['max_marks_per_question'])
                else:
                    max_marks = int(
                        each_sub_test['questions_details']['max_marks'])
                max_marks_dict[each_sub_test['test_set_name']] = max_marks
                sub_tests_data.append(
                    {"test_type": sub_test_type, "max_marks": max_marks, "test_name": each_sub_test['test_set_name']})
            test_marks_dict = {"name": test_name, "sub_marks": sub_tests_data}
            co += len(sub_tests_data)
            subject_dict[sub_id] = subject_dict.get(sub_id, dict())
            append_to_subjects = subject_dict[sub_id].get("marks", [])
            append_to_subjects.append(test_marks_dict)
            subject_dict[sub_id]['marks'] = append_to_subjects
            for fcss_id, stud_id, stud_name, stud_usn in student_data:
                print(stud_name)
                print()
                get_student_marks = c.execute(
                    get_student_marks_query, (test_id, fcss_id)).fetchone()
                if get_student_marks is not None:
                    marks = pickle.loads(get_student_marks[0])
                    print(marks)
                    marks_data = []
                    for each_marks_set in marks:
                        if each_marks_set['test_res_type'] == 'Descriptive':
                            marks_secured = each_marks_set['total_marks_obtained']
                            max_possible_marks = max_marks_dict[each_marks_set['test_set_name']]
                        elif each_marks_set['test_res_type'] == 'Consolidated':
                            marks_secured = each_marks_set['marks_secured']
                            max_possible_marks = each_marks_set['max_marks']
                        marks_data.append(
                            {"name": each_marks_set['test_set_name'], "marks_secured": int(marks_secured), 'max_marks': int(max_possible_marks)})
                else:
                    marks_data = []
                    for each_test_set in sub_tests_data:
                        marks_data.append(
                            {"name": each_test_set['test_name'], "marks_secured": 0, 'max_marks': each_test_set['max_marks']})
                final_student_data[stud_id] = final_student_data.get(
                    stud_id, {"student_name": stud_name, "student_usn": stud_usn, "student_id": stud_id, "marks": dict()})
                final_student_data[stud_id]['marks'][sub_id] = final_student_data[stud_id]['marks'].get(
                    sub_id, {"subject_id": sub_id, "subject_name": sub_name, "assessment": []})
                final_student_data[stud_id]['marks'][sub_id]['assessment'].append(
                    {"test_id": test_id, "test_name": test_name, "details": marks_data})
        subject_dict[sub_id] = subject_dict.get(sub_id, dict())
        subject_dict[sub_id]['marks'] = subject_dict[sub_id].get("marks", [])
        subject_dict[sub_id]['count'] = co
        subject_dict[sub_id]['name'] = sub_name
    p.pprint(final_student_data)
    p.pprint(subject_dict)
    viewia_data = {"student_data": final_student_data, "subject_data": subject_dict}
    # print(unserialised_pattern)
    response = {"status_code": 200,
                "status_message": "successful", "data": viewia_data}
    return response


def reset__password(data):
    conn = sql.connect('database.db')
    generate_otp_query = """
     INSERT INTO OTP(email,otp) VALUES (?,?)
    """
    get_otp_query = """
        SELECT otp FROM OTP WHERE email =?
    """
    delete_query = """
        DELETE FROM OTP WHERE email = ?
    """
    update_query = """
        UPDATE Faculty SET password = ? WHERE email_id = ?
    """
    c = conn.cursor()
    params = data.keys()
    print(params)
    if 'email' in params and 'otp' not in params and 'pass' not in params:
        otp = "".join(["{}".format(random.randint(0, 9)) for i in range(0, 6)])
        print(otp)
        c.execute(delete_query, (data['email'],))
        conn.commit()
        c.execute(generate_otp_query, (data['email'], otp))
        conn.commit()
        helper.sendotp(data['email'], otp)
        response = {"status_message": "Sucess",
                    "status_code": 200}
    elif 'email' in params and 'otp' in params:
        print('reset')
        value = c.execute(get_otp_query, (data['email'],)).fetchone()
        print(value)
        if data['otp'] == value[0]:
            c.execute(delete_query, (data['email'],))
            conn.commit()
            response = {"status_message": "Authorization Suceess",
                        "status_code": 200, }
        else:
            response = {"status_message": "Unauthorized access",
                        "status_code": 404, "data": "Invalid Authkey provided"}
    elif 'pass' in params and 'email' in params and 'otp' not in params:
        print(data)
        c.execute(update_query, (data['pass'], data['email']))
        conn.commit()
        print("updated")
        response = {"status_message": "Authorization Suceess",
                    "status_code": 200, }
    else:
        response = {"status_message": "Unauthorized access",
                    "status_code": 404, "data": "Invalid Authkey provided"}
    return response


def submit__batch(data):
    print(data)
    response = {"status_message": "Unauthorized access",
                "status_code": 404, "data": "Invalid Authkey provided"}
    return response

def submit__feedback(data):
    print(data)
    conn = sql.connect('database.db')
    check_authkey_query = """
        SELECT *FROM LoginAuthKey WHERE authkey = ? AND faculty_id = ? AND DELETED = 0
    """
    get_faculty_name_query = """
        SELECT name FROM Faculty WHERE faculty_id = ?
    """
    c = conn.cursor()
    _ = c.execute(check_authkey_query,
                  (data['authkey'], data['faculty_id'])).fetchone()
    if _ is None:
        response = {"status_message": "Unauthorized access",
                    "status_code": 404, "data": "Invalid Authkey provided"}
        return response
    faculty_name = c.execute(get_faculty_name_query,(data['faculty_id'],)).fetchone()
    faculty_name=faculty_name[0]
    feedback = data['feedback']
    page = data['location'].split('/')[-1]
    time = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    df = pd.read_csv('feedback.csv')
    feedback_list = [{'name':faculty_name,'feedback':feedback,'location':page,'time':time}]
    df = df.append(feedback_list)
    df.to_csv('feedback.csv',index = False)
    print(page)
    print(time)
    print(faculty_name)
    response = {"status_message": "Sucess",
                    "status_code": 200 }
    return response

def get_all_students(data):
    print(data)
    conn = sql.connect('database.db')
    check_authkey_query = """
        SELECT *FROM LoginAuthKey WHERE authkey = ? AND faculty_id = ? AND DELETED = 0
    """
    get_student_name_query ="""
        SELECT student_id,name,usn FROM Student S,Class C WHERE S.class_id = C.class_id AND C.class_id  = (SELECT class_id FROM Class WHERE sem = ? AND sec = ? AND graduation_year = ? AND department = ?) 
    """
    c = conn.cursor()
    _ = c.execute(check_authkey_query,
                  (data['authkey'], data['faculty_id'])).fetchone()
    if _ is None:
        response = {"status_message": "Unauthorized access",
                    "status_code": 404, "data": "Invalid Authkey provided"}
        return response
   
    students = c.execute(get_student_name_query,(data['sem'],data['sec'],data['year'],data['department'])).fetchall()
    print(students)
    if len(students)== 0 :
        response = {"status_message": "Ivalid class id",
                    "status_code": 404, "data": "Invalid class details provided"}
        return response
    else :
        response = {"status_message": "Sucessfull",
                    "status_code": 200 ,'data':students}
        return response

def get_indivisual_student(data):
    print(data)
    conn = sql.connect('database.db')
    check_authkey_query = """
        SELECT *FROM LoginAuthKey WHERE authkey = ? AND faculty_id = ? AND DELETED = 0
    """
    get_student_details_query = """
        SELECT * FROM Student WHERE student_id = ?
    """
    c = conn.cursor()
    _ = c.execute(check_authkey_query,
                  (data['authkey'], data['faculty_id'])).fetchone()
    if _ is None:
        response = {"status_message": "Unauthorized access",
                    "status_code": 404, "data": "Invalid Authkey provided"}
        return response
    student = c.execute(get_student_details_query,(data['student_id'],)).fetchone()
    print(student)
    response = {"status_message": "sucess",
                    "status_code": 200, 
                    "data": {'name':student[1],'usn':student[2],'bloodgroup':student[5],
                    'parent_name':student[6],'phone':student[7],'email':student[8],'p_address':student[9],
                    'c_address':student[10],'10':student[11],'12':student[12],
                    'student_pic':student[13]}
                }
    return response
