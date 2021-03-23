class CustomMeta(type):

    def __new__(cls, name, bases, namespace):
        new_keys = {}
        for key in namespace.keys():
            if key[0:2] == '__' and key[len(key) - 2:len(key)] == '__':
                continue
            else:
                new_keys[key] = "custom_" + key

        for old_key, new_key in new_keys.items():
            namespace[new_key] = namespace.pop(old_key)

        new_cls = super().__new__(cls, name, bases, namespace)
        return new_cls


# class CustomClass(metaclass=CustomMeta):
#     x = 50
#
#     def line(self):
#         return 100
#
#
# inst = CustomClass()
# print(inst.custom_x)
# print(inst.custom_line())
#
# inst.x  # ошибка
# inst.line() # ошибка
