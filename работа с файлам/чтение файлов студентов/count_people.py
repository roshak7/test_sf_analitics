with open('student_performance.csv') as f:
    # Инициализируем счетчики для юношей и девушек
    num_boys = 0
    num_girls = 0

# Проходим циклом по строкам файла  
    for line in f:
    # Разбиваем строку на части.
    # Разделитель - запятая.
        info = line.split(',')
        gender = info[0][1:-1]
    # Обновляем значения счетчика 
    # в зависимости от пола студента
        if gender == '"female"':
            num_girls += 1
        elif gender == '"male"':
            num_boys +=1    
    print('Мужчин:',num_boys,'Женщин:',num_girls)