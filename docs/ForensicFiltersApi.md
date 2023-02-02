# dmarcadvisor.ForensicFiltersApi

All URIs are relative to *https://eu.dmarcadvisor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forensic_filters_create**](ForensicFiltersApi.md#forensic_filters_create) | **POST** /api/v1/forensic-filters/ | Create forensic filter
[**forensic_filters_list**](ForensicFiltersApi.md#forensic_filters_list) | **GET** /api/v1/forensic-filters/ | List forensic filters
[**forensic_filters_read**](ForensicFiltersApi.md#forensic_filters_read) | **GET** /api/v1/forensic-filters/{id}/ | Get forensic filter


# **forensic_filters_create**
> ResponsesForensicFilter forensic_filters_create(data=data)

Create forensic filter

Creates a new forensic filter.

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.ForensicFiltersApi()
data = dmarcadvisor.Data17() # Data17 |  (optional)

try:
    # Create forensic filter
    api_response = api_instance.forensic_filters_create(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForensicFiltersApi->forensic_filters_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data17**](Data17.md)|  | [optional] 

### Return type

[**ResponsesForensicFilter**](ResponsesForensicFilter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forensic_filters_list**
> ResponsesForensicFilterList forensic_filters_list(page=page, limit=limit)

List forensic filters

Lists the latest forensic filters created by the user.

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.ForensicFiltersApi()
page = 56 # int | A page number within the paginated result set. (optional)
limit = 56 # int | Number of results to return per page. (optional)

try:
    # List forensic filters
    api_response = api_instance.forensic_filters_list(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForensicFiltersApi->forensic_filters_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 

### Return type

[**ResponsesForensicFilterList**](ResponsesForensicFilterList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forensic_filters_read**
> ResponsesForensicFilter forensic_filters_read(id)

Get forensic filter

Retrieves forensic filter details.

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.ForensicFiltersApi()
id = 'id_example' # str | 

try:
    # Get forensic filter
    api_response = api_instance.forensic_filters_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForensicFiltersApi->forensic_filters_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponsesForensicFilter**](ResponsesForensicFilter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

