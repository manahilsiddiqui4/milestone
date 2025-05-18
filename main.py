from faker import Faker

def hundred_employee_data():
    fake = Faker()
    employees = []

    for i in range(100):
        employee = {
            "id": i + 1,
            "name": fake.name(),
            "email": fake.email(),
            "phone_number": fake.phone_number(),
            "address": fake.address(),
            "job": fake.job(),
        }
        employees.append(employee)

    return employees

employee_data = hundred_employee_data()


for emp in employee_data[:100]:
    print(emp)
