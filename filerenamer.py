import os
import sys

def find_next_available_number(directory):
    files = [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]
    numbers = set()

    for file_name in files:
        try:
            number = int(os.path.splitext(file_name)[0])
            numbers.add(number)
        except ValueError:
            pass

    i = 1
    while i in numbers:
        i += 1

    return i

def organize_directory(directory):
    files = [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]
    files.sort()

    script_file = os.path.basename(sys.argv[0])
    if script_file in files:
        files.remove(script_file)

    print(f"Files in {directory}:")
    for index, file_name in enumerate(files, 1):
        print(f"File {index}: {file_name}")

    answer = input(f"\nOrganize all files in {directory}? (y/n): ")
    if answer.lower() == "y":
        print(f"\nOrganizing all files in {directory}")
        for file_name in files:
            new_number = find_next_available_number(directory)
            new_file_name = str(new_number) + os.path.splitext(file_name)[1]
            new_file_path = os.path.join(directory, new_file_name)
            os.rename(os.path.join(directory, file_name), new_file_path)
            print(f"{file_name} -> {new_file_name}")

        print("\nOrganizing complete.")
    else:
        print("\nOrganizing skipped.")

# Ask for directory path, default to current directory if left blank
directory_path = input("Enter the directory path (or press Enter to use the current directory): ")
if not directory_path:
    directory_path = os.getcwd()

organize_directory(directory_path)

input("Press Enter to exit...")
