d = {
    'house': 'дом',
    'river': 'река',
    'car': 'машина',
    'tree': 'дерево',
    'sky': 'небо'
}

english_input = input("Введите английские слова через пробел: ")

# Проверяем, не пустой ли ввод
if english_input.strip() == "":
    print("Вы не ввели ни одного слова.")
else:
    for word in english_input.split():
        if word not in d:
            print(f"Ошибка: слово '{word}' не найдено в словаре.")
            break
    else:
        # Если все слова в словаре, выводим перевод
        translated_words = [d[word] for word in english_input.split()]
        print("Перевод:", ' '.join(translated_words))