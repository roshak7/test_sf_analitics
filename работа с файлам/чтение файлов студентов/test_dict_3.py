with open('student_performance.csv') as f:
    parental_education = {}
    test_is_done = 0
    for line in f:
        info = line.split(',')
        parent = info[2][1:-1]
        prep_course = info[4][1:-1]
        if 'parental level of education' in parent:
            continue
        if parent in parental_education and 'completed' in prep_course:
            parental_education[parent] += 1
        elif parent not in parental_education and 'completed' in prep_course:
            parental_education[parent] = 1
        if 'completed' in prep_course:
            test_is_done += 1
        
print(round((parental_education["master's degree"] + parental_education["bachelor's degree"])*100 / test_is_done))