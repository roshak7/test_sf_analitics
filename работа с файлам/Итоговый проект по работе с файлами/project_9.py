def get_info_from_file(filename):
    if filename[-4:] =='.csv':
        with open(filename) as f:
            lines = f.readlines()
            result = [x[:-1].split(',') for x in lines]
        return result
    else:
        raise ValueError('Неправильный формат файла')
      