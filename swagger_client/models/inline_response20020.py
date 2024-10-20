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

class InlineResponse20020(object):
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
        'model_list': 'list[object]'
    }

    attribute_map = {
        'err': 'err',
        'err_msg': 'err_msg',
        'model_list': 'model_list'
    }

    def __init__(self, err=None, err_msg=None, model_list=None):  # noqa: E501
        """InlineResponse20020 - a model defined in Swagger"""  # noqa: E501
        self._err = None
        self._err_msg = None
        self._model_list = None
        self.discriminator = None
        if err is not None:
            self.err = err
        if err_msg is not None:
            self.err_msg = err_msg
        if model_list is not None:
            self.model_list = model_list

    @property
    def err(self):
        """Gets the err of this InlineResponse20020.  # noqa: E501

        Indicates whether the request was successful or if there was an error (true or false)  # noqa: E501

        :return: The err of this InlineResponse20020.  # noqa: E501
        :rtype: bool
        """
        return self._err

    @err.setter
    def err(self, err):
        """Sets the err of this InlineResponse20020.

        Indicates whether the request was successful or if there was an error (true or false)  # noqa: E501

        :param err: The err of this InlineResponse20020.  # noqa: E501
        :type: bool
        """

        self._err = err

    @property
    def err_msg(self):
        """Gets the err_msg of this InlineResponse20020.  # noqa: E501

        A message providing additional details of the operation  # noqa: E501

        :return: The err_msg of this InlineResponse20020.  # noqa: E501
        :rtype: str
        """
        return self._err_msg

    @err_msg.setter
    def err_msg(self, err_msg):
        """Sets the err_msg of this InlineResponse20020.

        A message providing additional details of the operation  # noqa: E501

        :param err_msg: The err_msg of this InlineResponse20020.  # noqa: E501
        :type: str
        """

        self._err_msg = err_msg

    @property
    def model_list(self):
        """Gets the model_list of this InlineResponse20020.  # noqa: E501

        A list of available Stable Diffusion models  # noqa: E501

        :return: The model_list of this InlineResponse20020.  # noqa: E501
        :rtype: list[object]
        """
        return self._model_list

    @model_list.setter
    def model_list(self, model_list):
        """Sets the model_list of this InlineResponse20020.

        A list of available Stable Diffusion models  # noqa: E501

        :param model_list: The model_list of this InlineResponse20020.  # noqa: E501
        :type: list[object]
        """

        self._model_list = model_list

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
        if issubclass(InlineResponse20020, dict):
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
        if not isinstance(other, InlineResponse20020):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
