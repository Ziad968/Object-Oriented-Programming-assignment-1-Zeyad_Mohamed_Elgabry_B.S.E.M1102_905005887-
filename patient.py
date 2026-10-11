class Patient:
    """One anonymous patient record."""

    total_patients = 0  # class attribute shared by all patients

    def __init__(self, name, age, district, condition, department):
        if not Patient.validate_text(name):
            raise ValueError("Name cannot be empty.")
        if not Patient.validate_age(age):
            raise ValueError("Age must be a whole number between 0 and 120.")

        Patient.total_patients += 1
        # Attributes
        self.patient_id = f"PT-{Patient.total_patients:03d}"
        self.name = name
        self.age = age
        self.district = district
        self.condition = condition
        self.department = department   # a Department object (object interaction)
        self.visits = 1
        self.status = "ADMITTED"

    # ---- Instance methods -------------------------------------------------
    def add_visit(self):
        """Record a follow-up visit (not allowed for discharged patients)."""
        if self.status == "DISCHARGED":
            print(f"  [!] {self.patient_id} is discharged. Re-admit first.")
            return
        self.visits += 1
        print(f"  [+] Visit recorded for {self.patient_id} (total visits: {self.visits}).")

    def update_record(self,name=None, age=None, district=None, condition=None):
        """Update age, district and/or condition of this patient."""
        if name is not None:
            if not Patient.validate_name(name):
                print("  [!] Invalid name - not updated.")
                return
            self.name = name
        if age is not None:
            if not Patient.validate_age(age):
                print("  [!] Invalid age - not updated.")
                return
            self.age = age
        if district is not None:
            self.district = district
        if condition is not None:
            self.condition = condition
        print(f"  [~] Record {self.patient_id} updated.")

    def discharge(self):
        """Mark the patient as discharged."""
        if self.status == "DISCHARGED":
            print(f"  [!] {self.patient_id} is already discharged.")
            return
        self.status = "DISCHARGED"
        print(f"  [-] {self.patient_id} has been discharged.")

    def display_info(self):
        """Print this patient's record."""
        print(f"Patient ID : {self.patient_id}")
        print(f"  Name       : {self.name}")
        print(f"  Age        : {self.age}")
        print(f"  District   : {self.district}")
        print(f"  Condition  : {self.condition}")
        self.department.display_info()
        print(f"  Visits     : {self.visits}")
        print(f"  Status     : {self.status}")

    # ---- Class method -------------------------------------------
    @classmethod
    def get_total_patients(cls):
        """Return how many patient records have been created so far."""
        return cls.total_patients

    # ---- Static method ------------------------------------------
    @staticmethod
    def validate_text(text):
        cleaned = text.replace(" ", "").replace("-", "")
        return cleaned.isalpha()
    @staticmethod
    def validate_age(age):
        """Check that age is a valid whole number from 0 to 120."""
        return isinstance(age, int) and 0 <= age <= 120

