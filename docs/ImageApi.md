# swagger_client.ImageApi

All URIs are relative to *https://virtserver.swaggerhub.com/ug61837361636/bev2/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_image_delete_post**](ImageApi.md#api_v2_image_delete_post) | **POST** /api/v2/image/delete | Delete Image Information
[**api_v2_image_feedbackinfo_post**](ImageApi.md#api_v2_image_feedbackinfo_post) | **POST** /api/v2/image/feedbackinfo | Update Image Feedback Information
[**api_v2_image_get_post**](ImageApi.md#api_v2_image_get_post) | **POST** /api/v2/image/get | Get Image Information
[**api_v2_image_getrequirement_post**](ImageApi.md#api_v2_image_getrequirement_post) | **POST** /api/v2/image/getrequirement | Get Project Requirement Information
[**api_v2_image_list_post**](ImageApi.md#api_v2_image_list_post) | **POST** /api/v2/image/list | List Images in a Project
[**api_v2_image_requirement_post**](ImageApi.md#api_v2_image_requirement_post) | **POST** /api/v2/image/requirement | Upload Project Requirement
[**api_v2_image_upload_post**](ImageApi.md#api_v2_image_upload_post) | **POST** /api/v2/image/upload | Upload Image

# **api_v2_image_delete_post**
> InlineResponse2009 api_v2_image_delete_post(body)

Delete Image Information

This API is responsible for deleting image information.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImageApi()
body = swagger_client.ImageDeleteBody() # ImageDeleteBody | 

try:
    # Delete Image Information
    api_response = api_instance.api_v2_image_delete_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->api_v2_image_delete_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImageDeleteBody**](ImageDeleteBody.md)|  | 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_image_feedbackinfo_post**
> InlineResponse20012 api_v2_image_feedbackinfo_post(body)

Update Image Feedback Information

This API is responsible for updating the feedback information of an image in a project.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImageApi()
body = swagger_client.ImageFeedbackinfoBody() # ImageFeedbackinfoBody | 

try:
    # Update Image Feedback Information
    api_response = api_instance.api_v2_image_feedbackinfo_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->api_v2_image_feedbackinfo_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImageFeedbackinfoBody**](ImageFeedbackinfoBody.md)|  | 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_image_get_post**
> InlineResponse20010 api_v2_image_get_post(body)

Get Image Information

This API is responsible for retrieving image information for a given project.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImageApi()
body = swagger_client.ImageGetBody() # ImageGetBody | 

try:
    # Get Image Information
    api_response = api_instance.api_v2_image_get_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->api_v2_image_get_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImageGetBody**](ImageGetBody.md)|  | 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_image_getrequirement_post**
> InlineResponse20014 api_v2_image_getrequirement_post(body)

Get Project Requirement Information

This API is responsible for retrieving the requirement information for a specific project.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImageApi()
body = swagger_client.ImageGetrequirementBody() # ImageGetrequirementBody | 

try:
    # Get Project Requirement Information
    api_response = api_instance.api_v2_image_getrequirement_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->api_v2_image_getrequirement_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImageGetrequirementBody**](ImageGetrequirementBody.md)|  | 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_image_list_post**
> InlineResponse20011 api_v2_image_list_post(body)

List Images in a Project

This API is responsible for listing the paths of all images stored in a specific project.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImageApi()
body = swagger_client.ImageListBody() # ImageListBody | 

try:
    # List Images in a Project
    api_response = api_instance.api_v2_image_list_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->api_v2_image_list_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImageListBody**](ImageListBody.md)|  | 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_image_requirement_post**
> InlineResponse20013 api_v2_image_requirement_post(body)

Upload Project Requirement

This API is responsible for uploading the project requirements for a specific project.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImageApi()
body = swagger_client.ImageRequirementBody() # ImageRequirementBody | 

try:
    # Upload Project Requirement
    api_response = api_instance.api_v2_image_requirement_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->api_v2_image_requirement_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImageRequirementBody**](ImageRequirementBody.md)|  | 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_image_upload_post**
> InlineResponse2012 api_v2_image_upload_post(token, username, projectname, type, image)

Upload Image

This API is responsible for uploading an image to S3 and optionally use it for feedback or inference.. There are two types of uploads including general image upload (type can be empty) and feedback image upload (type is \"feedback\").

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImageApi()
token = 'token_example' # str | 
username = 'username_example' # str | 
projectname = 'projectname_example' # str | 
type = 'type_example' # str | 
image = 'image_example' # str | 

try:
    # Upload Image
    api_response = api_instance.api_v2_image_upload_post(token, username, projectname, type, image)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->api_v2_image_upload_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **username** | **str**|  | 
 **projectname** | **str**|  | 
 **type** | **str**|  | 
 **image** | **str**|  | 

### Return type

[**InlineResponse2012**](InlineResponse2012.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

