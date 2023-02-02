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


class DomainsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def domains_delete0(self, id, **kwargs):  # noqa: E501
        """Delete domain  # noqa: E501

        Deletes the domain and all related data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.domains_delete0(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id:  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.domains_delete0_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.domains_delete0_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def domains_delete0_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete domain  # noqa: E501

        Deletes the domain and all related data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.domains_delete0_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id:  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method domains_delete0" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `domains_delete0`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/domains/{id}/', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def domains_list(self, **kwargs):  # noqa: E501
        """List domains  # noqa: E501

        Lists domains the current user has access to.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.domains_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: A page number within the paginated result set.
        :param int limit: Number of results to return per page.
        :param str ordering: Default: \"\".   Valid values: \"domain\", \"-domain\",\"volume\", \"-volume\",\"count_threat_other\", \"-count_threat_other\",\"state_dmarc\", \"-state_dmarc\",\"state_spf\", \"-state_spf\",\"state_dkim\", \"-state_dkim\",\"mx_txt\", \"-mx_txt\",\"soa_txt\", \"-soa_txt\"    (prefix with \"-\" for descending sort).
        :param str ordering2: Default: \"\".   Valid values: \"domain\", \"-domain\",\"volume\", \"-volume\",\"count_threat_other\", \"-count_threat_other\",\"state_dmarc\", \"-state_dmarc\",\"state_spf\", \"-state_spf\",\"state_dkim\", \"-state_dkim\",\"mx_txt\", \"-mx_txt\",\"soa_txt\", \"-soa_txt\"    (prefix with \"-\" for descending sort).
        :param str domain: Filter results by domain name.
        :param float group_id: Filter results by group id.
        :param str assigned: Show domains belonging to a group (True) or domains from the default group (False).
        :param str treat_as_top_level: Show domains treated as top level (True) or subdomains (False).
        :param float parent_id: Filter subdomains by their parent domain id.
        :param str domain_state: Filter results by domain state (\"active\", \"inactive\", \"unknown\").
        :return: ResponsesDomainList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.domains_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.domains_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def domains_list_with_http_info(self, **kwargs):  # noqa: E501
        """List domains  # noqa: E501

        Lists domains the current user has access to.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.domains_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: A page number within the paginated result set.
        :param int limit: Number of results to return per page.
        :param str ordering: Default: \"\".   Valid values: \"domain\", \"-domain\",\"volume\", \"-volume\",\"count_threat_other\", \"-count_threat_other\",\"state_dmarc\", \"-state_dmarc\",\"state_spf\", \"-state_spf\",\"state_dkim\", \"-state_dkim\",\"mx_txt\", \"-mx_txt\",\"soa_txt\", \"-soa_txt\"    (prefix with \"-\" for descending sort).
        :param str ordering2: Default: \"\".   Valid values: \"domain\", \"-domain\",\"volume\", \"-volume\",\"count_threat_other\", \"-count_threat_other\",\"state_dmarc\", \"-state_dmarc\",\"state_spf\", \"-state_spf\",\"state_dkim\", \"-state_dkim\",\"mx_txt\", \"-mx_txt\",\"soa_txt\", \"-soa_txt\"    (prefix with \"-\" for descending sort).
        :param str domain: Filter results by domain name.
        :param float group_id: Filter results by group id.
        :param str assigned: Show domains belonging to a group (True) or domains from the default group (False).
        :param str treat_as_top_level: Show domains treated as top level (True) or subdomains (False).
        :param float parent_id: Filter subdomains by their parent domain id.
        :param str domain_state: Filter results by domain state (\"active\", \"inactive\", \"unknown\").
        :return: ResponsesDomainList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'limit', 'ordering', 'ordering2', 'domain', 'group_id', 'assigned', 'treat_as_top_level', 'parent_id', 'domain_state']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method domains_list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'ordering' in params:
            query_params.append(('ordering', params['ordering']))  # noqa: E501
        if 'ordering2' in params:
            query_params.append(('ordering', params['ordering2']))  # noqa: E501
        if 'domain' in params:
            query_params.append(('domain', params['domain']))  # noqa: E501
        if 'group_id' in params:
            query_params.append(('group_id', params['group_id']))  # noqa: E501
        if 'assigned' in params:
            query_params.append(('assigned', params['assigned']))  # noqa: E501
        if 'treat_as_top_level' in params:
            query_params.append(('treat_as_top_level', params['treat_as_top_level']))  # noqa: E501
        if 'parent_id' in params:
            query_params.append(('parent_id', params['parent_id']))  # noqa: E501
        if 'domain_state' in params:
            query_params.append(('domain_state', params['domain_state']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/domains/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponsesDomainList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def domains_partial_update(self, id, **kwargs):  # noqa: E501
        """Update domain (partial)  # noqa: E501

        Updates some of the domain properties.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.domains_partial_update(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id:  (required)
        :param Data15 data:
        :return: ResponsesDomain
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.domains_partial_update_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.domains_partial_update_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def domains_partial_update_with_http_info(self, id, **kwargs):  # noqa: E501
        """Update domain (partial)  # noqa: E501

        Updates some of the domain properties.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.domains_partial_update_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id:  (required)
        :param Data15 data:
        :return: ResponsesDomain
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method domains_partial_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `domains_partial_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/domains/{id}/', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponsesDomain',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def domains_read(self, id, **kwargs):  # noqa: E501
        """Get domain  # noqa: E501

        Retrieves specific domain details.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.domains_read(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id:  (required)
        :return: ResponsesDomain
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.domains_read_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.domains_read_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def domains_read_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get domain  # noqa: E501

        Retrieves specific domain details.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.domains_read_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id:  (required)
        :return: ResponsesDomain
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method domains_read" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `domains_read`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/domains/{id}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponsesDomain',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def domains_refresh(self, id, **kwargs):  # noqa: E501
        """Refresh domain  # noqa: E501

        Refreshes domain's statistics.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.domains_refresh(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id:  (required)
        :return: ResponsesDomain
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.domains_refresh_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.domains_refresh_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def domains_refresh_with_http_info(self, id, **kwargs):  # noqa: E501
        """Refresh domain  # noqa: E501

        Refreshes domain's statistics.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.domains_refresh_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id:  (required)
        :return: ResponsesDomain
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method domains_refresh" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `domains_refresh`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/domains/{id}/refresh/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponsesDomain',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def domains_update(self, id, **kwargs):  # noqa: E501
        """Update domain  # noqa: E501

        Updates domain properties.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.domains_update(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id:  (required)
        :param Data14 data:
        :return: ResponsesDomain
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.domains_update_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.domains_update_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def domains_update_with_http_info(self, id, **kwargs):  # noqa: E501
        """Update domain  # noqa: E501

        Updates domain properties.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.domains_update_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id:  (required)
        :param Data14 data:
        :return: ResponsesDomain
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method domains_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `domains_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/domains/{id}/', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponsesDomain',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def domains_verify(self, id, **kwargs):  # noqa: E501
        """Verify domain  # noqa: E501

        Initiates a probe to verify this domain  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.domains_verify(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id:  (required)
        :param Data16 data:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.domains_verify_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.domains_verify_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def domains_verify_with_http_info(self, id, **kwargs):  # noqa: E501
        """Verify domain  # noqa: E501

        Initiates a probe to verify this domain  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.domains_verify_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id:  (required)
        :param Data16 data:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method domains_verify" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `domains_verify`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/domains/{id}/verify/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
