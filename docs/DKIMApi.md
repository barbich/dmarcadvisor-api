# dmarcadvisor.DKIMApi

All URIs are relative to *https://eu.dmarcadvisor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dkim_inspect_create**](DKIMApi.md#dkim_inspect_create) | **POST** /api/dkim/inspect/ | Inspect DKIM record
[**dkim_validate_create**](DKIMApi.md#dkim_validate_create) | **POST** /api/dkim/validate/ | Validate DKIM record


# **dkim_inspect_create**
> ResponsesDKIMInspection dkim_inspect_create(data=data)

Inspect DKIM record

Inspects a published DKIM record for a specific domain and selector.

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
api_instance = dmarcadvisor.DKIMApi(dmarcadvisor.ApiClient(configuration))
data = dmarcadvisor.Data() # Data |  (optional)

try:
    # Inspect DKIM record
    api_response = api_instance.dkim_inspect_create(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DKIMApi->dkim_inspect_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data**](Data.md)|  | [optional] 

### Return type

[**ResponsesDKIMInspection**](ResponsesDKIMInspection.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dkim_validate_create**
> ResponsesDKIMValidation dkim_validate_create(data=data)

Validate DKIM record

Validates a DKIM record string.

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
api_instance = dmarcadvisor.DKIMApi(dmarcadvisor.ApiClient(configuration))
data = dmarcadvisor.Data1() # Data1 |  (optional)

try:
    # Validate DKIM record
    api_response = api_instance.dkim_validate_create(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DKIMApi->dkim_validate_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data1**](Data1.md)|  | [optional] 

### Return type

[**ResponsesDKIMValidation**](ResponsesDKIMValidation.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

