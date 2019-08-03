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


class User(object):
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
        'user_id': 'str',
        'address': 'str',
        'user_type': 'int',
        'wallet_balance': 'int',
        'device_id': 'str',
        'device_type': 'int'
    }

    attribute_map = {
        'user_id': 'userId',
        'address': 'address',
        'user_type': 'userType',
        'wallet_balance': 'walletBalance',
        'device_id': 'deviceId',
        'device_type': 'deviceType'
    }

    def __init__(self, user_id=None, address=None, user_type=None, wallet_balance=None, device_id=None, device_type=None):  # noqa: E501
        """User - a model defined in Swagger"""  # noqa: E501

        self._user_id = None
        self._address = None
        self._user_type = None
        self._wallet_balance = None
        self._device_id = None
        self._device_type = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        if address is not None:
            self.address = address
        if user_type is not None:
            self.user_type = user_type
        if wallet_balance is not None:
            self.wallet_balance = wallet_balance
        if device_id is not None:
            self.device_id = device_id
        if device_type is not None:
            self.device_type = device_type

    @property
    def user_id(self):
        """Gets the user_id of this User.  # noqa: E501


        :return: The user_id of this User.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this User.


        :param user_id: The user_id of this User.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def address(self):
        """Gets the address of this User.  # noqa: E501


        :return: The address of this User.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this User.


        :param address: The address of this User.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def user_type(self):
        """Gets the user_type of this User.  # noqa: E501


        :return: The user_type of this User.  # noqa: E501
        :rtype: int
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        """Sets the user_type of this User.


        :param user_type: The user_type of this User.  # noqa: E501
        :type: int
        """

        self._user_type = user_type

    @property
    def wallet_balance(self):
        """Gets the wallet_balance of this User.  # noqa: E501


        :return: The wallet_balance of this User.  # noqa: E501
        :rtype: int
        """
        return self._wallet_balance

    @wallet_balance.setter
    def wallet_balance(self, wallet_balance):
        """Sets the wallet_balance of this User.


        :param wallet_balance: The wallet_balance of this User.  # noqa: E501
        :type: int
        """

        self._wallet_balance = wallet_balance

    @property
    def device_id(self):
        """Gets the device_id of this User.  # noqa: E501


        :return: The device_id of this User.  # noqa: E501
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this User.


        :param device_id: The device_id of this User.  # noqa: E501
        :type: str
        """

        self._device_id = device_id

    @property
    def device_type(self):
        """Gets the device_type of this User.  # noqa: E501


        :return: The device_type of this User.  # noqa: E501
        :rtype: int
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this User.


        :param device_type: The device_type of this User.  # noqa: E501
        :type: int
        """

        self._device_type = device_type

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
        if issubclass(User, dict):
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
        if not isinstance(other, User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
