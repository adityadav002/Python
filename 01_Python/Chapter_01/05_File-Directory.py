import os

# Specify the directory path
directory_path = '/Codes'

# List all entries in the specified directory
entries = os.listdir(directory_path)

# Print each entry
for entry in entries:
    print(entry)
