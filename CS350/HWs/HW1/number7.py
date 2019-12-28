def weekday(hourlysalary, hours):
    x= hourlysalary * hours if hours <=40 else (hourlysalary * 40) + ((hours - 40) * (hourlysalary * 1.5))
    return x
