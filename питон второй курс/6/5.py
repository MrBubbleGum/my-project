import pandas as pd

# 1 Список группы
index = ['1', '2', '3',
        '4', '5', '6', 
        '7', '8', '9', 
        '10', '11', '12',
        '13', 'starosta', '15']
members = ['Богословский Иван', 'Бодров Дмитрий', 'Борсук Назар',
           'Важная Яна', 'Гаврилова Дарья', 'Деревянко Сергей',
            'Думинский Артем', 'Заяц Максим', 'Калинин Владислав', 
            'Ковалев Иван', 'Ковалева Вероника', 'Ковалева Наталья', 
            'Козел Никита', 'Трубникова Мария', 'Комеко Станислав']
name = pd.Series(members, index=index)

# 2
print(name)
print(name[1::2])
print(name.index)

# 1 Создание DAtaFrane
is_starosta = ([False for _ in range(13)] + [True, False])
phone = (["+37581474858780", "+37571835795682", "+37588144847364", 
                   "+37598761887730", "+37545060910652", "+37590441153230", 
                   "+37585340046617", "+37569531348979", "+37548537787836", 
                   "+37566237192579", "+37506365210054", "+37563014470222", 
                   "+37517969088454", "+37590911834190", "+37537244628786"])
gender = (["men", "men", "men", 
                   "women", "women", "men", 
                   "men", "men", "men", 
                   "men", "women", "women", 
                   "men", "women", "men"])
year_birth = (["2006", "2006", "2006", 
                        "2006", "2005", "2005", 
                        "2005", "2006", "2006", 
                        "2006", "2005", "2005", 
                        "2006", "2005", "2006"])

group = pd.DataFrame({'Name': members, 'isStarosta': is_starosta, 'Phone': phone, 'Gender': gender, 'YearBirth': year_birth},index=index)
print(group)

# 2 Первые три записи
print(group.head(3))

# 3 столбик с именами
print(group['Name'])

# 4 3 столбика вместе — имя и пол
print(group[['Name','Gender']])

# 5 Данные по старосте
print(group.loc['starosta'])

# 6 FIO в качестве индексов FIO
new_index = ['B.I.', 'B.D.', 'B.N.',
             'V.Y.', 'G.D.', 'D.S.',
             'D.A.', 'Z.M.', 'K.V.',
             'K.I.', 'K.V.', 'K.N.',
             'K.N.', 'T.M.', 'K.S.']
new_group = pd.DataFrame({'Name': members, 'isStarosta': is_starosta, 'Phone': phone, 'Gender': gender, 'YearBirth': year_birth},index=new_index)
print(new_group) 

# 7 + столбик Age
age = [2024-int(i) for i in year_birth]
new_group['Age'] = age
print(new_group)

# 8 Mинимальный и максимальный возраст
print("Максимальный возраст: " + str(new_group['Age'].max()))
print("Минимальный возраст: " + str(new_group['Age'].min()))

# 9 Cводная таблица с количеством девушек, юношей и средним возрастом девушек и юношей
print("\nКоличество девушек и юношей:" + str(new_group['Gender'].value_counts()))

print("\nСредний возраст девушек и юношей:" + str(new_group.groupby('Gender')['Age'].mean()))

# 10 Pаспределение студентов по годам рождения
print("Распределение студентов по годам рождения:\n" + str(new_group['YearBirth'].value_counts().sort_index()))

# 11 DataFrame в виде csv-файла
new_group.to_csv('iti-21.csv')

# 12 Новый DataFrame, заполненный данными из созданного ранее csv-файла.
new_data_frame = pd.read_csv("iti-21.csv")
print(new_data_frame.head())

