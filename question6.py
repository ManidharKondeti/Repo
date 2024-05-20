sentence = "I am a teacher and I love to inspire and teach people"

# Split the sentence into words
words = sentence.split()

# Convert the list of words into a set to get unique words
unique_words = set(words)

# Find the number of unique words
num_unique_words = len(unique_words)

print("Number of unique words:", num_unique_words)
