# coding: utf-8

"""
    DMARC Advisor API

    # Introduction  Welcome to the DMARC Advisor REST API documentation!  This documentation will help you integrate the DMARC Advisor services into your software so you are not required to use our user interface. We have put a lot of effort into making the endpoints as self descriptive as possible but even if  you have any issues - head to the corresponding section in the reference below.  We have built the API on top of HTTP following  [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) best practices. The endpoints receive JSON in their request body and return JSON as a response  with the proper status code.  # Authentication  Most of our API endpoints are not publicly available so you must authenticate  in order to use them. To do so you need to acquire an API token first. Navigate  to the Manage Settings page and generate one there. You can always regenerate it but keep in mind that this will revoke your old token and it won't be accepted anymore.  Once you have a token you need to provide it as an HTTP header on each  request you make:  ``` Authorization: Token {your-api-token} ```  # Versioning  The API is constantly evolving to match the new features we add to the DMARC Advisor platform. In order to ensure backward compatibility and not break clients we have versioned the API. Each endpoint contains a parameter in the URL that specifies the requested version and looks like this:  ``` https://eu.dmarcadvisor.com/api/v{version-number}/domains/ ```  # Status Codes  Endpoint calls can result in one of the following HTTP Status Codes:  Code | Meaning --- | ---  200 | Successful operation (read, update, etc.) 201 | Resource created (usually on POST requests) 202 | Request for processing has been accepted (e.g. a long query job) 204 | Successful operation without a response body (e.g. delete) 400`*` | Invalid request parameters  401 | Unauthorized - your API token is either missing or invalid 402 | Account subscription has expired 403 | Forbidden - you are not permitted to perform the operation 404 | Requested resource not found 500 | Oops - something went wrong  `*` Have in mind that properties specified in the request body that are not supported will be IGNORED.   # Links and Permissions  [HATEOAS (Hypermedia as the Engine of Application State)](https://en.wikipedia.org/wiki/HATEOAS) is a very cool idea. In essence - endpoint responses provide navigation information by including hypermedia links to the available actions / resources. The main benefit is that clients do not have to be familiar how endpoint URLs are built and do not need to hardcode them inside their API integration.  We have embraced this idea but we have deviated from the specification a bit to have a simpler response structure. We have also added an extra layer on top - permissions. Responses may contain a `_links` property that lists all available actions and a `_permissions` property that specifies which of the actions are permitted to the current user.  ## Root  The API provides a root endpoint that lists all main resources and links to explore them.  For the latest API version call:  ``` https://eu.dmarcadvisor.com/api/ ```  For a specific API version call:  ``` https://eu.dmarcadvisor.com/api/v{version-number}/ ```  Example response:  ```json {     \"domains\": \"https://eu.dmarcadvisor.com/api/v1/domains/\",     \"domain_groups\": \"https://eu.dmarcadvisor.com/api/v1/domain-groups/\",     \"issues\": \"https://eu.dmarcadvisor.com/api/v1/issues/\",     \"tasks\": \"https://eu.dmarcadvisor.com/api/v1/tasks/\" } ```  ## Lists  All list API endpoints support pagination and share an identical response format (check a specific endpoint reference for a detailed response schema). The `_links` property contains URLs for navigation - first page, last page, next page, etc. and the `_permissions` property specifies what is permitted - e.g. only `list` or also `create`.  Example response:  ```json {     \"_links\": {         \"first\": \"https://eu.dmarcadvisor.com/api/v1/domains/\",         \"last\": \"https://eu.dmarcadvisor.com/api/v1/domains/?page=5\",         \"next\": \"https://eu.dmarcadvisor.com/api/v1/domains/?page=2\",         \"previous\": null     },     \"_permissions\": [         \"list\"     ],     \"count\": 24,     \"pages\": 5,     \"current_page\": 1,     \"per_page\": 5,     \"results\": [] } ```  ## Objects  Object API endpoints operate on a specific resource with a unique identifier. The `_links`  property works the same way as described above with one specific difference - the `self` key inside is used for multiple actions - `retrieve`, `update`, `partial_update` and `destroy`.  Example response:  ```json {     \"_links\": {         \"self\": \"https://eu.dmarcadvisor.com/api/v1/domains/17/\",         \"refresh\": \"https://eu.dmarcadvisor.com/api/v1/domains/17/refresh/\",         \"subdomains\": \"https://eu.dmarcadvisor.com/api/v1/domains/?parent_id=17&treat_as_top_level=False\"     },     \"_permissions\": [         \"retrieve\",         \"refresh\",         \"update\",         \"partial_update\",         \"destroy\"     ],     \"id\": 17,     ... } ```  # Working with date fields  API returns date fields as a string representing the `UTC` date and time in ISO 8601 format,  `YYYY-MM-DDTHH:MM:SS.mmmmmm` or, if microsecond is 0, `YYYY-MM-DDTHH:MM:SS`.  In example below Z is the zone designator for the zero UTC offset. ```json {   \"created\": \"2017-09-11T10:18:50.875874Z\" } ```   API accepts date time in ISO 8601 format with given UTC offset(Z for zero or ±HH:MM): ```json {   \"begin\": \"2017-09-11T10:18:50+03:00\",   \"end\": \"2017-09-11T10:18:50+03:00\" } ```  # How-To Guides  After getting familiar with the basics it's time to get our hands dirty and actually do something with the API. In this How To section we are going to describe some common scenarios - check the reference for more advanced cases.  DMARC Advisor does not provide any SDKs currently but communication with the API can be achieved in any programming language since all endpoints are HTTP based. We will use `curl` in our examples for simplicity.  ## Add Domain  The first step after creating an account at DMARC Advisor is to add a domain so we are going to describe how can this be achieved via the API.  ### 1. Get Token  Check the Authentication section for details how to obtain an API token - we will need it for calling the API.  ### 2. List Domain Groups  All domains live under a certain domain group (either the default one which you will automatically have after registration or a group you have created). In order to  create a domain we need to find a group to add it to first:  ``` curl -G https://eu.dmarcadvisor.com/api/v1/domain-groups/ -H 'Authorization: Token {your-api-token}' ```  You will get a paginated list of all available groups. Just choose the one you want to add a domain to (look inside the `results` property) and copy the `add_domain` URL under `_links` - we will use it in the next step.  ### 3. Add the Domain  After we've chosen a group we can actually add the domain:  ``` curl -d '{\"domains\":[\"example.com\"]}' https://eu.dmarcadvisor.com/api/v1/domain-groups/{chosen-group-id}/add-domains/ -H 'Authorization: Token {your-api-token}' -H 'Content-Type: application/json' ```  The response will contain URLs to the newly created domains:  ```json {     \"added\": [\"https://eu.dmarcadvisor.com/api/v1/domains/{created-domain-id}/\"] } ```  ### 4. List Domains  And voila - you have added your first domain via the API. Now let's verify that the domain is listed under the group. Copy the `domains` property under `_links` from the group you chose in step 2 and list the domains:  ``` curl -G 'https://eu.dmarcadvisor.com/api/v1/domains/?treat_as_top_level=True&group_id={chosen-group-id}' -H 'Authorization: Token {your-api-token}' ```  You should see the new domain in the `results` property of the paginated response.  # Reference  The API reference allows you to dive into each endpoint and check how example requests and response look like, what filters are supported and what is the meaning of each property.   # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from dmarcadvisor.api_client import ApiClient


class ReportDataApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def aggregate_report_domains_list(self, search_token, **kwargs):  # noqa: E501
        """Domains  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aggregate_report_domains_list(search_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_token:  (required)
        :param int page: A page number within the paginated result set.
        :param int limit: Number of results to return per page.
        :param str ordering: Default: \"-message_count\".   Valid values: \"message_count\", \"-message_count\",\"from_domain\", \"-from_domain\",\"ip\", \"-ip\",\"ptr\", \"-ptr\",\"reason\", \"-reason\",\"dkim_result\", \"-dkim_result\",\"dkim_policy_result\", \"-dkim_policy_result\",\"spf_result\", \"-spf_result\",\"spf_policy_result\", \"-spf_policy_result\",\"policy_applied\", \"-policy_applied\",\"spf_d\", \"-spf_d\",\"dkim_d\", \"-dkim_d\"    (prefix with \"-\" for descending sort).
        :param str source_number: Filter domains data by source.
        :param str ptr_org: Filter domains data by PTR grouping.
        :return: ResponsesQueryJobSourceDomainData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.aggregate_report_domains_list_with_http_info(search_token, **kwargs)  # noqa: E501
        else:
            (data) = self.aggregate_report_domains_list_with_http_info(search_token, **kwargs)  # noqa: E501
            return data

    def aggregate_report_domains_list_with_http_info(self, search_token, **kwargs):  # noqa: E501
        """Domains  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aggregate_report_domains_list_with_http_info(search_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_token:  (required)
        :param int page: A page number within the paginated result set.
        :param int limit: Number of results to return per page.
        :param str ordering: Default: \"-message_count\".   Valid values: \"message_count\", \"-message_count\",\"from_domain\", \"-from_domain\",\"ip\", \"-ip\",\"ptr\", \"-ptr\",\"reason\", \"-reason\",\"dkim_result\", \"-dkim_result\",\"dkim_policy_result\", \"-dkim_policy_result\",\"spf_result\", \"-spf_result\",\"spf_policy_result\", \"-spf_policy_result\",\"policy_applied\", \"-policy_applied\",\"spf_d\", \"-spf_d\",\"dkim_d\", \"-dkim_d\"    (prefix with \"-\" for descending sort).
        :param str source_number: Filter domains data by source.
        :param str ptr_org: Filter domains data by PTR grouping.
        :return: ResponsesQueryJobSourceDomainData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search_token', 'page', 'limit', 'ordering', 'source_number', 'ptr_org']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method aggregate_report_domains_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'search_token' is set
        if self.api_client.client_side_validation and ('search_token' not in params or
                                                       params['search_token'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `search_token` when calling `aggregate_report_domains_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'search_token' in params:
            path_params['search_token'] = params['search_token']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'ordering' in params:
            query_params.append(('ordering', params['ordering']))  # noqa: E501
        if 'source_number' in params:
            query_params.append(('source_number', params['source_number']))  # noqa: E501
        if 'ptr_org' in params:
            query_params.append(('ptr_org', params['ptr_org']))  # noqa: E501

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
        auth_settings = ['API key in header']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/aggregate-report/{search_token}/domains/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponsesQueryJobSourceDomainData',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def aggregate_report_progress(self, search_token, **kwargs):  # noqa: E501
        """Progress  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aggregate_report_progress(search_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_token:  (required)
        :return: ResponsesQueryJobProgress
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.aggregate_report_progress_with_http_info(search_token, **kwargs)  # noqa: E501
        else:
            (data) = self.aggregate_report_progress_with_http_info(search_token, **kwargs)  # noqa: E501
            return data

    def aggregate_report_progress_with_http_info(self, search_token, **kwargs):  # noqa: E501
        """Progress  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aggregate_report_progress_with_http_info(search_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_token:  (required)
        :return: ResponsesQueryJobProgress
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method aggregate_report_progress" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'search_token' is set
        if self.api_client.client_side_validation and ('search_token' not in params or
                                                       params['search_token'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `search_token` when calling `aggregate_report_progress`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'search_token' in params:
            path_params['search_token'] = params['search_token']  # noqa: E501

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
        auth_settings = ['API key in header']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/aggregate-report/{search_token}/progress/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponsesQueryJobProgress',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def aggregate_report_source_list(self, source_number, search_token, **kwargs):  # noqa: E501
        """Source data  # noqa: E501

        List given source data, such as messages count, spf, dkim and dmarc information  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aggregate_report_source_list(source_number, search_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str source_number:  (required)
        :param str search_token:  (required)
        :param int page: A page number within the paginated result set.
        :param int limit: Number of results to return per page.
        :param str search: Search in fields: \"server_name\"  .
        :param str ordering: Default: \"-message_count\".   Valid values: \"message_count\", \"-message_count\",\"server_name\", \"-server_name\",\"ip_count\", \"-ip_count\"    (prefix with \"-\" for descending sort).
        :return: ResponsesQueryJobSourceData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.aggregate_report_source_list_with_http_info(source_number, search_token, **kwargs)  # noqa: E501
        else:
            (data) = self.aggregate_report_source_list_with_http_info(source_number, search_token, **kwargs)  # noqa: E501
            return data

    def aggregate_report_source_list_with_http_info(self, source_number, search_token, **kwargs):  # noqa: E501
        """Source data  # noqa: E501

        List given source data, such as messages count, spf, dkim and dmarc information  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aggregate_report_source_list_with_http_info(source_number, search_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str source_number:  (required)
        :param str search_token:  (required)
        :param int page: A page number within the paginated result set.
        :param int limit: Number of results to return per page.
        :param str search: Search in fields: \"server_name\"  .
        :param str ordering: Default: \"-message_count\".   Valid values: \"message_count\", \"-message_count\",\"server_name\", \"-server_name\",\"ip_count\", \"-ip_count\"    (prefix with \"-\" for descending sort).
        :return: ResponsesQueryJobSourceData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['source_number', 'search_token', 'page', 'limit', 'search', 'ordering']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method aggregate_report_source_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'source_number' is set
        if self.api_client.client_side_validation and ('source_number' not in params or
                                                       params['source_number'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `source_number` when calling `aggregate_report_source_list`")  # noqa: E501
        # verify the required parameter 'search_token' is set
        if self.api_client.client_side_validation and ('search_token' not in params or
                                                       params['search_token'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `search_token` when calling `aggregate_report_source_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'source_number' in params:
            path_params['source_number'] = params['source_number']  # noqa: E501
        if 'search_token' in params:
            path_params['search_token'] = params['search_token']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'search' in params:
            query_params.append(('search', params['search']))  # noqa: E501
        if 'ordering' in params:
            query_params.append(('ordering', params['ordering']))  # noqa: E501

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
        auth_settings = ['API key in header']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/aggregate-report/{search_token}/source/{source_number}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponsesQueryJobSourceData',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def aggregate_report_sources(self, search_token, **kwargs):  # noqa: E501
        """Sources  # noqa: E501

        List report sources in 4 categories - dmarc capable, non compliant, forwarders, unknown.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aggregate_report_sources(search_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_token:  (required)
        :return: ResponsesQueryJobSources
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.aggregate_report_sources_with_http_info(search_token, **kwargs)  # noqa: E501
        else:
            (data) = self.aggregate_report_sources_with_http_info(search_token, **kwargs)  # noqa: E501
            return data

    def aggregate_report_sources_with_http_info(self, search_token, **kwargs):  # noqa: E501
        """Sources  # noqa: E501

        List report sources in 4 categories - dmarc capable, non compliant, forwarders, unknown.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aggregate_report_sources_with_http_info(search_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_token:  (required)
        :return: ResponsesQueryJobSources
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method aggregate_report_sources" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'search_token' is set
        if self.api_client.client_side_validation and ('search_token' not in params or
                                                       params['search_token'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `search_token` when calling `aggregate_report_sources`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'search_token' in params:
            path_params['search_token'] = params['search_token']  # noqa: E501

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
        auth_settings = ['API key in header']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/aggregate-report/{search_token}/sources/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponsesQueryJobSources',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
