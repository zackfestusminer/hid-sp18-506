#!/usr/bin/python
# -*- coding: utf-8 -*-
import connexion
import six
import snpPriceFunctions

from swagger_server.models.inline_response400 import InlineResponse400  # noqa: E501
from swagger_server.models.snp import Snp  # noqa: E501
from swagger_server import util


def create_snp(snp=None):  # noqa: E501
    """create_snp

    User can insert a new price details record. # noqa: E501

    :param snp: Creates a new price record.
    :type snp: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:

        # snp = Snp.from_dict(connexion.request.get_json())  # noqa: E501

        snp = connexion.request.get_json()
        return str(snpPriceFunctions.snp_insert(snp)) + ' row inserted'


def delete_snp_by_date(snpDate):  # noqa: E501
    """delete_snp_by_date

    Delete SNP Pricing data by date. # noqa: E501

    :param snpDate: Delete SNP pricing data by date
    :type snpDate: str

    :rtype: None
    """

    return str(snpPriceFunctions.snp_delete(snpDate)) \
        + ' row(s) deleted'


def get_snp():  # noqa: E501
    """get_snp

    Returns all SNP Prices from the system. # noqa: E501


    :rtype: List[Snp]
    """

    return Snp(snpPriceFunctions.snp_query_all())


def get_snp_by_date(snpDate):  # noqa: E501
    """get_snp_by_date

    Returns SNP Price details based on date # noqa: E501

    :param snpDate: SNP price details to return
    :type snpDate: str

    :rtype: List[Snp]
    """

    return Snp(snpPriceFunctions.snp_query_by_date(snpDate))


def update_snp_by_date(snpDate, snp=None):  # noqa: E501
    """update_snp_by_date

    Update a SNP pricing details based on date provided # noqa: E501

    :param snpDate: Update SNP Price data
    :type snpDate: str
    :param snp: Pricing Data for update
    :type snp: dict | bytes

    :rtype: List[Snp]
    """

    if connexion.request.is_json:

        # snp = Snp.from_dict(connexion.request.get_json())  # noqa: E501

        snp = connexion.request.get_json()
    return str(snpPriceFunctions.snp_update(snpDate, snp)) \
        + ' row(s) updated'



			