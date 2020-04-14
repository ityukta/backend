import sqlite3 as sql
import csv
import os
import base64
import requests


def writestudentdata(path, csv_file):
    conn = sql.connect('database.db')
    insert_query = """
        INSERT INTO student(name,usn,batch,class_id,blood_group,father_name,phone_no,parent_mail,permanent_address,current_address,c10th_res,c12th_res,student_picture)
        VALUES (? ,? ,? ,? ,? ,? ,? , ? ,? , ? , ?, ? ,?)
    """
    get_class_id_query = """
        SELECT class_id FROM Class WHERE sem = ? AND sec = ? AND graduation_year = ? AND department = ?
    """
    get_fcs_id_query = """
        SELECT fcs_id FROM Fcs WHERE class_id = ? AND subject_id IN ?
    """
    insert_into_fcss_query = """
        INSERT INTO Fcss(fcs_id, student_id) VALUES (?, ?)
    """
    c = conn.cursor()

    img = dict()
    for i in sorted(os.listdir(path)):
        with open(os.path.join(path, i), "rb") as imageFile:
            st = base64.b64encode(imageFile.read())
            img[(i.split("-")[0].strip()).upper()] = st
    data = csv_file
    for row in data:
        class_id = c.execute(get_class_id_query, (row['SEM'], row['Section'].upper(
        ), row['Graduation year'], 'ISE')).fetchone()
        # print("donr:")
        c.execute(insert_query, (row['Name'], row['USN'], row['Graduation year'], class_id[0], row['Blood group'], row['Parent/Guardian Name'],
                                 row['Parent/Guardian Phone number'], row['Parent/Guardian Email'], row['Address'], row['Address'], row['10th result'], row['12th result'], img.get(row['USN'].upper(), "")))
        student_id = c.lastrowid
        a = row['Subjects'].split(';')
        question_mark_string = ", ".join(['?' for i in range(len(a))])
        get_subject_id_query = f"""
            SELECT Fcs.fcs_id, Fcs.subject_id FROM Subject, Fcs WHERE Subject_code IN ({question_mark_string}) AND Fcs.subject_id = Subject.subject_id AND Fcs.class_id = ?
        """
        a.append(class_id[0])
        _ = c.execute(get_subject_id_query, tuple(a)).fetchall()
        for fcs_id, subject_id in _:
            c.execute(insert_into_fcss_query, (fcs_id, student_id))
        print(row['Name'], "Done")
    conn.commit()
    conn.close()
