import csv
from cs50 import SQL
open ('projects.db','w').close()
database = SQL("sqlite:///projects.db")

database.execute("CREATE TABLE patients(patient_id INTEGER PRIMARY KEY, patient_name TEXT, insurance_company TEXT)")

database.execute("CREATE TABLE admitted_ward(admission_id INTEGER PRIMARY KEY, ward TEXT, room INTEGER, date_admitted TEXT, date_released TEXT)")

database.execute("CREATE TABLE test(test_id INTEGER PRIMARY KEY, test_name TEXT, test_result TEXT, test_time TEXT,date_tested TEXT)")

database.execute("CREATE TABLE relations(patient_id INTEGER, admission_id INTEGER, test_id INTEGER, FOREIGN KEY(patient_id) REFERENCES patients(patient_id), FOREIGN KEY(admission_id) REFERENCES admitted_ward(admission_id), FOREIGN KEY(test_id) REFERENCES test(test_id))")

with open ('project.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        patient_name = row['patient_name']
        insurance_company = row['insurance_company']
        ward = row['ward']
        room = row['room']
        date_admitted = row['date_admitted']
        date_released = row['date_released']
        test_name = row['test_name']
        test_result = row['test_result']
        test_time = row['test_time']    
        date_tested = row['date_tested']
        #patient_id = row['patient_id']
        #admission_id = row['admission_id']
        #test_id = row['test_id']

        database.execute("INSERT INTO patients(patient_name,insurance_company) VALUES(?,?)",patient_name,insurance_company)
        database.execute("INSERT INTO admitted_ward(ward, room, date_admitted, date_released) VALUES(?,?,?,?)", ward, room, date_admitted, date_released,)
        database.execute("INSERT INTO test(test_name, test_result, test_time, date_tested) VALUES(?,?,?,?)", test_name, test_result, test_time, date_tested)
        database.execute("INSERT INTO relations(patient_id, admission_id, test_id) VALUES((SELECT patient_id FROM patients WHERE patient_name=?),(SELECT admission_id FROM admitted_ward WHERE room=?),(SELECT test_id FROM test WHERE test_name=?))",patient_name, room, test_name)