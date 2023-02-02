# dmarcadvisor.PolicyFiltersApi

All URIs are relative to *https://eu.dmarcadvisor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**policy_domain_filters_create**](PolicyFiltersApi.md#policy_domain_filters_create) | **POST** /api/v1/policy-domain-filters/ | Create policy filter
[**policy_domain_filters_list**](PolicyFiltersApi.md#policy_domain_filters_list) | **GET** /api/v1/policy-domain-filters/ | List policy filters
[**policy_domain_filters_read**](PolicyFiltersApi.md#policy_domain_filters_read) | **GET** /api/v1/policy-domain-filters/{id}/ | Get policy filter


# **policy_domain_filters_create**
> ResponsesPolicyPlannerFilter policy_domain_filters_create(data=data)

Create policy filter

Creates a new policy planner filter.

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
api_instance = dmarcadvisor.PolicyFiltersApi(dmarcadvisor.ApiClient(configuration))
data = dmarcadvisor.Data20() # Data20 |  (optional)

try:
    # Create policy filter
    api_response = api_instance.policy_domain_filters_create(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyFiltersApi->policy_domain_filters_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data20**](Data20.md)|  | [optional] 

### Return type

[**ResponsesPolicyPlannerFilter**](ResponsesPolicyPlannerFilter.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policy_domain_filters_list**
> ResponsesPolicyPlannerFilterList policy_domain_filters_list(page=page, limit=limit)

List policy filters

Lists the latest policy planner filters created by the user.

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
api_instance = dmarcadvisor.PolicyFiltersApi(dmarcadvisor.ApiClient(configuration))
page = 56 # int | A page number within the paginated result set. (optional)
limit = 56 # int | Number of results to return per page. (optional)

try:
    # List policy filters
    api_response = api_instance.policy_domain_filters_list(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyFiltersApi->policy_domain_filters_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 

### Return type

[**ResponsesPolicyPlannerFilterList**](ResponsesPolicyPlannerFilterList.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policy_domain_filters_read**
> ResponsesPolicyPlannerFilter policy_domain_filters_read(id)

Get policy filter

Retrieves policy planner filter details.

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
api_instance = dmarcadvisor.PolicyFiltersApi(dmarcadvisor.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get policy filter
    api_response = api_instance.policy_domain_filters_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyFiltersApi->policy_domain_filters_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponsesPolicyPlannerFilter**](ResponsesPolicyPlannerFilter.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

