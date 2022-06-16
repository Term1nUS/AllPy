list = [1, 2, 'aasf', '1', '123', 123]

print(list)

print([переменная for переменная in list if not isinstance(переменная, str)])