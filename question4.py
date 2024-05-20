it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies
it_companies_length = len(it_companies)
print("Length of it_companies:", it_companies_length)

# Add 'Twitter' to it_companies
it_companies.add('Twitter')

# Insert multiple IT companies at once to the set it_companies
it_companies.update(['LinkedIn', 'Snapchat', 'Uber'])

# Remove one of the companies from the set it_companies
it_companies.remove('IBM')

# What is the difference between remove and discard?
# - remove() raises an error if the element is not present in the set,
# - discard() doesn't raise any error if the element is not present.

# Join A and B
joined_set = A.union(B)
print("Joined set of A and B:", joined_set)

# Find A intersection B
intersection_set = A.intersection(B)
print("Intersection of A and B:", intersection_set)

# Is A subset of B
is_A_subset_of_B = A.issubset(B)
print("Is A subset of B:", is_A_subset_of_B)

# Are A and B disjoint sets
are_disjoint = A.isdisjoint(B)
print("Are A and B disjoint sets:", are_disjoint)

# Join A with B and B with A
joined_AB = A.union(B)
joined_BA = B.union(A)
print("Joined A with B:", joined_AB)
print("Joined B with A:", joined_BA)

# What is the symmetric difference between A and B
symmetric_difference = A.symmetric_difference(B)
print("Symmetric difference between A and B:", symmetric_difference)

# Delete the sets completely
del it_companies, A, B

# Convert the ages to a set and compare the length of the list and the set
age_set = set(age)
length_difference = len(age) - len(age_set)
print("Length difference between list and set of ages:", length_difference)
