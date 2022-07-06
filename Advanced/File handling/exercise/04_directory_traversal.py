# from os import listdir, path
#
#
# def traverse_dir(current_path, files_by_ext):
#     for el in listdir(current_path):
#         if path.isdir(path.join(current_path, el)):
#             traverse_dir(path.join(current_path, el), files_by_ext)
#         else:
#             extension = el.split(".")[-1]
#             if extension not in files_by_ext:
#                 files_by_ext[extension] = []
#             files_by_ext[extension].append(el)
#
#
# files_by_ext = {}
# traverse_dir(".", files_by_ext)
#
# with open("output.txt", "w") as file:
#     for ext, files in sorted(files_by_ext.items()):
#         file.write(f".{ext}\n")
#         for file_name in sorted(files):
#             file.write(f"- - - {file_name}\n")


from os import walk

files_by_ext = {}
for _, _, files in walk("."):
    for file in files:
        ext = file.split(".")[-1]
        if ext not in files_by_ext:
            files_by_ext[ext] = []
        files_by_ext[ext].append(file)

with open("output.txt", "w") as file:
    for ext, files in sorted(files_by_ext.items()):
        file.write(f".{ext}\n")
        for file_name in sorted(files):
            file.write(f"- - - {file_name}\n")