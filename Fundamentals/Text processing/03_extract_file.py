file_path = input().split("\\")

file_name, file_extension = file_path[-1].split(".")

print(f"File name: {file_name}")
print(f"File extension: {file_extension}")