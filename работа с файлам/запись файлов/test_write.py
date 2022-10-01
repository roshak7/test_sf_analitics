

# вычисление средних оценок студентов
with open('student_performance.csv') as f:
    math = []
    reading = []
    writing = []
    for line in f:
        info = line.split(',')
        if 'math' in info[5]:
            continue
        math.append(int(info[5][1:-1]))
        reading.append(int(info[6][1:-1]))
        writing.append(int(info[7][1:-2]))
math_mean = round(sum(math)/len(math), 3)
reading_mean = round(sum(reading)/len(reading), 3)
writing_mean = round(sum(writing)/len(writing), 3)
marks = [math_mean, reading_mean, writing_mean]
with open('mean_scores.txt', 'w') as f:
    for mark in marks:
        f.write(str(mark))
        f.write(' ')