with open('result.csv', encoding='windows-1251') as f:
    counter = 0
    total_sum = 0
    for line in f:
        info = line.split(',')[1:]
        print(info)
        if 'order_sum' in info[4]:
            continue
        total_sum += int(info[4])
        counter +=1
      
   # print(counter,total_sum)