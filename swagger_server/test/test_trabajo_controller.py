# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.http_problems import HTTPProblems  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.trabajo import Trabajo  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTrabajoController(BaseTestCase):
    """TrabajoController integration test stubs"""

    def test_cget(self):
        """Test case for cget

        Buscar trabajos por cliente
        """
        response = self.client.open(
            '/trabajo/cliente/{idCliente}'.format(id_cliente=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_estget(self):
        """Test case for estget

        Buscar trabajos por estado
        """
        query_string = [('estado_trabajo', 'Creado')]
        response = self.client.open(
            '/trabajo/findByEstadoTrabajo',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_iddelete(self):
        """Test case for iddelete

        Elimina un trabajo
        """
        response = self.client.open(
            '/trabajo/{trabajoId}'.format(trabajo_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_idget(self):
        """Test case for idget

        Buscar un trabajo por su ID
        """
        response = self.client.open(
            '/trabajo/{trabajoId}'.format(trabajo_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_idput(self):
        """Test case for idput

        Modifica un trabajo
        """
        body = None
        headers = [('if_match', 'if_match_example')]
        response = self.client.open(
            '/trabajo/{trabajoId}'.format(trabajo_id=56),
            method='PUT',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_tget(self):
        """Test case for tget

        Obtiene todos los trabajos de mantenimiento que se realizan sobre un vehículo
        """
        response = self.client.open(
            '/trabajo',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_toptions(self):
        """Test case for toptions

        Proporciona la lista de los métodos HTTP soportados
        """
        response = self.client.open(
            '/trabajo',
            method='OPTIONS')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_tpost(self):
        """Test case for tpost

        Crea un nuevo trabajo
        """
        body = Body()
        response = self.client.open(
            '/trabajo',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_vget(self):
        """Test case for vget

        Buscar trabajos por identificador vehiculo
        """
        response = self.client.open(
            '/trabajo/vehiculo/{idVehiculo}'.format(id_vehiculo=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
