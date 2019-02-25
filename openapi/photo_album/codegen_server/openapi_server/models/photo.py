# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Photo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, created_at=None, data=None):  # noqa: E501
        """Photo - a model defined in OpenAPI

        :param name: The name of this Photo.  # noqa: E501
        :type name: str
        :param created_at: The created_at of this Photo.  # noqa: E501
        :type created_at: int
        :param data: The data of this Photo.  # noqa: E501
        :type data: file
        """
        self.openapi_types = {
            'name': str,
            'created_at': int,
            'data': bytes
        }

        self.attribute_map = {
            'name': 'name',
            'created_at': 'created_at',
            'data': 'data'
        }

        self._name = name
        self._created_at = created_at
        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'Photo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Photo of this Photo.  # noqa: E501
        :rtype: Photo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this Photo.


        :return: The name of this Photo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Photo.


        :param name: The name of this Photo.
        :type name: str
        """

        self._name = name

    @property
    def created_at(self):
        """Gets the created_at of this Photo.


        :return: The created_at of this Photo.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Photo.


        :param created_at: The created_at of this Photo.
        :type created_at: int
        """

        self._created_at = created_at

    @property
    def data(self):
        """Gets the data of this Photo.


        :return: The data of this Photo.
        :rtype: file
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this Photo.


        :param data: The data of this Photo.
        :type data: file
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data
