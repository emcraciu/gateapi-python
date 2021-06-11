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


class DeliveryContract(object):
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
        'name': 'str',
        'underlying': 'str',
        'cycle': 'str',
        'type': 'str',
        'quanto_multiplier': 'str',
        'leverage_min': 'str',
        'leverage_max': 'str',
        'maintenance_rate': 'str',
        'mark_type': 'str',
        'mark_price': 'str',
        'index_price': 'str',
        'last_price': 'str',
        'maker_fee_rate': 'str',
        'taker_fee_rate': 'str',
        'order_price_round': 'str',
        'mark_price_round': 'str',
        'basis_rate': 'str',
        'basis_value': 'str',
        'basis_impact_value': 'str',
        'settle_price': 'str',
        'settle_price_interval': 'int',
        'settle_price_duration': 'int',
        'expire_time': 'int',
        'risk_limit_base': 'str',
        'risk_limit_step': 'str',
        'risk_limit_max': 'str',
        'order_size_min': 'int',
        'order_size_max': 'int',
        'order_price_deviate': 'str',
        'ref_discount_rate': 'str',
        'ref_rebate_rate': 'str',
        'orderbook_id': 'int',
        'trade_id': 'int',
        'trade_size': 'int',
        'position_size': 'int',
        'config_change_time': 'float',
        'in_delisting': 'bool',
        'orders_limit': 'int',
    }

    attribute_map = {
        'name': 'name',
        'underlying': 'underlying',
        'cycle': 'cycle',
        'type': 'type',
        'quanto_multiplier': 'quanto_multiplier',
        'leverage_min': 'leverage_min',
        'leverage_max': 'leverage_max',
        'maintenance_rate': 'maintenance_rate',
        'mark_type': 'mark_type',
        'mark_price': 'mark_price',
        'index_price': 'index_price',
        'last_price': 'last_price',
        'maker_fee_rate': 'maker_fee_rate',
        'taker_fee_rate': 'taker_fee_rate',
        'order_price_round': 'order_price_round',
        'mark_price_round': 'mark_price_round',
        'basis_rate': 'basis_rate',
        'basis_value': 'basis_value',
        'basis_impact_value': 'basis_impact_value',
        'settle_price': 'settle_price',
        'settle_price_interval': 'settle_price_interval',
        'settle_price_duration': 'settle_price_duration',
        'expire_time': 'expire_time',
        'risk_limit_base': 'risk_limit_base',
        'risk_limit_step': 'risk_limit_step',
        'risk_limit_max': 'risk_limit_max',
        'order_size_min': 'order_size_min',
        'order_size_max': 'order_size_max',
        'order_price_deviate': 'order_price_deviate',
        'ref_discount_rate': 'ref_discount_rate',
        'ref_rebate_rate': 'ref_rebate_rate',
        'orderbook_id': 'orderbook_id',
        'trade_id': 'trade_id',
        'trade_size': 'trade_size',
        'position_size': 'position_size',
        'config_change_time': 'config_change_time',
        'in_delisting': 'in_delisting',
        'orders_limit': 'orders_limit',
    }

    def __init__(
        self,
        name=None,
        underlying=None,
        cycle=None,
        type=None,
        quanto_multiplier=None,
        leverage_min=None,
        leverage_max=None,
        maintenance_rate=None,
        mark_type=None,
        mark_price=None,
        index_price=None,
        last_price=None,
        maker_fee_rate=None,
        taker_fee_rate=None,
        order_price_round=None,
        mark_price_round=None,
        basis_rate=None,
        basis_value=None,
        basis_impact_value=None,
        settle_price=None,
        settle_price_interval=None,
        settle_price_duration=None,
        expire_time=None,
        risk_limit_base=None,
        risk_limit_step=None,
        risk_limit_max=None,
        order_size_min=None,
        order_size_max=None,
        order_price_deviate=None,
        ref_discount_rate=None,
        ref_rebate_rate=None,
        orderbook_id=None,
        trade_id=None,
        trade_size=None,
        position_size=None,
        config_change_time=None,
        in_delisting=None,
        orders_limit=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        # type: (str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, int, int, int, str, str, str, int, int, str, str, str, int, int, int, int, float, bool, int, Configuration) -> None
        """DeliveryContract - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._underlying = None
        self._cycle = None
        self._type = None
        self._quanto_multiplier = None
        self._leverage_min = None
        self._leverage_max = None
        self._maintenance_rate = None
        self._mark_type = None
        self._mark_price = None
        self._index_price = None
        self._last_price = None
        self._maker_fee_rate = None
        self._taker_fee_rate = None
        self._order_price_round = None
        self._mark_price_round = None
        self._basis_rate = None
        self._basis_value = None
        self._basis_impact_value = None
        self._settle_price = None
        self._settle_price_interval = None
        self._settle_price_duration = None
        self._expire_time = None
        self._risk_limit_base = None
        self._risk_limit_step = None
        self._risk_limit_max = None
        self._order_size_min = None
        self._order_size_max = None
        self._order_price_deviate = None
        self._ref_discount_rate = None
        self._ref_rebate_rate = None
        self._orderbook_id = None
        self._trade_id = None
        self._trade_size = None
        self._position_size = None
        self._config_change_time = None
        self._in_delisting = None
        self._orders_limit = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if underlying is not None:
            self.underlying = underlying
        if cycle is not None:
            self.cycle = cycle
        if type is not None:
            self.type = type
        if quanto_multiplier is not None:
            self.quanto_multiplier = quanto_multiplier
        if leverage_min is not None:
            self.leverage_min = leverage_min
        if leverage_max is not None:
            self.leverage_max = leverage_max
        if maintenance_rate is not None:
            self.maintenance_rate = maintenance_rate
        if mark_type is not None:
            self.mark_type = mark_type
        if mark_price is not None:
            self.mark_price = mark_price
        if index_price is not None:
            self.index_price = index_price
        if last_price is not None:
            self.last_price = last_price
        if maker_fee_rate is not None:
            self.maker_fee_rate = maker_fee_rate
        if taker_fee_rate is not None:
            self.taker_fee_rate = taker_fee_rate
        if order_price_round is not None:
            self.order_price_round = order_price_round
        if mark_price_round is not None:
            self.mark_price_round = mark_price_round
        if basis_rate is not None:
            self.basis_rate = basis_rate
        if basis_value is not None:
            self.basis_value = basis_value
        if basis_impact_value is not None:
            self.basis_impact_value = basis_impact_value
        if settle_price is not None:
            self.settle_price = settle_price
        if settle_price_interval is not None:
            self.settle_price_interval = settle_price_interval
        if settle_price_duration is not None:
            self.settle_price_duration = settle_price_duration
        if expire_time is not None:
            self.expire_time = expire_time
        if risk_limit_base is not None:
            self.risk_limit_base = risk_limit_base
        if risk_limit_step is not None:
            self.risk_limit_step = risk_limit_step
        if risk_limit_max is not None:
            self.risk_limit_max = risk_limit_max
        if order_size_min is not None:
            self.order_size_min = order_size_min
        if order_size_max is not None:
            self.order_size_max = order_size_max
        if order_price_deviate is not None:
            self.order_price_deviate = order_price_deviate
        if ref_discount_rate is not None:
            self.ref_discount_rate = ref_discount_rate
        if ref_rebate_rate is not None:
            self.ref_rebate_rate = ref_rebate_rate
        if orderbook_id is not None:
            self.orderbook_id = orderbook_id
        if trade_id is not None:
            self.trade_id = trade_id
        if trade_size is not None:
            self.trade_size = trade_size
        if position_size is not None:
            self.position_size = position_size
        if config_change_time is not None:
            self.config_change_time = config_change_time
        if in_delisting is not None:
            self.in_delisting = in_delisting
        if orders_limit is not None:
            self.orders_limit = orders_limit

    @property
    def name(self):
        """Gets the name of this DeliveryContract.  # noqa: E501

        Futures contract  # noqa: E501

        :return: The name of this DeliveryContract.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeliveryContract.

        Futures contract  # noqa: E501

        :param name: The name of this DeliveryContract.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def underlying(self):
        """Gets the underlying of this DeliveryContract.  # noqa: E501

        Underlying  # noqa: E501

        :return: The underlying of this DeliveryContract.  # noqa: E501
        :rtype: str
        """
        return self._underlying

    @underlying.setter
    def underlying(self, underlying):
        """Sets the underlying of this DeliveryContract.

        Underlying  # noqa: E501

        :param underlying: The underlying of this DeliveryContract.  # noqa: E501
        :type: str
        """

        self._underlying = underlying

    @property
    def cycle(self):
        """Gets the cycle of this DeliveryContract.  # noqa: E501

        Cycle type, e.g. WEEKLY, QUARTERLY  # noqa: E501

        :return: The cycle of this DeliveryContract.  # noqa: E501
        :rtype: str
        """
        return self._cycle

    @cycle.setter
    def cycle(self, cycle):
        """Sets the cycle of this DeliveryContract.

        Cycle type, e.g. WEEKLY, QUARTERLY  # noqa: E501

        :param cycle: The cycle of this DeliveryContract.  # noqa: E501
        :type: str
        """
        allowed_values = ["WEEKLY", "BI-WEEKLY", "QUARTERLY", "BI-QUARTERLY"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and cycle not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `cycle` ({0}), must be one of {1}".format(cycle, allowed_values)  # noqa: E501
            )

        self._cycle = cycle

    @property
    def type(self):
        """Gets the type of this DeliveryContract.  # noqa: E501

        Futures contract type  # noqa: E501

        :return: The type of this DeliveryContract.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DeliveryContract.

        Futures contract type  # noqa: E501

        :param type: The type of this DeliveryContract.  # noqa: E501
        :type: str
        """
        allowed_values = ["inverse", "direct"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}".format(type, allowed_values)  # noqa: E501
            )

        self._type = type

    @property
    def quanto_multiplier(self):
        """Gets the quanto_multiplier of this DeliveryContract.  # noqa: E501

        Multiplier used in converting from invoicing to settlement currency  # noqa: E501

        :return: The quanto_multiplier of this DeliveryContract.  # noqa: E501
        :rtype: str
        """
        return self._quanto_multiplier

    @quanto_multiplier.setter
    def quanto_multiplier(self, quanto_multiplier):
        """Sets the quanto_multiplier of this DeliveryContract.

        Multiplier used in converting from invoicing to settlement currency  # noqa: E501

        :param quanto_multiplier: The quanto_multiplier of this DeliveryContract.  # noqa: E501
        :type: str
        """

        self._quanto_multiplier = quanto_multiplier

    @property
    def leverage_min(self):
        """Gets the leverage_min of this DeliveryContract.  # noqa: E501

        Minimum leverage  # noqa: E501

        :return: The leverage_min of this DeliveryContract.  # noqa: E501
        :rtype: str
        """
        return self._leverage_min

    @leverage_min.setter
    def leverage_min(self, leverage_min):
        """Sets the leverage_min of this DeliveryContract.

        Minimum leverage  # noqa: E501

        :param leverage_min: The leverage_min of this DeliveryContract.  # noqa: E501
        :type: str
        """

        self._leverage_min = leverage_min

    @property
    def leverage_max(self):
        """Gets the leverage_max of this DeliveryContract.  # noqa: E501

        Maximum leverage  # noqa: E501

        :return: The leverage_max of this DeliveryContract.  # noqa: E501
        :rtype: str
        """
        return self._leverage_max

    @leverage_max.setter
    def leverage_max(self, leverage_max):
        """Sets the leverage_max of this DeliveryContract.

        Maximum leverage  # noqa: E501

        :param leverage_max: The leverage_max of this DeliveryContract.  # noqa: E501
        :type: str
        """

        self._leverage_max = leverage_max

    @property
    def maintenance_rate(self):
        """Gets the maintenance_rate of this DeliveryContract.  # noqa: E501

        Maintenance rate of margin  # noqa: E501

        :return: The maintenance_rate of this DeliveryContract.  # noqa: E501
        :rtype: str
        """
        return self._maintenance_rate

    @maintenance_rate.setter
    def maintenance_rate(self, maintenance_rate):
        """Sets the maintenance_rate of this DeliveryContract.

        Maintenance rate of margin  # noqa: E501

        :param maintenance_rate: The maintenance_rate of this DeliveryContract.  # noqa: E501
        :type: str
        """

        self._maintenance_rate = maintenance_rate

    @property
    def mark_type(self):
        """Gets the mark_type of this DeliveryContract.  # noqa: E501

        Mark price type, internal - based on internal trading, index - based on external index price  # noqa: E501

        :return: The mark_type of this DeliveryContract.  # noqa: E501
        :rtype: str
        """
        return self._mark_type

    @mark_type.setter
    def mark_type(self, mark_type):
        """Sets the mark_type of this DeliveryContract.

        Mark price type, internal - based on internal trading, index - based on external index price  # noqa: E501

        :param mark_type: The mark_type of this DeliveryContract.  # noqa: E501
        :type: str
        """
        allowed_values = ["internal", "index"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and mark_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `mark_type` ({0}), must be one of {1}".format(  # noqa: E501
                    mark_type, allowed_values
                )
            )

        self._mark_type = mark_type

    @property
    def mark_price(self):
        """Gets the mark_price of this DeliveryContract.  # noqa: E501

        Current mark price  # noqa: E501

        :return: The mark_price of this DeliveryContract.  # noqa: E501
        :rtype: str
        """
        return self._mark_price

    @mark_price.setter
    def mark_price(self, mark_price):
        """Sets the mark_price of this DeliveryContract.

        Current mark price  # noqa: E501

        :param mark_price: The mark_price of this DeliveryContract.  # noqa: E501
        :type: str
        """

        self._mark_price = mark_price

    @property
    def index_price(self):
        """Gets the index_price of this DeliveryContract.  # noqa: E501

        Current index price  # noqa: E501

        :return: The index_price of this DeliveryContract.  # noqa: E501
        :rtype: str
        """
        return self._index_price

    @index_price.setter
    def index_price(self, index_price):
        """Sets the index_price of this DeliveryContract.

        Current index price  # noqa: E501

        :param index_price: The index_price of this DeliveryContract.  # noqa: E501
        :type: str
        """

        self._index_price = index_price

    @property
    def last_price(self):
        """Gets the last_price of this DeliveryContract.  # noqa: E501

        Last trading price  # noqa: E501

        :return: The last_price of this DeliveryContract.  # noqa: E501
        :rtype: str
        """
        return self._last_price

    @last_price.setter
    def last_price(self, last_price):
        """Sets the last_price of this DeliveryContract.

        Last trading price  # noqa: E501

        :param last_price: The last_price of this DeliveryContract.  # noqa: E501
        :type: str
        """

        self._last_price = last_price

    @property
    def maker_fee_rate(self):
        """Gets the maker_fee_rate of this DeliveryContract.  # noqa: E501

        Maker fee rate, where negative means rebate  # noqa: E501

        :return: The maker_fee_rate of this DeliveryContract.  # noqa: E501
        :rtype: str
        """
        return self._maker_fee_rate

    @maker_fee_rate.setter
    def maker_fee_rate(self, maker_fee_rate):
        """Sets the maker_fee_rate of this DeliveryContract.

        Maker fee rate, where negative means rebate  # noqa: E501

        :param maker_fee_rate: The maker_fee_rate of this DeliveryContract.  # noqa: E501
        :type: str
        """

        self._maker_fee_rate = maker_fee_rate

    @property
    def taker_fee_rate(self):
        """Gets the taker_fee_rate of this DeliveryContract.  # noqa: E501

        Taker fee rate  # noqa: E501

        :return: The taker_fee_rate of this DeliveryContract.  # noqa: E501
        :rtype: str
        """
        return self._taker_fee_rate

    @taker_fee_rate.setter
    def taker_fee_rate(self, taker_fee_rate):
        """Sets the taker_fee_rate of this DeliveryContract.

        Taker fee rate  # noqa: E501

        :param taker_fee_rate: The taker_fee_rate of this DeliveryContract.  # noqa: E501
        :type: str
        """

        self._taker_fee_rate = taker_fee_rate

    @property
    def order_price_round(self):
        """Gets the order_price_round of this DeliveryContract.  # noqa: E501

        Minimum order price increment  # noqa: E501

        :return: The order_price_round of this DeliveryContract.  # noqa: E501
        :rtype: str
        """
        return self._order_price_round

    @order_price_round.setter
    def order_price_round(self, order_price_round):
        """Sets the order_price_round of this DeliveryContract.

        Minimum order price increment  # noqa: E501

        :param order_price_round: The order_price_round of this DeliveryContract.  # noqa: E501
        :type: str
        """

        self._order_price_round = order_price_round

    @property
    def mark_price_round(self):
        """Gets the mark_price_round of this DeliveryContract.  # noqa: E501

        Minimum mark price increment  # noqa: E501

        :return: The mark_price_round of this DeliveryContract.  # noqa: E501
        :rtype: str
        """
        return self._mark_price_round

    @mark_price_round.setter
    def mark_price_round(self, mark_price_round):
        """Sets the mark_price_round of this DeliveryContract.

        Minimum mark price increment  # noqa: E501

        :param mark_price_round: The mark_price_round of this DeliveryContract.  # noqa: E501
        :type: str
        """

        self._mark_price_round = mark_price_round

    @property
    def basis_rate(self):
        """Gets the basis_rate of this DeliveryContract.  # noqa: E501

        Fair basis rate  # noqa: E501

        :return: The basis_rate of this DeliveryContract.  # noqa: E501
        :rtype: str
        """
        return self._basis_rate

    @basis_rate.setter
    def basis_rate(self, basis_rate):
        """Sets the basis_rate of this DeliveryContract.

        Fair basis rate  # noqa: E501

        :param basis_rate: The basis_rate of this DeliveryContract.  # noqa: E501
        :type: str
        """

        self._basis_rate = basis_rate

    @property
    def basis_value(self):
        """Gets the basis_value of this DeliveryContract.  # noqa: E501

        Fair basis value  # noqa: E501

        :return: The basis_value of this DeliveryContract.  # noqa: E501
        :rtype: str
        """
        return self._basis_value

    @basis_value.setter
    def basis_value(self, basis_value):
        """Sets the basis_value of this DeliveryContract.

        Fair basis value  # noqa: E501

        :param basis_value: The basis_value of this DeliveryContract.  # noqa: E501
        :type: str
        """

        self._basis_value = basis_value

    @property
    def basis_impact_value(self):
        """Gets the basis_impact_value of this DeliveryContract.  # noqa: E501

        Funding used for calculating impact bid, ask price  # noqa: E501

        :return: The basis_impact_value of this DeliveryContract.  # noqa: E501
        :rtype: str
        """
        return self._basis_impact_value

    @basis_impact_value.setter
    def basis_impact_value(self, basis_impact_value):
        """Sets the basis_impact_value of this DeliveryContract.

        Funding used for calculating impact bid, ask price  # noqa: E501

        :param basis_impact_value: The basis_impact_value of this DeliveryContract.  # noqa: E501
        :type: str
        """

        self._basis_impact_value = basis_impact_value

    @property
    def settle_price(self):
        """Gets the settle_price of this DeliveryContract.  # noqa: E501

        Settle price  # noqa: E501

        :return: The settle_price of this DeliveryContract.  # noqa: E501
        :rtype: str
        """
        return self._settle_price

    @settle_price.setter
    def settle_price(self, settle_price):
        """Sets the settle_price of this DeliveryContract.

        Settle price  # noqa: E501

        :param settle_price: The settle_price of this DeliveryContract.  # noqa: E501
        :type: str
        """

        self._settle_price = settle_price

    @property
    def settle_price_interval(self):
        """Gets the settle_price_interval of this DeliveryContract.  # noqa: E501

        Settle price update interval  # noqa: E501

        :return: The settle_price_interval of this DeliveryContract.  # noqa: E501
        :rtype: int
        """
        return self._settle_price_interval

    @settle_price_interval.setter
    def settle_price_interval(self, settle_price_interval):
        """Sets the settle_price_interval of this DeliveryContract.

        Settle price update interval  # noqa: E501

        :param settle_price_interval: The settle_price_interval of this DeliveryContract.  # noqa: E501
        :type: int
        """

        self._settle_price_interval = settle_price_interval

    @property
    def settle_price_duration(self):
        """Gets the settle_price_duration of this DeliveryContract.  # noqa: E501

        Settle price update duration in seconds  # noqa: E501

        :return: The settle_price_duration of this DeliveryContract.  # noqa: E501
        :rtype: int
        """
        return self._settle_price_duration

    @settle_price_duration.setter
    def settle_price_duration(self, settle_price_duration):
        """Sets the settle_price_duration of this DeliveryContract.

        Settle price update duration in seconds  # noqa: E501

        :param settle_price_duration: The settle_price_duration of this DeliveryContract.  # noqa: E501
        :type: int
        """

        self._settle_price_duration = settle_price_duration

    @property
    def expire_time(self):
        """Gets the expire_time of this DeliveryContract.  # noqa: E501

        Contract expiry timestamp  # noqa: E501

        :return: The expire_time of this DeliveryContract.  # noqa: E501
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this DeliveryContract.

        Contract expiry timestamp  # noqa: E501

        :param expire_time: The expire_time of this DeliveryContract.  # noqa: E501
        :type: int
        """

        self._expire_time = expire_time

    @property
    def risk_limit_base(self):
        """Gets the risk_limit_base of this DeliveryContract.  # noqa: E501

        Risk limit base  # noqa: E501

        :return: The risk_limit_base of this DeliveryContract.  # noqa: E501
        :rtype: str
        """
        return self._risk_limit_base

    @risk_limit_base.setter
    def risk_limit_base(self, risk_limit_base):
        """Sets the risk_limit_base of this DeliveryContract.

        Risk limit base  # noqa: E501

        :param risk_limit_base: The risk_limit_base of this DeliveryContract.  # noqa: E501
        :type: str
        """

        self._risk_limit_base = risk_limit_base

    @property
    def risk_limit_step(self):
        """Gets the risk_limit_step of this DeliveryContract.  # noqa: E501

        Step of adjusting risk limit  # noqa: E501

        :return: The risk_limit_step of this DeliveryContract.  # noqa: E501
        :rtype: str
        """
        return self._risk_limit_step

    @risk_limit_step.setter
    def risk_limit_step(self, risk_limit_step):
        """Sets the risk_limit_step of this DeliveryContract.

        Step of adjusting risk limit  # noqa: E501

        :param risk_limit_step: The risk_limit_step of this DeliveryContract.  # noqa: E501
        :type: str
        """

        self._risk_limit_step = risk_limit_step

    @property
    def risk_limit_max(self):
        """Gets the risk_limit_max of this DeliveryContract.  # noqa: E501

        Maximum risk limit the contract allowed  # noqa: E501

        :return: The risk_limit_max of this DeliveryContract.  # noqa: E501
        :rtype: str
        """
        return self._risk_limit_max

    @risk_limit_max.setter
    def risk_limit_max(self, risk_limit_max):
        """Sets the risk_limit_max of this DeliveryContract.

        Maximum risk limit the contract allowed  # noqa: E501

        :param risk_limit_max: The risk_limit_max of this DeliveryContract.  # noqa: E501
        :type: str
        """

        self._risk_limit_max = risk_limit_max

    @property
    def order_size_min(self):
        """Gets the order_size_min of this DeliveryContract.  # noqa: E501

        Minimum order size the contract allowed  # noqa: E501

        :return: The order_size_min of this DeliveryContract.  # noqa: E501
        :rtype: int
        """
        return self._order_size_min

    @order_size_min.setter
    def order_size_min(self, order_size_min):
        """Sets the order_size_min of this DeliveryContract.

        Minimum order size the contract allowed  # noqa: E501

        :param order_size_min: The order_size_min of this DeliveryContract.  # noqa: E501
        :type: int
        """

        self._order_size_min = order_size_min

    @property
    def order_size_max(self):
        """Gets the order_size_max of this DeliveryContract.  # noqa: E501

        Maximum order size the contract allowed  # noqa: E501

        :return: The order_size_max of this DeliveryContract.  # noqa: E501
        :rtype: int
        """
        return self._order_size_max

    @order_size_max.setter
    def order_size_max(self, order_size_max):
        """Sets the order_size_max of this DeliveryContract.

        Maximum order size the contract allowed  # noqa: E501

        :param order_size_max: The order_size_max of this DeliveryContract.  # noqa: E501
        :type: int
        """

        self._order_size_max = order_size_max

    @property
    def order_price_deviate(self):
        """Gets the order_price_deviate of this DeliveryContract.  # noqa: E501

        deviation between order price and current index price. If price of an order is denoted as order_price, it must meet the following condition:      abs(order_price - mark_price) <= mark_price * order_price_deviate  # noqa: E501

        :return: The order_price_deviate of this DeliveryContract.  # noqa: E501
        :rtype: str
        """
        return self._order_price_deviate

    @order_price_deviate.setter
    def order_price_deviate(self, order_price_deviate):
        """Sets the order_price_deviate of this DeliveryContract.

        deviation between order price and current index price. If price of an order is denoted as order_price, it must meet the following condition:      abs(order_price - mark_price) <= mark_price * order_price_deviate  # noqa: E501

        :param order_price_deviate: The order_price_deviate of this DeliveryContract.  # noqa: E501
        :type: str
        """

        self._order_price_deviate = order_price_deviate

    @property
    def ref_discount_rate(self):
        """Gets the ref_discount_rate of this DeliveryContract.  # noqa: E501

        Referral fee rate discount  # noqa: E501

        :return: The ref_discount_rate of this DeliveryContract.  # noqa: E501
        :rtype: str
        """
        return self._ref_discount_rate

    @ref_discount_rate.setter
    def ref_discount_rate(self, ref_discount_rate):
        """Sets the ref_discount_rate of this DeliveryContract.

        Referral fee rate discount  # noqa: E501

        :param ref_discount_rate: The ref_discount_rate of this DeliveryContract.  # noqa: E501
        :type: str
        """

        self._ref_discount_rate = ref_discount_rate

    @property
    def ref_rebate_rate(self):
        """Gets the ref_rebate_rate of this DeliveryContract.  # noqa: E501

        Referrer commission rate  # noqa: E501

        :return: The ref_rebate_rate of this DeliveryContract.  # noqa: E501
        :rtype: str
        """
        return self._ref_rebate_rate

    @ref_rebate_rate.setter
    def ref_rebate_rate(self, ref_rebate_rate):
        """Sets the ref_rebate_rate of this DeliveryContract.

        Referrer commission rate  # noqa: E501

        :param ref_rebate_rate: The ref_rebate_rate of this DeliveryContract.  # noqa: E501
        :type: str
        """

        self._ref_rebate_rate = ref_rebate_rate

    @property
    def orderbook_id(self):
        """Gets the orderbook_id of this DeliveryContract.  # noqa: E501

        Current orderbook ID  # noqa: E501

        :return: The orderbook_id of this DeliveryContract.  # noqa: E501
        :rtype: int
        """
        return self._orderbook_id

    @orderbook_id.setter
    def orderbook_id(self, orderbook_id):
        """Sets the orderbook_id of this DeliveryContract.

        Current orderbook ID  # noqa: E501

        :param orderbook_id: The orderbook_id of this DeliveryContract.  # noqa: E501
        :type: int
        """

        self._orderbook_id = orderbook_id

    @property
    def trade_id(self):
        """Gets the trade_id of this DeliveryContract.  # noqa: E501

        Current trade ID  # noqa: E501

        :return: The trade_id of this DeliveryContract.  # noqa: E501
        :rtype: int
        """
        return self._trade_id

    @trade_id.setter
    def trade_id(self, trade_id):
        """Sets the trade_id of this DeliveryContract.

        Current trade ID  # noqa: E501

        :param trade_id: The trade_id of this DeliveryContract.  # noqa: E501
        :type: int
        """

        self._trade_id = trade_id

    @property
    def trade_size(self):
        """Gets the trade_size of this DeliveryContract.  # noqa: E501

        Historical accumulation trade size  # noqa: E501

        :return: The trade_size of this DeliveryContract.  # noqa: E501
        :rtype: int
        """
        return self._trade_size

    @trade_size.setter
    def trade_size(self, trade_size):
        """Sets the trade_size of this DeliveryContract.

        Historical accumulation trade size  # noqa: E501

        :param trade_size: The trade_size of this DeliveryContract.  # noqa: E501
        :type: int
        """

        self._trade_size = trade_size

    @property
    def position_size(self):
        """Gets the position_size of this DeliveryContract.  # noqa: E501

        Current total long position size  # noqa: E501

        :return: The position_size of this DeliveryContract.  # noqa: E501
        :rtype: int
        """
        return self._position_size

    @position_size.setter
    def position_size(self, position_size):
        """Sets the position_size of this DeliveryContract.

        Current total long position size  # noqa: E501

        :param position_size: The position_size of this DeliveryContract.  # noqa: E501
        :type: int
        """

        self._position_size = position_size

    @property
    def config_change_time(self):
        """Gets the config_change_time of this DeliveryContract.  # noqa: E501

        Configuration's last changed time  # noqa: E501

        :return: The config_change_time of this DeliveryContract.  # noqa: E501
        :rtype: float
        """
        return self._config_change_time

    @config_change_time.setter
    def config_change_time(self, config_change_time):
        """Sets the config_change_time of this DeliveryContract.

        Configuration's last changed time  # noqa: E501

        :param config_change_time: The config_change_time of this DeliveryContract.  # noqa: E501
        :type: float
        """

        self._config_change_time = config_change_time

    @property
    def in_delisting(self):
        """Gets the in_delisting of this DeliveryContract.  # noqa: E501

        Contract is delisting  # noqa: E501

        :return: The in_delisting of this DeliveryContract.  # noqa: E501
        :rtype: bool
        """
        return self._in_delisting

    @in_delisting.setter
    def in_delisting(self, in_delisting):
        """Sets the in_delisting of this DeliveryContract.

        Contract is delisting  # noqa: E501

        :param in_delisting: The in_delisting of this DeliveryContract.  # noqa: E501
        :type: bool
        """

        self._in_delisting = in_delisting

    @property
    def orders_limit(self):
        """Gets the orders_limit of this DeliveryContract.  # noqa: E501

        Maximum number of open orders  # noqa: E501

        :return: The orders_limit of this DeliveryContract.  # noqa: E501
        :rtype: int
        """
        return self._orders_limit

    @orders_limit.setter
    def orders_limit(self, orders_limit):
        """Sets the orders_limit of this DeliveryContract.

        Maximum number of open orders  # noqa: E501

        :param orders_limit: The orders_limit of this DeliveryContract.  # noqa: E501
        :type: int
        """

        self._orders_limit = orders_limit

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
        if not isinstance(other, DeliveryContract):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeliveryContract):
            return True

        return self.to_dict() != other.to_dict()
