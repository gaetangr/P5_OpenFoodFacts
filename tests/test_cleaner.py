import pytest
from openfoodfacts.cleaner import DataCleaner
from openfoodfacts.downloader import Downloader

downloader = Downloader()
cleaner = DataCleaner()
products = downloader.get_product(1, 1)
clean_list = cleaner.clean(products)


class TestCleanerModule:
    """Test cleaner module work as expected"""

    def test_type_is_tuple(self):
        """ test if return data is list"""
        assert type(clean_list) == tuple

    def test_tuple_is_not_empty(self):
        """Test if return tuple is not empty """
        assert clean_list != ()

    def test_if_store_is_unique(self):
        """Test if the store data are unique"""
        assert type(clean_list[2]) == set

    def test_if_list_and_set_are_capitalized(self):
        """Test if value return from set is capitalized"""

        # retrieve a value from the set
        set_single_element = next(iter(clean_list[0]))
        # Take the first letter from the string
        set_single_element = str(set_single_element[0])
        # assert if the first letter is upper
        assert set_single_element.isupper() == True
