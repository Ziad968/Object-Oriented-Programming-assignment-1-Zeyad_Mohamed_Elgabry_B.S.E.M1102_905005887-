DEPARTMENTS = (
    ("General Medicine", "Ward A"),
    ("Pediatrics", "Ward B"),
    ("Maternity", "Ward C"),
    ("Surgery", "Ward D"),
    ("Emergency", "Ward E"),
)

class Department:
    """Represents a hospital department where a patient is treated."""

    def __init__(self, name, ward):
        # Attributes
        self.name = name
        self.ward = ward

    # Instance method
    def display_info(self):
        """Print the department details."""
        print(f"  Department : {self.name}")
        print(f"  Location   : {self.ward}")

    # Class method alternative constructor that reads the tuple
    @classmethod
    def from_list(cls, name):
        """Create a Department object from the DEPARTMENTS tuple."""
        for dept_name, ward in DEPARTMENTS:
            if dept_name.lower() == name.lower():
                return cls(dept_name, ward)
        raise ValueError(f"'{name}' is not a valid department.")

    # Static method utility that needs no object or class data
    @staticmethod
    def available_departments():
        """Return the names of all departments."""
        return [item[0] for item in DEPARTMENTS]

