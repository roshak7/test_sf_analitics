
# Вычисление средней суммы по возрастам 
with open('result.csv', encoding = 'windows-1251') as f:
    age1_sum, age2_sum, age3_sum = 0, 0, 0
    age1_count, age2_count, age3_count = 0, 0, 0
    for line in f:
        info = line.split(',')[1:] #Убираем первый столбец
        if 'age' in info[5]: # убираем первую строку
            continue
        age = int(info[5])
        if 18 <= age <= 30:
            age1_sum += int(info[4])
            age1_count += 1
        if 31 <= age <= 50:
            age2_sum += int(info[4])
            age2_count += 1
        if age >= 51:
            age3_sum += int(info[4])
            age3_count += 1
    age1_mean = round(age1_sum/age1_count, 3)
    age2_mean = round(age2_sum/age2_count, 3)
    age3_mean = round(age3_sum/age3_count, 3)
    print(age1_mean,age2_mean,age3_mean)
    print(age1_count, age2_count, age3_count)