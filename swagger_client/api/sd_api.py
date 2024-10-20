# coding: utf-8

"""
    BE v2 API

    API documentation for BE v2, handling authentication, project management, image operations, model management, and EC2 context.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class SDApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_v2_sd_getsdimg_post(self, body, **kwargs):  # noqa: E501
        """Get Stable Diffusion Image Base64  # noqa: E501

        This API is responsible for retrieving the base64 encoded Stable Diffusion images for a specific project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_sd_getsdimg_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SdGetsdimgBody body: (required)
        :return: InlineResponse20019
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v2_sd_getsdimg_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v2_sd_getsdimg_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def api_v2_sd_getsdimg_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Get Stable Diffusion Image Base64  # noqa: E501

        This API is responsible for retrieving the base64 encoded Stable Diffusion images for a specific project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_sd_getsdimg_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SdGetsdimgBody body: (required)
        :return: InlineResponse20019
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v2_sd_getsdimg_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `api_v2_sd_getsdimg_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/sd/getsdimg', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20019',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v2_sd_listsdmodel_post(self, body, **kwargs):  # noqa: E501
        """List Stable Diffusion Models  # noqa: E501

        This API is responsible for listing all available Stable Diffusion models.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_sd_listsdmodel_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SdListsdmodelBody body: (required)
        :return: InlineResponse20020
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v2_sd_listsdmodel_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v2_sd_listsdmodel_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def api_v2_sd_listsdmodel_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """List Stable Diffusion Models  # noqa: E501

        This API is responsible for listing all available Stable Diffusion models.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_sd_listsdmodel_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SdListsdmodelBody body: (required)
        :return: InlineResponse20020
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v2_sd_listsdmodel_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `api_v2_sd_listsdmodel_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/sd/listsdmodel', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20020',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v2_sd_modifysdmodel_post(self, body, **kwargs):  # noqa: E501
        """Modify Stable Diffusion Model  # noqa: E501

        This API is responsible for modifying the information of an existing Stable Diffusion model.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_sd_modifysdmodel_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SdModifysdmodelBody body: (required)
        :return: InlineResponse20021
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v2_sd_modifysdmodel_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v2_sd_modifysdmodel_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def api_v2_sd_modifysdmodel_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Modify Stable Diffusion Model  # noqa: E501

        This API is responsible for modifying the information of an existing Stable Diffusion model.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_sd_modifysdmodel_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SdModifysdmodelBody body: (required)
        :return: InlineResponse20021
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v2_sd_modifysdmodel_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `api_v2_sd_modifysdmodel_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/sd/modifysdmodel', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20021',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v2_sd_txt2img_post(self, body, **kwargs):  # noqa: E501
        """Text to Image Generation  # noqa: E501

        This API is responsible for generating images from text prompts using a Stable Diffusion model.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_sd_txt2img_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SdTxt2imgBody body: (required)
        :return: InlineResponse20018
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v2_sd_txt2img_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v2_sd_txt2img_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def api_v2_sd_txt2img_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Text to Image Generation  # noqa: E501

        This API is responsible for generating images from text prompts using a Stable Diffusion model.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_sd_txt2img_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SdTxt2imgBody body: (required)
        :return: InlineResponse20018
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v2_sd_txt2img_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `api_v2_sd_txt2img_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/sd/txt2img', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20018',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
