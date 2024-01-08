class Department:
    def __init__(self, id, name, num_beds, patients_list):
        if not isinstance(id, int):
            raise ValueError("'id' should be an integer.")
        if not isinstance(name, str):
            raise ValueError("'name' should be a string.")
        if not isinstance(num_beds, int):
            raise ValueError("'num_beds' should be an integer.")
        if not isinstance(patients_list, list):
            raise ValueError("'patients_list' should be a list.")

        self.id = id
        self.name = name
        self.num_beds = num_beds
        self.patients_list = patients_list

    def get_id(self):
        return self.id

    def set_id(self, id):
        if not isinstance(id, int):
            raise ValueError("'id' should be an integer.")
        self.id = id

    def get_name(self):
        return self.name

    def set_name(self, name):
        if not isinstance(name, str):
            raise ValueError("'name' should be a string.")
        self.name = name

    def get_num_beds(self):
        return self.num_beds

    def set_num_beds(self, num_beds):
        if not isinstance(num_beds, int):
            raise ValueError("'num_beds' should be an integer.")
        self.num_beds = num_beds

    def get_patients_list(self):
        return self.patients_list

    def set_patients_list(self, patients_list):
        if not isinstance(patients_list, list):
            raise ValueError("'patients_list' should be a list.")
        self.patients_list = patients_list

    def __str__(self):
        result = "List of patients: "
        for patient in self.patients_list:
            result += f"\n{patient}"
        return f"{self.name} Department\nID: {self.id}\nNumber of beds: {self.num_beds}\n{result}\n{self.num_beds - len(self.patients_list)} available beds"
