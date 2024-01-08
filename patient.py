class Patient:
    def __init__(self, first_name, last_name, pers_num_code, disease):
        if not isinstance(first_name, str):
            raise ValueError("'first_name' should be a string.")
        if not isinstance(last_name, str):
            raise ValueError("'last_name' should be a string.")
        if not isinstance(pers_num_code, int):
            raise ValueError("'pers_num_code' should be an integer.")
        if not isinstance(disease, str):
            raise ValueError("'disease' should be a string.")
        if int(str(pers_num_code)[0]) not in {1, 2, 5, 6}:
            raise ValueError("chosen 'pers_num_code' does not meet expected properties.")
        if len(str(pers_num_code)) != 13:
            raise ValueError("chosen 'pers_num_code' does not meet expected properties.")

        self.first_name = first_name
        self.last_name = last_name
        self.pers_num_code = pers_num_code
        self.disease = disease

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_pers_num_code(self):
        return self.pers_num_code

    def set_pers_num_code(self, pers_num_code):
        self.pers_num_code = pers_num_code

    def get_disease(self):
        return self.disease

    def set_disease(self, disease):
        self.disease = disease

    def get_age(self):
        pers_num_code = str(self.pers_num_code)
        digits = []
        for digit in pers_num_code:
            digits.append(int(digit))
        if digits[0] == 5 or digits[0] == 6:
            if digits[1] == 0:
                age = 23 - digits[2]
            else:
                age = 23 - ((digits[1]*10) + digits[2])
        elif digits[0] == 1 or digits[0] == 2:
            if digits[1] == 0:
                age = 123 - digits[2]
            else:
                age = 123 - ((digits[1]*10) + digits[2])
        return age

    def __str__(self):
        return f"{self.first_name} {self.last_name} with identity number {self.pers_num_code}, suffering of {self.disease}"