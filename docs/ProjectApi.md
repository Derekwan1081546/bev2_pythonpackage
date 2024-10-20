# swagger_client.ProjectApi

All URIs are relative to *https://virtserver.swaggerhub.com/ug61837361636/bev2/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_project_create_post**](ProjectApi.md#api_v2_project_create_post) | **POST** /api/v2/project/create | Create Project
[**api_v2_project_delete_post**](ProjectApi.md#api_v2_project_delete_post) | **POST** /api/v2/project/delete | Delete Project
[**api_v2_project_get_post**](ProjectApi.md#api_v2_project_get_post) | **POST** /api/v2/project/get | Get Single Project Information
[**api_v2_project_list_post**](ProjectApi.md#api_v2_project_list_post) | **POST** /api/v2/project/list | List All Projects From User Account
[**api_v2_project_listall_post**](ProjectApi.md#api_v2_project_listall_post) | **POST** /api/v2/project/listall | List All Projects
[**api_v2_project_update_post**](ProjectApi.md#api_v2_project_update_post) | **POST** /api/v2/project/update | Update Project Information

# **api_v2_project_create_post**
> InlineResponse2011 api_v2_project_create_post(body)

Create Project

This API is responsible for creating a new project for AI model training or image generation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectApi()
body = swagger_client.ProjectCreateBody() # ProjectCreateBody | 

try:
    # Create Project
    api_response = api_instance.api_v2_project_create_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->api_v2_project_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectCreateBody**](ProjectCreateBody.md)|  | 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_project_delete_post**
> InlineResponse2004 api_v2_project_delete_post(body)

Delete Project

This API is responsible for deleting a project.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectApi()
body = swagger_client.ProjectDeleteBody() # ProjectDeleteBody | 

try:
    # Delete Project
    api_response = api_instance.api_v2_project_delete_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->api_v2_project_delete_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectDeleteBody**](ProjectDeleteBody.md)|  | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_project_get_post**
> InlineResponse2005 api_v2_project_get_post(body)

Get Single Project Information

This API is responsible for getting the information of a single project.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectApi()
body = swagger_client.ProjectGetBody() # ProjectGetBody | 

try:
    # Get Single Project Information
    api_response = api_instance.api_v2_project_get_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->api_v2_project_get_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectGetBody**](ProjectGetBody.md)|  | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_project_list_post**
> InlineResponse2006 api_v2_project_list_post(body)

List All Projects From User Account

This API is responsible for listing all projects from the user account.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectApi()
body = swagger_client.ProjectListBody() # ProjectListBody | 

try:
    # List All Projects From User Account
    api_response = api_instance.api_v2_project_list_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->api_v2_project_list_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectListBody**](ProjectListBody.md)|  | 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_project_listall_post**
> InlineResponse2007 api_v2_project_listall_post(body)

List All Projects

This API is responsible for listing all project information.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectApi()
body = swagger_client.ProjectListallBody() # ProjectListallBody | 

try:
    # List All Projects
    api_response = api_instance.api_v2_project_listall_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->api_v2_project_listall_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectListallBody**](ProjectListallBody.md)|  | 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_project_update_post**
> InlineResponse2008 api_v2_project_update_post(body)

Update Project Information

This API is responsible for updating various aspects of a project, such as confirming the project status, modifying image generation remaining count, or updating image quantity.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectApi()
body = swagger_client.ProjectUpdateBody() # ProjectUpdateBody | 

try:
    # Update Project Information
    api_response = api_instance.api_v2_project_update_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->api_v2_project_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectUpdateBody**](ProjectUpdateBody.md)|  | 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

