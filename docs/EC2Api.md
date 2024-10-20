# swagger_client.EC2Api

All URIs are relative to *https://virtserver.swaggerhub.com/ug61837361636/bev2/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_ec2context_delete_ec2_post**](EC2Api.md#api_v2_ec2context_delete_ec2_post) | **POST** /api/v2/ec2context/delete_ec2 | Delete EC2 Instance
[**api_v2_ec2context_deploy_ec2_post**](EC2Api.md#api_v2_ec2context_deploy_ec2_post) | **POST** /api/v2/ec2context/deploy_ec2 | Deploy EC2 Instance
[**api_v2_ec2context_start_ec2_post**](EC2Api.md#api_v2_ec2context_start_ec2_post) | **POST** /api/v2/ec2context/start_ec2 | Start EC2 Instance
[**api_v2_ec2context_stop_ec2_post**](EC2Api.md#api_v2_ec2context_stop_ec2_post) | **POST** /api/v2/ec2context/stop_ec2 | Stop EC2 Instance

# **api_v2_ec2context_delete_ec2_post**
> InlineResponse20025 api_v2_ec2context_delete_ec2_post(body)

Delete EC2 Instance

This API is responsible for deleting an existing EC2 instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EC2Api()
body = swagger_client.Ec2contextDeleteEc2Body() # Ec2contextDeleteEc2Body | 

try:
    # Delete EC2 Instance
    api_response = api_instance.api_v2_ec2context_delete_ec2_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EC2Api->api_v2_ec2context_delete_ec2_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Ec2contextDeleteEc2Body**](Ec2contextDeleteEc2Body.md)|  | 

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_ec2context_deploy_ec2_post**
> InlineResponse20022 api_v2_ec2context_deploy_ec2_post(body)

Deploy EC2 Instance

This API is responsible for deploying an EC2 instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EC2Api()
body = swagger_client.Ec2contextDeployEc2Body() # Ec2contextDeployEc2Body | 

try:
    # Deploy EC2 Instance
    api_response = api_instance.api_v2_ec2context_deploy_ec2_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EC2Api->api_v2_ec2context_deploy_ec2_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Ec2contextDeployEc2Body**](Ec2contextDeployEc2Body.md)|  | 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_ec2context_start_ec2_post**
> InlineResponse20023 api_v2_ec2context_start_ec2_post(body)

Start EC2 Instance

This API is responsible for starting a stopped EC2 instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EC2Api()
body = swagger_client.Ec2contextStartEc2Body() # Ec2contextStartEc2Body | 

try:
    # Start EC2 Instance
    api_response = api_instance.api_v2_ec2context_start_ec2_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EC2Api->api_v2_ec2context_start_ec2_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Ec2contextStartEc2Body**](Ec2contextStartEc2Body.md)|  | 

### Return type

[**InlineResponse20023**](InlineResponse20023.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_ec2context_stop_ec2_post**
> InlineResponse20024 api_v2_ec2context_stop_ec2_post(body)

Stop EC2 Instance

This API is responsible for stopping a running EC2 instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EC2Api()
body = swagger_client.Ec2contextStopEc2Body() # Ec2contextStopEc2Body | 

try:
    # Stop EC2 Instance
    api_response = api_instance.api_v2_ec2context_stop_ec2_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EC2Api->api_v2_ec2context_stop_ec2_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Ec2contextStopEc2Body**](Ec2contextStopEc2Body.md)|  | 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

