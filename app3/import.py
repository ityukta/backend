import sqlite3 as sql
import csv
from urllib import request as r
import requests
conn = sql.connect('database.db')

insert_query = """
    INSERT INTO student(name,usn,batch,class_id,blood_group,father_name,phone_no,parent_mail,permanent_address,current_address,c10th_res,c12th_res,student_picture) 
    VALUES (? ,? ,? ,? ,? ,? ,? , ? ,? , ? , ?,? ,?)
 """
get_class_id_query = """
    SELECT class_id FROM Class WHERE sem = ? AND sec = ? AND graduation_year = ? AND department = ?
"""
c = conn.cursor()
f = open('Contact.csv','r')
data = csv.DictReader(f, skipinitialspace = True)
for row in data:
    class_id = c.execute(get_class_id_query,(row['SEM'],row['Section'],row['Graduation year'],'ISE')).fetchone()
  
    c.execute(insert_query,(row['Name'],row['USN'],row['Graduation year'],class_id[0],row['Blood group'],row['Parent Name'], row['Parent Phone'],row['Parent Email'],
    row['Address'],row['Address'],row['10th result'],row['12th result'],row['pic']))
    
conn.commit()
conn.close()  
print(df.Name)
df = pd.read_csv("Contact.csv")
print(text)
import base64

with open("Bhumika V.jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
    print(encoded_string)

conn.close()