# coding: utf-8

"""
    Energy API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Body(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'watt': 'int',
        'usage_id': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'watt': 'watt',
        'usage_id': 'usageId',
        'user_id': 'userId'
    }

    def __init__(self, watt=None, usage_id=None, user_id=None):  # noqa: E501
        """Body - a model defined in Swagger"""  # noqa: E501

        self._watt = None
        self._usage_id = None
        self._user_id = None
        self.discriminator = None

        if watt is not None:
            self.watt = watt
        if usage_id is not None:
            self.usage_id = usage_id
        if user_id is not None:
            self.user_id = user_id

    @property
    def watt(self):
        """Gets the watt of this Body.  # noqa: E501


        :return: The watt of this Body.  # noqa: E501
        :rtype: int
        """
        return self._watt

    @watt.setter
    def watt(self, watt):
        """Sets the watt of this Body.


        :param watt: The watt of this Body.  # noqa: E501
        :type: int
        """

        self._watt = watt

    @property
    def usage_id(self):
        """Gets the usage_id of this Body.  # noqa: E501


        :return: The usage_id of this Body.  # noqa: E501
        :rtype: str
        """
        return self._usage_id

    @usage_id.setter
    def usage_id(self, usage_id):
        """Sets the usage_id of this Body.


        :param usage_id: The usage_id of this Body.  # noqa: E501
        :type: str
        """

        self._usage_id = usage_id

    @property
    def user_id(self):
        """Gets the user_id of this Body.  # noqa: E501


        :return: The user_id of this Body.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Body.


        :param user_id: The user_id of this Body.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Body, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Body):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
