# Patient Record System

| | |
|---|---|
| **Module** | PROG211 – Object-Oriented Programming 1 |
| **Assignment** | Real-World Solutions under DPG Standards (Individual, 10%) |
| **Domain** | Health – Patient Record System |
| **Institution** | Limkokwing University of Creative Technology, Sierra Leone |
| **Student** |  Zeyad Mohamed Elgabry / 905005887
| **Examiner** | Amandus Benjamin Coker |

A simple Python program that manages patient records using Object-Oriented Programming. It lets a clinic register patients, assign them to a department, record follow-up visits and discharge them, while keeping the stored personal data to a minimum.

---

## 1. The Real-World Problem

Many small clinics still keep patient information in paper registers. Paper records are slow to search, easy to lose, and hard to keep organised when the same patient returns several times. This program offers a lightweight digital alternative that runs on any computer, needs no internet connection and no paid software.

## 2. Features

- Register a new patient (name, age, district, condition, department)
- Automatic unique patient ID (`PT-001`, `PT-002`, ...)
- Record follow-up visits (blocked for discharged patients)
- Discharge a patient
- Update a patient's record
- Display all patients in a readable format
- Input validation (letters-only text fields, age range, valid department)
- Starts with an empty record list and goes straight to the menu, so no patient data is shown until it is entered
- Optional built-in demo (menu option 5) that creates sample patients and shows objects interacting

## 3. How the Code Meets the Assignment Tasks

| Task | Requirement | Where it is in the code |
|------|-------------|--------------------------|
| **Task 1** | At least two classes with attributes and methods | `Department` (`department.py`) and `Patient` (`patient.py`) |
| **Task 1** | Object creation and interaction between objects | A `Patient` stores a `Department` object, and `Patient.display_info()` calls `Department.display_info()` |
| **Task 2** | One data structure (list or dictionary) | A **dictionary** `{patient_id: Patient}` created in `main()` |
| **Task 2** | Function to add and display records | `add_patient()` and `display_patients()` in `patient_record_system.py` |
| **Task 2 (bonus)** | Tuples | `DEPARTMENTS` in `department.py` is a tuple of `(department name, ward)` tuples |
| **Task 3** | At least one instance method | `Patient`: `add_visit()`, `update_record()`, `discharge()`, `display_info()`; `Department`: `display_info()` |
| **Task 3** | At least one class method (`@classmethod`) | `Patient.get_total_patients()` and `Department.from_list()` |
| **Task 3** | Static methods | `Patient.validate_text()`, `Patient.validate_age()` and `Department.available_departments()` |

### Class overview

**`Department`** (`department.py`)

| Attribute | Meaning |
|-----------|---------|
| `name` | Department name, e.g. `Pediatrics` |
| `ward` | Ward / location, e.g. `Ward B` |

**`Patient`** (`patient.py`)

| Attribute | Meaning |
|-----------|---------|
| `patient_id` | Auto-generated unique ID (`PT-001`) |
| `name` | Patient name (letters only) |
| `age` | Whole number from 0 to 120 |
| `district` | Broad area, not a full address |
| `condition` | General description of the condition |
| `department` | A `Department` object |
| `visits` | Number of visits (starts at 1) |
| `status` | `ADMITTED` or `DISCHARGED` |
| `total_patients` | Class attribute: counter shared by all patients |

## 4. Digital Public Goods (DPG) Alignment

| DPG Principle | How this project meets it |
|---------------|---------------------------|
| **Open-source** | The complete source code is published in this public GitHub repository, so anyone can read, copy, test and improve it. |
| **Inclusive and accessible design** | Runs on any computer with Python 3, with no internet connection, paid libraries or special hardware. It uses a simple numbered text menu, plain English messages and plain-text output that works with screen readers. Clear error messages guide users who enter wrong input. |
| **Privacy-respecting** | See section 5 below. |
| **Modular and reusable** | Each class lives in its own file (`department.py`, `patient.py`) and is imported into the main program, so a class can be edited or reused in another project without touching the rest. Departments are defined in one tuple, so the system can be adapted to another clinic by editing a single place. |

## 5. Privacy and Data Minimisation

The assignment requires that **no sensitive personal data is stored**. This project follows the principle of *data minimisation*: it keeps only what is needed to identify and manage a patient record.

**What is stored**

- Patient **name** (the only direct identifier)
- Age
- District (a broad area)
- A general condition label
- Department, visit count and status

**What is deliberately NOT stored**

- Phone numbers, email addresses
- Home or street addresses
- National ID or passport numbers
- Photos, biometric data, or financial information

**Additional privacy measures**

- **Nothing is displayed at start-up.** The program opens with an empty record list and shows records only after the user adds them (or chooses the optional demo).
- **Records stay in memory only.** Nothing is written to disk or sent over a network, so no patient data remains after the program closes.
- **The name is not used for lookups.** Every operation (visit, discharge) uses the anonymous ID (`PT-001`), so the name does not need to be typed or exposed.
- **Input validation** (`validate_text()` and `validate_age()`) rejects invalid or unexpected data before it is stored.
- **All sample data in this repository is fictional.**
- For real deployment, the name field could be replaced by initials or removed entirely, since the system works with the ID alone.

## 6. Requirements

- Python 3.8 or newer
- No external libraries

## 7. How to Run

```bash
git clone https://github.com/<your-username>/<your-repository>.git
cd <your-repository>
python patient_record_system.py
```

The program starts directly with the interactive menu and an **empty** record list. Nothing is displayed until you add patients. Menu option 5 runs an optional demo with fictional sample data.

## 8. Example Usage (sample input / output)

### Part A – Demo (menu option 5)

```text
===== DEMO: creating objects =====
Patient PT-001 added.
Patient PT-002 added.
Patient PT-003 added.

===== DEMO: interaction between objects =====
  [+] Visit recorded for PT-001 (total visits: 2).
  [+] Visit recorded for PT-002 (total visits: 2).
  [-] PT-003 has been discharged.
  [!] PT-003 is discharged. Re-admit first.
  [~] Record PT-001 updated.

===== ALL PATIENT RECORDS (3) =====
Patient ID : PT-001
  Name       : John Doe
  Age        : 34
  District   : Port Loko
  Condition  : Malaria (recovering)
  Department : General Medicine
  Location   : Ward A
  Visits     : 2
  Status     : ADMITTED
----------------------------------------
Patient ID : PT-003
  Name       : Bob Johnson
  Age        : 27
  District   : Kenema
  Condition  : Prenatal care
  Department : Maternity
  Location   : Ward C
  Visits     : 1
  Status     : DISCHARGED
----------------------------------------
Total patients (class method)       : 3
Departments (static method)         : ['General Medicine', 'Pediatrics', 'Maternity', 'Surgery', 'Emergency']
```

_(Patient PT-002 is also displayed in the full output.)_

### Part B – Interactive menu (starts empty)

```text
===== PATIENT RECORD SYSTEM =====
1. Add new patient
2. Add a visit
3. Discharge patient
4. Display all patients
5. Run demo (sample data)
6. Exit
Choose an option (1-6): 4
No records to display.

Choose an option (1-6): 1
Name: Ahmed Bangura
Age: 40
District: Bombali
Condition: Fever
Departments: General Medicine, Pediatrics, Maternity, Surgery, Emergency
Department: Surgery
Patient PT-001 added.

Choose an option (1-6): 2
Patient ID (e.g. PT-001): PT-001
  [+] Visit recorded for PT-001 (total visits: 2).

Choose an option (1-6): 3
Patient ID (e.g. PT-001): PT-001
  [-] PT-001 has been discharged.
```

### Part C – Input validation

```text
Choose an option (1-6): 1
Name: Ahmed1
  [!] Name must contain letters only. try again.
```

## 9. Project Structure

```text
<your-repository>/
├── department.py              # Department class + DEPARTMENTS tuple
├── patient.py                 # Patient class
├── patient_record_system.py   # Main program (dictionary, functions, demo, menu)
└── README.md                  # Documentation
```

## 10. Limitations and Future Improvements

- Records are kept in memory only and are lost when the program closes (this is intentional for privacy, but a future version could add encrypted storage).
- Re-admitting a discharged patient is not yet implemented.
- A search-by-district feature could be added.

## 11. License

MIT License – free to use, modify and share.
