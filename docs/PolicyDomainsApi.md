# dmarcadvisor.PolicyDomainsApi

All URIs are relative to *https://eu.dmarcadvisor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**policy_domains_list**](PolicyDomainsApi.md#policy_domains_list) | **GET** /api/v1/policy-domains/ | List policy domains


# **policy_domains_list**
> ResponsesPolicyDomainList policy_domains_list(page=page, limit=limit, filter_id=filter_id, policy_ready=policy_ready, recommendation=recommendation)

List policy domains

Lists policy domains the current user has access to.

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
api_instance = dmarcadvisor.PolicyDomainsApi(dmarcadvisor.ApiClient(configuration))
page = 56 # int | A page number within the paginated result set. (optional)
limit = 56 # int | Number of results to return per page. (optional)
filter_id = 8.14 # float | Policy filter id to filter domains by. (optional)
policy_ready = 'policy_ready_example' # str | Show domains ready for new policy (True) or not (False). (optional)
recommendation = 'recommendation_example' # str | Filter results by recommendation. (optional)

try:
    # List policy domains
    api_response = api_instance.policy_domains_list(page=page, limit=limit, filter_id=filter_id, policy_ready=policy_ready, recommendation=recommendation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyDomainsApi->policy_domains_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **filter_id** | **float**| Policy filter id to filter domains by. | [optional] 
 **policy_ready** | **str**| Show domains ready for new policy (True) or not (False). | [optional] 
 **recommendation** | **str**| Filter results by recommendation. | [optional] 

### Return type

[**ResponsesPolicyDomainList**](ResponsesPolicyDomainList.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

