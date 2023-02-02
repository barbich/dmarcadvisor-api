# dmarcadvisor.DomainGroupsApi

All URIs are relative to *https://eu.dmarcadvisor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**domain_groups_add_domains**](DomainGroupsApi.md#domain_groups_add_domains) | **POST** /api/v1/domain-groups/{id}/add-domains/ | Add domain(s)
[**domain_groups_delete**](DomainGroupsApi.md#domain_groups_delete) | **DELETE** /api/v1/domain-groups/{id}/ | Delete domain group
[**domain_groups_list**](DomainGroupsApi.md#domain_groups_list) | **GET** /api/v1/domain-groups/ | List domain groups
[**domain_groups_move_domains**](DomainGroupsApi.md#domain_groups_move_domains) | **POST** /api/v1/domain-groups/{id}/move-domains/ | Move domains
[**domain_groups_partial_update**](DomainGroupsApi.md#domain_groups_partial_update) | **PATCH** /api/v1/domain-groups/{id}/ | Update domain group (partial)
[**domain_groups_read**](DomainGroupsApi.md#domain_groups_read) | **GET** /api/v1/domain-groups/{id}/ | Get domain group
[**domain_groups_remove_domains**](DomainGroupsApi.md#domain_groups_remove_domains) | **POST** /api/v1/domain-groups/{id}/remove-domains/ | Remove domain(s)
[**domain_groups_update**](DomainGroupsApi.md#domain_groups_update) | **PUT** /api/v1/domain-groups/{id}/ | Update domain group


# **domain_groups_add_domains**
> ResponsesDomainAdd domain_groups_add_domains(id, data=data)

Add domain(s)

Add domains to the target group.

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# Configure API key authorization: API key in header
configuration = dmarcadvisor.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dmarcadvisor.DomainGroupsApi(dmarcadvisor.ApiClient(configuration))
id = 'id_example' # str | 
data = dmarcadvisor.Data10() # Data10 |  (optional)

try:
    # Add domain(s)
    api_response = api_instance.domain_groups_add_domains(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainGroupsApi->domain_groups_add_domains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Data10**](Data10.md)|  | [optional] 

### Return type

[**ResponsesDomainAdd**](ResponsesDomainAdd.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domain_groups_delete**
> domain_groups_delete(id)

Delete domain group

Remove a domain group. Important: deleting a domain group does not delete domains!

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# Configure API key authorization: API key in header
configuration = dmarcadvisor.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dmarcadvisor.DomainGroupsApi(dmarcadvisor.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete domain group
    api_instance.domain_groups_delete(id)
except ApiException as e:
    print("Exception when calling DomainGroupsApi->domain_groups_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domain_groups_list**
> ResponsesDomainGroupList domain_groups_list(page=page, limit=limit, label=label, domain_state=domain_state)

List domain groups

List current user's domain groups.

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# Configure API key authorization: API key in header
configuration = dmarcadvisor.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dmarcadvisor.DomainGroupsApi(dmarcadvisor.ApiClient(configuration))
page = 56 # int | A page number within the paginated result set. (optional)
limit = 56 # int | Number of results to return per page. (optional)
label = 'label_example' # str | Filter results by domain group name. (optional)
domain_state = 'domain_state_example' # str | Filter results by domain state (\"active\", \"inactive\", \"unknown\"). (optional)

try:
    # List domain groups
    api_response = api_instance.domain_groups_list(page=page, limit=limit, label=label, domain_state=domain_state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainGroupsApi->domain_groups_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **label** | **str**| Filter results by domain group name. | [optional] 
 **domain_state** | **str**| Filter results by domain state (\&quot;active\&quot;, \&quot;inactive\&quot;, \&quot;unknown\&quot;). | [optional] 

### Return type

[**ResponsesDomainGroupList**](ResponsesDomainGroupList.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domain_groups_move_domains**
> ResponsesDomainMove domain_groups_move_domains(id, data=data)

Move domains

Move domains from their source group into the target group (the group in the URL).

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# Configure API key authorization: API key in header
configuration = dmarcadvisor.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dmarcadvisor.DomainGroupsApi(dmarcadvisor.ApiClient(configuration))
id = 'id_example' # str | 
data = dmarcadvisor.Data11() # Data11 |  (optional)

try:
    # Move domains
    api_response = api_instance.domain_groups_move_domains(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainGroupsApi->domain_groups_move_domains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Data11**](Data11.md)|  | [optional] 

### Return type

[**ResponsesDomainMove**](ResponsesDomainMove.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domain_groups_partial_update**
> ResponsesDomainGroup domain_groups_partial_update(id, data=data)

Update domain group (partial)

Update some of the domain group's related properties. Setting \"hide_assigned_domains\" to other than the DEFAULT group is not allowed. Setting \"parked_domains\" for the DEFAULT group is not allowed.

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# Configure API key authorization: API key in header
configuration = dmarcadvisor.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dmarcadvisor.DomainGroupsApi(dmarcadvisor.ApiClient(configuration))
id = 'id_example' # str | 
data = dmarcadvisor.Data9() # Data9 |  (optional)

try:
    # Update domain group (partial)
    api_response = api_instance.domain_groups_partial_update(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainGroupsApi->domain_groups_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Data9**](Data9.md)|  | [optional] 

### Return type

[**ResponsesDomainGroup**](ResponsesDomainGroup.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domain_groups_read**
> ResponsesDomainGroup domain_groups_read(id)

Get domain group

Get domain group details.

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# Configure API key authorization: API key in header
configuration = dmarcadvisor.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dmarcadvisor.DomainGroupsApi(dmarcadvisor.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get domain group
    api_response = api_instance.domain_groups_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainGroupsApi->domain_groups_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponsesDomainGroup**](ResponsesDomainGroup.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domain_groups_remove_domains**
> domain_groups_remove_domains(id, data=data)

Remove domain(s)

Remove domains from the target group (except default).

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# Configure API key authorization: API key in header
configuration = dmarcadvisor.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dmarcadvisor.DomainGroupsApi(dmarcadvisor.ApiClient(configuration))
id = 'id_example' # str | 
data = dmarcadvisor.Data12() # Data12 |  (optional)

try:
    # Remove domain(s)
    api_instance.domain_groups_remove_domains(id, data=data)
except ApiException as e:
    print("Exception when calling DomainGroupsApi->domain_groups_remove_domains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Data12**](Data12.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domain_groups_update**
> ResponsesDomainGroup domain_groups_update(id, data=data)

Update domain group

Update domain group related properties (e.g. label, notes). Setting \"hide_assigned_domains\" to other than the DEFAULT group is not allowed. Setting \"parked_domains\" for the DEFAULT group is not allowed.

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# Configure API key authorization: API key in header
configuration = dmarcadvisor.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dmarcadvisor.DomainGroupsApi(dmarcadvisor.ApiClient(configuration))
id = 'id_example' # str | 
data = dmarcadvisor.Data8() # Data8 |  (optional)

try:
    # Update domain group
    api_response = api_instance.domain_groups_update(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainGroupsApi->domain_groups_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Data8**](Data8.md)|  | [optional] 

### Return type

[**ResponsesDomainGroup**](ResponsesDomainGroup.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

