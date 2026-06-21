from databse import connect

class Hospital:


    def add_patient(self,name,age,disease):
        db = connect()
        cursor = db.cursor()
        cursor.execute("INSERT INTO patients(name,age,disease) VALUES(?,?,?)",(name,age,disease))
        db.commit()
        db.close()
        print("Patient added")



    def view_patients(self):
        db = connect()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM patients")
        data = cursor.fetchall()

        for p in data:
            print(p)
        db.close()




    def add_doctor(self,name,speciality):
        db = connect()
        cursor = db.cursor()
        cursor.execute( "INSERT INTO doctors(name,speciality) VALUES(?,?)", (name,speciality))
        db.commit()
        db.close()
        print("Doctor added")





    def view_doctors(self):
        db = connect()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM doctors")
        doctors = cursor.fetchall()
        for d in doctors:
            print(d)
        db.close()





    def create_appointment(self,patient,doctor,date):
        db = connect()
        cursor = db.cursor()
        cursor.execute(
      """
        INSERT INTO appointments
        (patient_id,doctor_id,date)

        VALUES(?,?,?)

        """,
        (patient,doctor,date))
        db.commit()
        db.close()
        print("Appointment created")






    def add_record(self,patient,diagnosis,medicine):
        db = connect()
        cursor = db.cursor()
        cursor.execute(
        """
        INSERT INTO records
        (patient_id,diagnosis,medicine)

        VALUES(?,?,?)

        """,
        (patient,diagnosis,medicine)
        )
        db.commit()
        db.close()
        print("Medical record saved")







    def create_bill(self,patient,amount):
        db = connect()
        cursor = db.cursor()
        cursor.execute( "INSERT INTO bills(patient_id,amount) VALUES(?,?)", (patient,amount) )
        db.commit()
        db.close()
        print("Bill created")