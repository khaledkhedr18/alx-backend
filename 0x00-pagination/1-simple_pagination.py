#!/usr/bin/env python3
'''Task 1: Simple Pagination'''
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    '''Returns a tuple of size two containing a start index
    and end index'''
    myTuple = (((page - 1) * page_size), (page * page_size))
    return myTuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves a specific page of data from the dataset.

        Args:
            page (int): The page number to retrieve. Defaults to 1.
            page_size (int): The number of items per page. Defaults to 10.

        Returns:
            List[List]: A list of lists containing data for the specified page.
        """
        assert isinstance(
            page, int) and page > 0, "Page must be a positive integer"
        assert isinstance(
            page_size, int) and page_size > 0, "Page size must be a P integer"
        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)
        if start_index > len(dataset):
            return []

        if end_index > len(dataset):
            end_index = len(dataset)
        return dataset[start_index: end_index]
