age_dict = {
'age1': {'age1_sum': 311449, 'age1_count': 502, 'age1_promo': 142},
'age2': {'age2_sum': 294126, 'age2_count': 467, 'age2_promo': 100},
'age3': {'age3_sum': 19181, 'age3_count': 33, 'age3_promo': 4}
}
with open('age_report.csv', 'w') as f:#Записываем в файл age_report.csv
    line = 'age_category,sum,count,promo\n'
    f.write(line)
    for key in age_dict:
        if key == 'age1':
            line = '18-30,'
        if key == 'age2':
            line = '31-50,'
        if key == 'age3':
            line = '50+,'
        for subkey in age_dict[key].values():
            line += str(subkey) + ',' # строка age + итерация по значениям           
        line = line[:-1] + '\n' # отбрасываем в конце запятую
        f.write(line)