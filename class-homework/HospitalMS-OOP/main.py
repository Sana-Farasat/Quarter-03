class Hospital:
    def __init__(self, name):
        self.name = name
        self.doctors = []
        self.patients = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)
        print(f"Doctor {doctor.name} added.")

    def remove_doctor(self, doctor_name):
        for doc in self.doctors:
            if doc.name == doctor_name:
                self.doctors.remove(doc)
                print(f"Doctor {doctor_name} removed.")
                return
        print("Doctor not found!")

    def add_patient(self, patient):
        self.patients.append(patient)
        print(f"Patient {patient.name} added.")

    def remove_patient(self, patient_name):
        for pat in self.patients:
            if pat.name == patient_name:
                self.patients.remove(pat)
                print(f"Patient {patient_name} removed.")
                return
        print("Patient not found!")

    def display_info(self):
        print(f"\n--- Hospital: {self.name} ---")
        print("\nDoctors:")
        for doc in self.doctors:
            print(doc)
        print("\nPatients:")
        for pat in self.patients:
            print(pat)


class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization

    def __str__(self):
        return f"Doctor Name: {self.name}, Specialization: {self.specialization}"


class Patient:
    def __init__(self, name, disease):
        self.name = name
        self.disease = disease

    def __str__(self):
        return f"Patient Name: {self.name}, Disease: {self.disease}"


# Making instance
hospital = Hospital("City Hospital")

# Add doctors
d1 = Doctor("Sana", "Pediatrics")
d2 = Doctor("Ahmed", "Cardiology")
hospital.add_doctor(d1)
hospital.add_doctor(d2)

# Add patients
p1 = Patient("Tania", "Fever")
p2 = Patient("Rania", "Heart Disease")
hospital.add_patient(p1)
hospital.add_patient(p2)

# Display all hospital data
hospital.display_info()

# Remove one doctor and one patient
hospital.remove_doctor("Ahmed")
hospital.remove_patient("Rina")

# Display updated data
hospital.display_info()
