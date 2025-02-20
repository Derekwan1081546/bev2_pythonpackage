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

class InlineResponse20030(object):
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
        'model': 'list[object]'
    }

    attribute_map = {
        'model': 'model'
    }

    def __init__(self, model=None):  # noqa: E501
        """InlineResponse20030 - a model defined in Swagger"""  # noqa: E501
        self._model = None
        self.discriminator = None
        if model is not None:
            self.model = model

    @property
    def model(self):
        """Gets the model of this InlineResponse20030.  # noqa: E501

        List of available models with their details  # noqa: E501

        :return: The model of this InlineResponse20030.  # noqa: E501
        :rtype: list[object]
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this InlineResponse20030.

        List of available models with their details  # noqa: E501

        :param model: The model of this InlineResponse20030.  # noqa: E501
        :type: list[object]
        """

        self._model = model

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
        if issubclass(InlineResponse20030, dict):
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
        if not isinstance(other, InlineResponse20030):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
