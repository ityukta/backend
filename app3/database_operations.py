"""
contains functions to perform all database operations
"""
import sqlite3 as sql
import string
import random


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
            teacher_picture BLOB NULL,
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

    create_workshops_table = """
        CREATE TABLE IF NOT EXISTS Workshops(
            workshop_id INTEGER PRIMARY KEY AUTOINCREMENT,
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
            student_picture BLOB NOT NULL,
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
            marks BLOB NOT NULL,
            FOREIGN KEY(fcss_id) REFERENCES Fcss(fcss_id) ON DELETE SET NULL
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
        c.execute(insert_faculty_type_query,
                  (data['type_description'], faculty_id))
        conn.commit()
        conn.close()
        response = {"status_message": "successful",
                    "status_code": 200, "data": data}
    except Exception as E:
        response = {"status_message": "Unsuccessful",
                    "status_code": 301, "data": str(E)}
    return response


def validate_login(data):
    """ Function to validate initial register"""
    conn = sql.connect('database.db')
    get_login_credentials_query = """
        SELECT *FROM Faculty WHERE email_id = ? AND password = ?
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
        print("facultydet", faculty_details)
        if(faculty_details['approved'] == 0):
            response = {"status_message": "Unsuccessful", "status_code": 301,
                        "data": "User Still not approved, contact admin"}
        else:
            insert_login_authkey_query = """
                INSERT INTO LoginAuthKey(authkey, faculty_id) VALUES (? , ?)
            """
            random_authkey = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(16))
            c.execute(insert_login_authkey_query, (random_authkey, faculty_details['faculty_id']))
            conn.commit()
            response = {"status_message": "Successful",
                        "status_code": 200, "authkey": random_authkey, "data": faculty_details}
    conn.close()
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
    _ = c.execute(check_authkey_query, (data['authkey'], data['faculty_id'])).fetchone()
    if _ is None:
        response = {"status_message": "Unauthorized access", "status_code": 404, "data": "Invalid Authkey provided"}
        return response
    get_data_query = """
        SELECT *FROM Faculty WHERE faculty_id = ?
    """
    f_data = c.execute(get_data_query, (data['faculty_id'], )).fetchone()
    if f_data is not None:
        f_data = dict(
            zip([cur[0] for cur in c.description], f_data))
        response = {"statusmessage": "Successful", "status_code":200, "data": f_data}
        return response
    else:
         response = {"status_message": "Unsuccessful", "status_code": 301, "data": "data not available"}

def get_class_details(data):
    conn = sql.connect('database.db')
    check_authkey_query = """
        SELECT *FROM LoginAuthKey WHERE authkey = ? AND faculty_id = ? AND DELETED = 0
    """
    c = conn.cursor()
    _ = c.execute(check_authkey_query, (data['authkey'], data['faculty_id'])).fetchone()
    if _ is None:
        response = {"status_message": "Unauthorized access", "status_code": 404, "data": "Invalid Authkey provided"}
        return response
    get_data_query =  """
        SELECT *FROM class WHERE classteacher_id = ?
    """
    c_data = c.execute(get_data_query, (data['faculty_id'])).fetchone()
    if c_data is not None:
        c_data = dict(
            zip([cur[0] for cur in c.description], c_data))
        response = {"statusmessage": "Successful", "status_code":200, "data": c_data}
        return response
