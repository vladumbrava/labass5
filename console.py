from domain.patient import Patient
from domain.department import Department
from repository.departmentRepository import DepartmentRepository
import domain.utils as u

def main():
    departmentrepo = DepartmentRepository()
    patient1 = Patient('Vlad','Dumbrava',5050206394422,'boala2')
    patient16 = Patient('Nicu','Dumbrava',5050206394322,'boala2')
    patient2 = Patient('Marinela','Dumbrava',2720102639442,'boala1')
    patient3 = Patient('Gabriel','Dumbrava',1990102639442,'boala1')
    patient4 = Patient('Gigi','Dumbrava',1670102639442,'boala4')
    patient5 = Patient('Andrei','Dumbrava',1900102639442,'boala5')
    patient6 = Patient('Ionut','Dumbrava',1890102639442,'boala6')
    patient7 = Patient('Clara','Dumbrava',2700102639442,'boala7')
    patient8 = Patient('Sorin','Dumbrava',1650102639442,'boala8')
    patient9 = Patient('Gigi','Dumbrava',5060102639442,'boala9')
    patient10 = Patient('Finu','Dumbrava',5060102639422,'boala1')
    patient11 = Patient('Finu1','Dumbrava',5060102639422,'boala2')
    patient12 = Patient('Finu2','Dumbrava',5060102639422,'boala2')
    patient13 = Patient('Finu3','Dumbrava',5060102639422,'boala3')
    patient14 = Patient('Finu4','Dumbrava',5060102639422,'boala3')
    patient15 = Patient('Finu5','Dumbrava',5060102639422,'boala3')
    oncology_list = [patient1, patient2, patient3, patient10, patient11, patient12, patient13, patient14, patient15,patient16]
    ginecology_list = [patient4, patient5, patient6]
    cardiology_list = [patient7, patient8, patient9]
    oncology = Department(1,'Oncology',5,oncology_list)
    ginecology = Department(2,'Ginecology',3,ginecology_list)
    cardiology = Department(3,'Cardiology',6,cardiology_list)
    list_departments = [oncology, ginecology, cardiology]
    departmentrepo.set_departments_list(list_departments)

    while True:
        print("\nMenu")
        print("1. Show departments")
        print("2. Add a department")
        print("3. Add a patient to a department")
        print("4. Delete a department (by name)")
        print("5. Delete a patient from a department (by name)")
        print("6. Update a department (identified by name)")
        print("7. Update a patient from a department (identified by name)")
        print("8. Get the age of all patients")
        print("9. Sort patients in a department by personal numerical code")
        print("10. Sort departments by number of patients")
        print("11. Sort departments by number of patients having age above given limit")
        print("12. Sort departments by number of patients and patients alphabetically")
        print("13. Identify departments with patients under given age")
        print("14. Identify patients from a department for which first name or last name contain given string")
        print("15. Identify departments with patients having given first name")
        print("16. Form groups of 'k' patients from the same department having the same disease")
        print("17. Form groups of 'k' departments having at most 'p' patients suffering from the same disease")

        try:
            choice = int(input("Enter a choice: "))
            if choice == 1:
                print(f"{departmentrepo}\n")
            elif choice == 2:
                try:
                    id = int(input("Enter id: "))
                    name = input("Enter name of department: ")
                    try:
                        num_beds = int(input("Enter number of beds: "))
                        patients_list = []
                        try:
                            departmentrepo.add_department(Department(id, name, num_beds, patients_list))
                        except ValueError as e:
                            print(f"Error: {e}")
                    except ValueError:
                        print("'num_beds' should be an integer.")
                except ValueError:
                    print("Error: 'id' should be an integer.")

            elif choice == 3:
                print(f"Choose from the departments below: \n")
                print(f"{departmentrepo}\n")
                department = input("Enter the name of the department you want your patient into: ")
                first_name = input("Enter first name of patient: ")
                last_name = input("Enter last name of patient: ")
                try:
                    pers_num_code = int(input("Enter PNC: "))
                    disease = input("Enter disease: ")
                    try:
                        patient = Patient(first_name, last_name, pers_num_code, disease)
                        try:
                            departmentrepo.add_patient_to_department(patient,department)
                        except ValueError as er:
                            print(f"Error: {er}")
                    except ValueError as e:
                        print(f"Error: {e}")
                except ValueError:
                    print("Error: 'pers_num_code' should be an integer.")
                print(departmentrepo)

            elif choice == 4:
                print(f"{departmentrepo}\n")
                name = input("Enter the name of the department you want to delete: ")
                try:
                    departmentrepo.delete_department(name)
                except ValueError as e:
                    print(f"Error: {e}")

            elif choice == 5:
                print(f"{departmentrepo}\n")
                department = input("Enter the name of the department: ")
                first_name = input("Enter the first name of the patient you want to remove: ")
                last_name = input("Enter the last name of the patient you want to remove: ")
                try:
                    departmentrepo.delete_patient_from_department(department, first_name, last_name)
                except ValueError as e:
                    print(f"Error: {e}")

            elif choice == 6:
                department = input("Enter the name of the department you want to update: ")
                try:
                    print(departmentrepo.get_department(department))
                    previous_dep = departmentrepo.get_department(department)
                    update_choice = input("Enter the name of the property you want to modify (ID, Name, Number of beds, List of patients): ")
                    if update_choice == "ID":
                        id = int(input("Enter modified ID: "))
                        try:
                            departmentrepo.update_department(department, id, previous_dep.name, previous_dep.num_beds, previous_dep.patients_list)
                        except ValueError as e:
                            print(f"Error: {e}")
                    if update_choice == "Name":
                        name = input("Enter modified name: ")
                        try:
                            departmentrepo.update_department(department, previous_dep.id, name, previous_dep.num_beds, previous_dep.patients_list)
                        except ValueError as e:
                            print(f"Error: {e}")
                    if update_choice == "Number of beds":
                        num_beds = int(input("Enter modified number of beds: "))
                        try:
                            departmentrepo.update_department(department, previous_dep.id, previous_dep.name, num_beds, previous_dep.patients_list)
                        except ValueError as e:
                            print(f"Error: {e}")
                    if update_choice == "List of patients":
                        patients_choice = int(input("Enter '1' to remove the patients or '2' to keep them: "))
                        if patients_choice == 1:
                            try:
                                departmentrepo.update_department(department, previous_dep.id, previous_dep.name, previous_dep.num_beds, [])
                            except ValueError as e:
                                print(f"Error: {e}")
                except ValueError as e:
                    print(f"Error: {e}")

            elif choice == 7:
                department = input("Enter name of department: ")
                first_name = input("Enter first name of patient: ")
                last_name = input("Enter last name of patient: ")
                try:
                    departmentrepo.get_patient_from_department(department, first_name, last_name)
                    mod_first_name = input("Enter modified first name: ")
                    mod_last_name = input("Enter modified last name: ")
                    try:
                        pers_num_code = int(input("Enter modified 'pers_num_code': "))
                        disease = input("Enter modified disease: ")
                        try:
                            patient = Patient(mod_first_name, mod_last_name, pers_num_code, disease)
                            try:
                                departmentrepo.update_patient_from_department(department, first_name, last_name, patient)
                            except ValueError as e:
                                print(f"Error: {e}")
                        except ValueError as e:
                            print(f"Error: {e}")
                    except ValueError as e:
                        print(f"Error: {e}")
                except ValueError as e:
                    print(f"Error: {e}")

            elif choice == 8:
                print(departmentrepo.get_age_all_patients())

            elif choice == 9:
                print(f"Choose from the departments below: \n")
                print(f"{departmentrepo}\n")
                department = input("Enter the name of the department you want to do the sort for: ")
                try:
                    list_patients, method = departmentrepo.sort_patients_in_department_by_pers_num_code_method(department)
                    u.sorting(list_patients,method)
                except ValueError as e:
                    print(f"Error: {e}")

            elif choice == 10:
                try:
                    u.sorting(departmentrepo.departments_list,departmentrepo.sort_departments_by_num_patients_method())
                except ValueError as e:
                    print(f"Error: {e}")

            elif choice == 11:
                try:
                    age = int(input("Enter limit of age: "))
                    try:
                        u.sorting(departmentrepo.departments_list,departmentrepo.sort_departments_by_num_patients_above_age_method(age))
                    except ValueError as e:
                        print(f"Error: {e}")
                except ValueError:
                    print("Error: 'age' should be a positive integer.")

            elif choice == 12:
                try:
                    u.sorting(departmentrepo.departments_list,departmentrepo.sort_departments_by_num_patients_method())
                except ValueError as e:
                    print(f"Error: {e}")
                for i in range(len(departmentrepo.departments_list)):
                    u.sorting(departmentrepo.departments_list[i].patients_list,departmentrepo.sort_patients_alphabetically())

            elif choice == 13:
                age = int(input("Enter maximum age: "))
                try:
                    result = departmentrepo.search_departments_with_patients_under_age(age)
                    for department in result:
                        print(f"{department.get_name()} Department")
                except ValueError as e:
                    print(f"Error: {e}")

            elif choice == 14:
                department = input("Enter department: ")
                string = input("Enter string: ")
                try:
                    result = departmentrepo.search_patients_from_dep_name_as_string(department, string)
                    for patient in result:
                        print(f"{patient.get_first_name()} {patient.get_last_name()}")
                except ValueError as e:
                    print(f"Error: {e}")

            elif choice == 15:
                first_name = input("Enter wanted first name: ")
                try:
                    result = departmentrepo.search_departments_with_patients_with_giv_f_name(first_name)
                    for dep in result:
                        print(f"{dep.get_name()}")
                except ValueError as e:
                    print(f"Error: {e}")

            elif choice == 16:
                k = int(input("Please enter the value for k: "))
                patients_map = departmentrepo.group_patients_by_department_and_disease()
                # for key, patients in patients_map.items():
                #     department_id, disease = key
                #     print(f"Department {department_id}, Disease {disease}:")
                #     for patient in patients:
                #         print(f"  {patient.get_first_name()} {patient.get_last_name()}")

                # key_to_search = ("Oncology","boala2")
                # lista_apc = patients_map.get(key_to_search)
                # print(lista_apc[0])

                for key, patients in patients_map.items():
                    i = 0
                    department_id, disease = key
                    print(f"Department {department_id}, Disease {disease}:")
                    list_of_pac = departmentrepo.backtrack_groups(patients, k)
                    for patient in list_of_pac:
                        i+=1
                        print(f"Group {i}:")
                        for pac in patient:
                            print(f"{pac.get_first_name()} {pac.get_last_name()} ")
                    print("\n")
        except ValueError:
            print("Error: 'choice' should be a positive integer (1-16)")

if __name__ == "__main__":
    main()