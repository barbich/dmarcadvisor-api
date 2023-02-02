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

# Configure API key authorization: API key in header
configuration = dmarcadvisor.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dmarcadvisor.ForensicMetadataApi(dmarcadvisor.ApiClient(configuration))

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

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

