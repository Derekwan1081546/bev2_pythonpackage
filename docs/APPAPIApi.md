# swagger_client.APPAPIApi

All URIs are relative to *https://virtserver.swaggerhub.com/ug61837361636/bev2/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_download_image_origin_post**](APPAPIApi.md#api_v1_download_image_origin_post) | **POST** /api/v1/downloadImageOrigin | Download Original Image from S3
[**api_v1_download_image_post**](APPAPIApi.md#api_v1_download_image_post) | **POST** /api/v1/downloadImage | Download Image After Inference
[**api_v1_feedback_post**](APPAPIApi.md#api_v1_feedback_post) | **POST** /api/v1/feedback | Model Inference Feedback
[**api_v1_get_model_list_post**](APPAPIApi.md#api_v1_get_model_list_post) | **POST** /api/v1/getModelList | Get Model List from RDS and S3
[**api_v1_get_model_post**](APPAPIApi.md#api_v1_get_model_post) | **POST** /api/v1/getModel | Download Model from RDS and S3
[**api_v1_remote_inference_by_id_post**](APPAPIApi.md#api_v1_remote_inference_by_id_post) | **POST** /api/v1/remoteInferenceById | Run Inference on Image by ID
[**api_v1_style_transform_post**](APPAPIApi.md#api_v1_style_transform_post) | **POST** /api/v1/styleTransform | Style Transform for Image
[**api_v1_upload_image_post**](APPAPIApi.md#api_v1_upload_image_post) | **POST** /api/v1/uploadImage | Upload Image for Inference or Dataset

# **api_v1_download_image_origin_post**
> str api_v1_download_image_origin_post(body)

Download Original Image from S3

This API is responsible for downloading the original images stored in S3.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APPAPIApi()
body = swagger_client.V1DownloadImageOriginBody() # V1DownloadImageOriginBody | 

try:
    # Download Original Image from S3
    api_response = api_instance.api_v1_download_image_origin_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APPAPIApi->api_v1_download_image_origin_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DownloadImageOriginBody**](V1DownloadImageOriginBody.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_download_image_post**
> str api_v1_download_image_post(body)

Download Image After Inference

This API is responsible for downloading images after inference from S3 storage.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APPAPIApi()
body = swagger_client.V1DownloadImageBody() # V1DownloadImageBody | 

try:
    # Download Image After Inference
    api_response = api_instance.api_v1_download_image_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APPAPIApi->api_v1_download_image_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DownloadImageBody**](V1DownloadImageBody.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_feedback_post**
> InlineResponse20027 api_v1_feedback_post(body)

Model Inference Feedback

This API is responsible for providing feedback on model inference. Users can label objects on images and send the label information to the server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APPAPIApi()
body = swagger_client.V1FeedbackBody() # V1FeedbackBody | 

try:
    # Model Inference Feedback
    api_response = api_instance.api_v1_feedback_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APPAPIApi->api_v1_feedback_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1FeedbackBody**](V1FeedbackBody.md)|  | 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_get_model_list_post**
> InlineResponse20030 api_v1_get_model_list_post(body)

Get Model List from RDS and S3

This API is responsible for getting the list of available models stored in both RDS and S3.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APPAPIApi()
body = swagger_client.V1GetModelListBody() # V1GetModelListBody | 

try:
    # Get Model List from RDS and S3
    api_response = api_instance.api_v1_get_model_list_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APPAPIApi->api_v1_get_model_list_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1GetModelListBody**](V1GetModelListBody.md)|  | 

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_get_model_post**
> str api_v1_get_model_post(body)

Download Model from RDS and S3

This API is responsible for downloading a model stored in RDS or S3.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APPAPIApi()
body = swagger_client.V1GetModelBody() # V1GetModelBody | 

try:
    # Download Model from RDS and S3
    api_response = api_instance.api_v1_get_model_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APPAPIApi->api_v1_get_model_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1GetModelBody**](V1GetModelBody.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_remote_inference_by_id_post**
> InlineResponse20029 api_v1_remote_inference_by_id_post(body)

Run Inference on Image by ID

This API is responsible for running inference on images that are saved in S3. Images must be uploaded using the `imageUpload` API first.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APPAPIApi()
body = swagger_client.V1RemoteInferenceByIdBody() # V1RemoteInferenceByIdBody | 

try:
    # Run Inference on Image by ID
    api_response = api_instance.api_v1_remote_inference_by_id_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APPAPIApi->api_v1_remote_inference_by_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1RemoteInferenceByIdBody**](V1RemoteInferenceByIdBody.md)|  | 

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_style_transform_post**
> InlineResponse20028 api_v1_style_transform_post(access_token, file, transform_style, device_info)

Style Transform for Image

This API is responsible for uploading images to run inference with style transformation. Users can apply different styles such as \"Pixart\" or \"RealTek\" to an image.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APPAPIApi()
access_token = 'access_token_example' # str | 
file = 'file_example' # str | 
transform_style = 'transform_style_example' # str | 
device_info = 'device_info_example' # str | 

try:
    # Style Transform for Image
    api_response = api_instance.api_v1_style_transform_post(access_token, file, transform_style, device_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APPAPIApi->api_v1_style_transform_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**|  | 
 **file** | **str**|  | 
 **transform_style** | **str**|  | 
 **device_info** | **str**|  | 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_upload_image_post**
> InlineResponse20026 api_v1_upload_image_post(access_token, original_image_file, purpose, device_info, label_info, description)

Upload Image for Inference or Dataset

This API is responsible for uploading images to run inference or store as a dataset. The image will be saved to S3, and its metadata will be inserted into the RDS image table.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APPAPIApi()
access_token = 'access_token_example' # str | 
original_image_file = 'original_image_file_example' # str | 
purpose = 'purpose_example' # str | 
device_info = 'device_info_example' # str | 
label_info = 'label_info_example' # str | 
description = 'description_example' # str | 

try:
    # Upload Image for Inference or Dataset
    api_response = api_instance.api_v1_upload_image_post(access_token, original_image_file, purpose, device_info, label_info, description)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APPAPIApi->api_v1_upload_image_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**|  | 
 **original_image_file** | **str**|  | 
 **purpose** | **str**|  | 
 **device_info** | **str**|  | 
 **label_info** | **str**|  | 
 **description** | **str**|  | 

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

