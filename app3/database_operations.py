"""
contains functions to perform all database operations
"""
import sqlite3 as sql
import string
import random
import datetime


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
                c.execute(insert_education_details_query, (degree, branch, educational_institution, percentage, year_of_passing, university, inp_faculty_id))
        elif attrs == 'work_experience':
            work_experience
    conn.commit()
    response = {"msg": "successful"}
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
            random_authkey = ''.join(random.SystemRandom().choice(
                string.ascii_uppercase + string.digits) for _ in range(16))
            c.execute(insert_login_authkey_query,
                      (random_authkey, faculty_details['faculty_id']))
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
            SELECT name FROM faculty WHERE faculty_id = ?
        """
        f_data = c.execute(get_teacher_data, (teacher_id, )).fetchone()
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
        SELECT *FROM Class WHERE department = ? and sec = ? and graduation_year = ?

    """
    class_id_details = c.execute(get_class_id_query,(data['dept'],data['sec'],data['graduation_year'])).fetchone()
    if class_id_details is None:
        response = {"statusmessage": "Error",
                "status_code": 501, "data": "class not found"}
        return response
    get_fcs_details_query = """ 
        SELECT *FROM Fcs WHERE class_id= ?
    """
    print(class_id_details)

    fcs_data= c.execute(get_fcs_details_query,(class_id_details[0],)).fetchall()
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
        faculty_name = c.execute(get_faculty_query,(fcs[1],)).fetchone()
        print(faculty_name)

        subject_details = c.execute(get_subject_details_query,(fcs[3],)).fetchone()
        print(subject_details)
        if faculty_name is None  or subject_details is None:
            response = {"statusmessage": "Error",
                    "status_code": 501, "data": "class not found"}
            return response
        res.append({
            'sem' : class_id_details[1] , 'name':faculty_name[0] , 'subject_name' : subject_details[1] , 
            'subject_code': subject_details[2] , 'credits':subject_details[3] , 'teacher_picture':faculty_name[1], 
            'faculty_id':fcs[1]
            })
    response = {"status_message": "successful",
                    "status_code": 200, "data": res}
    return response

def add_subject(data):
    conn = sql.connect('database.db')
   
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
            INSERT INTO Fcs(faculty_id,class_id,subject_id) VALUES(?,?,?)
    """
    c= conn.cursor()
    
   

    c_id = c.execute(get_class_id_query,(data['sem'],data['sec'],data['year'],data['dept'])).fetchone()
    print(c_id)



    c.execute(add_subject_details,(data['subject_name'],data['subjectcode'],data['credits']))
    conn.commit()

    s_id = c.execute(get_subject_id_query,(data['subjectcode'],)).fetchone()
    print(s_id)
    if c_id is None or s_id is None:
        response = {"statusmessage": "Error",
                    "status_code": 501, "data": "class not found"}
        return response
    c.execute(add_fcs_query,(data['subjectteacher'],c_id[0],s_id[0]))
    conn.commit()
    response = {"status_message": "successful",
                    "status_code": 200, "data": "successfully added"}
    return response




    

    