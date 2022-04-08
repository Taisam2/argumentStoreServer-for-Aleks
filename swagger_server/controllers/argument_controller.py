import connexion
import six

from swagger_server.models.argument import Argument  # noqa: E501
from swagger_server import util


def add_argument(body):  # noqa: E501
    """Add an argument

     # noqa: E501

    :param body: Adds an argument to the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Argument.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
