# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1_pod_affinity import V1PodAffinity


class TestV1PodAffinity(unittest.TestCase):
    """ V1PodAffinity unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1PodAffinity(self):
        """
        Test V1PodAffinity
        """
        model = kubernetes.client.models.v1_pod_affinity.V1PodAffinity()


if __name__ == '__main__':
    unittest.main()