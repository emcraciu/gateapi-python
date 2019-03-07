# coding: utf-8

"""
    Gate API v4

    APIv4 provides spot, margin and futures trading operations. There are public APIs to retrieve the real-time market statistics, and private APIs which needs authentication to trade on user's behalf.  # noqa: E501

    OpenAPI spec version: 4.5.0
    Contact: support@mail.gate.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class SpotAccount(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'currency': 'str',
        'available': 'str',
        'locked': 'str'
    }

    attribute_map = {
        'currency': 'currency',
        'available': 'available',
        'locked': 'locked'
    }

    def __init__(self, currency=None, available=None, locked=None):  # noqa: E501
        """SpotAccount - a model defined in OpenAPI"""  # noqa: E501

        self._currency = None
        self._available = None
        self._locked = None
        self.discriminator = None

        if currency is not None:
            self.currency = currency
        if available is not None:
            self.available = available
        if locked is not None:
            self.locked = locked

    @property
    def currency(self):
        """Gets the currency of this SpotAccount.  # noqa: E501

        Currency detail  # noqa: E501

        :return: The currency of this SpotAccount.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this SpotAccount.

        Currency detail  # noqa: E501

        :param currency: The currency of this SpotAccount.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def available(self):
        """Gets the available of this SpotAccount.  # noqa: E501

        Available amount  # noqa: E501

        :return: The available of this SpotAccount.  # noqa: E501
        :rtype: str
        """
        return self._available

    @available.setter
    def available(self, available):
        """Sets the available of this SpotAccount.

        Available amount  # noqa: E501

        :param available: The available of this SpotAccount.  # noqa: E501
        :type: str
        """

        self._available = available

    @property
    def locked(self):
        """Gets the locked of this SpotAccount.  # noqa: E501

        Locked amount, used in trading  # noqa: E501

        :return: The locked of this SpotAccount.  # noqa: E501
        :rtype: str
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this SpotAccount.

        Locked amount, used in trading  # noqa: E501

        :param locked: The locked of this SpotAccount.  # noqa: E501
        :type: str
        """

        self._locked = locked

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SpotAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
