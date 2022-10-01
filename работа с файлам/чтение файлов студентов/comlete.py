num_none  = 0
num_completed  = 0
with open ('student_performance.csv') as f:
    for line in f:
        info = line.split(',')
        test = info[4][1:-1]
        gender= info[0][1:-1]
        if test == 'none':
            if gender == 'female':
                num_none += 1
        if test == 'completed':
            if gender == 'female':
                num_completed += 1

    print(num_none,num_completed)