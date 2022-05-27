if __name__ == '__main__':
    simple_dict={'emp1':{'name': 'Bille', 'salary': 7500},
                 'emp2':{'name': 'Israel', 'salary': 8005},
                 'emp3':{'name': 'Katherine', 'salary': 5010}
                 }
    # salary_emp1 is the salary of emp1
    # salary_emp2 is the salary of emp2
    # salary_emp3 is the salary of emp3
    # Gross_Salary is the total sum of all salaries paid

    salary_emp1 = simple_dict['emp1']['salary']
    print(simple_dict['emp1']['name'] + ' salary  is ' + str(salary_emp1))

    salary_emp2 = simple_dict['emp2']['salary']
    print(simple_dict['emp2']['name'] + ' salary  is ' + str(salary_emp2))

    salary_emp3 = simple_dict['emp3']['salary']
    print(simple_dict['emp3']['name'] + ' salary  is ' + str(salary_emp3))

    Gross_Salary = salary_emp3+salary_emp2+salary_emp1

    print('The Company will pay its staff the total sum of ' + str(Gross_Salary))
    print('=======================================================================')

    # Question B
    subjects = {'Physics': 82, 'Math': 65, 'history': 75}
    key_min = min(subjects, key=subjects.get)
    print('The minimum key is ' + key_min)


