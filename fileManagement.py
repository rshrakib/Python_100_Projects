import os
import glob
import shutil as sh

sh.copy('image2.jpg','copy.jpg' )
sh.move('copy.jpg', "copy2.jpg")
# os.remove("copy2.jpg")

# os.rename('image.jpg', 'image2.jpg')

name_path = os.path.basename("image2.jpg")
print(name_path)

ext = os.path.splitext('image2.jpg')
print(ext)

# os.makedirs("hello")
current = os.getcwd()
print(current)
# os.rmdir("hello")

# list= os.listdir()
# for file in list:
#     print(file)

size = os.path.getsize("image2.jpg")
print(size)

exists = os.path.exists("image2.jpg")
print(exists)
exists_dir = os.path.isdir("android")
print(exists_dir)