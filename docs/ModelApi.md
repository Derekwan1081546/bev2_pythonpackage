# swagger_client.ModelApi

All URIs are relative to *https://virtserver.swaggerhub.com/ug61837361636/bev2/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_model_delete_post**](ModelApi.md#api_v2_model_delete_post) | **POST** /api/v2/model/delete | Delete Model
[**api_v2_model_download_post**](ModelApi.md#api_v2_model_download_post) | **POST** /api/v2/model/download | Download Model
[**api_v2_model_get_post**](ModelApi.md#api_v2_model_get_post) | **POST** /api/v2/model/get | Get Model Information
[**api_v2_model_list_post**](ModelApi.md#api_v2_model_list_post) | **POST** /api/v2/model/list | List Models
[**api_v2_model_upload_post**](ModelApi.md#api_v2_model_upload_post) | **POST** /api/v2/model/upload | Upload Model

# **api_v2_model_delete_post**
> InlineResponse20015 api_v2_model_delete_post(body)

Delete Model

This API is responsible for deleting a specific model associated with a project.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ModelApi()
body = swagger_client.ModelDeleteBody() # ModelDeleteBody | 

try:
    # Delete Model
    api_response = api_instance.api_v2_model_delete_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->api_v2_model_delete_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModelDeleteBody**](ModelDeleteBody.md)|  | 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_model_download_post**
> str api_v2_model_download_post(body)

Download Model

This API is responsible for downloading a specific model associated with a project.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ModelApi()
body = swagger_client.ModelDownloadBody() # ModelDownloadBody | 

try:
    # Download Model
    api_response = api_instance.api_v2_model_download_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->api_v2_model_download_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModelDownloadBody**](ModelDownloadBody.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_model_get_post**
> InlineResponse20016 api_v2_model_get_post(body)

Get Model Information

This API is responsible for retrieving model information for a specific project.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ModelApi()
body = swagger_client.ModelGetBody() # ModelGetBody | 

try:
    # Get Model Information
    api_response = api_instance.api_v2_model_get_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->api_v2_model_get_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModelGetBody**](ModelGetBody.md)|  | 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_model_list_post**
> InlineResponse20017 api_v2_model_list_post(body)

List Models

This API is responsible for listing all models associated with a specific project.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ModelApi()
body = swagger_client.ModelListBody() # ModelListBody | 

try:
    # List Models
    api_response = api_instance.api_v2_model_list_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->api_v2_model_list_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModelListBody**](ModelListBody.md)|  | 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_model_upload_post**
> InlineResponse2013 api_v2_model_upload_post(token, username, projectname, model)

Upload Model

This API is responsible for uploading a model file to a specific project for inference or training.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ModelApi()
token = 'token_example' # str | 
username = 'username_example' # str | 
projectname = 'projectname_example' # str | 
model = 'model_example' # str | 

try:
    # Upload Model
    api_response = api_instance.api_v2_model_upload_post(token, username, projectname, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->api_v2_model_upload_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **username** | **str**|  | 
 **projectname** | **str**|  | 
 **model** | **str**|  | 

### Return type

[**InlineResponse2013**](InlineResponse2013.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

