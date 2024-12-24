import os

def bulk_file_rename(folder_path, prefix, extension):
    try:
        file_list = os.listdir(folder_path)

        for index, file_name in enumerate(file_list):
            old_file_path = os.path.join(folder_path,file_name)

            new_file_name = f"{prefix}_{index+1}.{extension}"
            new_file_path =os.path.join(folder_path, new_file_name)

            os.rename(old_file_path, new_file_path)

            print(f"Renamed: {file_name}->{new_file_name}")
        print("Bulk Renaming successful!!!")
    except FileNotFoundError:
        print("Folder not found, Please provide a valid folder path!")


folder_path = "D://source"
prefix = "renamed"
extension = "pdf"

bulk_file_rename(folder_path, prefix, extension)

