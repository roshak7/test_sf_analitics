with open('first_ver.csv', encoding='utf-8') as f:
    lines_first = f.readlines()
    
with open('sec_ver.csv', encoding='utf-8') as f:
    lines_second = f.readlines()
    
data = lines_first + lines_second[1:]
 
with open('result.csv', 'w') as f:
    f.writelines(data)