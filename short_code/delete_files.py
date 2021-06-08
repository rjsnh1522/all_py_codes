import os

files_path = [os.path.abspath(x) for x in os.listdir()]
# print(files_path)

print(os.listdir())
# for fldr in files_path:
for folder_path in files_path:
    if os.path.isdir(folder_path):
        for file in os.listdir(folder_path):
            if file.endswith('.mp4'):
                print(os.path.join(folder_path, file))