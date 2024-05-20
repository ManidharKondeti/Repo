# Create a tuple containing names of your sisters and your brothers
sisters = ("Emma", "Sophia")
brothers = ("Liam", "Noah")

# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters

# How many siblings do you have?
num_siblings = len(siblings)

# Modify the siblings tuple and add the name of your father and mother
father = "John"
mother = "Emily"
family_members = siblings + (father, mother)

print("Siblings:", siblings)
print("Number of siblings:", num_siblings)
print("Family members:", family_members)
