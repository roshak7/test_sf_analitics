students_list = []
with open('student_performance.csv') as f:
    for line in f:
        line = line.strip().split(',')
        for i in range(len(line)):
            line[i] = line[i][1:-1]
            if line[i].isdigit() == True:
                line[i] = int(line[i])
        students_list.append(line)
#print(students_list)