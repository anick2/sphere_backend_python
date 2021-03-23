class CustomList(list):

    def make_operation(self, l1, l2, op):
        result = []
        sign = -1 if op == '-' else 1

        if op == '-':
            for i in range(min(l1.__len__(), l2.__len__())):
                result.append(l1.__getitem__(i) - l2.__getitem__(i))
        else:
            for i in range(min(l1.__len__(), l2.__len__())):
                result.append(l1.__getitem__(i) + l2.__getitem__(i))

        if l2.__len__() <= l1.__len__():
            result += [l1.__getitem__(elem)
                       for elem in range(l2.__len__(), l1.__len__())]
        else:
            result += [sign * l2.__getitem__(elem)
                       for elem in range(l1.__len__(), l2.__len__())]

        return result

    def __add__(self, other):
        result = self.make_operation(super(CustomList, self), other, '+')
        return CustomList(result)

    def __radd__(self, other):
        result = self.make_operation(other, super(CustomList, self), '+')
        return CustomList(result)

    def __sub__(self, other):
        result = self.make_operation(super(CustomList, self), other, '-')
        return CustomList(result)

    def __rsub__(self, other):
        result = self.make_operation(other, super(CustomList, self), '-')
        return CustomList(result)

    def sum_list(self):
        result = 0
        for i in range(super(CustomList, self).__len__()):
            result += super(CustomList, self).__getitem__(i)
        return result

    def __lt__(self, other):
        return self.sum_list() < sum(other)

    def __le__(self, other):
        return self.sum_list() <= sum(other)

    def __eq__(self, other):
        return self.sum_list() == sum(other)

    def __ne__(self, other):
        return self.sum_list() != sum(other)

    def __gt__(self, other):
        return self.sum_list() > sum(other)

    def __ge__(self, other):
        return self.sum_list() >= sum(other)
