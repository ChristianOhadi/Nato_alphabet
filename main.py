import csv

with open('nato_phonetic_alphabet.csv', mode='r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    # Skip the header row
    next(csv_reader)
    phonetic_dict = {row[0]: row[1] for row in csv_reader}

# Print the resulting dictionary
while True:
    # Get user input
    word = input("Enter a word (or type 'exit' to stop): ").upper()  # Convert the word to uppercase

    # Check if the user wants to exit
    if word == "EXIT":
        print("Exiting the program. Goodbye!")
        break

    # Create a list of phonetic code words using list comprehension
    phonetic_code_words = [phonetic_dict[letter] for letter in word if letter in phonetic_dict]

    # Print the list of phonetic code words
    if phonetic_code_words:
        print("Phonetic Code Words:", phonetic_code_words)
    else:
        print("Please enter a valid word containing only alphabetic characters.")
