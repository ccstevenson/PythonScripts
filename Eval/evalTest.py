rate = 31.50
hpy = 2080

formula = 'rate*hpy'

salary = eval(formula)
print 'Salary:', salary
# Output: Salary: 65520.0

# List of employee tuples of the form (hourlyRate, hoursPerYear)
employees = [(31.50, 2080), (17.25, 1770), (22.00, 2300), (12.00, 1500), (9.50, 1600)]

salarysum = eval('sum(rate * hpy for rate, hpy in employees)')

print 'Sum of all salaries:', salarysum
# Output: Sum of all salaries: 179852.5

# Adding safety using optional parameters
# eval(expression[, allowedGlobals[, allowedLocals]])
salarysum = eval('sum(rate * hpy for rate, hpy in employees)', 
                 {'__builtins__':None, 'sum':sum}, # Globals--only sum() allowed.
                 {'employees':employees,}) # Locals --only employee allowed.

print 'Sum of all salaries:', salarysum
# Output: Sum of all salaries: 179852.5

# Without allowing sum
'''salarysum = eval('sum(rate * hpy for rate, hpy in employees)', 
                 {'__builtins__':None,}, # Globals--we've disallowed sum().
                 {'employees':employees,}) # Locals --only employee allowed.

print 'Sum of all salaries:', salarysum'''
# Fails! 'NameError: name 'sum' is not defined'




