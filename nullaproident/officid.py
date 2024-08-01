employees = {'Alice', 'Bob', 'Charlie', 'David'}
neighbors = {'Charlie', 'Eve', 'Frank', 'Grace'}

intersection = employees.intersection(neighbors)
difference_employees = employees.difference(intersection)
difference_neighbors = neighbors.difference(intersection)

print("Elements in employees but not in neighbors:", difference_employees)
print("Elements in neighbors but not in employees:", difference_neighbors)
