class CustomList(list):

    def __sub__(self, other):
        result = []
        a = super(CustomList, self)

        for i in range(min(a.__len__(), other.__len__())):
            result.append(a.__getitem__(i) - other.__getitem__(i))

        if other.__len__() <= a.__len__():
            result += [a.__getitem__(l) for l in range(other.__len__(), a.__len__())]
        else:
            result += [-other.__getitem__(l) for l in range(a.__len__(), other.__len__())]

        return CustomList(result)

    def __add__(self, other):
        result = []
        a = super(CustomList, self)

        for i in range(min(a.__len__(), other.__len__())):
            result.append(a.__getitem__(i) + other.__getitem__(i))

        if other.__len__() <= a.__len__():
            result += [a.__getitem__(l) for l in range(other.__len__(), a.__len__())]
        else:
            result += [other.__getitem__(l) for l in range(a.__len__(), other.__len__())]

        return CustomList(result)

    def sum_list(self):
        result = 0
        for i in range(super(CustomList, self).__len__()):
            result += super(CustomList, self).__getitem__(i)
        return result

    def __lt__(self, other):
        return self.sum_list() < sum(other)
    
    def __le__(self, other):
        return super(CustomList, self) <= sum(other)

    def __eq__(self, other):
        return super(CustomList, self) == sum(other)

    def __ne__(self, other):
        return super(CustomList, self) != sum(other)

    def __gt__(self, other):
        return super(CustomList, self) > sum(other)

    def __ge__(self, other):
        return super(CustomList, self) >= sum(other)

