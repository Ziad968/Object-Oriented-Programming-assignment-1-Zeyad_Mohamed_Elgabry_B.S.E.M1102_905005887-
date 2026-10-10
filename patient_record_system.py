import contextlib
import io

from department import Department
from patient import Patient



# TASK 2: the ONE data structure (a dictionary) + add / display functions
def add_patient(records, patient):
    """Add a Patient to the dictionary using the patient ID as the key."""
    records[patient.patient_id] = patient
    print(f"Patient {patient.patient_id} added.")


def display_patients(records):
    """Loop through the dictionary and display every patient."""
    if not records:
        print("No records to display.")
        return
    print(f"\n===== ALL PATIENT RECORDS ({len(records)}) =====")
    for patient in records.values():
        patient.display_info()
        print("-" * 40)

def seed_demo_patients(records):
    p1 = Patient("John Doe", 34, "Western Area", "Malaria", Department.from_list("General Medicine"))
    p2 = Patient("Jane Smith", 5, "Bo", "Typhoid", Department.from_list("Pediatrics"))
    p3 = Patient("Bob Johnson", 27, "Kenema", "Prenatal care", Department.from_list("Maternity"))

    for p in (p1, p2, p3):
        records[p.patient_id] = p          # بيضيفهم من غير print

    with contextlib.redirect_stdout(io.StringIO()):
        p1.add_visit()
        p2.add_visit()
        p3.discharge()
        p1.update_record(condition="Malaria recovering", district="Port Loko")



def menu(records):
    """Simple text menu so the user can try the program."""
    while True:
        print("\n===== PATIENT RECORD SYSTEM =====")
        print("1. Add new patient")
        print("2. Add a visit")
        print("3. Discharge patient")
        print("4. Display all patients")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            try:
                name = input("Name: ").strip()
                if not Patient.validate_text(name):
                    print("  [!] Name must contain letters only. try again.")
                    raise ValueError("Name must contain letters only.")
                age = int(input("Age: "))
                district = input("District: ").strip()
                if not Patient.validate_text(district):
                    raise ValueError("District must contain letters only.")
                condition = input("Condition: ").strip()
                if not Patient.validate_text(condition):
                    raise ValueError("Condition must contain letters only.")
                print("Departments:", ", ".join(Department.available_departments()))
                dept = Department.from_list(input("Department: ").strip())
                add_patient(records, Patient(name, age, district, condition, dept))
            except ValueError as error:
                print(f"[!] {error}")
        elif choice in ("2", "3"):
            patient_id = input("Patient ID (e.g. PT-001): ").strip().upper()
            if patient_id in records:
                if choice == "2":
                    records[patient_id].add_visit()
                else:
                    records[patient_id].discharge()
            else:
                print("[!] Patient not found.")
        elif choice == "4":
            display_patients(records)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("[!] Invalid choice.")


def main():
    records = {}        # the single data structure of the program
    seed_demo_patients(records) 
    menu(records)


if __name__ == "__main__":
    main()
