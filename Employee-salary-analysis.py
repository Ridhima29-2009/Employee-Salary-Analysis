import numpy as np

employees = np.array(["Amit", "Riya", "Rahul", "Priya", "Neha", "Arjun"])

salary = np.array([35000, 48000, 42000, 55000, 60000, 45000])

experience = np.array([2, 5, 3, 7, 8, 4])


print("Employees:")
print(employees)

print("\nSalaries:")
print(salary)

print("\nYears of Experience:")
print(experience)

print("\nTotal Number of Employees:")
print(employees.size)


# Salary Analysis

total_salary = np.sum(salary)
print("\nTotal Salary:")
print(total_salary)

average_salary = np.mean(salary)
print("\nAverage Salary:")
print(average_salary)

highest_salary = np.max(salary)
print("\nHighest Salary:")
print(highest_salary)

lowest_salary = np.min(salary)
print("\nLowest Salary:")
print(lowest_salary)

median_salary = np.median(salary)
print("\nMedian Salary:")
print(median_salary)

variance_salary = np.var(salary)
print("\nVariance of Salary:")
print(variance_salary)

standard_deviation_salary = np.std(salary)
print("\nStandard Deviation of Salary:")
print(standard_deviation_salary)


# Experience Analysis

average_experience = np.mean(experience)
print("\nAverage Experience:")
print(average_experience)

highest_experience = np.max(experience)
print("\nHighest Experience:")
print(highest_experience)

lowest_experience = np.min(experience)
print("\nLowest Experience:")
print(lowest_experience)


# Employee Analysis

highest_paid_employee = employees[np.argmax(salary)]
print("\nHighest Paid Employee:")
print(highest_paid_employee)

lowest_paid_employee = employees[np.argmin(salary)]
print("\nLowest Paid Employee:")
print(lowest_paid_employee)

high_earners = employees[salary > 45000]
print("\nEmployees Earning More Than ₹45000:")
print(high_earners)

low_earners = employees[salary < 40000]
print("\nEmployees Earning Less Than ₹40000:")
print(low_earners)

high_experience = employees[experience > 5]
print("\nEmployees With Experience Greater Than 5 Years:")
print(high_experience)

low_experience = employees[experience < 3]
print("\nEmployees With Experience Less Than 3 Years:")
print(low_experience)


# Sorting

ascending_salary = np.sort(salary)
print("\nSalary in Ascending Order:")
print(ascending_salary)

descending_salary = np.sort(salary)[::-1]
print("\nSalary in Descending Order:")
print(descending_salary)


# Searching

position_of_priya = np.where(employees == "Priya")
print("\nPosition of Priya:")
print(position_of_priya)

employee_with_60000 = employees[np.where(salary == 60000)]
print("\nEmployee Earning ₹60000:")
print(employee_with_60000)


# Final Report

print("\n========== Employee Salary Analysis ==========")

print("Total Employees:", employees.size)
print("Total Salary Paid:", total_salary)
print("Average Salary:", average_salary)

print("Highest Salary:", highest_salary)
print("Lowest Salary:", lowest_salary)

print("Highest Paid Employee:", highest_paid_employee)
print("Lowest Paid Employee:", lowest_paid_employee)

print("Average Experience:", average_experience)

print("=============================================")