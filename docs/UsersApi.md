# dmarcadvisor.UsersApi

All URIs are relative to *https://eu.dmarcadvisor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_activation_reminder**](UsersApi.md#users_activation_reminder) | **POST** /api/v1/users/{id}/activation-reminder/ | Send an email activation reminder
[**users_convert_to_sso**](UsersApi.md#users_convert_to_sso) | **PUT** /api/v1/users/{id}/convert-to-sso/ | Convert an user to SSO login
[**users_create**](UsersApi.md#users_create) | **POST** /api/v1/users/ | Create and add a new user to an account
[**users_delete**](UsersApi.md#users_delete) | **DELETE** /api/v1/users/{id}/ | Delete an user
[**users_list**](UsersApi.md#users_list) | **GET** /api/v1/users/ | Get a list of all users within an account
[**users_partial_update**](UsersApi.md#users_partial_update) | **PATCH** /api/v1/users/{id}/ | Partial update of user details
[**users_password_change**](UsersApi.md#users_password_change) | **POST** /api/v1/users/{id}/password-change/ | Change user password
[**users_password_reset**](UsersApi.md#users_password_reset) | **POST** /api/v1/users/{id}/password-reset/ | Send password reset email
[**users_read**](UsersApi.md#users_read) | **GET** /api/v1/users/{id}/ | Get user details
[**users_update**](UsersApi.md#users_update) | **PUT** /api/v1/users/{id}/ | Update user details


# **users_activation_reminder**
> users_activation_reminder(id)

Send an email activation reminder

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.UsersApi()
id = 'id_example' # str | 

try:
    # Send an email activation reminder
    api_instance.users_activation_reminder(id)
except ApiException as e:
    print("Exception when calling UsersApi->users_activation_reminder: %s\n" % e)
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

# **users_convert_to_sso**
> ResponsesUser users_convert_to_sso(id)

Convert an user to SSO login

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.UsersApi()
id = 'id_example' # str | 

try:
    # Convert an user to SSO login
    api_response = api_instance.users_convert_to_sso(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_convert_to_sso: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponsesUser**](ResponsesUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_create**
> ResponsesUser users_create(data=data)

Create and add a new user to an account

An email with an activation list is send upon each user creation. Note, the user must click through the link in order to activate the account.

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.UsersApi()
data = dmarcadvisor.Data24() # Data24 |  (optional)

try:
    # Create and add a new user to an account
    api_response = api_instance.users_create(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data24**](Data24.md)|  | [optional] 

### Return type

[**ResponsesUser**](ResponsesUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_delete**
> users_delete(id)

Delete an user

Note, account owner could not be deleted.

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.UsersApi()
id = 'id_example' # str | 

try:
    # Delete an user
    api_instance.users_delete(id)
except ApiException as e:
    print("Exception when calling UsersApi->users_delete: %s\n" % e)
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

# **users_list**
> ResponsesUserList users_list(page=page, limit=limit, username=username, email=email, ordering=ordering)

Get a list of all users within an account

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.UsersApi()
page = 56 # int | A page number within the paginated result set. (optional)
limit = 56 # int | Number of results to return per page. (optional)
username = 'username_example' # str | Filter users by username. (optional)
email = 'email_example' # str | Filter users by email address. (optional)
ordering = 'ordering_example' # str | Default: \"\".   Valid values: \"username\", \"-username\",\"email\", \"-email\"    (prefix with \"-\" for descending sort). (optional)

try:
    # Get a list of all users within an account
    api_response = api_instance.users_list(page=page, limit=limit, username=username, email=email, ordering=ordering)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **username** | **str**| Filter users by username. | [optional] 
 **email** | **str**| Filter users by email address. | [optional] 
 **ordering** | **str**| Default: \&quot;\&quot;.   Valid values: \&quot;username\&quot;, \&quot;-username\&quot;,\&quot;email\&quot;, \&quot;-email\&quot;    (prefix with \&quot;-\&quot; for descending sort). | [optional] 

### Return type

[**ResponsesUserList**](ResponsesUserList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_partial_update**
> ResponsesUser users_partial_update(id, data=data)

Partial update of user details

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.UsersApi()
id = 'id_example' # str | 
data = dmarcadvisor.Data26() # Data26 |  (optional)

try:
    # Partial update of user details
    api_response = api_instance.users_partial_update(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Data26**](Data26.md)|  | [optional] 

### Return type

[**ResponsesUser**](ResponsesUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_password_change**
> users_password_change(id, data=data)

Change user password

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.UsersApi()
id = 'id_example' # str | 
data = dmarcadvisor.Data27() # Data27 |  (optional)

try:
    # Change user password
    api_instance.users_password_change(id, data=data)
except ApiException as e:
    print("Exception when calling UsersApi->users_password_change: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Data27**](Data27.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_password_reset**
> users_password_reset(id)

Send password reset email

Sends an email to the user that can trigger a password reset.

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.UsersApi()
id = 'id_example' # str | 

try:
    # Send password reset email
    api_instance.users_password_reset(id)
except ApiException as e:
    print("Exception when calling UsersApi->users_password_reset: %s\n" % e)
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

# **users_read**
> ResponsesUser users_read(id)

Get user details

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.UsersApi()
id = 'id_example' # str | 

try:
    # Get user details
    api_response = api_instance.users_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponsesUser**](ResponsesUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_update**
> ResponsesUser users_update(id, data=data)

Update user details

Every email change request  triggers an email confirmation. Note, there is a separate endpoint for password changes, see \"Change user password\".

### Example
```python
from __future__ import print_function
import time
import dmarcadvisor
from dmarcadvisor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dmarcadvisor.UsersApi()
id = 'id_example' # str | 
data = dmarcadvisor.Data25() # Data25 |  (optional)

try:
    # Update user details
    api_response = api_instance.users_update(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Data25**](Data25.md)|  | [optional] 

### Return type

[**ResponsesUser**](ResponsesUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

