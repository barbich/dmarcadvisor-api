# coding: utf-8

"""
    DMARC Advisor API

    # Introduction  Welcome to the DMARC Advisor REST API documentation!  This documentation will help you integrate the DMARC Advisor services into your software so you are not required to use our user interface. We have put a lot of effort into making the endpoints as self descriptive as possible but even if  you have any issues - head to the corresponding section in the reference below.  We have built the API on top of HTTP following  [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) best practices. The endpoints receive JSON in their request body and return JSON as a response  with the proper status code.  # Authentication  Most of our API endpoints are not publicly available so you must authenticate  in order to use them. To do so you need to acquire an API token first. Navigate  to the Manage Settings page and generate one there. You can always regenerate it but keep in mind that this will revoke your old token and it won't be accepted anymore.  Once you have a token you need to provide it as an HTTP header on each  request you make:  ``` Authorization: Token {your-api-token} ```  # Versioning  The API is constantly evolving to match the new features we add to the DMARC Advisor platform. In order to ensure backward compatibility and not break clients we have versioned the API. Each endpoint contains a parameter in the URL that specifies the requested version and looks like this:  ``` https://eu.dmarcadvisor.com/api/v{version-number}/domains/ ```  # Status Codes  Endpoint calls can result in one of the following HTTP Status Codes:  Code | Meaning --- | ---  200 | Successful operation (read, update, etc.) 201 | Resource created (usually on POST requests) 202 | Request for processing has been accepted (e.g. a long query job) 204 | Successful operation without a response body (e.g. delete) 400`*` | Invalid request parameters  401 | Unauthorized - your API token is either missing or invalid 402 | Account subscription has expired 403 | Forbidden - you are not permitted to perform the operation 404 | Requested resource not found 500 | Oops - something went wrong  `*` Have in mind that properties specified in the request body that are not supported will be IGNORED.   # Links and Permissions  [HATEOAS (Hypermedia as the Engine of Application State)](https://en.wikipedia.org/wiki/HATEOAS) is a very cool idea. In essence - endpoint responses provide navigation information by including hypermedia links to the available actions / resources. The main benefit is that clients do not have to be familiar how endpoint URLs are built and do not need to hardcode them inside their API integration.  We have embraced this idea but we have deviated from the specification a bit to have a simpler response structure. We have also added an extra layer on top - permissions. Responses may contain a `_links` property that lists all available actions and a `_permissions` property that specifies which of the actions are permitted to the current user.  ## Root  The API provides a root endpoint that lists all main resources and links to explore them.  For the latest API version call:  ``` https://eu.dmarcadvisor.com/api/ ```  For a specific API version call:  ``` https://eu.dmarcadvisor.com/api/v{version-number}/ ```  Example response:  ```json {     \"domains\": \"https://eu.dmarcadvisor.com/api/v1/domains/\",     \"domain_groups\": \"https://eu.dmarcadvisor.com/api/v1/domain-groups/\",     \"issues\": \"https://eu.dmarcadvisor.com/api/v1/issues/\",     \"tasks\": \"https://eu.dmarcadvisor.com/api/v1/tasks/\" } ```  ## Lists  All list API endpoints support pagination and share an identical response format (check a specific endpoint reference for a detailed response schema). The `_links` property contains URLs for navigation - first page, last page, next page, etc. and the `_permissions` property specifies what is permitted - e.g. only `list` or also `create`.  Example response:  ```json {     \"_links\": {         \"first\": \"https://eu.dmarcadvisor.com/api/v1/domains/\",         \"last\": \"https://eu.dmarcadvisor.com/api/v1/domains/?page=5\",         \"next\": \"https://eu.dmarcadvisor.com/api/v1/domains/?page=2\",         \"previous\": null     },     \"_permissions\": [         \"list\"     ],     \"count\": 24,     \"pages\": 5,     \"current_page\": 1,     \"per_page\": 5,     \"results\": [] } ```  ## Objects  Object API endpoints operate on a specific resource with a unique identifier. The `_links`  property works the same way as described above with one specific difference - the `self` key inside is used for multiple actions - `retrieve`, `update`, `partial_update` and `destroy`.  Example response:  ```json {     \"_links\": {         \"self\": \"https://eu.dmarcadvisor.com/api/v1/domains/17/\",         \"refresh\": \"https://eu.dmarcadvisor.com/api/v1/domains/17/refresh/\",         \"subdomains\": \"https://eu.dmarcadvisor.com/api/v1/domains/?parent_id=17&treat_as_top_level=False\"     },     \"_permissions\": [         \"retrieve\",         \"refresh\",         \"update\",         \"partial_update\",         \"destroy\"     ],     \"id\": 17,     ... } ```  # Working with date fields  API returns date fields as a string representing the `UTC` date and time in ISO 8601 format,  `YYYY-MM-DDTHH:MM:SS.mmmmmm` or, if microsecond is 0, `YYYY-MM-DDTHH:MM:SS`.  In example below Z is the zone designator for the zero UTC offset. ```json {   \"created\": \"2017-09-11T10:18:50.875874Z\" } ```   API accepts date time in ISO 8601 format with given UTC offset(Z for zero or ±HH:MM): ```json {   \"begin\": \"2017-09-11T10:18:50+03:00\",   \"end\": \"2017-09-11T10:18:50+03:00\" } ```  # How-To Guides  After getting familiar with the basics it's time to get our hands dirty and actually do something with the API. In this How To section we are going to describe some common scenarios - check the reference for more advanced cases.  DMARC Advisor does not provide any SDKs currently but communication with the API can be achieved in any programming language since all endpoints are HTTP based. We will use `curl` in our examples for simplicity.  ## Add Domain  The first step after creating an account at DMARC Advisor is to add a domain so we are going to describe how can this be achieved via the API.  ### 1. Get Token  Check the Authentication section for details how to obtain an API token - we will need it for calling the API.  ### 2. List Domain Groups  All domains live under a certain domain group (either the default one which you will automatically have after registration or a group you have created). In order to  create a domain we need to find a group to add it to first:  ``` curl -G https://eu.dmarcadvisor.com/api/v1/domain-groups/ -H 'Authorization: Token {your-api-token}' ```  You will get a paginated list of all available groups. Just choose the one you want to add a domain to (look inside the `results` property) and copy the `add_domain` URL under `_links` - we will use it in the next step.  ### 3. Add the Domain  After we've chosen a group we can actually add the domain:  ``` curl -d '{\"domains\":[\"example.com\"]}' https://eu.dmarcadvisor.com/api/v1/domain-groups/{chosen-group-id}/add-domains/ -H 'Authorization: Token {your-api-token}' -H 'Content-Type: application/json' ```  The response will contain URLs to the newly created domains:  ```json {     \"added\": [\"https://eu.dmarcadvisor.com/api/v1/domains/{created-domain-id}/\"] } ```  ### 4. List Domains  And voila - you have added your first domain via the API. Now let's verify that the domain is listed under the group. Copy the `domains` property under `_links` from the group you chose in step 2 and list the domains:  ``` curl -G 'https://eu.dmarcadvisor.com/api/v1/domains/?treat_as_top_level=True&group_id={chosen-group-id}' -H 'Authorization: Token {your-api-token}' ```  You should see the new domain in the `results` property of the paginated response.  # Reference  The API reference allows you to dive into each endpoint and check how example requests and response look like, what filters are supported and what is the meaning of each property.   # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from dmarcadvisor.configuration import Configuration


class Data11(object):
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
        'domains': 'list[Apiv1domaingroupsidmovedomainsDomains]',
        'domain_state': 'str'
    }

    attribute_map = {
        'domains': 'domains',
        'domain_state': 'domain_state'
    }

    def __init__(self, domains=None, domain_state=None, _configuration=None):  # noqa: E501
        """Data11 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._domains = None
        self._domain_state = None
        self.discriminator = None

        self.domains = domains
        if domain_state is not None:
            self.domain_state = domain_state

    @property
    def domains(self):
        """Gets the domains of this Data11.  # noqa: E501

          # noqa: E501

        :return: The domains of this Data11.  # noqa: E501
        :rtype: list[Apiv1domaingroupsidmovedomainsDomains]
        """
        return self._domains

    @domains.setter
    def domains(self, domains):
        """Sets the domains of this Data11.

          # noqa: E501

        :param domains: The domains of this Data11.  # noqa: E501
        :type: list[Apiv1domaingroupsidmovedomainsDomains]
        """
        if self._configuration.client_side_validation and domains is None:
            raise ValueError("Invalid value for `domains`, must not be `None`")  # noqa: E501

        self._domains = domains

    @property
    def domain_state(self):
        """Gets the domain_state of this Data11.  # noqa: E501

        Domain state. Available options are: \"active\", \"inactive\" and \"unknown\".  # noqa: E501

        :return: The domain_state of this Data11.  # noqa: E501
        :rtype: str
        """
        return self._domain_state

    @domain_state.setter
    def domain_state(self, domain_state):
        """Sets the domain_state of this Data11.

        Domain state. Available options are: \"active\", \"inactive\" and \"unknown\".  # noqa: E501

        :param domain_state: The domain_state of this Data11.  # noqa: E501
        :type: str
        """

        self._domain_state = domain_state

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
        if issubclass(Data11, dict):
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
        if not isinstance(other, Data11):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Data11):
            return True

        return self.to_dict() != other.to_dict()
