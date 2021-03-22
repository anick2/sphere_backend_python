class CustomMeta(type):

    def __new__(cls, name, bases, namespace):
        for key in namespace.keys():
            if key[0:2] == '__' and key[len(key) - 2:len(key)] == '__':
                continue
            else:
                namespace["custom_" + key] = namespace.pop(key)
        new_cls = super().__new__(cls, name, bases, namespace)
        return new_cls


class CustomClass(metaclass=CustomMeta):
    x = 50
    def line(self):
        return 100


inst = CustomClass()
print(inst.custom_x)
print(inst.custom_line())

# inst.x  # ошибка
# inst.line() # ошибка
