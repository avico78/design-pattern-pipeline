def read_csv(*args, **kwargs):
    path = kwargs.get('path')
    with open(path, "r", encoding='utf8') as file:
        content = file.readlines()
    return [x.split(',') for x in content]
