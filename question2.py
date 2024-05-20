# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog["name"] = "Fido"
dog["color"] = "Brown"
dog["breed"] = "Labrador"
dog["legs"] = 4
dog["age"] = 3

# Create a student dictionary
student = {
    "first_name": "John",
    "last_name": "Doe",
    "gender": "Male",
    "age": 25,
    "marital_status": "Single",
    "skills": ["Python", "Data Analysis"],
    "country": "USA",
    "city": "New York",
    "address": "123 Main Street"
}

# Get the length of the student dictionary
student_length = len(student)

# Get the value of skills and check the data type
skills_value = student["skills"]
skills_data_type = type(skills_value)

# Modify the skills values by adding one or two skills
student["skills"].extend(["Machine Learning", "Communication"])

# Get the dictionary keys as a list
student_keys = list(student.keys())

# Get the dictionary values as a list
student_values = list(student.values())

print("Dog dictionary:", dog)
print("Student dictionary length:", student_length)
print("Data type of skills:", skills_data_type)
print("Modified skills:", student["skills"])
print("Dictionary keys:", student_keys)
print("Dictionary values:", student_values)
