# L-7-3
employee_data = {
    101: [(1, 5000), (2, 7000), (3, 6000)],  
    102: [(4, 8000), (5, 9000), (6, 6500)],  
    103: [(7, 7500), (8, 5000), (9, 9500)]   
}


dept_salary = {}


for dept_no, employees in employee_data.items():
    
    salaries = [salary for roll_no, salary in employees]
    
    
    min_salary = min(salaries)
    max_salary = max(salaries)
    

    dept_salary[dept_no] = {'Min Salary': min_salary, 'Max Salary': max_salary}

for dept_no, salary_info in dept_salary.items():
    print(f"Department {dept_no}: Min Salary = {salary_info['Min Salary']}, Max Salary = {salary_info['Max Salary']}")
