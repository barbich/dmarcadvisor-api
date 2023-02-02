# dmarcadvisor.ReportDataApi

All URIs are relative to *https://eu.dmarcadvisor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aggregate_report_domains_list**](ReportDataApi.md#aggregate_report_domains_list) | **GET** /api/v1/aggregate-report/{search_token}/domains/ | Domains
[**aggregate_report_progress**](ReportDataApi.md#aggregate_report_progress) | **GET** /api/v1/aggregate-report/{search_token}/progress/ | Progress
[**aggregate_report_source_list**](ReportDataApi.md#aggregate_report_source_list) | **GET** /api/v1/aggregate-report/{search_token}/source/{source_number}/ | Source data
[**aggregate_report_sources**](ReportDataApi.md#aggregate_report_sources) | **GET** /api/v1/aggregate-report/{search_token}/sources/ | Sources


# **aggregate_report_domains_list**
> ResponsesQueryJobSourceDomainData aggregate_report_domains_list(search_token, page=page, limit=limit, ordering=ordering, source_number=source_number, ptr_org=ptr_org)

Domains

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.ReportDataApi()
search_token = 'search_token_example' # str | 
page = 56 # int | A page number within the paginated result set. (optional)
limit = 56 # int | Number of results to return per page. (optional)
ordering = 'ordering_example' # str | Default: \"-message_count\".   Valid values: \"message_count\", \"-message_count\",\"from_domain\", \"-from_domain\",\"ip\", \"-ip\",\"ptr\", \"-ptr\",\"reason\", \"-reason\",\"dkim_result\", \"-dkim_result\",\"dkim_policy_result\", \"-dkim_policy_result\",\"spf_result\", \"-spf_result\",\"spf_policy_result\", \"-spf_policy_result\",\"policy_applied\", \"-policy_applied\",\"spf_d\", \"-spf_d\",\"dkim_d\", \"-dkim_d\"    (prefix with \"-\" for descending sort). (optional)
source_number = 'source_number_example' # str | Filter domains data by source. (optional)
ptr_org = 'ptr_org_example' # str | Filter domains data by PTR grouping. (optional)

try:
    # Domains
    api_response = api_instance.aggregate_report_domains_list(search_token, page=page, limit=limit, ordering=ordering, source_number=source_number, ptr_org=ptr_org)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportDataApi->aggregate_report_domains_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_token** | **str**|  | 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **ordering** | **str**| Default: \&quot;-message_count\&quot;.   Valid values: \&quot;message_count\&quot;, \&quot;-message_count\&quot;,\&quot;from_domain\&quot;, \&quot;-from_domain\&quot;,\&quot;ip\&quot;, \&quot;-ip\&quot;,\&quot;ptr\&quot;, \&quot;-ptr\&quot;,\&quot;reason\&quot;, \&quot;-reason\&quot;,\&quot;dkim_result\&quot;, \&quot;-dkim_result\&quot;,\&quot;dkim_policy_result\&quot;, \&quot;-dkim_policy_result\&quot;,\&quot;spf_result\&quot;, \&quot;-spf_result\&quot;,\&quot;spf_policy_result\&quot;, \&quot;-spf_policy_result\&quot;,\&quot;policy_applied\&quot;, \&quot;-policy_applied\&quot;,\&quot;spf_d\&quot;, \&quot;-spf_d\&quot;,\&quot;dkim_d\&quot;, \&quot;-dkim_d\&quot;    (prefix with \&quot;-\&quot; for descending sort). | [optional] 
 **source_number** | **str**| Filter domains data by source. | [optional] 
 **ptr_org** | **str**| Filter domains data by PTR grouping. | [optional] 

### Return type

[**ResponsesQueryJobSourceDomainData**](ResponsesQueryJobSourceDomainData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aggregate_report_progress**
> ResponsesQueryJobProgress aggregate_report_progress(search_token)

Progress

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.ReportDataApi()
search_token = 'search_token_example' # str | 

try:
    # Progress
    api_response = api_instance.aggregate_report_progress(search_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportDataApi->aggregate_report_progress: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_token** | **str**|  | 

### Return type

[**ResponsesQueryJobProgress**](ResponsesQueryJobProgress.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aggregate_report_source_list**
> ResponsesQueryJobSourceData aggregate_report_source_list(source_number, search_token, page=page, limit=limit, search=search, ordering=ordering)

Source data

List given source data, such as messages count, spf, dkim and dmarc information

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.ReportDataApi()
source_number = 'source_number_example' # str | 
search_token = 'search_token_example' # str | 
page = 56 # int | A page number within the paginated result set. (optional)
limit = 56 # int | Number of results to return per page. (optional)
search = 'search_example' # str | Search in fields: \"server_name\"  . (optional)
ordering = 'ordering_example' # str | Default: \"-message_count\".   Valid values: \"message_count\", \"-message_count\",\"server_name\", \"-server_name\",\"ip_count\", \"-ip_count\"    (prefix with \"-\" for descending sort). (optional)

try:
    # Source data
    api_response = api_instance.aggregate_report_source_list(source_number, search_token, page=page, limit=limit, search=search, ordering=ordering)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportDataApi->aggregate_report_source_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_number** | **str**|  | 
 **search_token** | **str**|  | 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| Search in fields: \&quot;server_name\&quot;  . | [optional] 
 **ordering** | **str**| Default: \&quot;-message_count\&quot;.   Valid values: \&quot;message_count\&quot;, \&quot;-message_count\&quot;,\&quot;server_name\&quot;, \&quot;-server_name\&quot;,\&quot;ip_count\&quot;, \&quot;-ip_count\&quot;    (prefix with \&quot;-\&quot; for descending sort). | [optional] 

### Return type

[**ResponsesQueryJobSourceData**](ResponsesQueryJobSourceData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aggregate_report_sources**
> ResponsesQueryJobSources aggregate_report_sources(search_token)

Sources

List report sources in 4 categories - dmarc capable, non compliant, forwarders, unknown.

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.ReportDataApi()
search_token = 'search_token_example' # str | 

try:
    # Sources
    api_response = api_instance.aggregate_report_sources(search_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportDataApi->aggregate_report_sources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_token** | **str**|  | 

### Return type

[**ResponsesQueryJobSources**](ResponsesQueryJobSources.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

