from databse import create_tables

from hospital import Hospital



create_tables()


hospital = Hospital()



while True:


    print("""
1. Add Patient
2. View Patients
3. Add Doctor
4. View Doctors
5. Create Appointment
6. Add Medical Record
7. Create Bill
8. Exit

""")


    choice=input("Choose: ")

    if choice=="1":
        name=input("Name: ")
        age=int(input("Age: "))
        disease=input("Disease: ")
        hospital.add_patient(name,age,disease)


    elif choice=="2":
        hospital.view_patients()




    elif choice=="3":
        name=input("Doctor name: ")
        speciality=input("Speciality: ")
        hospital.add_doctor(name,speciality)




    elif choice=="4":
        hospital.view_doctors()


    elif choice=="5":
        patient=int(input("Patient ID: "))
        doctor=int(input("Doctor ID: "))
        date=input("Date: ")
        hospital.create_appointment(patient,doctor,date)


    elif choice=="6":
        patient=int(input("Patient ID: "))
        diagnosis=input("Diagnosis: ")
        medicine=input("Medicine: ")
        hospital.add_record(patient,diagnosis,medicine)



    elif choice=="7":
        patient=int(input("Patient ID: "))
        amount=float(input("Amount: "))
        hospital.create_bill(patient,amount)

    elif choice=="8":
        break
