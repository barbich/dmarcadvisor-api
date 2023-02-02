# dmarcadvisor.TasksApi

All URIs are relative to *https://eu.dmarcadvisor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tasks_list**](TasksApi.md#tasks_list) | **GET** /api/v1/tasks/ | List tasks
[**tasks_partial_update**](TasksApi.md#tasks_partial_update) | **PATCH** /api/v1/tasks/{id}/ | Update task (partial)
[**tasks_read**](TasksApi.md#tasks_read) | **GET** /api/v1/tasks/{id}/ | Get task
[**tasks_update**](TasksApi.md#tasks_update) | **PUT** /api/v1/tasks/{id}/ | Update task


# **tasks_list**
> ResponsesTaskList tasks_list(page=page, limit=limit, group_id=group_id, top_level=top_level, solved=solved, ignored=ignored, domain_state=domain_state, assigned_to_group=assigned_to_group, domain=domain)

List tasks

Lists all domain tasks generated for the account.

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.TasksApi()
page = 56 # int | A page number within the paginated result set. (optional)
limit = 56 # int | Number of results to return per page. (optional)
group_id = 8.14 # float | Filter results by domains belonging to the group id. (optional)
top_level = 'top_level_example' # str | Show tasks for domains treated as top level (True) or for subdomains (False). (optional)
solved = 'solved_example' # str | Show solved tasks (True) or not (False). (optional)
ignored = 'ignored_example' # str | Show ignored tasks (True) or not (False). (optional)
domain_state = 'domain_state_example' # str | Filter results by domain state (\"active\", \"inactive\", \"unknown\"). (optional)
assigned_to_group = 'assigned_to_group_example' # str | Filter results by domains assigned to a group (different than the default one). (optional)
domain = 'domain_example' # str | Filter results by domain. (optional)

try:
    # List tasks
    api_response = api_instance.tasks_list(page=page, limit=limit, group_id=group_id, top_level=top_level, solved=solved, ignored=ignored, domain_state=domain_state, assigned_to_group=assigned_to_group, domain=domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->tasks_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **group_id** | **float**| Filter results by domains belonging to the group id. | [optional] 
 **top_level** | **str**| Show tasks for domains treated as top level (True) or for subdomains (False). | [optional] 
 **solved** | **str**| Show solved tasks (True) or not (False). | [optional] 
 **ignored** | **str**| Show ignored tasks (True) or not (False). | [optional] 
 **domain_state** | **str**| Filter results by domain state (\&quot;active\&quot;, \&quot;inactive\&quot;, \&quot;unknown\&quot;). | [optional] 
 **assigned_to_group** | **str**| Filter results by domains assigned to a group (different than the default one). | [optional] 
 **domain** | **str**| Filter results by domain. | [optional] 

### Return type

[**ResponsesTaskList**](ResponsesTaskList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_partial_update**
> ResponsesTask tasks_partial_update(id, data=data)

Update task (partial)

Updates some of the task properties.

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.TasksApi()
id = 'id_example' # str | 
data = dmarcadvisor.Data23() # Data23 |  (optional)

try:
    # Update task (partial)
    api_response = api_instance.tasks_partial_update(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->tasks_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Data23**](Data23.md)|  | [optional] 

### Return type

[**ResponsesTask**](ResponsesTask.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_read**
> ResponsesTask tasks_read(id)

Get task

Retrieves task details.

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.TasksApi()
id = 'id_example' # str | 

try:
    # Get task
    api_response = api_instance.tasks_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->tasks_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponsesTask**](ResponsesTask.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_update**
> ResponsesTask tasks_update(id, data=data)

Update task

Updates task properties.

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.TasksApi()
id = 'id_example' # str | 
data = dmarcadvisor.Data22() # Data22 |  (optional)

try:
    # Update task
    api_response = api_instance.tasks_update(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->tasks_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Data22**](Data22.md)|  | [optional] 

### Return type

[**ResponsesTask**](ResponsesTask.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

