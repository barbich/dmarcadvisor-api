# dmarcadvisor.DomainsApi

All URIs are relative to *https://eu.dmarcadvisor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**domains_delete0**](DomainsApi.md#domains_delete0) | **DELETE** /api/v1/domains/{id}/ | Delete domain
[**domains_list**](DomainsApi.md#domains_list) | **GET** /api/v1/domains/ | List domains
[**domains_partial_update**](DomainsApi.md#domains_partial_update) | **PATCH** /api/v1/domains/{id}/ | Update domain (partial)
[**domains_read**](DomainsApi.md#domains_read) | **GET** /api/v1/domains/{id}/ | Get domain
[**domains_refresh**](DomainsApi.md#domains_refresh) | **POST** /api/v1/domains/{id}/refresh/ | Refresh domain
[**domains_update**](DomainsApi.md#domains_update) | **PUT** /api/v1/domains/{id}/ | Update domain
[**domains_verify**](DomainsApi.md#domains_verify) | **POST** /api/v1/domains/{id}/verify/ | Verify domain


# **domains_delete0**
> domains_delete0(id)

Delete domain

Deletes the domain and all related data.

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.DomainsApi()
id = 'id_example' # str | 

try:
    # Delete domain
    api_instance.domains_delete0(id)
except ApiException as e:
    print("Exception when calling DomainsApi->domains_delete0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domains_list**
> ResponsesDomainList domains_list(page=page, limit=limit, ordering=ordering, ordering2=ordering2, domain=domain, group_id=group_id, assigned=assigned, treat_as_top_level=treat_as_top_level, parent_id=parent_id, domain_state=domain_state)

List domains

Lists domains the current user has access to.

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.DomainsApi()
page = 56 # int | A page number within the paginated result set. (optional)
limit = 56 # int | Number of results to return per page. (optional)
ordering = 'ordering_example' # str | Default: \"\".   Valid values: \"domain\", \"-domain\",\"volume\", \"-volume\",\"count_threat_other\", \"-count_threat_other\",\"state_dmarc\", \"-state_dmarc\",\"state_spf\", \"-state_spf\",\"state_dkim\", \"-state_dkim\",\"mx_txt\", \"-mx_txt\",\"soa_txt\", \"-soa_txt\"    (prefix with \"-\" for descending sort). (optional)
ordering2 = 'ordering_example' # str | Default: \"\".   Valid values: \"domain\", \"-domain\",\"volume\", \"-volume\",\"count_threat_other\", \"-count_threat_other\",\"state_dmarc\", \"-state_dmarc\",\"state_spf\", \"-state_spf\",\"state_dkim\", \"-state_dkim\",\"mx_txt\", \"-mx_txt\",\"soa_txt\", \"-soa_txt\"    (prefix with \"-\" for descending sort). (optional)
domain = 'domain_example' # str | Filter results by domain name. (optional)
group_id = 8.14 # float | Filter results by group id. (optional)
assigned = 'assigned_example' # str | Show domains belonging to a group (True) or domains from the default group (False). (optional)
treat_as_top_level = 'treat_as_top_level_example' # str | Show domains treated as top level (True) or subdomains (False). (optional)
parent_id = 8.14 # float | Filter subdomains by their parent domain id. (optional)
domain_state = 'domain_state_example' # str | Filter results by domain state (\"active\", \"inactive\", \"unknown\"). (optional)

try:
    # List domains
    api_response = api_instance.domains_list(page=page, limit=limit, ordering=ordering, ordering2=ordering2, domain=domain, group_id=group_id, assigned=assigned, treat_as_top_level=treat_as_top_level, parent_id=parent_id, domain_state=domain_state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->domains_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **ordering** | **str**| Default: \&quot;\&quot;.   Valid values: \&quot;domain\&quot;, \&quot;-domain\&quot;,\&quot;volume\&quot;, \&quot;-volume\&quot;,\&quot;count_threat_other\&quot;, \&quot;-count_threat_other\&quot;,\&quot;state_dmarc\&quot;, \&quot;-state_dmarc\&quot;,\&quot;state_spf\&quot;, \&quot;-state_spf\&quot;,\&quot;state_dkim\&quot;, \&quot;-state_dkim\&quot;,\&quot;mx_txt\&quot;, \&quot;-mx_txt\&quot;,\&quot;soa_txt\&quot;, \&quot;-soa_txt\&quot;    (prefix with \&quot;-\&quot; for descending sort). | [optional] 
 **ordering2** | **str**| Default: \&quot;\&quot;.   Valid values: \&quot;domain\&quot;, \&quot;-domain\&quot;,\&quot;volume\&quot;, \&quot;-volume\&quot;,\&quot;count_threat_other\&quot;, \&quot;-count_threat_other\&quot;,\&quot;state_dmarc\&quot;, \&quot;-state_dmarc\&quot;,\&quot;state_spf\&quot;, \&quot;-state_spf\&quot;,\&quot;state_dkim\&quot;, \&quot;-state_dkim\&quot;,\&quot;mx_txt\&quot;, \&quot;-mx_txt\&quot;,\&quot;soa_txt\&quot;, \&quot;-soa_txt\&quot;    (prefix with \&quot;-\&quot; for descending sort). | [optional] 
 **domain** | **str**| Filter results by domain name. | [optional] 
 **group_id** | **float**| Filter results by group id. | [optional] 
 **assigned** | **str**| Show domains belonging to a group (True) or domains from the default group (False). | [optional] 
 **treat_as_top_level** | **str**| Show domains treated as top level (True) or subdomains (False). | [optional] 
 **parent_id** | **float**| Filter subdomains by their parent domain id. | [optional] 
 **domain_state** | **str**| Filter results by domain state (\&quot;active\&quot;, \&quot;inactive\&quot;, \&quot;unknown\&quot;). | [optional] 

### Return type

[**ResponsesDomainList**](ResponsesDomainList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domains_partial_update**
> ResponsesDomain domains_partial_update(id, data=data)

Update domain (partial)

Updates some of the domain properties.

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.DomainsApi()
id = 'id_example' # str | 
data = dmarcadvisor.Data15() # Data15 |  (optional)

try:
    # Update domain (partial)
    api_response = api_instance.domains_partial_update(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->domains_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Data15**](Data15.md)|  | [optional] 

### Return type

[**ResponsesDomain**](ResponsesDomain.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domains_read**
> ResponsesDomain domains_read(id)

Get domain

Retrieves specific domain details.

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.DomainsApi()
id = 'id_example' # str | 

try:
    # Get domain
    api_response = api_instance.domains_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->domains_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponsesDomain**](ResponsesDomain.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domains_refresh**
> ResponsesDomain domains_refresh(id)

Refresh domain

Refreshes domain's statistics.

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.DomainsApi()
id = 'id_example' # str | 

try:
    # Refresh domain
    api_response = api_instance.domains_refresh(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->domains_refresh: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponsesDomain**](ResponsesDomain.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domains_update**
> ResponsesDomain domains_update(id, data=data)

Update domain

Updates domain properties.

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.DomainsApi()
id = 'id_example' # str | 
data = dmarcadvisor.Data14() # Data14 |  (optional)

try:
    # Update domain
    api_response = api_instance.domains_update(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->domains_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Data14**](Data14.md)|  | [optional] 

### Return type

[**ResponsesDomain**](ResponsesDomain.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domains_verify**
> domains_verify(id, data=data)

Verify domain

Initiates a probe to verify this domain

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.DomainsApi()
id = 'id_example' # str | 
data = dmarcadvisor.Data16() # Data16 |  (optional)

try:
    # Verify domain
    api_instance.domains_verify(id, data=data)
except ApiException as e:
    print("Exception when calling DomainsApi->domains_verify: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Data16**](Data16.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

