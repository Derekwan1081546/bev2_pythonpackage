# coding: utf-8

"""
    BE v2 API

    API documentation for BE v2, handling authentication, project management, image operations, model management, and EC2 context.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.ec2_api import EC2Api  # noqa: E501
from swagger_client.rest import ApiException


class TestEC2Api(unittest.TestCase):
    """EC2Api unit test stubs"""

    def setUp(self):
        self.api = EC2Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v2_ec2context_delete_ec2_post(self):
        """Test case for api_v2_ec2context_delete_ec2_post

        Delete EC2 Instance  # noqa: E501
        """
        pass

    def test_api_v2_ec2context_deploy_ec2_post(self):
        """Test case for api_v2_ec2context_deploy_ec2_post

        Deploy EC2 Instance  # noqa: E501
        """
        pass

    def test_api_v2_ec2context_start_ec2_post(self):
        """Test case for api_v2_ec2context_start_ec2_post

        Start EC2 Instance  # noqa: E501
        """
        pass

    def test_api_v2_ec2context_stop_ec2_post(self):
        """Test case for api_v2_ec2context_stop_ec2_post

        Stop EC2 Instance  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
