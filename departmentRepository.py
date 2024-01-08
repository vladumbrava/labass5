from domain.department import Department
from domain.patient import Patient
import domain.utils as u
class DepartmentRepository:
    def __init__(self):
        self.departments_list = []

    def get_departments_list(self):
        return self.departments_list

    def set_departments_list(self, departments_list):
        self.departments_list = departments_list

    def add_department(self, department):
        if not isinstance(department, Department):
            raise ValueError("'department' should have type Department.")
        for d in self.departments_list:
            if d.id == department.id:
                raise ValueError("'id' is a unique number, there exists another department with the same one.")
            if d.name == department.name:
                raise ValueError("'name' is a unique string, there exists another department with the same one.")
        self.departments_list.append(department)

    def add_patient_to_department(self, patient, department):
        if not isinstance(patient, Patient):
            raise ValueError("'patient' should have type Patient.")
        for dep in self.departments_list:
            if dep.name == department:
                if len(dep.get_patients_list()) == dep.get_num_beds():
                    raise ValueError("there are no beds left in the department.")
                for p in dep.patients_list:
                    if p.pers_num_code == patient.pers_num_code:
                        raise ValueError("'pers_num_code' is a unique number, there exists another patient with the same one.")
                dep.patients_list.append(patient)

    def delete_department(self, name):
        if not isinstance(name, str):
            raise ValueError("'name' should be a string.")
        index = -1
        for i in range(len(self.departments_list)):
            if self.departments_list[i].name == name:
                index = i
                self.departments_list.pop(i)
        if index == -1:
            raise ValueError("there is no department with chosen 'name'")

    def delete_patient_from_department(self, department, first_name, last_name):
        if not isinstance(department, str):
            raise ValueError("'name' should be a string.")
        index = -1
        for i in range(len(self.departments_list)):
            if self.departments_list[i].name == department:
                index = i
        if index == -1:
            raise ValueError("there is no department with chosen 'name'")
        patient_index = -1
        patients_list = self.departments_list[index].get_patients_list()
        for i in range(len(patients_list)):
            patient = patients_list[i]
            if patient.get_first_name() == first_name and patient.get_last_name() == last_name:
                patient_index = i
                break
        if patient_index == -1:
            raise ValueError("there is no patient with chosen 'first_name' and 'last_name' in the department.")
        del patients_list[patient_index]

    def get_department(self, department):
        index = -1
        for i in range(len(self.departments_list)):
            if self.departments_list[i].name == department:
                index = i
        if index == -1:
            raise ValueError("there is no department with chosen 'name'")
        return self.departments_list[index]

    def get_patient_from_department(self, department, first_name, last_name):
        index = -1
        for i in range(len(self.departments_list)):
            if self.departments_list[i].name == department:
                index = i
        if index == -1:
            raise ValueError("there is no department with chosen 'name'")
        patients_list = self.departments_list[index].get_patients_list()
        patient_index = -1
        for i in range(len(patients_list)):
            if patients_list[i].get_first_name() == first_name and patients_list[i].get_last_name() == last_name:
                patient_index = i
        if patient_index == -1:
            raise ValueError("there is no patient with chosen name")
        return patients_list[patient_index]


    def update_department(self, department, id, name, num_beds, patients_list):
        index = -1
        for i in range(len(self.departments_list)):
            if self.departments_list[i].name == department:
                index = i
        if index == -1:
            raise ValueError("there is no department with chosen 'name'")
        self.departments_list[index].set_id(id)
        self.departments_list[index].set_name(name)
        self.departments_list[index].set_num_beds(num_beds)
        self.departments_list[index].set_patients_list(patients_list)

    def update_patient_from_department(self, department, first_name, last_name, updated_patient):
        index = -1
        for i in range(len(self.departments_list)):
            if self.departments_list[i].name == department:
                index = i
        if index == -1:
            raise ValueError("there is no department with chosen 'name'")
        patients_list = self.departments_list[index].get_patients_list()
        patient_index = -1
        for i in range(len(patients_list)):
            if patients_list[i].get_first_name() == first_name and patients_list[i].get_last_name() == last_name:
                patient_index = i
        if patient_index == -1:
            raise ValueError("there is no patient with chosen name")
        patients_list[patient_index] = updated_patient

    def get_age_all_patients(self):
        result = ""
        for dep in self.departments_list:
            for pat in dep.get_patients_list():
                result += f"{pat.get_first_name()} {pat.get_last_name()} ({dep.get_name()}) - {pat.get_age()}\n"
        return result

    def sort_patients_in_department_by_pers_num_code_method(self, department):
        index = -1
        for i in range(len(self.departments_list)):
            if self.departments_list[i].name == department:
                index = i
        if index == -1:
            raise ValueError(f"there is no department named {department}")
        sort_department = self.departments_list[index].patients_list
        return sort_department, lambda patient: patient.pers_num_code

    def sort_departments_by_num_patients_method(self):
        if len(self.departments_list) == 0:
            raise ValueError("'departmentRepository' is empty.")
        return lambda dep: len(dep.get_patients_list())

    def sort_departments_by_num_patients_above_age_method(self, age):
        if not isinstance(age, int):
            raise ValueError("'age' should be a positive integer.")
        if len(self.departments_list) == 0:
            raise ValueError("'departmentRepository' is empty.")
        return lambda dep: sum(1 for patient in dep.get_patients_list() if patient.get_age() > age)

    def sort_patients_alphabetically(self):
        for i in range(len(self.departments_list)):
            if len(self.departments_list[i].patients_list) != 1:
                return lambda patient: (patient.get_last_name(), patient.get_first_name())

    def search_departments_with_patients_under_age(self, max_age):
        if not isinstance(max_age, int):
            raise ValueError("'max_age' should be an integer.")
        search_method = lambda dep: any(patient.get_age() < max_age for patient in dep.get_patients_list())
        result_departments = u.searching(self.departments_list, search_method)
        return result_departments

    def search_patients_from_dep_name_as_string(self, department, string):
        if not isinstance(department, str):
            raise ValueError("'department' should be a string.")
        if not isinstance(string, str):
            raise ValueError("'string' should be a string.")
        index = -1
        for i in range(len(self.departments_list)):
            if self.departments_list[i].name == department:
                index = i
        if index == -1:
            raise ValueError("there is no department with chosen 'name'")
        search_method = lambda pat: (string in pat.get_first_name()) or (string in pat.get_last_name())
        patients_list = self.departments_list[index].get_patients_list()
        result = u.searching(patients_list, search_method)
        return result

    def search_departments_with_patients_with_giv_f_name(self, first_name):
        if not isinstance(first_name, str):
            raise ValueError("'first_name' should be a string.")
        search_method = lambda dep: any(pat.get_first_name() == first_name for pat in dep.get_patients_list())
        result = u.searching(self.departments_list, search_method)
        return result

    def group_patients_by_department_and_disease(self):
        patient_groups = {}
        for department in self.departments_list:
            for patient in department.get_patients_list():
                key = (department.get_name(), patient.get_disease())
                if key not in patient_groups:
                    patient_groups[key] = []

                patient_groups[key].append(patient)

        return patient_groups

    def backtrack_groups(self, elements, k):
        def backtrack(start, current_group):
            if len(current_group) == k:
                result.append(current_group.copy())
                return

            for i in range(start, len(elements)):
                current_group.append(elements[i])

                backtrack(i + 1, current_group)

                current_group.pop()

        result = []
        backtrack(0, [])

        return result

    def __str__(self):
        result = "List of departments: "
        for department in self.departments_list:
            result += f"\n\n{department}"
        return result
