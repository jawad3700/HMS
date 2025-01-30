class Patient:
    def __init__(self, patient_id, name, age, gender, disease):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.disease = disease

class Doctor:
    def __init__(self, doctor_id, name, specialty):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty

class Appointment:
    def __init__(self, appointment_id, patient, doctor, date, time):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time

class HospitalManagement:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []

    def add_patient(self):
        patient_id = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        age = int(input("Enter Patient Age: "))
        gender = input("Enter Patient Gender (M/F): ")
        disease = input("Enter Disease: ")

        new_patient = Patient(patient_id, name, age, gender, disease)
        self.patients.append(new_patient)
        print(f"Patient {name} added successfully!\n")

    def add_doctor(self):
        doctor_id = input("Enter Doctor ID: ")
        name = input("Enter Doctor Name: ")
        specialty = input("Enter Doctor Specialty: ")

        new_doctor = Doctor(doctor_id, name, specialty)
        self.doctors.append(new_doctor)
        print(f"Doctor {name} added successfully!\n")

    def book_appointment(self):
        patient_id = input("Enter Patient ID: ")
        doctor_id = input("Enter Doctor ID: ")
        date = input("Enter Appointment Date (DD/MM/YYYY): ")
        time = input("Enter Appointment Time (HH:MM): ")

        patient = None
        doctor = None

        for p in self.patients:
            if p.patient_id == patient_id:
                patient = p
                break

        for d in self.doctors:
            if d.doctor_id == doctor_id:
                doctor = d
                break

        if patient and doctor:
            appointment_id = len(self.appointments) + 1
            new_appointment = Appointment(appointment_id, patient, doctor, date, time)
            self.appointments.append(new_appointment)
            print(f"Appointment booked successfully with Dr. {doctor.name}!\n")
        else:
            print("Patient or Doctor not found. Please check IDs.\n")

    def list_patients(self):
        if not self.patients:
            print("No patients in the system.\n")
            return
        print("List of Patients:")
        for patient in self.patients:
            print(f"ID: {patient.patient_id}, Name: {patient.name}, Age: {patient.age}, Gender: {patient.gender}, Disease: {patient.disease}")
        print()

    def list_doctors(self):
        if not self.doctors:
            print("No doctors in the system.\n")
            return
        print("List of Doctors:")
        for doctor in self.doctors:
            print(f"ID: {doctor.doctor_id}, Name: {doctor.name}, Specialty: {doctor.specialty}")
        print()

    def list_appointments(self):
        if not self.appointments:
            print("No appointments booked.\n")
            return
        print("List of Appointments:")
        for appointment in self.appointments:
            print(f"Appointment ID: {appointment.appointment_id}, Patient: {appointment.patient.name}, Doctor: {appointment.doctor.name}, Date: {appointment.date}, Time: {appointment.time}")
        print()

def main():
    hospital = HospitalManagement()

    while True:
        print("Hospital Management System")
        print("1. Add Patient")
        print("2. Add Doctor")
        print("3. Book Appointment")
        print("4. List Patients")
        print("5. List Doctors")
        print("6. List Appointments")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            hospital.add_patient()
        elif choice == "2":
            hospital.add_doctor()
        elif choice == "3":
            hospital.book_appointment()
        elif choice == "4":
            hospital.list_patients()
        elif choice == "5":
            hospital.list_doctors()
        elif choice == "6":
            hospital.list_appointments()
        elif choice == "7":
            print("Exiting Hospital Management System.")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
