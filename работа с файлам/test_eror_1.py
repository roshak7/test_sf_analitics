def get_dict_value(my_dict, string):
    try:
        return my_dict[string]
    except KeyError:
        print('Такого ключа в словаре нет')