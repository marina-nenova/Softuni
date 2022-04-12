text = input().split()
even_length = [word for word in text if len(word) % 2 ==0]
print(*even_length, sep="\n")
print("\n".join(even_length))