


# Разметка на столбцы для списка
nested = [['course_1', 'course_2','course_3'], [1, 2, 3], [4, 7, 7], [6, 5, 8]]
with open('nested_file.csv', 'w') as f:
    f.write('course_number,first_id,second_id,third_id,\n')
    for i in range(len(nested[0])):
        f.write(str(nested[0][i]))
        f.write(',')
        for j in range(1,len(nested)):
            f.write(str(nested[j][i]))
            f.write(',')
        f.write('\n') 















#Запись Фруктов в столбцы


#fruit_dict = {'Банан': 16, 'Яблоко': 28, 'Персик': 37, 
 #            'Манго': 100, 'Апельсин': 30}
#with open('fruits.csv', 'w', encoding='utf-8') as f:
  #  f.write('фрукт,цена\n')
   # for key in fruit_dict:
      #  f.write(key + ',' + str(fruit_dict[key]) + '\n')