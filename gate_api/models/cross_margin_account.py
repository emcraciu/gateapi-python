# coding: utf-8

"""
    Gate API v4

    Welcome to Gate.io API  APIv4 provides spot, margin and futures trading operations. There are public APIs to retrieve the real-time market statistics, and private APIs which needs authentication to trade on user's behalf.  # noqa: E501

    Contact: support@mail.gate.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from gate_api.configuration import Configuration


class CrossMarginAccount(object):
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
        'user_id': 'int',
        'locked': 'bool',
        'balances': 'dict(str, CrossMarginBalance)',
        'total': 'str',
        'borrowed': 'str',
        'interest': 'str',
        'risk': 'str',
    }

    attribute_map = {
        'user_id': 'user_id',
        'locked': 'locked',
        'balances': 'balances',
        'total': 'total',
        'borrowed': 'borrowed',
        'interest': 'interest',
        'risk': 'risk',
    }

    def __init__(
        self,
        user_id=None,
        locked=None,
        balances=None,
        total=None,
        borrowed=None,
        interest=None,
        risk=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        # type: (int, bool, dict(str, CrossMarginBalance), str, str, str, str, Configuration) -> None
        """CrossMarginAccount - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user_id = None
        self._locked = None
        self._balances = None
        self._total = None
        self._borrowed = None
        self._interest = None
        self._risk = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        if locked is not None:
            self.locked = locked
        if balances is not None:
            self.balances = balances
        if total is not None:
            self.total = total
        if borrowed is not None:
            self.borrowed = borrowed
        if interest is not None:
            self.interest = interest
        if risk is not None:
            self.risk = risk

    @property
    def user_id(self):
        """Gets the user_id of this CrossMarginAccount.  # noqa: E501

        User ID  # noqa: E501

        :return: The user_id of this CrossMarginAccount.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this CrossMarginAccount.

        User ID  # noqa: E501

        :param user_id: The user_id of this CrossMarginAccount.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def locked(self):
        """Gets the locked of this CrossMarginAccount.  # noqa: E501

        Whether account is locked  # noqa: E501

        :return: The locked of this CrossMarginAccount.  # noqa: E501
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this CrossMarginAccount.

        Whether account is locked  # noqa: E501

        :param locked: The locked of this CrossMarginAccount.  # noqa: E501
        :type: bool
        """

        self._locked = locked

    @property
    def balances(self):
        """Gets the balances of this CrossMarginAccount.  # noqa: E501


        :return: The balances of this CrossMarginAccount.  # noqa: E501
        :rtype: dict(str, CrossMarginBalance)
        """
        return self._balances

    @balances.setter
    def balances(self, balances):
        """Sets the balances of this CrossMarginAccount.


        :param balances: The balances of this CrossMarginAccount.  # noqa: E501
        :type: dict(str, CrossMarginBalance)
        """

        self._balances = balances

    @property
    def total(self):
        """Gets the total of this CrossMarginAccount.  # noqa: E501

        Total account value in USDT, i.e., the sum of all currencies' `(available+freeze)*price*discount`  # noqa: E501

        :return: The total of this CrossMarginAccount.  # noqa: E501
        :rtype: str
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this CrossMarginAccount.

        Total account value in USDT, i.e., the sum of all currencies' `(available+freeze)*price*discount`  # noqa: E501

        :param total: The total of this CrossMarginAccount.  # noqa: E501
        :type: str
        """

        self._total = total

    @property
    def borrowed(self):
        """Gets the borrowed of this CrossMarginAccount.  # noqa: E501

        Total borrowed value in USDT, i.e., the sum of all currencies' `borrowed*price*discount`  # noqa: E501

        :return: The borrowed of this CrossMarginAccount.  # noqa: E501
        :rtype: str
        """
        return self._borrowed

    @borrowed.setter
    def borrowed(self, borrowed):
        """Sets the borrowed of this CrossMarginAccount.

        Total borrowed value in USDT, i.e., the sum of all currencies' `borrowed*price*discount`  # noqa: E501

        :param borrowed: The borrowed of this CrossMarginAccount.  # noqa: E501
        :type: str
        """

        self._borrowed = borrowed

    @property
    def interest(self):
        """Gets the interest of this CrossMarginAccount.  # noqa: E501

        Total unpaid interests in USDT, i.e., the sum of all currencies' `interest*price*discount`  # noqa: E501

        :return: The interest of this CrossMarginAccount.  # noqa: E501
        :rtype: str
        """
        return self._interest

    @interest.setter
    def interest(self, interest):
        """Sets the interest of this CrossMarginAccount.

        Total unpaid interests in USDT, i.e., the sum of all currencies' `interest*price*discount`  # noqa: E501

        :param interest: The interest of this CrossMarginAccount.  # noqa: E501
        :type: str
        """

        self._interest = interest

    @property
    def risk(self):
        """Gets the risk of this CrossMarginAccount.  # noqa: E501

        Risk rate. When it belows 110%, liquidation will be triggered. Calculation formula: `total / (borrowed+interest)`  # noqa: E501

        :return: The risk of this CrossMarginAccount.  # noqa: E501
        :rtype: str
        """
        return self._risk

    @risk.setter
    def risk(self, risk):
        """Sets the risk of this CrossMarginAccount.

        Risk rate. When it belows 110%, liquidation will be triggered. Calculation formula: `total / (borrowed+interest)`  # noqa: E501

        :param risk: The risk of this CrossMarginAccount.  # noqa: E501
        :type: str
        """

        self._risk = risk

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item,
                        value.items(),
                    )
                )
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
        if not isinstance(other, CrossMarginAccount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CrossMarginAccount):
            return True

        return self.to_dict() != other.to_dict()
