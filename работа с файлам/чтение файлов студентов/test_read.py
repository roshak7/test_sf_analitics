f = open('student_performance.csv')
reading_score_list = []
for line in f:
    info = line.split(',')
    reading_score = info[6]
    if 'reading score' in reading_score:
        continue
    reading_score_list.append(int(reading_score[1:-1]))
f.close()
reading_score_mean = sum(reading_score_list)/len(reading_score_list)
less_mean = list(filter(lambda x: x < reading_score_mean, reading_score_list))
print(len(less_mean)/len(reading_score_list))