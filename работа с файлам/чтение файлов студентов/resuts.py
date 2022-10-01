maths = []

with open('student_performance.csv') as f:

    for line in f:
        info = line.split(',')
        if info[0] == '"gender"':
            continue
        else:
            grade = int(info[5][1:-1])
            maths.append(grade)
a = max(maths)

count= 0
math_score_mean = sum(maths) / len(maths)
print(math_score_mean)
#for i in maths:
   # if i < a:
    #    count += 1











#КОЛИЧСТВО УЧЕНИКОВ С НАИВЫСШИМ БАЛЛОМ
#count= 0
#for i in maths:
   # if i == a:
      #  count+=1.
#print(int(count))
