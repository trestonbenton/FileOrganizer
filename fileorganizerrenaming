import os
import sys

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
        for index, file_name in enumerate(files, 1):
            new_file_name = str(index) + os.path.splitext(file_name)[1]
            new_file_path = os.path.join(directory, new_file_name)
            if os.path.exists(new_file_path):
                print(f"File '{new_file_name}' already exists, skipping.")
            else:
                os.rename(os.path.join(directory, file_name), new_file_path)
                print(f"{file_name} -> {new_file_name}")

        print("\nOrganizing complete.")
    else:
        print("\nOrganizing skipped.")

directory_path = input("Enter the directory path: ")

organize_directory(directory_path)

input("Press Enter to exit...")
