# dmarcadvisor.SourceFiltersApi

All URIs are relative to *https://eu.dmarcadvisor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**source_filters_create**](SourceFiltersApi.md#source_filters_create) | **POST** /api/v1/source-filters/ | Create source filter
[**source_filters_list**](SourceFiltersApi.md#source_filters_list) | **GET** /api/v1/source-filters/ | List source filters
[**source_filters_read**](SourceFiltersApi.md#source_filters_read) | **GET** /api/v1/source-filters/{id}/ | Get source filter


# **source_filters_create**
> ResponsesSourceFilter source_filters_create(data=data)

Create source filter

Creates a new source filter.

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.SourceFiltersApi()
data = dmarcadvisor.Data21() # Data21 |  (optional)

try:
    # Create source filter
    api_response = api_instance.source_filters_create(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceFiltersApi->source_filters_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data21**](Data21.md)|  | [optional] 

### Return type

[**ResponsesSourceFilter**](ResponsesSourceFilter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **source_filters_list**
> ResponsesSourceFilterList source_filters_list(page=page, limit=limit)

List source filters

Lists stored source filters ordered by date descendingly.

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.SourceFiltersApi()
page = 56 # int | A page number within the paginated result set. (optional)
limit = 56 # int | Number of results to return per page. (optional)

try:
    # List source filters
    api_response = api_instance.source_filters_list(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceFiltersApi->source_filters_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 

### Return type

[**ResponsesSourceFilterList**](ResponsesSourceFilterList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **source_filters_read**
> ResponsesSourceFilter source_filters_read(id)

Get source filter

Retrieves source filter details.

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.SourceFiltersApi()
id = 'id_example' # str | 

try:
    # Get source filter
    api_response = api_instance.source_filters_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceFiltersApi->source_filters_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponsesSourceFilter**](ResponsesSourceFilter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

