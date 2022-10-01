with open('first_ver.csv',  encoding='utf-8') as f:
    customers_count = len(f.readlines()) - 1