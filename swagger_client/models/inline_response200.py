# coding: utf-8

"""
    BE v2 API

    API documentation for BE v2, handling authentication, project management, image operations, model management, and EC2 context.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse200(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'err': 'bool',
        'err_msg': 'str',
        'role': 'str',
        'token': 'str',
        'user_id': 'int'
    }

    attribute_map = {
        'err': 'err',
        'err_msg': 'err_msg',
        'role': 'role',
        'token': 'token',
        'user_id': 'user_id'
    }

    def __init__(self, err=None, err_msg=None, role=None, token=None, user_id=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger"""  # noqa: E501
        self._err = None
        self._err_msg = None
        self._role = None
        self._token = None
        self._user_id = None
        self.discriminator = None
        if err is not None:
            self.err = err
        if err_msg is not None:
            self.err_msg = err_msg
        if role is not None:
            self.role = role
        if token is not None:
            self.token = token
        if user_id is not None:
            self.user_id = user_id

    @property
    def err(self):
        """Gets the err of this InlineResponse200.  # noqa: E501


        :return: The err of this InlineResponse200.  # noqa: E501
        :rtype: bool
        """
        return self._err

    @err.setter
    def err(self, err):
        """Sets the err of this InlineResponse200.


        :param err: The err of this InlineResponse200.  # noqa: E501
        :type: bool
        """

        self._err = err

    @property
    def err_msg(self):
        """Gets the err_msg of this InlineResponse200.  # noqa: E501


        :return: The err_msg of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._err_msg

    @err_msg.setter
    def err_msg(self, err_msg):
        """Sets the err_msg of this InlineResponse200.


        :param err_msg: The err_msg of this InlineResponse200.  # noqa: E501
        :type: str
        """

        self._err_msg = err_msg

    @property
    def role(self):
        """Gets the role of this InlineResponse200.  # noqa: E501


        :return: The role of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this InlineResponse200.


        :param role: The role of this InlineResponse200.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def token(self):
        """Gets the token of this InlineResponse200.  # noqa: E501


        :return: The token of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this InlineResponse200.


        :param token: The token of this InlineResponse200.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def user_id(self):
        """Gets the user_id of this InlineResponse200.  # noqa: E501


        :return: The user_id of this InlineResponse200.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this InlineResponse200.


        :param user_id: The user_id of this InlineResponse200.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(InlineResponse200, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
