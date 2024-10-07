employees = [
("John Doe", "Accounting", "john.doe@example.com"),
("Jane Smith", "Marketing", "jane.smith@example.com"),
("Emily Davis", "HR", "emily.davis@example.com"),
("Michael Brown", "IT", "michael.brown@example.com")
]

for i in range(len(employees)):
  print(f"{employees[i][0]} - {employees[i][1]}")
  
print("================================== Second ============================")

# 2. Print the email addresses of all employees in alphabetical order by their last names.

def emails():
  email_list = []
  for i in range(len(employees)):
    email_list.append(employees[i][2])
    
  return sorted(email_list, key=lambda email: email.split('.')[1])

print(emails())

print("================================== Third ============================")

# 3. Add a new employee ("David Wilson", "Sales", "david.wilson@example.com")
# and print the updated list.

employees.append(("David Wilson", "Sales", "david.wilson@example.com"))

print(employees)


print("================================== Fouth ============================")

# 4. Find and print the department of "Jane Smith".

for i in range(len(employees)):
  if(employees[i][0] == "Jane Smith"):
    print(employees[i][1])
    break
