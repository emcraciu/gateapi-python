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


class FuturesTicker(object):
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
        'contract': 'str',
        'last': 'str',
        'change_percentage': 'str',
        'total_size': 'str',
        'volume_24h': 'str',
        'volume_24h_btc': 'str',
        'volume_24h_usd': 'str',
        'mark_price': 'str',
        'funding_rate': 'str',
        'index_price': 'str',
        'quanto_base_rate': 'str'
    }

    attribute_map = {
        'contract': 'contract',
        'last': 'last',
        'change_percentage': 'change_percentage',
        'total_size': 'total_size',
        'volume_24h': 'volume_24h',
        'volume_24h_btc': 'volume_24h_btc',
        'volume_24h_usd': 'volume_24h_usd',
        'mark_price': 'mark_price',
        'funding_rate': 'funding_rate',
        'index_price': 'index_price',
        'quanto_base_rate': 'quanto_base_rate'
    }

    def __init__(self, contract=None, last=None, change_percentage=None, total_size=None, volume_24h=None, volume_24h_btc=None, volume_24h_usd=None, mark_price=None, funding_rate=None, index_price=None, quanto_base_rate=None):  # noqa: E501
        """FuturesTicker - a model defined in OpenAPI"""  # noqa: E501

        self._contract = None
        self._last = None
        self._change_percentage = None
        self._total_size = None
        self._volume_24h = None
        self._volume_24h_btc = None
        self._volume_24h_usd = None
        self._mark_price = None
        self._funding_rate = None
        self._index_price = None
        self._quanto_base_rate = None
        self.discriminator = None

        if contract is not None:
            self.contract = contract
        if last is not None:
            self.last = last
        if change_percentage is not None:
            self.change_percentage = change_percentage
        if total_size is not None:
            self.total_size = total_size
        if volume_24h is not None:
            self.volume_24h = volume_24h
        if volume_24h_btc is not None:
            self.volume_24h_btc = volume_24h_btc
        if volume_24h_usd is not None:
            self.volume_24h_usd = volume_24h_usd
        if mark_price is not None:
            self.mark_price = mark_price
        if funding_rate is not None:
            self.funding_rate = funding_rate
        if index_price is not None:
            self.index_price = index_price
        if quanto_base_rate is not None:
            self.quanto_base_rate = quanto_base_rate

    @property
    def contract(self):
        """Gets the contract of this FuturesTicker.  # noqa: E501

        Futures contract  # noqa: E501

        :return: The contract of this FuturesTicker.  # noqa: E501
        :rtype: str
        """
        return self._contract

    @contract.setter
    def contract(self, contract):
        """Sets the contract of this FuturesTicker.

        Futures contract  # noqa: E501

        :param contract: The contract of this FuturesTicker.  # noqa: E501
        :type: str
        """

        self._contract = contract

    @property
    def last(self):
        """Gets the last of this FuturesTicker.  # noqa: E501

        Last trading price  # noqa: E501

        :return: The last of this FuturesTicker.  # noqa: E501
        :rtype: str
        """
        return self._last

    @last.setter
    def last(self, last):
        """Sets the last of this FuturesTicker.

        Last trading price  # noqa: E501

        :param last: The last of this FuturesTicker.  # noqa: E501
        :type: str
        """

        self._last = last

    @property
    def change_percentage(self):
        """Gets the change_percentage of this FuturesTicker.  # noqa: E501

        Change percentage.  # noqa: E501

        :return: The change_percentage of this FuturesTicker.  # noqa: E501
        :rtype: str
        """
        return self._change_percentage

    @change_percentage.setter
    def change_percentage(self, change_percentage):
        """Sets the change_percentage of this FuturesTicker.

        Change percentage.  # noqa: E501

        :param change_percentage: The change_percentage of this FuturesTicker.  # noqa: E501
        :type: str
        """

        self._change_percentage = change_percentage

    @property
    def total_size(self):
        """Gets the total_size of this FuturesTicker.  # noqa: E501

        Contract total size  # noqa: E501

        :return: The total_size of this FuturesTicker.  # noqa: E501
        :rtype: str
        """
        return self._total_size

    @total_size.setter
    def total_size(self, total_size):
        """Sets the total_size of this FuturesTicker.

        Contract total size  # noqa: E501

        :param total_size: The total_size of this FuturesTicker.  # noqa: E501
        :type: str
        """

        self._total_size = total_size

    @property
    def volume_24h(self):
        """Gets the volume_24h of this FuturesTicker.  # noqa: E501

        Trade size in recent 24h  # noqa: E501

        :return: The volume_24h of this FuturesTicker.  # noqa: E501
        :rtype: str
        """
        return self._volume_24h

    @volume_24h.setter
    def volume_24h(self, volume_24h):
        """Sets the volume_24h of this FuturesTicker.

        Trade size in recent 24h  # noqa: E501

        :param volume_24h: The volume_24h of this FuturesTicker.  # noqa: E501
        :type: str
        """

        self._volume_24h = volume_24h

    @property
    def volume_24h_btc(self):
        """Gets the volume_24h_btc of this FuturesTicker.  # noqa: E501

        Trade volume in recent 24h in BTC  # noqa: E501

        :return: The volume_24h_btc of this FuturesTicker.  # noqa: E501
        :rtype: str
        """
        return self._volume_24h_btc

    @volume_24h_btc.setter
    def volume_24h_btc(self, volume_24h_btc):
        """Sets the volume_24h_btc of this FuturesTicker.

        Trade volume in recent 24h in BTC  # noqa: E501

        :param volume_24h_btc: The volume_24h_btc of this FuturesTicker.  # noqa: E501
        :type: str
        """

        self._volume_24h_btc = volume_24h_btc

    @property
    def volume_24h_usd(self):
        """Gets the volume_24h_usd of this FuturesTicker.  # noqa: E501

        Trade volume in recent 24h in USD  # noqa: E501

        :return: The volume_24h_usd of this FuturesTicker.  # noqa: E501
        :rtype: str
        """
        return self._volume_24h_usd

    @volume_24h_usd.setter
    def volume_24h_usd(self, volume_24h_usd):
        """Sets the volume_24h_usd of this FuturesTicker.

        Trade volume in recent 24h in USD  # noqa: E501

        :param volume_24h_usd: The volume_24h_usd of this FuturesTicker.  # noqa: E501
        :type: str
        """

        self._volume_24h_usd = volume_24h_usd

    @property
    def mark_price(self):
        """Gets the mark_price of this FuturesTicker.  # noqa: E501

        Recent mark price  # noqa: E501

        :return: The mark_price of this FuturesTicker.  # noqa: E501
        :rtype: str
        """
        return self._mark_price

    @mark_price.setter
    def mark_price(self, mark_price):
        """Sets the mark_price of this FuturesTicker.

        Recent mark price  # noqa: E501

        :param mark_price: The mark_price of this FuturesTicker.  # noqa: E501
        :type: str
        """

        self._mark_price = mark_price

    @property
    def funding_rate(self):
        """Gets the funding_rate of this FuturesTicker.  # noqa: E501

        Funding rate  # noqa: E501

        :return: The funding_rate of this FuturesTicker.  # noqa: E501
        :rtype: str
        """
        return self._funding_rate

    @funding_rate.setter
    def funding_rate(self, funding_rate):
        """Sets the funding_rate of this FuturesTicker.

        Funding rate  # noqa: E501

        :param funding_rate: The funding_rate of this FuturesTicker.  # noqa: E501
        :type: str
        """

        self._funding_rate = funding_rate

    @property
    def index_price(self):
        """Gets the index_price of this FuturesTicker.  # noqa: E501

        Index price  # noqa: E501

        :return: The index_price of this FuturesTicker.  # noqa: E501
        :rtype: str
        """
        return self._index_price

    @index_price.setter
    def index_price(self, index_price):
        """Sets the index_price of this FuturesTicker.

        Index price  # noqa: E501

        :param index_price: The index_price of this FuturesTicker.  # noqa: E501
        :type: str
        """

        self._index_price = index_price

    @property
    def quanto_base_rate(self):
        """Gets the quanto_base_rate of this FuturesTicker.  # noqa: E501

        Exchange rate of base currency and settlement currency in Quanto contract. Not existed in contract of other types  # noqa: E501

        :return: The quanto_base_rate of this FuturesTicker.  # noqa: E501
        :rtype: str
        """
        return self._quanto_base_rate

    @quanto_base_rate.setter
    def quanto_base_rate(self, quanto_base_rate):
        """Sets the quanto_base_rate of this FuturesTicker.

        Exchange rate of base currency and settlement currency in Quanto contract. Not existed in contract of other types  # noqa: E501

        :param quanto_base_rate: The quanto_base_rate of this FuturesTicker.  # noqa: E501
        :type: str
        """

        self._quanto_base_rate = quanto_base_rate

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
        if not isinstance(other, FuturesTicker):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
