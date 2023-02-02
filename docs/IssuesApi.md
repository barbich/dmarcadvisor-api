# dmarcadvisor.IssuesApi

All URIs are relative to *https://eu.dmarcadvisor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**issues_list**](IssuesApi.md#issues_list) | **GET** /api/v1/issues/ | List issues
[**issues_partial_update**](IssuesApi.md#issues_partial_update) | **PATCH** /api/v1/issues/{id}/ | Update issue (partial)
[**issues_read**](IssuesApi.md#issues_read) | **GET** /api/v1/issues/{id}/ | Get issue
[**issues_update**](IssuesApi.md#issues_update) | **PUT** /api/v1/issues/{id}/ | Update issue


# **issues_list**
> ResponsesIssueList issues_list(page=page, limit=limit, group_id=group_id, top_level=top_level, solved=solved, ignored=ignored, domain_state=domain_state, assigned_to_group=assigned_to_group, domain=domain)

List issues

Lists all domain issues discovered for the account.

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.IssuesApi()
page = 56 # int | A page number within the paginated result set. (optional)
limit = 56 # int | Number of results to return per page. (optional)
group_id = 8.14 # float | Filter results by domains belonging to the group id. (optional)
top_level = 'top_level_example' # str | Show issues for domains treated as top level (True) or for subdomains (False). (optional)
solved = 'solved_example' # str | Show solved issues (True) or not (False). (optional)
ignored = 'ignored_example' # str | Show ignored issues (True) or not (False). (optional)
domain_state = 'domain_state_example' # str | Filter results by domain state (\"active\", \"inactive\", \"unknown\"). (optional)
assigned_to_group = 'assigned_to_group_example' # str | Filter results by domains assigned to a group (different than the default one). (optional)
domain = 'domain_example' # str | Filter results by domain. (optional)

try:
    # List issues
    api_response = api_instance.issues_list(page=page, limit=limit, group_id=group_id, top_level=top_level, solved=solved, ignored=ignored, domain_state=domain_state, assigned_to_group=assigned_to_group, domain=domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssuesApi->issues_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **group_id** | **float**| Filter results by domains belonging to the group id. | [optional] 
 **top_level** | **str**| Show issues for domains treated as top level (True) or for subdomains (False). | [optional] 
 **solved** | **str**| Show solved issues (True) or not (False). | [optional] 
 **ignored** | **str**| Show ignored issues (True) or not (False). | [optional] 
 **domain_state** | **str**| Filter results by domain state (\&quot;active\&quot;, \&quot;inactive\&quot;, \&quot;unknown\&quot;). | [optional] 
 **assigned_to_group** | **str**| Filter results by domains assigned to a group (different than the default one). | [optional] 
 **domain** | **str**| Filter results by domain. | [optional] 

### Return type

[**ResponsesIssueList**](ResponsesIssueList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issues_partial_update**
> ResponsesIssue issues_partial_update(id, data=data)

Update issue (partial)

Updates some of the issue properties.

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.IssuesApi()
id = 'id_example' # str | 
data = dmarcadvisor.Data19() # Data19 |  (optional)

try:
    # Update issue (partial)
    api_response = api_instance.issues_partial_update(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssuesApi->issues_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Data19**](Data19.md)|  | [optional] 

### Return type

[**ResponsesIssue**](ResponsesIssue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issues_read**
> ResponsesIssue issues_read(id)

Get issue

Retrieves issue details.

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.IssuesApi()
id = 'id_example' # str | 

try:
    # Get issue
    api_response = api_instance.issues_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssuesApi->issues_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponsesIssue**](ResponsesIssue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issues_update**
> ResponsesIssue issues_update(id, data=data)

Update issue

Updates issue properties.

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.IssuesApi()
id = 'id_example' # str | 
data = dmarcadvisor.Data18() # Data18 |  (optional)

try:
    # Update issue
    api_response = api_instance.issues_update(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssuesApi->issues_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Data18**](Data18.md)|  | [optional] 

### Return type

[**ResponsesIssue**](ResponsesIssue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

