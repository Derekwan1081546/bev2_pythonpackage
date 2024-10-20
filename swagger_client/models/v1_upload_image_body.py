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

class V1UploadImageBody(object):
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
        'access_token': 'str',
        'original_image_file': 'str',
        'purpose': 'str',
        'device_info': 'str',
        'label_info': 'str',
        'description': 'str'
    }

    attribute_map = {
        'access_token': 'access_token',
        'original_image_file': 'originalImageFile',
        'purpose': 'Purpose',
        'device_info': 'DeviceInfo',
        'label_info': 'LabelInfo',
        'description': 'Description'
    }

    def __init__(self, access_token=None, original_image_file=None, purpose=None, device_info=None, label_info=None, description=None):  # noqa: E501
        """V1UploadImageBody - a model defined in Swagger"""  # noqa: E501
        self._access_token = None
        self._original_image_file = None
        self._purpose = None
        self._device_info = None
        self._label_info = None
        self._description = None
        self.discriminator = None
        if access_token is not None:
            self.access_token = access_token
        if original_image_file is not None:
            self.original_image_file = original_image_file
        if purpose is not None:
            self.purpose = purpose
        if device_info is not None:
            self.device_info = device_info
        if label_info is not None:
            self.label_info = label_info
        if description is not None:
            self.description = description

    @property
    def access_token(self):
        """Gets the access_token of this V1UploadImageBody.  # noqa: E501

        Access token to authenticate the request  # noqa: E501

        :return: The access_token of this V1UploadImageBody.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this V1UploadImageBody.

        Access token to authenticate the request  # noqa: E501

        :param access_token: The access_token of this V1UploadImageBody.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def original_image_file(self):
        """Gets the original_image_file of this V1UploadImageBody.  # noqa: E501

        The image file to be uploaded  # noqa: E501

        :return: The original_image_file of this V1UploadImageBody.  # noqa: E501
        :rtype: str
        """
        return self._original_image_file

    @original_image_file.setter
    def original_image_file(self, original_image_file):
        """Sets the original_image_file of this V1UploadImageBody.

        The image file to be uploaded  # noqa: E501

        :param original_image_file: The original_image_file of this V1UploadImageBody.  # noqa: E501
        :type: str
        """

        self._original_image_file = original_image_file

    @property
    def purpose(self):
        """Gets the purpose of this V1UploadImageBody.  # noqa: E501

        The purpose of the upload (e.g., \"inference\", \"dataset\")  # noqa: E501

        :return: The purpose of this V1UploadImageBody.  # noqa: E501
        :rtype: str
        """
        return self._purpose

    @purpose.setter
    def purpose(self, purpose):
        """Sets the purpose of this V1UploadImageBody.

        The purpose of the upload (e.g., \"inference\", \"dataset\")  # noqa: E501

        :param purpose: The purpose of this V1UploadImageBody.  # noqa: E501
        :type: str
        """

        self._purpose = purpose

    @property
    def device_info(self):
        """Gets the device_info of this V1UploadImageBody.  # noqa: E501

        Information about the device used to capture the image (e.g., \"samsung s24\")  # noqa: E501

        :return: The device_info of this V1UploadImageBody.  # noqa: E501
        :rtype: str
        """
        return self._device_info

    @device_info.setter
    def device_info(self, device_info):
        """Sets the device_info of this V1UploadImageBody.

        Information about the device used to capture the image (e.g., \"samsung s24\")  # noqa: E501

        :param device_info: The device_info of this V1UploadImageBody.  # noqa: E501
        :type: str
        """

        self._device_info = device_info

    @property
    def label_info(self):
        """Gets the label_info of this V1UploadImageBody.  # noqa: E501

        Label information for the image  # noqa: E501

        :return: The label_info of this V1UploadImageBody.  # noqa: E501
        :rtype: str
        """
        return self._label_info

    @label_info.setter
    def label_info(self, label_info):
        """Sets the label_info of this V1UploadImageBody.

        Label information for the image  # noqa: E501

        :param label_info: The label_info of this V1UploadImageBody.  # noqa: E501
        :type: str
        """

        self._label_info = label_info

    @property
    def description(self):
        """Gets the description of this V1UploadImageBody.  # noqa: E501

        Description of the image  # noqa: E501

        :return: The description of this V1UploadImageBody.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1UploadImageBody.

        Description of the image  # noqa: E501

        :param description: The description of this V1UploadImageBody.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(V1UploadImageBody, dict):
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
        if not isinstance(other, V1UploadImageBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
