with open('student_performance.csv') as f:
             test_prep_course = {}
             for line in f:
                            info = line.split(',')
                            prep_course = info[4][1:-1]
                            if 'test preparation course' in prep_course:
                                continue
                            if prep_course in test_prep_course:
                                        test_prep_course[prep_course] +=1
                            else:
                                        test_prep_course[prep_course] = 1
