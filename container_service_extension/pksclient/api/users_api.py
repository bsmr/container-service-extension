# coding: utf-8

"""
    PKS

    PKS API  # noqa: E501

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from container_service_extension.pksclient.api_client import ApiClient


class UsersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_user(self, cluster_name, **kwargs):  # noqa: E501
        """create_user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_user(cluster_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cluster_name: The cluster name (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_user_with_http_info(cluster_name, **kwargs)  # noqa: E501
        else:
            (data) = self.create_user_with_http_info(cluster_name, **kwargs)  # noqa: E501
            return data

    def create_user_with_http_info(self, cluster_name, **kwargs):  # noqa: E501
        """create_user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_user_with_http_info(cluster_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cluster_name: The cluster name (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cluster_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cluster_name' is set
        if ('cluster_name' not in params or
                params['cluster_name'] is None):
            raise ValueError("Missing the required parameter `cluster_name` when calling `create_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cluster_name' in params:
            path_params['clusterName'] = params['cluster_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'uaa']  # noqa: E501

        return self.api_client.call_api(
            '/clusters/{clusterName}/binds', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_binding(self, cluster_name, user_name, **kwargs):  # noqa: E501
        """get_binding  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_binding(cluster_name, user_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cluster_name: The cluster name (required)
        :param str user_name: name of user to get kubeconfig for (required)
        :param bool suppress_cluster_role_binding: set to true in order to get a kubeconfig with no cluster role binding data
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_binding_with_http_info(cluster_name, user_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_binding_with_http_info(cluster_name, user_name, **kwargs)  # noqa: E501
            return data

    def get_binding_with_http_info(self, cluster_name, user_name, **kwargs):  # noqa: E501
        """get_binding  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_binding_with_http_info(cluster_name, user_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cluster_name: The cluster name (required)
        :param str user_name: name of user to get kubeconfig for (required)
        :param bool suppress_cluster_role_binding: set to true in order to get a kubeconfig with no cluster role binding data
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cluster_name', 'user_name', 'suppress_cluster_role_binding']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_binding" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cluster_name' is set
        if ('cluster_name' not in params or
                params['cluster_name'] is None):
            raise ValueError("Missing the required parameter `cluster_name` when calling `get_binding`")  # noqa: E501
        # verify the required parameter 'user_name' is set
        if ('user_name' not in params or
                params['user_name'] is None):
            raise ValueError("Missing the required parameter `user_name` when calling `get_binding`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cluster_name' in params:
            path_params['clusterName'] = params['cluster_name']  # noqa: E501
        if 'user_name' in params:
            path_params['userName'] = params['user_name']  # noqa: E501

        query_params = []
        if 'suppress_cluster_role_binding' in params:
            query_params.append(('suppressClusterRoleBinding', params['suppress_cluster_role_binding']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'uaa']  # noqa: E501

        return self.api_client.call_api(
            '/clusters/{clusterName}/binds/{userName}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
