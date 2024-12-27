import os

path = input("Enter the folder path: ")
extension = input("input the extension (e.g. .zip, .jpg) : ")
os.chdir(path)

for file in os.listdir():
    if file.endswith(extension):
        os.remove(os.path.join(path,file))

print(f"All files ends with {extension} is deleted.")