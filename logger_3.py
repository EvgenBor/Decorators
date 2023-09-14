import datetime

def log_decorator(path):
    def _log_decorator(my_function):
        def foo(*args, **kwargs):
            date_time = datetime.datetime.now()
            func_name = my_function.__name__
            result = my_function(*args, **kwargs)
            with open(f'{path}', 'a', encoding='utf-8') as file:
                file.write(f'Дата и время вызова функции: {date_time}\n'
                           f'Имя функции: {func_name}\n'
                           f'Аргументы функции: {args, kwargs}\n'
                           f'Возвращаемое значение функции: {result}\n')
            return result
        return foo
    return _log_decorator