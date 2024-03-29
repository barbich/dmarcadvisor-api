# dmarcadvisor.ForensicReportsApi

All URIs are relative to *https://eu.dmarcadvisor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forensics_list**](ForensicReportsApi.md#forensics_list) | **GET** /api/v1/forensics/ | List forensic reports


# **forensics_list**
> ResponsesForensicReportList forensics_list(cursor=cursor, limit=limit, filter_id=filter_id)

List forensic reports

Lists forensic reports belonging to the current account.

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
api_instance = dmarcadvisor.ForensicReportsApi(dmarcadvisor.ApiClient(configuration))
cursor = 'cursor_example' # str | The pagination cursor value. (optional)
limit = 56 # int | Number of results to return per page. (optional)
filter_id = 8.14 # float | Forensic filter id to filter reports by. (optional)

try:
    # List forensic reports
    api_response = api_instance.forensics_list(cursor=cursor, limit=limit, filter_id=filter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForensicReportsApi->forensics_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| The pagination cursor value. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **filter_id** | **float**| Forensic filter id to filter reports by. | [optional] 

### Return type

[**ResponsesForensicReportList**](ResponsesForensicReportList.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

