class FlatIterator:

    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

        
    def __iter__(self):
        self.main_cursor = 0
        self.nested_cursor = -1
        return self
        

    def __next__(self):

        self.nested_cursor += 1
        nested_limit = len(self.list_of_lists[self.main_cursor]) 
        if nested_limit == self.nested_cursor:
            self.main_cursor += 1
            self.nested_cursor = 0
        
        
        main_limit = len(self.list_of_lists)
        if main_limit == self.main_cursor:
            raise StopIteration
        

        return self.list_of_lists[self.main_cursor][self.nested_cursor]
        



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
