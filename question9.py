# Read the number of students from the user
N = int(input("Enter the number of students: "))

# Initialize an empty list to store weights in pounds
weights_lbs = []

# Read the weights of N students into the list
for i in range(N):
    weight_lbs = float(input(f"Enter the weight of student {i+1} in pounds: "))
    weights_lbs.append(weight_lbs)

# Convert weights from pounds to kilograms
weights_kg = []
for weight_lbs in weights_lbs:
    weight_kg = round(weight_lbs * 0.453592, 2)  # Convert pounds to kilograms and round to 2 decimal places
    weights_kg.append(weight_kg)

# Print the converted weights in kilograms
print("Weights in kilograms:", weights_kg)
