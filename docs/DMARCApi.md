# dmarcadvisor.DMARCApi

All URIs are relative to *https://eu.dmarcadvisor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dmarc_inspect_create**](DMARCApi.md#dmarc_inspect_create) | **POST** /api/v1/dmarc/inspect/ | Inspect DMARC record
[**dmarc_validate_create**](DMARCApi.md#dmarc_validate_create) | **POST** /api/v1/dmarc/validate/ | Validate DMARC record


# **dmarc_inspect_create**
> ResponsesDMARCInspection dmarc_inspect_create(data=data)

Inspect DMARC record

Inspects a published DMARC record for a specific domain.

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
api_instance = dmarcadvisor.DMARCApi(dmarcadvisor.ApiClient(configuration))
data = dmarcadvisor.Data3() # Data3 |  (optional)

try:
    # Inspect DMARC record
    api_response = api_instance.dmarc_inspect_create(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DMARCApi->dmarc_inspect_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data3**](Data3.md)|  | [optional] 

### Return type

[**ResponsesDMARCInspection**](ResponsesDMARCInspection.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dmarc_validate_create**
> ResponsesDMARCValidation dmarc_validate_create(data=data)

Validate DMARC record

Validates a DMARC record string.

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
api_instance = dmarcadvisor.DMARCApi(dmarcadvisor.ApiClient(configuration))
data = dmarcadvisor.Data4() # Data4 |  (optional)

try:
    # Validate DMARC record
    api_response = api_instance.dmarc_validate_create(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DMARCApi->dmarc_validate_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data4**](Data4.md)|  | [optional] 

### Return type

[**ResponsesDMARCValidation**](ResponsesDMARCValidation.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

