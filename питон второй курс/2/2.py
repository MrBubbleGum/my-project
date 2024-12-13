
words_input = input("Введите слова через пробел: ")

words = [word.lower() for word in words_input.split()]

last_word = words[-1] if words else None  

result = (last_word is not None) and (words.count(last_word) > 1)

print(result)