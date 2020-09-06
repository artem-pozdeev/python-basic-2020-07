class MyZeroDivisionError(ValueError):

    def __init__(self, value, *args):
        self.value = value
        print(type(args))
        for item in args:
            print(item)

    def __str__(self):
        return f'Заданное значение равно нулю {self.value}'
