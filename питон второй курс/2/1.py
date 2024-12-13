def is_valid_password(password):
    criteria = [
        len(password) >= 8, 
        any(char in '$#!?-_' for char in password), \
        any(char in 'ABCD' for char in password)  \
    ]

    return all(criteria)

password = input("Введите пароль: ")
print(is_valid_password(password))