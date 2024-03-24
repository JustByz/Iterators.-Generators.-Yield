'''
Доработать класс FlatIterator в коде ниже. Должен получиться итератор, который принимает список списков и возвращает их плоское представление,
т. е. последовательность, состоящую из вложенных элементов. Функция test в коде ниже также должна отработать без ошибок.
'''


class FlatIterator:

    def __init__(self, list_of_list, index = -1):
        self.list_of_list = list_of_list
        self.index = index

    def __iter__(self):
        self.list_sum = sum(self.list_of_list, [])
        return self

    def __next__(self):
        if self.index == len(self.list_sum) - 1:
            raise StopIteration
        self.index += 1
        return self.list_sum[self.index]
    

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()