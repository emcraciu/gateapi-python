# coding: utf-8

"""
    Gate API v4

    APIv4 provides spot, margin and futures trading operations. There are public APIs to retrieve the real-time market statistics, and private APIs which needs authentication to trade on user's behalf.  # noqa: E501

    OpenAPI spec version: 4.7.2
    Contact: support@mail.gate.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class RepayRequest(object):
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
        'currency_pair': 'str',
        'currency': 'str',
        'mode': 'str',
        'amount': 'str'
    }

    attribute_map = {
        'currency_pair': 'currency_pair',
        'currency': 'currency',
        'mode': 'mode',
        'amount': 'amount'
    }

    def __init__(self, currency_pair=None, currency=None, mode=None, amount=None):  # noqa: E501
        """RepayRequest - a model defined in OpenAPI"""  # noqa: E501

        self._currency_pair = None
        self._currency = None
        self._mode = None
        self._amount = None
        self.discriminator = None

        self.currency_pair = currency_pair
        self.currency = currency
        self.mode = mode
        if amount is not None:
            self.amount = amount

    @property
    def currency_pair(self):
        """Gets the currency_pair of this RepayRequest.  # noqa: E501

        Currency pair  # noqa: E501

        :return: The currency_pair of this RepayRequest.  # noqa: E501
        :rtype: str
        """
        return self._currency_pair

    @currency_pair.setter
    def currency_pair(self, currency_pair):
        """Sets the currency_pair of this RepayRequest.

        Currency pair  # noqa: E501

        :param currency_pair: The currency_pair of this RepayRequest.  # noqa: E501
        :type: str
        """
        if currency_pair is None:
            raise ValueError("Invalid value for `currency_pair`, must not be `None`")  # noqa: E501

        self._currency_pair = currency_pair

    @property
    def currency(self):
        """Gets the currency of this RepayRequest.  # noqa: E501

        Loan currency  # noqa: E501

        :return: The currency of this RepayRequest.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this RepayRequest.

        Loan currency  # noqa: E501

        :param currency: The currency of this RepayRequest.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def mode(self):
        """Gets the mode of this RepayRequest.  # noqa: E501

        Repay mode. all - repay all; partial - repay only some portion  # noqa: E501

        :return: The mode of this RepayRequest.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this RepayRequest.

        Repay mode. all - repay all; partial - repay only some portion  # noqa: E501

        :param mode: The mode of this RepayRequest.  # noqa: E501
        :type: str
        """
        if mode is None:
            raise ValueError("Invalid value for `mode`, must not be `None`")  # noqa: E501
        allowed_values = ["all", "partial"]  # noqa: E501
        if mode not in allowed_values:
            raise ValueError(
                "Invalid value for `mode` ({0}), must be one of {1}"  # noqa: E501
                .format(mode, allowed_values)
            )

        self._mode = mode

    @property
    def amount(self):
        """Gets the amount of this RepayRequest.  # noqa: E501

        Repay amount. Required in `partial` mode  # noqa: E501

        :return: The amount of this RepayRequest.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this RepayRequest.

        Repay amount. Required in `partial` mode  # noqa: E501

        :param amount: The amount of this RepayRequest.  # noqa: E501
        :type: str
        """

        self._amount = amount

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
        if not isinstance(other, RepayRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
