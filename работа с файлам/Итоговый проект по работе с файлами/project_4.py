with open('result.csv',encoding='windows-1251') as f:
    female_count = 0
    male_count = 0
    for line in f:
        info = line.split(',')[1::]
        gender = info[-1]
        if 'м' in gender:
            male_count += 1
        elif 'ж' in gender:
            female_count += 1
    print(female_count,male_count)
        