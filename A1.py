# 1.5x
# Double
# Holiday OT (double for first 8 hours, triple 4 hours after)

# Basic salary: 10 per hour
# Give a number (amount of hours). Only positive number or 0
# Calculate the OT rate
# Final pay at the end of the day

base_pay = 5
hours_worked = float(input('How many hours have you worked? '))

if (1/3600) <= hours_worked <= 8:
    double_rate = 2 * base_pay
    double_pay = hours_worked * double_rate
    overtime_pay = double_pay
elif 9 <= hours_worked <= 12:
    double_rate = 2 * base_pay
    double_pay = 8 * double_rate
    triple_rate = 3 * base_pay
    triple_pay = (hours_worked - 8) * triple_rate
    overtime_pay = double_pay + triple_pay
elif hours_worked > 12:
    double_rate = 2 * base_pay
    double_pay = 8 * double_rate
    triple_rate = 3 * base_pay
    triple_pay = 4 * triple_rate
    overtime_pay = double_pay + triple_pay
else:
    overtime_pay = 0

print('You work for ' + str(hours_worked))
print('Your final pay is ' + str(overtime_pay))


# =========================================================================

# basic_salary = 10 # per hour
# hours_worked = int(input("Enter the number of hours worked: "))

# if hours_worked >= 12:
#     overtime_hours = hours_worked - 12
#     regular_hours = 8
#     double_rate = 2 * basic_salary
#     triple_rate = 3 * basic_salary
#     overtime_pay = (8 * double_rate) + (4 * triple_rate) + (overtime_hours * triple_rate)
#     final_pay = (regular_hours * basic_salary) + overtime_pay
# elif hours_worked > 8:
#     overtime_hours = hours_worked - 8
#     regular_hours = 8
#     double_rate = 2 * basic_salary
#     overtime_pay = (regular_hours * basic_salary * 2) + (overtime_hours * basic_salary * 3)
#     final_pay = (regular_hours * basic_salary) + overtime_pay
# else:
#     regular_hours = hours_worked
#     overtime_hours = 0
#     final_pay = regular_hours * basic_salary

# print("Regular hours worked: ", regular_hours)
# print("Overtime hours worked: ", overtime_hours)
# print("Final pay: ", final_pay)

# d