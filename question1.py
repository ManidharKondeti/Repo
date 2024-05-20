ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
sorted_ages = sorted(ages)
min_age = sorted_ages[0]
max_age = sorted_ages[-1]

# Add the min age and the max age again to the list
ages.extend([min_age, max_age])

# Find the median age
n = len(ages)
if n % 2 == 0:
    median_age = (sorted_ages[n//2 - 1] + sorted_ages[n//2]) / 2
else:
    median_age = sorted_ages[n//2]

# Find the average age
average_age = sum(ages) / len(ages)

# Find the range of the ages
age_range = max_age - min_age

print("Sorted ages:", sorted_ages)
print("Min age:", min_age)
print("Max age:", max_age)
print("Median age:", median_age)
print("Average age:", average_age)
print("Age range:", age_range)
