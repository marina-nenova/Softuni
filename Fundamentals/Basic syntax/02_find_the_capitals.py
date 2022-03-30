text = input()
index_list = []
for index in range(len(text)):
    if text[index].isupper():
        index_list.append(index)
print(index_list)
