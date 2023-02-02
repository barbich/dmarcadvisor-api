# coding: utf-8

"""
    DMARC Advisor API

    # Introduction  Welcome to the DMARC Advisor REST API documentation!  This documentation will help you integrate the DMARC Advisor services into your software so you are not required to use our user interface. We have put a lot of effort into making the endpoints as self descriptive as possible but even if  you have any issues - head to the corresponding section in the reference below.  We have built the API on top of HTTP following  [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) best practices. The endpoints receive JSON in their request body and return JSON as a response  with the proper status code.  # Authentication  Most of our API endpoints are not publicly available so you must authenticate  in order to use them. To do so you need to acquire an API token first. Navigate  to the Manage Settings page and generate one there. You can always regenerate it but keep in mind that this will revoke your old token and it won't be accepted anymore.  Once you have a token you need to provide it as an HTTP header on each  request you make:  ``` Authorization: Token {your-api-token} ```  # Versioning  The API is constantly evolving to match the new features we add to the DMARC Advisor platform. In order to ensure backward compatibility and not break clients we have versioned the API. Each endpoint contains a parameter in the URL that specifies the requested version and looks like this:  ``` https://eu.dmarcadvisor.com/api/v{version-number}/domains/ ```  # Status Codes  Endpoint calls can result in one of the following HTTP Status Codes:  Code | Meaning --- | ---  200 | Successful operation (read, update, etc.) 201 | Resource created (usually on POST requests) 202 | Request for processing has been accepted (e.g. a long query job) 204 | Successful operation without a response body (e.g. delete) 400`*` | Invalid request parameters  401 | Unauthorized - your API token is either missing or invalid 402 | Account subscription has expired 403 | Forbidden - you are not permitted to perform the operation 404 | Requested resource not found 500 | Oops - something went wrong  `*` Have in mind that properties specified in the request body that are not supported will be IGNORED.   # Links and Permissions  [HATEOAS (Hypermedia as the Engine of Application State)](https://en.wikipedia.org/wiki/HATEOAS) is a very cool idea. In essence - endpoint responses provide navigation information by including hypermedia links to the available actions / resources. The main benefit is that clients do not have to be familiar how endpoint URLs are built and do not need to hardcode them inside their API integration.  We have embraced this idea but we have deviated from the specification a bit to have a simpler response structure. We have also added an extra layer on top - permissions. Responses may contain a `_links` property that lists all available actions and a `_permissions` property that specifies which of the actions are permitted to the current user.  ## Root  The API provides a root endpoint that lists all main resources and links to explore them.  For the latest API version call:  ``` https://eu.dmarcadvisor.com/api/ ```  For a specific API version call:  ``` https://eu.dmarcadvisor.com/api/v{version-number}/ ```  Example response:  ```json {     \"domains\": \"https://eu.dmarcadvisor.com/api/v1/domains/\",     \"domain_groups\": \"https://eu.dmarcadvisor.com/api/v1/domain-groups/\",     \"issues\": \"https://eu.dmarcadvisor.com/api/v1/issues/\",     \"tasks\": \"https://eu.dmarcadvisor.com/api/v1/tasks/\" } ```  ## Lists  All list API endpoints support pagination and share an identical response format (check a specific endpoint reference for a detailed response schema). The `_links` property contains URLs for navigation - first page, last page, next page, etc. and the `_permissions` property specifies what is permitted - e.g. only `list` or also `create`.  Example response:  ```json {     \"_links\": {         \"first\": \"https://eu.dmarcadvisor.com/api/v1/domains/\",         \"last\": \"https://eu.dmarcadvisor.com/api/v1/domains/?page=5\",         \"next\": \"https://eu.dmarcadvisor.com/api/v1/domains/?page=2\",         \"previous\": null     },     \"_permissions\": [         \"list\"     ],     \"count\": 24,     \"pages\": 5,     \"current_page\": 1,     \"per_page\": 5,     \"results\": [] } ```  ## Objects  Object API endpoints operate on a specific resource with a unique identifier. The `_links`  property works the same way as described above with one specific difference - the `self` key inside is used for multiple actions - `retrieve`, `update`, `partial_update` and `destroy`.  Example response:  ```json {     \"_links\": {         \"self\": \"https://eu.dmarcadvisor.com/api/v1/domains/17/\",         \"refresh\": \"https://eu.dmarcadvisor.com/api/v1/domains/17/refresh/\",         \"subdomains\": \"https://eu.dmarcadvisor.com/api/v1/domains/?parent_id=17&treat_as_top_level=False\"     },     \"_permissions\": [         \"retrieve\",         \"refresh\",         \"update\",         \"partial_update\",         \"destroy\"     ],     \"id\": 17,     ... } ```  # Working with date fields  API returns date fields as a string representing the `UTC` date and time in ISO 8601 format,  `YYYY-MM-DDTHH:MM:SS.mmmmmm` or, if microsecond is 0, `YYYY-MM-DDTHH:MM:SS`.  In example below Z is the zone designator for the zero UTC offset. ```json {   \"created\": \"2017-09-11T10:18:50.875874Z\" } ```   API accepts date time in ISO 8601 format with given UTC offset(Z for zero or ±HH:MM): ```json {   \"begin\": \"2017-09-11T10:18:50+03:00\",   \"end\": \"2017-09-11T10:18:50+03:00\" } ```  # How-To Guides  After getting familiar with the basics it's time to get our hands dirty and actually do something with the API. In this How To section we are going to describe some common scenarios - check the reference for more advanced cases.  DMARC Advisor does not provide any SDKs currently but communication with the API can be achieved in any programming language since all endpoints are HTTP based. We will use `curl` in our examples for simplicity.  ## Add Domain  The first step after creating an account at DMARC Advisor is to add a domain so we are going to describe how can this be achieved via the API.  ### 1. Get Token  Check the Authentication section for details how to obtain an API token - we will need it for calling the API.  ### 2. List Domain Groups  All domains live under a certain domain group (either the default one which you will automatically have after registration or a group you have created). In order to  create a domain we need to find a group to add it to first:  ``` curl -G https://eu.dmarcadvisor.com/api/v1/domain-groups/ -H 'Authorization: Token {your-api-token}' ```  You will get a paginated list of all available groups. Just choose the one you want to add a domain to (look inside the `results` property) and copy the `add_domain` URL under `_links` - we will use it in the next step.  ### 3. Add the Domain  After we've chosen a group we can actually add the domain:  ``` curl -d '{\"domains\":[\"example.com\"]}' https://eu.dmarcadvisor.com/api/v1/domain-groups/{chosen-group-id}/add-domains/ -H 'Authorization: Token {your-api-token}' -H 'Content-Type: application/json' ```  The response will contain URLs to the newly created domains:  ```json {     \"added\": [\"https://eu.dmarcadvisor.com/api/v1/domains/{created-domain-id}/\"] } ```  ### 4. List Domains  And voila - you have added your first domain via the API. Now let's verify that the domain is listed under the group. Copy the `domains` property under `_links` from the group you chose in step 2 and list the domains:  ``` curl -G 'https://eu.dmarcadvisor.com/api/v1/domains/?treat_as_top_level=True&group_id={chosen-group-id}' -H 'Authorization: Token {your-api-token}' ```  You should see the new domain in the `results` property of the paginated response.  # Reference  The API reference allows you to dive into each endpoint and check how example requests and response look like, what filters are supported and what is the meaning of each property.   # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import io
import json
import logging
import re
import ssl

import certifi
# python 2 and python 3 compatibility library
import six
from six.moves.urllib.parse import urlencode

try:
    import urllib3
except ImportError:
    raise ImportError('Swagger python client requires urllib3.')


logger = logging.getLogger(__name__)


class RESTResponse(io.IOBase):

    def __init__(self, resp):
        self.urllib3_response = resp
        self.status = resp.status
        self.reason = resp.reason
        self.data = resp.data

    def getheaders(self):
        """Returns a dictionary of the response headers."""
        return self.urllib3_response.getheaders()

    def getheader(self, name, default=None):
        """Returns a given response header."""
        return self.urllib3_response.getheader(name, default)


class RESTClientObject(object):

    def __init__(self, configuration, pools_size=4, maxsize=None):
        # urllib3.PoolManager will pass all kw parameters to connectionpool
        # https://github.com/shazow/urllib3/blob/f9409436f83aeb79fbaf090181cd81b784f1b8ce/urllib3/poolmanager.py#L75  # noqa: E501
        # https://github.com/shazow/urllib3/blob/f9409436f83aeb79fbaf090181cd81b784f1b8ce/urllib3/connectionpool.py#L680  # noqa: E501
        # maxsize is the number of requests to host that are allowed in parallel  # noqa: E501
        # Custom SSL certificates and client certificates: http://urllib3.readthedocs.io/en/latest/advanced-usage.html  # noqa: E501

        # cert_reqs
        if configuration.verify_ssl:
            cert_reqs = ssl.CERT_REQUIRED
        else:
            cert_reqs = ssl.CERT_NONE

        # ca_certs
        if configuration.ssl_ca_cert:
            ca_certs = configuration.ssl_ca_cert
        else:
            # if not set certificate file, use Mozilla's root certificates.
            ca_certs = certifi.where()

        addition_pool_args = {}
        if configuration.assert_hostname is not None:
            addition_pool_args['assert_hostname'] = configuration.assert_hostname  # noqa: E501

        if maxsize is None:
            if configuration.connection_pool_maxsize is not None:
                maxsize = configuration.connection_pool_maxsize
            else:
                maxsize = 4

        # https pool manager
        if configuration.proxy:
            self.pool_manager = urllib3.ProxyManager(
                num_pools=pools_size,
                maxsize=maxsize,
                cert_reqs=cert_reqs,
                ca_certs=ca_certs,
                cert_file=configuration.cert_file,
                key_file=configuration.key_file,
                proxy_url=configuration.proxy,
                **addition_pool_args
            )
        else:
            self.pool_manager = urllib3.PoolManager(
                num_pools=pools_size,
                maxsize=maxsize,
                cert_reqs=cert_reqs,
                ca_certs=ca_certs,
                cert_file=configuration.cert_file,
                key_file=configuration.key_file,
                **addition_pool_args
            )

    def request(self, method, url, query_params=None, headers=None,
                body=None, post_params=None, _preload_content=True,
                _request_timeout=None):
        """Perform requests.

        :param method: http request method
        :param url: http request url
        :param query_params: query parameters in the url
        :param headers: http request headers
        :param body: request json body, for `application/json`
        :param post_params: request post parameters,
                            `application/x-www-form-urlencoded`
                            and `multipart/form-data`
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        """
        method = method.upper()
        assert method in ['GET', 'HEAD', 'DELETE', 'POST', 'PUT',
                          'PATCH', 'OPTIONS']

        if post_params and body:
            raise ValueError(
                "body parameter cannot be used with post_params parameter."
            )

        post_params = post_params or {}
        headers = headers or {}

        timeout = None
        if _request_timeout:
            if isinstance(_request_timeout, (int, ) if six.PY3 else (int, long)):  # noqa: E501,F821
                timeout = urllib3.Timeout(total=_request_timeout)
            elif (isinstance(_request_timeout, tuple) and
                  len(_request_timeout) == 2):
                timeout = urllib3.Timeout(
                    connect=_request_timeout[0], read=_request_timeout[1])

        if 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/json'

        try:
            # For `POST`, `PUT`, `PATCH`, `OPTIONS`, `DELETE`
            if method in ['POST', 'PUT', 'PATCH', 'OPTIONS', 'DELETE']:
                if query_params:
                    url += '?' + urlencode(query_params)
                if re.search('json', headers['Content-Type'], re.IGNORECASE):
                    request_body = '{}'
                    if body is not None:
                        request_body = json.dumps(body)
                    r = self.pool_manager.request(
                        method, url,
                        body=request_body,
                        preload_content=_preload_content,
                        timeout=timeout,
                        headers=headers)
                elif headers['Content-Type'] == 'application/x-www-form-urlencoded':  # noqa: E501
                    r = self.pool_manager.request(
                        method, url,
                        fields=post_params,
                        encode_multipart=False,
                        preload_content=_preload_content,
                        timeout=timeout,
                        headers=headers)
                elif headers['Content-Type'] == 'multipart/form-data':
                    # must del headers['Content-Type'], or the correct
                    # Content-Type which generated by urllib3 will be
                    # overwritten.
                    del headers['Content-Type']
                    r = self.pool_manager.request(
                        method, url,
                        fields=post_params,
                        encode_multipart=True,
                        preload_content=_preload_content,
                        timeout=timeout,
                        headers=headers)
                # Pass a `string` parameter directly in the body to support
                # other content types than Json when `body` argument is
                # provided in serialized form
                elif isinstance(body, str):
                    request_body = body
                    r = self.pool_manager.request(
                        method, url,
                        body=request_body,
                        preload_content=_preload_content,
                        timeout=timeout,
                        headers=headers)
                else:
                    # Cannot generate the request from given parameters
                    msg = """Cannot prepare a request message for provided
                             arguments. Please check that your arguments match
                             declared content type."""
                    raise ApiException(status=0, reason=msg)
            # For `GET`, `HEAD`
            else:
                r = self.pool_manager.request(method, url,
                                              fields=query_params,
                                              preload_content=_preload_content,
                                              timeout=timeout,
                                              headers=headers)
        except urllib3.exceptions.SSLError as e:
            msg = "{0}\n{1}".format(type(e).__name__, str(e))
            raise ApiException(status=0, reason=msg)

        if _preload_content:
            r = RESTResponse(r)

            # In the python 3, the response.data is bytes.
            # we need to decode it to string.
            if six.PY3:
                r.data = r.data.decode('utf8')

            # log response body
            logger.debug("response body: %s", r.data)

        if not 200 <= r.status <= 299:
            raise ApiException(http_resp=r)

        return r

    def GET(self, url, headers=None, query_params=None, _preload_content=True,
            _request_timeout=None):
        return self.request("GET", url,
                            headers=headers,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            query_params=query_params)

    def HEAD(self, url, headers=None, query_params=None, _preload_content=True,
             _request_timeout=None):
        return self.request("HEAD", url,
                            headers=headers,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            query_params=query_params)

    def OPTIONS(self, url, headers=None, query_params=None, post_params=None,
                body=None, _preload_content=True, _request_timeout=None):
        return self.request("OPTIONS", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def DELETE(self, url, headers=None, query_params=None, body=None,
               _preload_content=True, _request_timeout=None):
        return self.request("DELETE", url,
                            headers=headers,
                            query_params=query_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def POST(self, url, headers=None, query_params=None, post_params=None,
             body=None, _preload_content=True, _request_timeout=None):
        return self.request("POST", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def PUT(self, url, headers=None, query_params=None, post_params=None,
            body=None, _preload_content=True, _request_timeout=None):
        return self.request("PUT", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def PATCH(self, url, headers=None, query_params=None, post_params=None,
              body=None, _preload_content=True, _request_timeout=None):
        return self.request("PATCH", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)


class ApiException(Exception):

    def __init__(self, status=None, reason=None, http_resp=None):
        if http_resp:
            self.status = http_resp.status
            self.reason = http_resp.reason
            self.body = http_resp.data
            self.headers = http_resp.getheaders()
        else:
            self.status = status
            self.reason = reason
            self.body = None
            self.headers = None

    def __str__(self):
        """Custom error messages for exception"""
        error_message = "({0})\n"\
                        "Reason: {1}\n".format(self.status, self.reason)
        if self.headers:
            error_message += "HTTP response headers: {0}\n".format(
                self.headers)

        if self.body:
            error_message += "HTTP response body: {0}\n".format(self.body)

        return error_message
