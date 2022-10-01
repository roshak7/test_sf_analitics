with open('first_ver.csv', encoding = 'utf-8') as f:
    total_sum = 0
    for line in f:
        info= line.split(',')[1:]
        if 'order_sum' in info[4]:
            continue
        total_sum += int(info[4])
    print(total_sum)