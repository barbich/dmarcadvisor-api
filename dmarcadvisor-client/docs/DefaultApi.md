# dmarcadvisor.DefaultApi

All URIs are relative to *https://eu.dmarcadvisor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**domains_delete_create**](DefaultApi.md#domains_delete_create) | **POST** /api/v1/domains/delete/ | Delete domains in bulk


# **domains_delete_create**
> domains_delete_create(data=data)

Delete domains in bulk

Deletes the posted domain list and all related data.

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.DefaultApi()
data = dmarcadvisor.Data13() # Data13 |  (optional)

try:
    # Delete domains in bulk
    api_instance.domains_delete_create(data=data)
except ApiException as e:
    print("Exception when calling DefaultApi->domains_delete_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data13**](Data13.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

