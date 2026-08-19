
def totalemployee(emps):
    numofemp = len(emps)
    return numofemp

def calculate_total_salary(emps):
    totalsal = sum(item['salary'] for item in emps)
    return totalsal

def average_salary(numemp,totalsal):
    return totalsal/numemp

def highest_salary(emps):

    most_salary_item = max(emps, key=lambda item: item['salary'])
    print(most_salary_item['name'])
    print(most_salary_item['salary'])


def group_department(emps):
    dep_salary = {}
    dep_count = {}
    for emp in emps:
        
        dep = emp['department']
        if dep not in dep_salary:
            dep_salary[dep] = 0

        if dep not in dep_count:
            dep_count[dep] = 0

        dep_salary[dep] += emp['salary']
        dep_count[dep] += 1
    
    for key, value in dep_salary.items():
        print(key)
        print(f"Employees :  {dep_count[key]}")
        print(f"Salary :  {value:,.0f}")
        print("")

employees = [
    {"id":1,"name":"Somchai","department":"IT","salary":45000},
    {"id":2,"name":"Malee","department":"Finance","salary":52000},
    {"id":3,"name":"Anan","department":"IT","salary":40000},
    {"id":4,"name":"Suda","department":"HR","salary":35000},
    {"id":5,"name":"John","department":"IT","salary":60000},
    {"id":6,"name":"Lisa","department":"Finance","salary":55000},
]

numofemp = totalemployee(employees)
totalsal = calculate_total_salary(employees)
averagesal = average_salary(numofemp,totalsal)

print(f"Total Employees : {numofemp}")
print('')
print(f"Total salaies : {totalsal:,.0f}")
print("")
print(f"Average salaies : {averagesal:,.2f}")
print("")

group_department(employees)
highest_salary(employees)
