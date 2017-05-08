# coding: utf-8

"""
    kubeResource

    Manage Resources from k8s

    OpenAPI spec version: 1.0.0
    Contact: jonathan@saharacluster.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class DefaultApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def apis_fqdn_v1_namespaces_namespace_resource_name_get(self, namespace, name, fqdn, resource, **kwargs):
        """
        Gets a specific Resource
        Returns a specific Resource in a namespace
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.apis_fqdn_v1_namespaces_namespace_resource_name_get(namespace, name, fqdn, resource, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str namespace: The Resource's namespace (required)
        :param str name: The Resource's name (required)
        :param str fqdn: The Third party Resource fqdn (required)
        :param str resource: The Resource type (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.apis_fqdn_v1_namespaces_namespace_resource_name_get_with_http_info(namespace, name, fqdn, resource, **kwargs)
        else:
            (data) = self.apis_fqdn_v1_namespaces_namespace_resource_name_get_with_http_info(namespace, name, fqdn, resource, **kwargs)
            return data

    def apis_fqdn_v1_namespaces_namespace_resource_name_get_with_http_info(self, namespace, name, fqdn, resource, **kwargs):
        """
        Gets a specific Resource
        Returns a specific Resource in a namespace
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.apis_fqdn_v1_namespaces_namespace_resource_name_get_with_http_info(namespace, name, fqdn, resource, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str namespace: The Resource's namespace (required)
        :param str name: The Resource's name (required)
        :param str fqdn: The Third party Resource fqdn (required)
        :param str resource: The Resource type (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['namespace', 'name', 'fqdn', 'resource']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method apis_fqdn_v1_namespaces_namespace_resource_name_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params) or (params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `apis_fqdn_v1_namespaces_namespace_resource_name_get`")
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `apis_fqdn_v1_namespaces_namespace_resource_name_get`")
        # verify the required parameter 'fqdn' is set
        if ('fqdn' not in params) or (params['fqdn'] is None):
            raise ValueError("Missing the required parameter `fqdn` when calling `apis_fqdn_v1_namespaces_namespace_resource_name_get`")
        # verify the required parameter 'resource' is set
        if ('resource' not in params) or (params['resource'] is None):
            raise ValueError("Missing the required parameter `resource` when calling `apis_fqdn_v1_namespaces_namespace_resource_name_get`")


        collection_formats = {}

        path_params = {}
        if 'namespace' in params:
            path_params['namespace'] = params['namespace']
        if 'name' in params:
            path_params['name'] = params['name']
        if 'fqdn' in params:
            path_params['fqdn'] = params['fqdn']
        if 'resource' in params:
            path_params['resource'] = params['resource']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api('/apis/{fqdn}/v1/namespaces/{namespace}/{resource}/{name}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='object',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def apis_fqdn_v1_resource_get(self, fqdn, resource, **kwargs):
        """
        Gets Resources
        Returns a list of Resources
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.apis_fqdn_v1_resource_get(fqdn, resource, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str fqdn: The Third party Resource fqdn (required)
        :param str resource: The Resource type (required)
        :param bool watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.apis_fqdn_v1_resource_get_with_http_info(fqdn, resource, **kwargs)
        else:
            (data) = self.apis_fqdn_v1_resource_get_with_http_info(fqdn, resource, **kwargs)
            return data

    def apis_fqdn_v1_resource_get_with_http_info(self, fqdn, resource, **kwargs):
        """
        Gets Resources
        Returns a list of Resources
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.apis_fqdn_v1_resource_get_with_http_info(fqdn, resource, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str fqdn: The Third party Resource fqdn (required)
        :param str resource: The Resource type (required)
        :param bool watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fqdn', 'resource', 'watch']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method apis_fqdn_v1_resource_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fqdn' is set
        if ('fqdn' not in params) or (params['fqdn'] is None):
            raise ValueError("Missing the required parameter `fqdn` when calling `apis_fqdn_v1_resource_get`")
        # verify the required parameter 'resource' is set
        if ('resource' not in params) or (params['resource'] is None):
            raise ValueError("Missing the required parameter `resource` when calling `apis_fqdn_v1_resource_get`")


        collection_formats = {}

        path_params = {}
        if 'fqdn' in params:
            path_params['fqdn'] = params['fqdn']
        if 'resource' in params:
            path_params['resource'] = params['resource']

        query_params = {}
        if 'watch' in params:
            query_params['watch'] = params['watch']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api('/apis/{fqdn}/v1/{resource}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='object',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def apis_fqdn_v1_resource_post(self, fqdn, resource, **kwargs):
        """
        Create a Resource
        Creates a third party resource of the type specified
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.apis_fqdn_v1_resource_post(fqdn, resource, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str fqdn: The Third party Resource fqdn (required)
        :param str resource: The Resource type (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.apis_fqdn_v1_resource_post_with_http_info(fqdn, resource, **kwargs)
        else:
            (data) = self.apis_fqdn_v1_resource_post_with_http_info(fqdn, resource, **kwargs)
            return data

    def apis_fqdn_v1_resource_post_with_http_info(self, fqdn, resource, **kwargs):
        """
        Create a Resource
        Creates a third party resource of the type specified
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.apis_fqdn_v1_resource_post_with_http_info(fqdn, resource, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str fqdn: The Third party Resource fqdn (required)
        :param str resource: The Resource type (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fqdn', 'resource']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method apis_fqdn_v1_resource_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fqdn' is set
        if ('fqdn' not in params) or (params['fqdn'] is None):
            raise ValueError("Missing the required parameter `fqdn` when calling `apis_fqdn_v1_resource_post`")
        # verify the required parameter 'resource' is set
        if ('resource' not in params) or (params['resource'] is None):
            raise ValueError("Missing the required parameter `resource` when calling `apis_fqdn_v1_resource_post`")


        collection_formats = {}

        path_params = {}
        if 'fqdn' in params:
            path_params['fqdn'] = params['fqdn']
        if 'resource' in params:
            path_params['resource'] = params['resource']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api('/apis/{fqdn}/v1/{resource}', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='object',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
