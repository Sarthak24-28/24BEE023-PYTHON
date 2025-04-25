import pickle

employee = {
    "empcode": 101,
    "empname": "Sarthak",
    "doj": "2021-06-15",
    "salary": 75000
}

with open("employee.dat", "wb") as file:
    pickle.dump(employee, file)
    print("Employee data has been serialized to 'employee.dat'.")

with open("employee.dat", "rb") as file:
    loaded_employee = pickle.load(file)
    print("\nDeserialized Employee Data:")
    print("Employee Code:",loaded_employee['empcode'])
    print("Employee Name:",loaded_employee['empname'])
    print("Date of Joining:",loaded_employee['doj'])
    print("Salary:",loaded_employee['salary'])
