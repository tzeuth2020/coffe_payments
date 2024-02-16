import csv

def add_coffee_entry(employee_name, coffee_price):
    employee_name = ' '.join(employee_name.split())
    logs = read_coffee_logs()
    if employee_name in logs:
        logs[employee_name] += float(coffee_price)
    else:
        logs[employee_name] = float(coffee_price)
    update_coffee_logs(logs)


def read_coffee_logs():
    logs = {}
    try:
        with open('coffee_logs.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                logs[row[0]] = float(row[1])
    except FileNotFoundError:
        pass
    return logs

def update_coffee_logs(logs):
    with open('coffee_logs.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for employee, amount in logs.items():
            writer.writerow([employee, amount])

def choose_payer(logs, total_spent, today_employees):
    today_payers = {employee: amount for employee, amount in logs.items() if employee in today_employees}
    if today_payers:
        payer = max(today_payers, key=today_payers.get)
        amount_paid = total_spent
        logs[payer] -= amount_paid
        update_coffee_logs(logs)
        return payer, amount_paid
    else:
        return None, 0


def main():
    total_spent_today = 0
    today_employees = set()
    while True:
        new_entry = input("Is there an additional coffee order? (yes/no): ")
        if new_entry.lower() == 'yes':
            employee_name = input("Enter the employee's name: ")
            coffee_price = input("Enter the price of their coffee: ")

            #removes trailing whitespace from employee name and price 
            employee_name = ' '.join(employee_name.split())
            coffee_price = ' '.join(coffee_price.split())

            #checks if the coffee price is a valid number and removes the preciding $ if there is one
            if coffee_price.startswith('$'):
                coffee_price = coffee_price[1:]
            try:
                coffee_price = float(coffee_price)
            except ValueError:
                print("Invalid coffee price. Price must be a number.")

            add_coffee_entry(employee_name, coffee_price)
            total_spent_today += float(coffee_price)
            today_employees.add(employee_name)
        else:
            break

    logs = read_coffee_logs()
    payer, amount_paid = choose_payer(logs, total_spent_today, today_employees)
    if payer:
        print(f"{payer} pays ${amount_paid:.2f} for coffee today.")
    else:
        print("No one paid for coffee today.")

if __name__ == "__main__":
    main()
