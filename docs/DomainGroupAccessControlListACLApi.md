# dmarcadvisor.DomainGroupAccessControlListACLApi

All URIs are relative to *https://eu.dmarcadvisor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**domain_groups_acl_add_admin_users**](DomainGroupAccessControlListACLApi.md#domain_groups_acl_add_admin_users) | **POST** /api/v1/domain-groups-acl/{id}/add-admin-users/ | Add write level access for an user of a domain group
[**domain_groups_acl_add_readonly_users**](DomainGroupAccessControlListACLApi.md#domain_groups_acl_add_readonly_users) | **POST** /api/v1/domain-groups-acl/{id}/add-readonly-users/ | Add read-only level access for an user of a domain group
[**domain_groups_acl_list**](DomainGroupAccessControlListACLApi.md#domain_groups_acl_list) | **GET** /api/v1/domain-groups-acl/ | Get a list of all domain groups and user access levels
[**domain_groups_acl_set_no_access**](DomainGroupAccessControlListACLApi.md#domain_groups_acl_set_no_access) | **POST** /api/v1/domain-groups-acl/{id}/set-no-access/ | Remove access level for an user of a domain group


# **domain_groups_acl_add_admin_users**
> ResponsesDomainGroupWriteAdd domain_groups_acl_add_admin_users(id, data=data)

Add write level access for an user of a domain group

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.DomainGroupAccessControlListACLApi()
id = 'id_example' # str | 
data = dmarcadvisor.Data5() # Data5 |  (optional)

try:
    # Add write level access for an user of a domain group
    api_response = api_instance.domain_groups_acl_add_admin_users(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainGroupAccessControlListACLApi->domain_groups_acl_add_admin_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Data5**](Data5.md)|  | [optional] 

### Return type

[**ResponsesDomainGroupWriteAdd**](ResponsesDomainGroupWriteAdd.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domain_groups_acl_add_readonly_users**
> ResponsesDomainGroupReadAdd domain_groups_acl_add_readonly_users(id, data=data)

Add read-only level access for an user of a domain group

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.DomainGroupAccessControlListACLApi()
id = 'id_example' # str | 
data = dmarcadvisor.Data6() # Data6 |  (optional)

try:
    # Add read-only level access for an user of a domain group
    api_response = api_instance.domain_groups_acl_add_readonly_users(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainGroupAccessControlListACLApi->domain_groups_acl_add_readonly_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Data6**](Data6.md)|  | [optional] 

### Return type

[**ResponsesDomainGroupReadAdd**](ResponsesDomainGroupReadAdd.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domain_groups_acl_list**
> ResponsesDomainGroupsACLList domain_groups_acl_list(page=page, limit=limit, label=label)

Get a list of all domain groups and user access levels

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.DomainGroupAccessControlListACLApi()
page = 56 # int | A page number within the paginated result set. (optional)
limit = 56 # int | Number of results to return per page. (optional)
label = 'label_example' # str | Filter domain groups by label. (optional)

try:
    # Get a list of all domain groups and user access levels
    api_response = api_instance.domain_groups_acl_list(page=page, limit=limit, label=label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainGroupAccessControlListACLApi->domain_groups_acl_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **label** | **str**| Filter domain groups by label. | [optional] 

### Return type

[**ResponsesDomainGroupsACLList**](ResponsesDomainGroupsACLList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domain_groups_acl_set_no_access**
> domain_groups_acl_set_no_access(id, data=data)

Remove access level for an user of a domain group

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.DomainGroupAccessControlListACLApi()
id = 'id_example' # str | 
data = dmarcadvisor.Data7() # Data7 |  (optional)

try:
    # Remove access level for an user of a domain group
    api_instance.domain_groups_acl_set_no_access(id, data=data)
except ApiException as e:
    print("Exception when calling DomainGroupAccessControlListACLApi->domain_groups_acl_set_no_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Data7**](Data7.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

