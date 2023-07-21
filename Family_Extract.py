import re
import sys

# Define the file path
file_path = sys.argv[1]

# Define the list of words to search for
search_words = ["idae", "aceae"]

# Initialize a dictionary to store word counts and total values
word_counts = {}
word_totals = {}

# Open the file for reading
with open(file_path, "r") as f:
    # Read the lines of the file
    lines = f.readlines()

    # Loop through each line
    for line in lines:
        # Split the line into columns
        columns = line.strip().split("\t")

        # Check if there are enough columns
        if len(columns) >= 4:
            # Get the second column value
            second_column = columns[1]

            # Get the fourth column value
            fourth_column = columns[3]

            # Find the first word ending with "idae" or "aceae"
            match = re.search(r"\b(\w+(?:idae|aceae))\b", fourth_column)
            if match:
                # Retrieve the word
                word = match.group(1)

                # Count the word occurrence
                if word in word_counts:
                    word_counts[word] += 1
                    word_totals[word] += int(second_column)
                else:
                    word_counts[word] = 1
                    word_totals[word] = int(second_column)

# Print the word counts and totals
for word, count in word_counts.items():
    total = word_totals[word]
    print(f"{word}\t{count}\t{total}")
