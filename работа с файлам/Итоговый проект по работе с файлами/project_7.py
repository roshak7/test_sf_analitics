age1_sum = 311449 
age2_sum = 294126 
age3_sum = 19181 
age1_count = 502
age2_count = 467
age3_count = 33
with open('result.csv', encoding = 'windows-1251') as f:
    age_dict = {'age1': {'age1_sum': age1_sum, 'age1_count': age1_count, 'age1_promo': 0},
               'age2': {'age2_sum': age2_sum, 'age2_count': age2_count, 'age2_promo': 0},
               'age3': {'age3_sum': age3_sum, 'age3_count': age3_count, 'age3_promo': 0}}
    for line in f:
        info = line.split(',')[1:]
        if 'age' in info[5]:
            continue
        age = int(info[5])
        if 18<=age<=30:
            age_dict['age1']['age1_promo'] += int(info[3])#Суммируем столбец промо и добавляем в словарь
        if 31<=age<=50:
            age_dict['age2']['age2_promo'] += int(info[3])
        if age>=51:
            age_dict['age3']['age3_promo'] += int(info[3])
print(age_dict)