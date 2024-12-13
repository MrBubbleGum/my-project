
t = {
    'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
    'е': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k',
    'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
    'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c',
    'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '',
    'э': 'e', 'ю': 'yu', 'я': 'ya'
}

def remove_extra_hyphens(func):
    def wrapper(text):
        result = func(text)
        return '-'.join(part for part in result.split('-') if part)
    return wrapper

@remove_extra_hyphens
def to_lat(text):
    text = text.lower()
    transformed = []
    for char in text:
        if char in t:
            transformed.append(t[char])
        elif char.isalpha() or char.isdigit():  
            transformed.append(char)
        else:
            transformed.append('-')
    return ''.join(transformed)

input_text = input("Введите ваше слово: ")

if not input_text:
    print("Введите слово с количеством символов больше 0")
else:
    result = to_lat(input_text)
    print("Результат:", result)