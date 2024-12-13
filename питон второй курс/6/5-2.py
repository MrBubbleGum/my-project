import pandas as pd

# Задание 1(загрузка таблицы и удаление пропущенных значений)
polit = pd.read_csv("polit.csv", sep=';')
polit.dropna()

print(polit)    
numeric_columns = ['fh09', 'polity09', 'gini', 'fparl08', 'corr0509']
for col in numeric_columns:
    polit[col] = polit[col].str.replace(',', '.').astype(float)

numeric_columns = ['fh09', 'polity09', 'gini', 'fparl08', 'mena', 'lati', 'cari', 'east', 'sovi', 'afri', 'corr0509']
for col in numeric_columns:
    polit[col] = pd.to_numeric(polit[col], errors='coerce')

#Задание 2(Freedom House (fh09) выше 5)
not_free = polit[polit['fh09'] > 5]
print("\nСтраны с fh09 > 5:\n", not_free)

#Задание 3(Выбрать в датафрейме строки, которые соответствуют странам Африки (afri) с процентом женщин в парламенте (fparl08) выше 30%. Сохранить их в датафрейм af_w.
af_w = polit[(polit['afri']==1.0) & (polit['fparl08']>30)]
print("\nСтраны Африки с долей женщин в парламенте > 30%:\n", af_w)

#Задание 4(Выбрать в датафрейме строки, которые соответствуют странам Африки или Латинской Америки (afri и lati) со значением индекса Polity2 (polity09) больше или равным 8. Сохраните их в датафрейм la_dem.
la_dem = polit[((polit['afri']==1)|(polit['lati']==1)) & (polit['polity09']>=8)]
print("\nСтраны Африки или Латинской Америки с polity09 >= 8:\n", la_dem)

#Задание 5(Добавить в датафрейм polit столбец corr_round, в котором будут храниться округленные до 2 знака после запятой значения индекса Control of Corruption (corr0509).)
polit['corr_round'] = polit['corr0509'].round(2)
print(polit[['ctry', 'corr0509', 'corr_round']])

#Задание 6(Добавьте в датафрейм polit столбец fh_status, в котором будут храниться типы стран в зависимости от значения индекса Freedom House (значения free, partly free, not free).)
def get_country_type(value):
    if 1.0 <= value <= 2.5:
        return 'Free'
    elif 3.0 <= value <= 5.0:
        return 'Partly Free'
    elif 5.5 <= value <= 7.0:
        return 'Not Free'
    else:
        return 'Unknown'
polit['fh_status'] = polit['fh09'].apply(get_country_type)
print(polit)

#Задание 7(Сгруппировать строки в таблице в соответствии со значениями столбца fh_status, полученного в предыдущей части и выведите минимальное, среднее и максимальное значение показателя gini (индекс Джини) по каждой группе.)
gini_stats = polit.groupby('fh_status')['gini'].agg(['min', 'mean', 'max'])
print("\nМинимальное, среднее и максимальное значение gini по fh_status:\n", gini_stats)

#Задание 8(Сгруппируйте строки в таблице в соответствии со значениями столбца fh_status и запишите строки, относящиеся к разным группам, в отдельные csv-файлы.)
for status, group in polit.groupby('fh_status'):
    filename = f'polit_{status.replace(" ", "_").lower()}.csv'
    group.to_csv(filename, index=False)
    print(f"\nДанные для статуса {status} сохранены в файл {filename}")
