import sqlite3 as sql
import csv
from urllib import request as r
import requests
import os
import base64

conn = sql.connect('database.db')

insert_query = """
    INSERT INTO student(name,usn,batch,class_id,blood_group,father_name,phone_no,parent_mail,permanent_address,current_address,c10th_res,c12th_res,student_picture) 
    VALUES (? ,? ,? ,? ,? ,? ,? , ? ,? , ? , ?,? ,?)
 """
get_class_id_query = """
    SELECT class_id FROM Class WHERE sem = ? AND sec = ? AND graduation_year = ? AND department = ?
"""
c = conn.cursor()



img= []
for i in sorted(os.listdir('pics'), key=lambda x: os.stat(os.path.join('pics',x)).st_ctime):
    
    with open(os.path.join('pics',i), "rb") as imageFile:
        st = base64.b64encode(imageFile.read())
        img.append(st)
f = open('Contact.csv','r')
i= 0
data = csv.DictReader(f, skipinitialspace = True)
for row in data:
    class_id = c.execute(get_class_id_query,(row['SEM'],row['Section'].upper(),row['Graduation year'],'ISE')).fetchone()
    print(class_id)
    print("donr:")
    c.execute(insert_query,(row['Name'],row['USN'],row['Graduation year'],class_id[0],row['Blood group'],row['Parent Name'], row['Parent Phone'],row['Parent Email'],
    row['Address'],row['Address'],row['10th result'],row['12th result'],img[i]))
    # i+=1
conn.commit()
conn.close()  

