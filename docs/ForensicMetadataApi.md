# dmarcadvisor.ForensicMetadataApi

All URIs are relative to *https://eu.dmarcadvisor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forensic_metadata_read**](ForensicMetadataApi.md#forensic_metadata_read) | **GET** /api/v1/forensic-metadata/ | Get forensic metadata


# **forensic_metadata_read**
> ResponsesForensicMetadata forensic_metadata_read()

Get forensic metadata

Retrieves forensic metadata.

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.ForensicMetadataApi()

try:
    # Get forensic metadata
    api_response = api_instance.forensic_metadata_read()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForensicMetadataApi->forensic_metadata_read: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponsesForensicMetadata**](ResponsesForensicMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

