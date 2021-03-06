# coding: utf-8

"""
    kubeResource

    Manage Resources from k8s

    OpenAPI spec version: 1.0.0
    Contact: jonathan@saharacluster.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kube_resource
from kube_resource.rest import ApiException
from kube_resource.models.v1_delete_options import V1DeleteOptions


class TestV1DeleteOptions(unittest.TestCase):
    """ V1DeleteOptions unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1DeleteOptions(self):
        """
        Test V1DeleteOptions
        """
        model = kube_resource.models.v1_delete_options.V1DeleteOptions()


if __name__ == '__main__':
    unittest.main()
