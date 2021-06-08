import connexion
import six

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.http_problems import HTTPProblems  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.trabajo import Trabajo  # noqa: E501
from swagger_server import util


def cget(id_cliente):  # noqa: E501
    """Buscar trabajos por cliente

    Buscar trabajos por el cliente que lo ha encargado # noqa: E501

    :param id_cliente: Id del cliente
    :type id_cliente: int

    :rtype: InlineResponse200
    """
    return 'do some magic!'


def estget(estado_trabajo):  # noqa: E501
    """Buscar trabajos por estado

    Buscar trabajos por su estado actual # noqa: E501

    :param estado_trabajo: Elegir tipo de trabajo para su búsqueda
    :type estado_trabajo: str

    :rtype: InlineResponse200
    """
    return 'do some magic!'


def iddelete(trabajo_id):  # noqa: E501
    """Elimina un trabajo

    Elimina un trabajo identificada por &#x60;trabajoId&#x60;. # noqa: E501

    :param trabajo_id: ID del trabajo
    :type trabajo_id: int

    :rtype: None
    """
    return 'do some magic!'


def idget(trabajo_id):  # noqa: E501
    """Buscar un trabajo por su ID

    Devuelve el trabajo especificado por &#x60;trabajoId&#x60; # noqa: E501

    :param trabajo_id: ID del trabajo
    :type trabajo_id: int

    :rtype: Trabajo
    """
    return 'do some magic!'


def idput(body, if_match, trabajo_id):  # noqa: E501
    """Modifica un trabajo

    Actualiza los datos de un trabajo por un trabajoId # noqa: E501

    :param body: &#x60;Trabajo&#x60; data
    :type body: dict | bytes
    :param if_match: ETag del recurso que se desea modificar
    :type if_match: str
    :param trabajo_id: ID del trabajo
    :type trabajo_id: int

    :rtype: Trabajo
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def tget():  # noqa: E501
    """Obtiene todos los trabajos de mantenimiento que se realizan sobre un vehículo

     # noqa: E501


    :rtype: InlineResponse200
    """
    return 'do some magic!'


def toptions():  # noqa: E501
    """Proporciona la lista de los métodos HTTP soportados

    Devuelve una cabecera &#x60;Allow&#x60; con la lista de métodos HTTP soportados (separados por comas). # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def tpost(body):  # noqa: E501
    """Crea un nuevo trabajo

    Genera un nuevo trabajo de mantenimiento para un determinado vehículo # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Trabajo
    """
    if connexion.request.is_json:
        body = Body.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def vget(id_vehiculo):  # noqa: E501
    """Buscar trabajos por identificador vehiculo

    Buscar trabajos por el vehículo del cliente que lo ha encargado # noqa: E501

    :param id_vehiculo: Id del vehiculo
    :type id_vehiculo: int

    :rtype: InlineResponse200
    """
    return 'do some magic!'
