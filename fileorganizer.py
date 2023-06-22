import os
import shutil
import concurrent.futures

def organize_files(folder_path):
    script_name = os.path.basename(__file__)

    def process_file(file):
        if file == script_name:
            return

        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file)
            ext = ext[1:]

            ext_folder = os.path.join(folder_path, ext)
            os.makedirs(ext_folder, exist_ok=True)

            dest = os.path.join(ext_folder, file)
            shutil.move(file_path, dest)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        files = os.listdir(folder_path)
        executor.map(process_file, files)

    print("File organization completed!")

current_dir = os.getcwd()

if __name__ == "__main__":
    organize_files(current_dir)
