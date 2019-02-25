# coding: utf-8

"""
    Sample OpenAPI Specification

    An OpenAPI specification sample for [Build, Deploy, and Manage Networked APIs: An Overview](https://goo.gl/VardtG) document.  # noqa: E501

    OpenAPI spec version: 0.0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.default_api import DefaultApi  # noqa: E501
from openapi_client.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_photo(self):
        """Test case for add_photo

        """
        pass

    def test_batchget_photo(self):
        """Test case for batchget_photo

        """
        pass

    def test_create_user(self):
        """Test case for create_user

        """
        pass

    def test_delete_photo(self):
        """Test case for delete_photo

        """
        pass

    def test_get_photo(self):
        """Test case for get_photo

        """
        pass

    def test_get_user(self):
        """Test case for get_user

        """
        pass

    def test_list_photos(self):
        """Test case for list_photos

        """
        pass

    def test_update_user(self):
        """Test case for update_user

        """
        pass


if __name__ == '__main__':
    unittest.main()
