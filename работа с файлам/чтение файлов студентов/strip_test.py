with open ('student_performance.csv') as f:
    counter = 0
    for line in f:
        info = line.strip().split(',')[-5:]
        counter += 1
        print(info)
        if counter == 5:
            break