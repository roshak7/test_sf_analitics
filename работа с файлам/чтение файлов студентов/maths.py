with open('student_performance.csv') as f:
    math_score = []
    for line in f:
        info = line.split(',')
        gender = info[0][1:-1]
        if 'gender' not in gender and gender == 'female':
            math = int(info[5][1:-1])
            math_score.append(math)
math_mean = sum(math_score)/len(math_score)
female_math_score = len([x for x in math_score if x > math_mean])






#СТУДЕНТЫ ПО БАЛЛАМ КОЛИЧЕСТВО
#with open('student_performance.csv') as f:
   # math_score =  []
    #for line in f:
     #   info = line.split(',')
      #  if 'math' in info[5]:
       #     continue
       # math_score.append(int(info[5][1:-1]))
#less_than_50 = len([x for x in math_score if x < 50])
#from_50_to_90 = len([x for x in math_score if 50 <= x < 90])
#more_than_90 = len([x for x in math_score if x >= 90])