company_users = {}

while True:
    command = input()
    if command == "End":
        break
    split_command = command.split(" -> ")
    company_name = split_command[0]
    company_number = split_command[1]

    if company_name not in company_users:
        company_users[company_name] = []

    if company_number in company_users[company_name]:
        continue
    else:
        company_users[company_name].append(company_number)

for company_name, company_number in company_users.items():
    print(company_name)
    for number in company_number:
        print(f"-- {number}")
