#!/usr/bin/env python3
'''Task 0: Simple helper function'''


def index_range(page: int, page_size: int) -> tuple:
    '''Returns a tuple of size two containing a start index
    and end index'''
    myTuple = (((page - 1) * page_size), (page * page_size))
    return myTuple
