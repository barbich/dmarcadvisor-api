# dmarcadvisor.SourceDataApi

All URIs are relative to *https://eu.dmarcadvisor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**source_domains_list**](SourceDataApi.md#source_domains_list) | **GET** /api/v1/source-domains/ | List source domains
[**sources_list**](SourceDataApi.md#sources_list) | **GET** /api/v1/sources/ | List sources


# **source_domains_list**
> ResponsesSourceDomainList source_domains_list(page=page, limit=limit, source_number=source_number, filter_id=filter_id)

List source domains

Lists current account's known domain volume by source.

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.SourceDataApi()
page = 56 # int | A page number within the paginated result set. (optional)
limit = 56 # int | Number of results to return per page. (optional)
source_number = 'source_number_example' # str | Source number to return data for. (optional)
filter_id = 8.14 # float | Source filter id to filter data by. (optional)

try:
    # List source domains
    api_response = api_instance.source_domains_list(page=page, limit=limit, source_number=source_number, filter_id=filter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceDataApi->source_domains_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **source_number** | **str**| Source number to return data for. | [optional] 
 **filter_id** | **float**| Source filter id to filter data by. | [optional] 

### Return type

[**ResponsesSourceDomainList**](ResponsesSourceDomainList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_list**
> ResponsesSourceList sources_list(page=page, limit=limit, filter_id=filter_id)

List sources

Lists current account's known sources with volume totals.

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.SourceDataApi()
page = 56 # int | A page number within the paginated result set. (optional)
limit = 56 # int | Number of results to return per page. (optional)
filter_id = 8.14 # float | Source filter id to filter data by. (optional)

try:
    # List sources
    api_response = api_instance.sources_list(page=page, limit=limit, filter_id=filter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceDataApi->sources_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **filter_id** | **float**| Source filter id to filter data by. | [optional] 

### Return type

[**ResponsesSourceList**](ResponsesSourceList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

