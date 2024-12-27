import os, shutil

def organize_files(directory):
    file_types = {
        'images':['.jpg','.jpeg','.png','.gif'],
        'videos': ['.mp4', '.mkv', '.3gp'],
        'documents': ['.pdf','.doc', '.docx', '.txt', '.pptx'],
        'others': []
    }

    for subdir in file_types:
        os.makedirs(os.path.join(directory, subdir),exist_ok=True)

    for filename in  os.listdir(directory):
        file_path  = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()

            file_move = False

            for category,extension in file_types.items():
                if file_extension in extension:
                    shutil.move(file_path, os.path.join(directory, category, filename))
                    file_move = True
                    break
            if not file_move:
                shutil.move(file_path, os.path.join(directory, 'others',filename))
    print("File organize successful!!")


directory_path = input("Enter the directory: ")
organize_files(directory_path)