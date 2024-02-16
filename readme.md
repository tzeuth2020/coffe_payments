Coffee Payment System


Overview
The Coffee Payment System is a Python program designed to manage coffee purchases among coworkers at Bertram Labs. It allows users to input coffee purchases for each coworker, keeps track of the total amount spent on coffee, and determines who pays for coffee each day based on a fair calculation.


How it Works
The program takes user input through the command line interface. Users are prompted to input whether there is a new coffee entry for a coworker, along with the employee's name and the price of their coffee. If the user is done entering coffee entries, they can indicate so, and the program proceeds to calculate who pays for coffee that day.

Input
The input process involves the following steps:

1. The user is prompted to indicate whether there is a new coffee entry for a coworker. 
2. If the user responds affirmatively, they are asked to input the employee's name and the price of their coffee. The price must be a valid positive number that can be preceded by a '$'. There are no restrictions on what the name can be. Preceding and trailing whitespace for the names are ignored. 
3. This process continues until the user indicates that there are no more coffee entries.


Output
The program outputs the name of the employee who will pay for coffee that day, along with the total amount paid. If no one bought coffee that day, it outputs "No one paid for coffee today."

coffee_logs.csv
The program maintains a CSV file named coffee_logs.csv to store the total amount spent on coffee by each employee. The CSV file has two columns: "Employee Name" and "Total Amount Spent on Coffee." Each row corresponds to a single employee and their total spending on coffee.

Fair Calculation of Coffee Payment
The program ensures fair calculation of who pays for coffee by keeping track of the total amount spent on coffee minus the total amount paid for coffee. It identifies the employee covered the least of their all time coffee purchases out of all the employees who bought coffee for that day, and designates them as the payer for that day. After the payment is made, the program updates the total amount spent on coffee in the CSV file. 

Updates to Names and Payments Totals
If any mistakes are made entering in the names or prices, the easiest way to correct it would be to edit the coffe_logs.csv file directly to fix any mistakes. 