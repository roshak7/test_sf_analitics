with open('result.csv',encoding = 'windows-1251') as f:
    female_sum = 0
    male_sum = 0
    for line in f:
        info = line.split(',')[1:]
        if 'gender' in info[8]:
            continue
        if 'м' in info[8]:
            male_sum += int(info[4])
        elif 'ж' in info[8]:
            female_sum += int(info[4])
print(female_sum,male_sum)