# swagger_client.SDApi

All URIs are relative to *https://virtserver.swaggerhub.com/ug61837361636/bev2/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_sd_getsdimg_post**](SDApi.md#api_v2_sd_getsdimg_post) | **POST** /api/v2/sd/getsdimg | Get Stable Diffusion Image Base64
[**api_v2_sd_listsdmodel_post**](SDApi.md#api_v2_sd_listsdmodel_post) | **POST** /api/v2/sd/listsdmodel | List Stable Diffusion Models
[**api_v2_sd_modifysdmodel_post**](SDApi.md#api_v2_sd_modifysdmodel_post) | **POST** /api/v2/sd/modifysdmodel | Modify Stable Diffusion Model
[**api_v2_sd_txt2img_post**](SDApi.md#api_v2_sd_txt2img_post) | **POST** /api/v2/sd/txt2img | Text to Image Generation

# **api_v2_sd_getsdimg_post**
> InlineResponse20019 api_v2_sd_getsdimg_post(body)

Get Stable Diffusion Image Base64

This API is responsible for retrieving the base64 encoded Stable Diffusion images for a specific project.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SDApi()
body = swagger_client.SdGetsdimgBody() # SdGetsdimgBody | 

try:
    # Get Stable Diffusion Image Base64
    api_response = api_instance.api_v2_sd_getsdimg_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SDApi->api_v2_sd_getsdimg_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SdGetsdimgBody**](SdGetsdimgBody.md)|  | 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_sd_listsdmodel_post**
> InlineResponse20020 api_v2_sd_listsdmodel_post(body)

List Stable Diffusion Models

This API is responsible for listing all available Stable Diffusion models.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SDApi()
body = swagger_client.SdListsdmodelBody() # SdListsdmodelBody | 

try:
    # List Stable Diffusion Models
    api_response = api_instance.api_v2_sd_listsdmodel_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SDApi->api_v2_sd_listsdmodel_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SdListsdmodelBody**](SdListsdmodelBody.md)|  | 

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_sd_modifysdmodel_post**
> InlineResponse20021 api_v2_sd_modifysdmodel_post(body)

Modify Stable Diffusion Model

This API is responsible for modifying the information of an existing Stable Diffusion model.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SDApi()
body = swagger_client.SdModifysdmodelBody() # SdModifysdmodelBody | 

try:
    # Modify Stable Diffusion Model
    api_response = api_instance.api_v2_sd_modifysdmodel_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SDApi->api_v2_sd_modifysdmodel_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SdModifysdmodelBody**](SdModifysdmodelBody.md)|  | 

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_sd_txt2img_post**
> InlineResponse20018 api_v2_sd_txt2img_post(body)

Text to Image Generation

This API is responsible for generating images from text prompts using a Stable Diffusion model.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SDApi()
body = swagger_client.SdTxt2imgBody() # SdTxt2imgBody | 

try:
    # Text to Image Generation
    api_response = api_instance.api_v2_sd_txt2img_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SDApi->api_v2_sd_txt2img_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SdTxt2imgBody**](SdTxt2imgBody.md)|  | 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

