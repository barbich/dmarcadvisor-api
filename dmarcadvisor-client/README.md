# dmarcadvisor-api
# Introduction  Welcome to the DMARC Advisor REST API documentation!  This documentation will help you integrate the DMARC Advisor services into your software so you are not required to use our user interface. We have put a lot of effort into making the endpoints as self descriptive as possible but even if  you have any issues - head to the corresponding section in the reference below.  We have built the API on top of HTTP following  [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) best practices. The endpoints receive JSON in their request body and return JSON as a response  with the proper status code.  # Authentication  Most of our API endpoints are not publicly available so you must authenticate  in order to use them. To do so you need to acquire an API token first. Navigate  to the Manage Settings page and generate one there. You can always regenerate it but keep in mind that this will revoke your old token and it won't be accepted anymore.  Once you have a token you need to provide it as an HTTP header on each  request you make:  ``` Authorization: Token {your-api-token} ```  # Versioning  The API is constantly evolving to match the new features we add to the DMARC Advisor platform. In order to ensure backward compatibility and not break clients we have versioned the API. Each endpoint contains a parameter in the URL that specifies the requested version and looks like this:  ``` https://eu.dmarcadvisor.com/api/v{version-number}/domains/ ```  # Status Codes  Endpoint calls can result in one of the following HTTP Status Codes:  Code | Meaning --- | ---  200 | Successful operation (read, update, etc.) 201 | Resource created (usually on POST requests) 202 | Request for processing has been accepted (e.g. a long query job) 204 | Successful operation without a response body (e.g. delete) 400`*` | Invalid request parameters  401 | Unauthorized - your API token is either missing or invalid 402 | Account subscription has expired 403 | Forbidden - you are not permitted to perform the operation 404 | Requested resource not found 500 | Oops - something went wrong  `*` Have in mind that properties specified in the request body that are not supported will be IGNORED.   # Links and Permissions  [HATEOAS (Hypermedia as the Engine of Application State)](https://en.wikipedia.org/wiki/HATEOAS) is a very cool idea. In essence - endpoint responses provide navigation information by including hypermedia links to the available actions / resources. The main benefit is that clients do not have to be familiar how endpoint URLs are built and do not need to hardcode them inside their API integration.  We have embraced this idea but we have deviated from the specification a bit to have a simpler response structure. We have also added an extra layer on top - permissions. Responses may contain a `_links` property that lists all available actions and a `_permissions` property that specifies which of the actions are permitted to the current user.  ## Root  The API provides a root endpoint that lists all main resources and links to explore them.  For the latest API version call:  ``` https://eu.dmarcadvisor.com/api/ ```  For a specific API version call:  ``` https://eu.dmarcadvisor.com/api/v{version-number}/ ```  Example response:  ```json {     \"domains\": \"https://eu.dmarcadvisor.com/api/v1/domains/\",     \"domain_groups\": \"https://eu.dmarcadvisor.com/api/v1/domain-groups/\",     \"issues\": \"https://eu.dmarcadvisor.com/api/v1/issues/\",     \"tasks\": \"https://eu.dmarcadvisor.com/api/v1/tasks/\" } ```  ## Lists  All list API endpoints support pagination and share an identical response format (check a specific endpoint reference for a detailed response schema). The `_links` property contains URLs for navigation - first page, last page, next page, etc. and the `_permissions` property specifies what is permitted - e.g. only `list` or also `create`.  Example response:  ```json {     \"_links\": {         \"first\": \"https://eu.dmarcadvisor.com/api/v1/domains/\",         \"last\": \"https://eu.dmarcadvisor.com/api/v1/domains/?page=5\",         \"next\": \"https://eu.dmarcadvisor.com/api/v1/domains/?page=2\",         \"previous\": null     },     \"_permissions\": [         \"list\"     ],     \"count\": 24,     \"pages\": 5,     \"current_page\": 1,     \"per_page\": 5,     \"results\": [] } ```  ## Objects  Object API endpoints operate on a specific resource with a unique identifier. The `_links`  property works the same way as described above with one specific difference - the `self` key inside is used for multiple actions - `retrieve`, `update`, `partial_update` and `destroy`.  Example response:  ```json {     \"_links\": {         \"self\": \"https://eu.dmarcadvisor.com/api/v1/domains/17/\",         \"refresh\": \"https://eu.dmarcadvisor.com/api/v1/domains/17/refresh/\",         \"subdomains\": \"https://eu.dmarcadvisor.com/api/v1/domains/?parent_id=17&treat_as_top_level=False\"     },     \"_permissions\": [         \"retrieve\",         \"refresh\",         \"update\",         \"partial_update\",         \"destroy\"     ],     \"id\": 17,     ... } ```  # Working with date fields  API returns date fields as a string representing the `UTC` date and time in ISO 8601 format,  `YYYY-MM-DDTHH:MM:SS.mmmmmm` or, if microsecond is 0, `YYYY-MM-DDTHH:MM:SS`.  In example below Z is the zone designator for the zero UTC offset. ```json {   \"created\": \"2017-09-11T10:18:50.875874Z\" } ```   API accepts date time in ISO 8601 format with given UTC offset(Z for zero or ±HH:MM): ```json {   \"begin\": \"2017-09-11T10:18:50+03:00\",   \"end\": \"2017-09-11T10:18:50+03:00\" } ```  # How-To Guides  After getting familiar with the basics it's time to get our hands dirty and actually do something with the API. In this How To section we are going to describe some common scenarios - check the reference for more advanced cases.  DMARC Advisor does not provide any SDKs currently but communication with the API can be achieved in any programming language since all endpoints are HTTP based. We will use `curl` in our examples for simplicity.  ## Add Domain  The first step after creating an account at DMARC Advisor is to add a domain so we are going to describe how can this be achieved via the API.  ### 1. Get Token  Check the Authentication section for details how to obtain an API token - we will need it for calling the API.  ### 2. List Domain Groups  All domains live under a certain domain group (either the default one which you will automatically have after registration or a group you have created). In order to  create a domain we need to find a group to add it to first:  ``` curl -G https://eu.dmarcadvisor.com/api/v1/domain-groups/ -H 'Authorization: Token {your-api-token}' ```  You will get a paginated list of all available groups. Just choose the one you want to add a domain to (look inside the `results` property) and copy the `add_domain` URL under `_links` - we will use it in the next step.  ### 3. Add the Domain  After we've chosen a group we can actually add the domain:  ``` curl -d '{\"domains\":[\"example.com\"]}' https://eu.dmarcadvisor.com/api/v1/domain-groups/{chosen-group-id}/add-domains/ -H 'Authorization: Token {your-api-token}' -H 'Content-Type: application/json' ```  The response will contain URLs to the newly created domains:  ```json {     \"added\": [\"https://eu.dmarcadvisor.com/api/v1/domains/{created-domain-id}/\"] } ```  ### 4. List Domains  And voila - you have added your first domain via the API. Now let's verify that the domain is listed under the group. Copy the `domains` property under `_links` from the group you chose in step 2 and list the domains:  ``` curl -G 'https://eu.dmarcadvisor.com/api/v1/domains/?treat_as_top_level=True&group_id={chosen-group-id}' -H 'Authorization: Token {your-api-token}' ```  You should see the new domain in the `results` property of the paginated response.  # Reference  The API reference allows you to dive into each endpoint and check how example requests and response look like, what filters are supported and what is the meaning of each property. 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import dmarcadvisor 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import dmarcadvisor
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.DKIMApi(dmarcadvisor.ApiClient(configuration))
data = dmarcadvisor.Data() # Data |  (optional)

try:
    # Inspect DKIM record
    api_response = api_instance.dkim_inspect_create(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DKIMApi->dkim_inspect_create: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://eu.dmarcadvisor.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DKIMApi* | [**dkim_inspect_create**](docs/DKIMApi.md#dkim_inspect_create) | **POST** /api/dkim/inspect/ | Inspect DKIM record
*DKIMApi* | [**dkim_validate_create**](docs/DKIMApi.md#dkim_validate_create) | **POST** /api/dkim/validate/ | Validate DKIM record
*DMARCApi* | [**dmarc_inspect_create**](docs/DMARCApi.md#dmarc_inspect_create) | **POST** /api/v1/dmarc/inspect/ | Inspect DMARC record
*DMARCApi* | [**dmarc_validate_create**](docs/DMARCApi.md#dmarc_validate_create) | **POST** /api/v1/dmarc/validate/ | Validate DMARC record
*DomainGroupAccessControlListACLApi* | [**domain_groups_acl_add_admin_users**](docs/DomainGroupAccessControlListACLApi.md#domain_groups_acl_add_admin_users) | **POST** /api/v1/domain-groups-acl/{id}/add-admin-users/ | Add write level access for an user of a domain group
*DomainGroupAccessControlListACLApi* | [**domain_groups_acl_add_readonly_users**](docs/DomainGroupAccessControlListACLApi.md#domain_groups_acl_add_readonly_users) | **POST** /api/v1/domain-groups-acl/{id}/add-readonly-users/ | Add read-only level access for an user of a domain group
*DomainGroupAccessControlListACLApi* | [**domain_groups_acl_list**](docs/DomainGroupAccessControlListACLApi.md#domain_groups_acl_list) | **GET** /api/v1/domain-groups-acl/ | Get a list of all domain groups and user access levels
*DomainGroupAccessControlListACLApi* | [**domain_groups_acl_set_no_access**](docs/DomainGroupAccessControlListACLApi.md#domain_groups_acl_set_no_access) | **POST** /api/v1/domain-groups-acl/{id}/set-no-access/ | Remove access level for an user of a domain group
*DomainGroupsApi* | [**domain_groups_add_domains**](docs/DomainGroupsApi.md#domain_groups_add_domains) | **POST** /api/v1/domain-groups/{id}/add-domains/ | Add domain(s)
*DomainGroupsApi* | [**domain_groups_delete**](docs/DomainGroupsApi.md#domain_groups_delete) | **DELETE** /api/v1/domain-groups/{id}/ | Delete domain group
*DomainGroupsApi* | [**domain_groups_list**](docs/DomainGroupsApi.md#domain_groups_list) | **GET** /api/v1/domain-groups/ | List domain groups
*DomainGroupsApi* | [**domain_groups_move_domains**](docs/DomainGroupsApi.md#domain_groups_move_domains) | **POST** /api/v1/domain-groups/{id}/move-domains/ | Move domains
*DomainGroupsApi* | [**domain_groups_partial_update**](docs/DomainGroupsApi.md#domain_groups_partial_update) | **PATCH** /api/v1/domain-groups/{id}/ | Update domain group (partial)
*DomainGroupsApi* | [**domain_groups_read**](docs/DomainGroupsApi.md#domain_groups_read) | **GET** /api/v1/domain-groups/{id}/ | Get domain group
*DomainGroupsApi* | [**domain_groups_remove_domains**](docs/DomainGroupsApi.md#domain_groups_remove_domains) | **POST** /api/v1/domain-groups/{id}/remove-domains/ | Remove domain(s)
*DomainGroupsApi* | [**domain_groups_update**](docs/DomainGroupsApi.md#domain_groups_update) | **PUT** /api/v1/domain-groups/{id}/ | Update domain group
*DomainsApi* | [**domains_delete0**](docs/DomainsApi.md#domains_delete0) | **DELETE** /api/v1/domains/{id}/ | Delete domain
*DomainsApi* | [**domains_list**](docs/DomainsApi.md#domains_list) | **GET** /api/v1/domains/ | List domains
*DomainsApi* | [**domains_partial_update**](docs/DomainsApi.md#domains_partial_update) | **PATCH** /api/v1/domains/{id}/ | Update domain (partial)
*DomainsApi* | [**domains_read**](docs/DomainsApi.md#domains_read) | **GET** /api/v1/domains/{id}/ | Get domain
*DomainsApi* | [**domains_refresh**](docs/DomainsApi.md#domains_refresh) | **POST** /api/v1/domains/{id}/refresh/ | Refresh domain
*DomainsApi* | [**domains_update**](docs/DomainsApi.md#domains_update) | **PUT** /api/v1/domains/{id}/ | Update domain
*DomainsApi* | [**domains_verify**](docs/DomainsApi.md#domains_verify) | **POST** /api/v1/domains/{id}/verify/ | Verify domain
*ForensicFiltersApi* | [**forensic_filters_create**](docs/ForensicFiltersApi.md#forensic_filters_create) | **POST** /api/v1/forensic-filters/ | Create forensic filter
*ForensicFiltersApi* | [**forensic_filters_list**](docs/ForensicFiltersApi.md#forensic_filters_list) | **GET** /api/v1/forensic-filters/ | List forensic filters
*ForensicFiltersApi* | [**forensic_filters_read**](docs/ForensicFiltersApi.md#forensic_filters_read) | **GET** /api/v1/forensic-filters/{id}/ | Get forensic filter
*ForensicMetadataApi* | [**forensic_metadata_read**](docs/ForensicMetadataApi.md#forensic_metadata_read) | **GET** /api/v1/forensic-metadata/ | Get forensic metadata
*ForensicReportsApi* | [**forensics_list**](docs/ForensicReportsApi.md#forensics_list) | **GET** /api/v1/forensics/ | List forensic reports
*IssuesApi* | [**issues_list**](docs/IssuesApi.md#issues_list) | **GET** /api/v1/issues/ | List issues
*IssuesApi* | [**issues_partial_update**](docs/IssuesApi.md#issues_partial_update) | **PATCH** /api/v1/issues/{id}/ | Update issue (partial)
*IssuesApi* | [**issues_read**](docs/IssuesApi.md#issues_read) | **GET** /api/v1/issues/{id}/ | Get issue
*IssuesApi* | [**issues_update**](docs/IssuesApi.md#issues_update) | **PUT** /api/v1/issues/{id}/ | Update issue
*PolicyDomainsApi* | [**policy_domains_list**](docs/PolicyDomainsApi.md#policy_domains_list) | **GET** /api/v1/policy-domains/ | List policy domains
*PolicyFiltersApi* | [**policy_domain_filters_create**](docs/PolicyFiltersApi.md#policy_domain_filters_create) | **POST** /api/v1/policy-domain-filters/ | Create policy filter
*PolicyFiltersApi* | [**policy_domain_filters_list**](docs/PolicyFiltersApi.md#policy_domain_filters_list) | **GET** /api/v1/policy-domain-filters/ | List policy filters
*PolicyFiltersApi* | [**policy_domain_filters_read**](docs/PolicyFiltersApi.md#policy_domain_filters_read) | **GET** /api/v1/policy-domain-filters/{id}/ | Get policy filter
*ReportDataApi* | [**aggregate_report_domains_list**](docs/ReportDataApi.md#aggregate_report_domains_list) | **GET** /api/v1/aggregate-report/{search_token}/domains/ | Domains
*ReportDataApi* | [**aggregate_report_progress**](docs/ReportDataApi.md#aggregate_report_progress) | **GET** /api/v1/aggregate-report/{search_token}/progress/ | Progress
*ReportDataApi* | [**aggregate_report_source_list**](docs/ReportDataApi.md#aggregate_report_source_list) | **GET** /api/v1/aggregate-report/{search_token}/source/{source_number}/ | Source data
*ReportDataApi* | [**aggregate_report_sources**](docs/ReportDataApi.md#aggregate_report_sources) | **GET** /api/v1/aggregate-report/{search_token}/sources/ | Sources
*ReportsApi* | [**detail_viewer_create**](docs/ReportsApi.md#detail_viewer_create) | **POST** /api/v1/detail-viewer/ | Create Detail Viewer report
*ReportsApi* | [**detail_viewer_list**](docs/ReportsApi.md#detail_viewer_list) | **GET** /api/v1/detail-viewer/ | List Detail Viewer reports
*ReportsApi* | [**detail_viewer_read**](docs/ReportsApi.md#detail_viewer_read) | **GET** /api/v1/detail-viewer/{search_token}/ | List/create Detail Viewer reports.
*SourceDataApi* | [**source_domains_list**](docs/SourceDataApi.md#source_domains_list) | **GET** /api/v1/source-domains/ | List source domains
*SourceDataApi* | [**sources_list**](docs/SourceDataApi.md#sources_list) | **GET** /api/v1/sources/ | List sources
*SourceFiltersApi* | [**source_filters_create**](docs/SourceFiltersApi.md#source_filters_create) | **POST** /api/v1/source-filters/ | Create source filter
*SourceFiltersApi* | [**source_filters_list**](docs/SourceFiltersApi.md#source_filters_list) | **GET** /api/v1/source-filters/ | List source filters
*SourceFiltersApi* | [**source_filters_read**](docs/SourceFiltersApi.md#source_filters_read) | **GET** /api/v1/source-filters/{id}/ | Get source filter
*SourceRefreshApi* | [**sources_refresh_create**](docs/SourceRefreshApi.md#sources_refresh_create) | **POST** /api/v1/sources/refresh/ | Create source refresh
*SourceRefreshApi* | [**sources_refresh_read**](docs/SourceRefreshApi.md#sources_refresh_read) | **GET** /api/v1/sources/refresh/ | Get source refresh
*TasksApi* | [**tasks_list**](docs/TasksApi.md#tasks_list) | **GET** /api/v1/tasks/ | List tasks
*TasksApi* | [**tasks_partial_update**](docs/TasksApi.md#tasks_partial_update) | **PATCH** /api/v1/tasks/{id}/ | Update task (partial)
*TasksApi* | [**tasks_read**](docs/TasksApi.md#tasks_read) | **GET** /api/v1/tasks/{id}/ | Get task
*TasksApi* | [**tasks_update**](docs/TasksApi.md#tasks_update) | **PUT** /api/v1/tasks/{id}/ | Update task
*UsersApi* | [**users_activation_reminder**](docs/UsersApi.md#users_activation_reminder) | **POST** /api/v1/users/{id}/activation-reminder/ | Send an email activation reminder
*UsersApi* | [**users_convert_to_sso**](docs/UsersApi.md#users_convert_to_sso) | **PUT** /api/v1/users/{id}/convert-to-sso/ | Convert an user to SSO login
*UsersApi* | [**users_create**](docs/UsersApi.md#users_create) | **POST** /api/v1/users/ | Create and add a new user to an account
*UsersApi* | [**users_delete**](docs/UsersApi.md#users_delete) | **DELETE** /api/v1/users/{id}/ | Delete an user
*UsersApi* | [**users_list**](docs/UsersApi.md#users_list) | **GET** /api/v1/users/ | Get a list of all users within an account
*UsersApi* | [**users_partial_update**](docs/UsersApi.md#users_partial_update) | **PATCH** /api/v1/users/{id}/ | Partial update of user details
*UsersApi* | [**users_password_change**](docs/UsersApi.md#users_password_change) | **POST** /api/v1/users/{id}/password-change/ | Change user password
*UsersApi* | [**users_password_reset**](docs/UsersApi.md#users_password_reset) | **POST** /api/v1/users/{id}/password-reset/ | Send password reset email
*UsersApi* | [**users_read**](docs/UsersApi.md#users_read) | **GET** /api/v1/users/{id}/ | Get user details
*UsersApi* | [**users_update**](docs/UsersApi.md#users_update) | **PUT** /api/v1/users/{id}/ | Update user details
*DefaultApi* | [**domains_delete_create**](docs/DefaultApi.md#domains_delete_create) | **POST** /api/v1/domains/delete/ | Delete domains in bulk


## Documentation For Models

 - [Apiv1domaingroupsidmovedomainsDomains](docs/Apiv1domaingroupsidmovedomainsDomains.md)
 - [Data](docs/Data.md)
 - [Data1](docs/Data1.md)
 - [Data10](docs/Data10.md)
 - [Data11](docs/Data11.md)
 - [Data12](docs/Data12.md)
 - [Data13](docs/Data13.md)
 - [Data14](docs/Data14.md)
 - [Data15](docs/Data15.md)
 - [Data16](docs/Data16.md)
 - [Data17](docs/Data17.md)
 - [Data18](docs/Data18.md)
 - [Data19](docs/Data19.md)
 - [Data2](docs/Data2.md)
 - [Data20](docs/Data20.md)
 - [Data21](docs/Data21.md)
 - [Data22](docs/Data22.md)
 - [Data23](docs/Data23.md)
 - [Data24](docs/Data24.md)
 - [Data25](docs/Data25.md)
 - [Data26](docs/Data26.md)
 - [Data27](docs/Data27.md)
 - [Data3](docs/Data3.md)
 - [Data4](docs/Data4.md)
 - [Data5](docs/Data5.md)
 - [Data6](docs/Data6.md)
 - [Data7](docs/Data7.md)
 - [Data8](docs/Data8.md)
 - [Data9](docs/Data9.md)
 - [Model](docs/Model.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author



