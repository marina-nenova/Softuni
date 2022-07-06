words = input().split()
searched_word = input()

palindromes_list = [word for word in words if word == word[::-1]]
searched_word_found = palindromes_list.count(searched_word)

print(palindromes_list)
print(f"Found palindrome {searched_word_found} times")