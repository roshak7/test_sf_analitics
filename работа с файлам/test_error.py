div_list = [12, 5, 0, 16, 7]
def division_18(div_list):
    result = []
    for i in div_list:
        try:
            result.append(round(18/i, 3))
        except ZeroDivisionError:
            result.append(0)
    return result
    
print(division_18(div_list))