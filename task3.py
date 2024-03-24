'''
Необязательное задание. Написать итератор, аналогичный итератору из задания 1, но обрабатывающий списки с любым уровнем вложенности. Шаблон и тест в коде ниже:
'''

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list(reversed(list_of_list))

    def __iter__(self):
        return self

    def __next__(self):
        while self.list_of_list:
            self.entity = self.list_of_list.pop()
            if type(self.entity) is not list:
                return self.entity
            else:
                for el in reversed(self.entity):
                    self.list_of_list.append(el)
        raise StopIteration


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

def new_list(list_of_lists_2):
    for list_ in list_of_lists_2:
        if isinstance(list_, list):
            for x in new_list(list_):
                yield x
        else:
            yield list_

if __name__ == '__main__':
    test_3()