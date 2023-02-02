# dmarcadvisor.SourceRefreshApi

All URIs are relative to *https://eu.dmarcadvisor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sources_refresh_create**](SourceRefreshApi.md#sources_refresh_create) | **POST** /api/v1/sources/refresh/ | Create source refresh
[**sources_refresh_read**](SourceRefreshApi.md#sources_refresh_read) | **GET** /api/v1/sources/refresh/ | Get source refresh


# **sources_refresh_create**
> ResponsesSourceRefresh sources_refresh_create()

Create source refresh

Creates (triggers) source data refreshing.

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
api_instance = dmarcadvisor.SourceRefreshApi(dmarcadvisor.ApiClient(configuration))

try:
    # Create source refresh
    api_response = api_instance.sources_refresh_create()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceRefreshApi->sources_refresh_create: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponsesSourceRefresh**](ResponsesSourceRefresh.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_refresh_read**
> ResponsesSourceRefresh sources_refresh_read()

Get source refresh

Retrieves source refresh details.

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
api_instance = dmarcadvisor.SourceRefreshApi(dmarcadvisor.ApiClient(configuration))

try:
    # Get source refresh
    api_response = api_instance.sources_refresh_read()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceRefreshApi->sources_refresh_read: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponsesSourceRefresh**](ResponsesSourceRefresh.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

