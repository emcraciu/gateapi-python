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


class FuturesPriceTrigger(object):
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
        'strategy_type': 'int',
        'price_type': 'int',
        'price': 'str',
        'rule': 'int',
        'expiration': 'int'
    }

    attribute_map = {
        'strategy_type': 'strategy_type',
        'price_type': 'price_type',
        'price': 'price',
        'rule': 'rule',
        'expiration': 'expiration'
    }

    def __init__(self, strategy_type=None, price_type=None, price=None, rule=None, expiration=None):  # noqa: E501
        """FuturesPriceTrigger - a model defined in OpenAPI"""  # noqa: E501

        self._strategy_type = None
        self._price_type = None
        self._price = None
        self._rule = None
        self._expiration = None
        self.discriminator = None

        if strategy_type is not None:
            self.strategy_type = strategy_type
        if price_type is not None:
            self.price_type = price_type
        if price is not None:
            self.price = price
        if rule is not None:
            self.rule = rule
        if expiration is not None:
            self.expiration = expiration

    @property
    def strategy_type(self):
        """Gets the strategy_type of this FuturesPriceTrigger.  # noqa: E501

        How the order will be triggered   - `0`: by price, which means order will be triggered on price condition satisfied  - `1`: by price gap, which means order will be triggered on gap of recent two prices of specified `price_type` satisfied.  Only `0` is supported currently  # noqa: E501

        :return: The strategy_type of this FuturesPriceTrigger.  # noqa: E501
        :rtype: int
        """
        return self._strategy_type

    @strategy_type.setter
    def strategy_type(self, strategy_type):
        """Sets the strategy_type of this FuturesPriceTrigger.

        How the order will be triggered   - `0`: by price, which means order will be triggered on price condition satisfied  - `1`: by price gap, which means order will be triggered on gap of recent two prices of specified `price_type` satisfied.  Only `0` is supported currently  # noqa: E501

        :param strategy_type: The strategy_type of this FuturesPriceTrigger.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1]  # noqa: E501
        if strategy_type not in allowed_values:
            raise ValueError(
                "Invalid value for `strategy_type` ({0}), must be one of {1}"  # noqa: E501
                .format(strategy_type, allowed_values)
            )

        self._strategy_type = strategy_type

    @property
    def price_type(self):
        """Gets the price_type of this FuturesPriceTrigger.  # noqa: E501

        Price type. 0 - latest deal price, 1 - mark price, 2 - index price  # noqa: E501

        :return: The price_type of this FuturesPriceTrigger.  # noqa: E501
        :rtype: int
        """
        return self._price_type

    @price_type.setter
    def price_type(self, price_type):
        """Sets the price_type of this FuturesPriceTrigger.

        Price type. 0 - latest deal price, 1 - mark price, 2 - index price  # noqa: E501

        :param price_type: The price_type of this FuturesPriceTrigger.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2]  # noqa: E501
        if price_type not in allowed_values:
            raise ValueError(
                "Invalid value for `price_type` ({0}), must be one of {1}"  # noqa: E501
                .format(price_type, allowed_values)
            )

        self._price_type = price_type

    @property
    def price(self):
        """Gets the price of this FuturesPriceTrigger.  # noqa: E501

        Value of price on price triggered, or price gap on price gap triggered  # noqa: E501

        :return: The price of this FuturesPriceTrigger.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this FuturesPriceTrigger.

        Value of price on price triggered, or price gap on price gap triggered  # noqa: E501

        :param price: The price of this FuturesPriceTrigger.  # noqa: E501
        :type: str
        """

        self._price = price

    @property
    def rule(self):
        """Gets the rule of this FuturesPriceTrigger.  # noqa: E501

        Trigger condition type  - `1`: calculated price based on `strategy_type` and `price_type` >= `price` - `2`: calculated price based on `strategy_type` and `price_type` <= `price`  # noqa: E501

        :return: The rule of this FuturesPriceTrigger.  # noqa: E501
        :rtype: int
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """Sets the rule of this FuturesPriceTrigger.

        Trigger condition type  - `1`: calculated price based on `strategy_type` and `price_type` >= `price` - `2`: calculated price based on `strategy_type` and `price_type` <= `price`  # noqa: E501

        :param rule: The rule of this FuturesPriceTrigger.  # noqa: E501
        :type: int
        """
        allowed_values = [1, 2]  # noqa: E501
        if rule not in allowed_values:
            raise ValueError(
                "Invalid value for `rule` ({0}), must be one of {1}"  # noqa: E501
                .format(rule, allowed_values)
            )

        self._rule = rule

    @property
    def expiration(self):
        """Gets the expiration of this FuturesPriceTrigger.  # noqa: E501

        How many seconds will the order wait for the condition being triggered. Order will be cancelled on timed out  # noqa: E501

        :return: The expiration of this FuturesPriceTrigger.  # noqa: E501
        :rtype: int
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this FuturesPriceTrigger.

        How many seconds will the order wait for the condition being triggered. Order will be cancelled on timed out  # noqa: E501

        :param expiration: The expiration of this FuturesPriceTrigger.  # noqa: E501
        :type: int
        """

        self._expiration = expiration

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
        if not isinstance(other, FuturesPriceTrigger):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
