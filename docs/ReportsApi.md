# dmarcadvisor.ReportsApi

All URIs are relative to *https://eu.dmarcadvisor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**detail_viewer_create**](ReportsApi.md#detail_viewer_create) | **POST** /api/v1/detail-viewer/ | Create Detail Viewer report
[**detail_viewer_list**](ReportsApi.md#detail_viewer_list) | **GET** /api/v1/detail-viewer/ | List Detail Viewer reports
[**detail_viewer_read**](ReportsApi.md#detail_viewer_read) | **GET** /api/v1/detail-viewer/{search_token}/ | List/create Detail Viewer reports.


# **detail_viewer_create**
> ResponsesQueryJob detail_viewer_create(data=data)

Create Detail Viewer report

Report creation is asynchronous process. In case report already exists for the given input, response status code is 200. If report creation is started, then 202 is returned. While report is being prepared, only available call is to check its progress (available in \"_links\"). Progress endpoint must be called on certain time interval. When progress value become 100 %, report is ready and its data could be retrieved. Any calls to report data before it is ready will return 404 Not found.

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.ReportsApi()
data = dmarcadvisor.Data2() # Data2 |  (optional)

try:
    # Create Detail Viewer report
    api_response = api_instance.detail_viewer_create(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->detail_viewer_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data2**](Data2.md)|  | [optional] 

### Return type

[**ResponsesQueryJob**](ResponsesQueryJob.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detail_viewer_list**
> ResponsesQueryJobList detail_viewer_list(page=page, limit=limit, ordering=ordering)

List Detail Viewer reports

List current user`s Detail Viewer reports. Each report availability is up to 3 days.

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.ReportsApi()
page = 56 # int | A page number within the paginated result set. (optional)
limit = 56 # int | Number of results to return per page. (optional)
ordering = 'ordering_example' # str | Default: \"-created\".   Valid values: \"created\", \"-created\"    (prefix with \"-\" for descending sort). (optional)

try:
    # List Detail Viewer reports
    api_response = api_instance.detail_viewer_list(page=page, limit=limit, ordering=ordering)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->detail_viewer_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **ordering** | **str**| Default: \&quot;-created\&quot;.   Valid values: \&quot;created\&quot;, \&quot;-created\&quot;    (prefix with \&quot;-\&quot; for descending sort). | [optional] 

### Return type

[**ResponsesQueryJobList**](ResponsesQueryJobList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detail_viewer_read**
> detail_viewer_read(search_token)

List/create Detail Viewer reports.

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.ReportsApi()
search_token = 'search_token_example' # str | 

try:
    # List/create Detail Viewer reports.
    api_instance.detail_viewer_read(search_token)
except ApiException as e:
    print("Exception when calling ReportsApi->detail_viewer_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_token** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

