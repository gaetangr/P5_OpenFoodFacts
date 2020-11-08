import pytest
from openfoodfacts.cleaner import DataCleaner
from openfoodfacts.downloader import Downloader
import requests


downloader = Downloader()

downloader.get_product()


class TestDownloaderModule:
    """Test Downloader module work as expected"""

    def test_response_is_200(self):
        """ test if request is ok"""
        r = downloader.url
        status = requests.get(r).status_code
        assert status == 200
