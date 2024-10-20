# swagger_client.AuthApi

All URIs are relative to *https://virtserver.swaggerhub.com/ug61837361636/bev2/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_auth_deleteuser_post**](AuthApi.md#api_v2_auth_deleteuser_post) | **POST** /api/v2/auth/deleteuser | Delete User Account
[**api_v2_auth_listuser_post**](AuthApi.md#api_v2_auth_listuser_post) | **POST** /api/v2/auth/listuser | List All Users
[**api_v2_auth_modifyuser_post**](AuthApi.md#api_v2_auth_modifyuser_post) | **POST** /api/v2/auth/modifyuser | Modify User Information
[**api_v2_auth_signin_post**](AuthApi.md#api_v2_auth_signin_post) | **POST** /api/v2/auth/signin | User Signin
[**api_v2_auth_signup_post**](AuthApi.md#api_v2_auth_signup_post) | **POST** /api/v2/auth/signup | User Signup

# **api_v2_auth_deleteuser_post**
> InlineResponse2003 api_v2_auth_deleteuser_post(body)

Delete User Account

This API is responsible for deleting the user's account.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
body = swagger_client.AuthDeleteuserBody() # AuthDeleteuserBody | 

try:
    # Delete User Account
    api_response = api_instance.api_v2_auth_deleteuser_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->api_v2_auth_deleteuser_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthDeleteuserBody**](AuthDeleteuserBody.md)|  | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_auth_listuser_post**
> InlineResponse2001 api_v2_auth_listuser_post(body)

List All Users

This API is responsible for listing all users' information.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
body = swagger_client.AuthListuserBody() # AuthListuserBody | 

try:
    # List All Users
    api_response = api_instance.api_v2_auth_listuser_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->api_v2_auth_listuser_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthListuserBody**](AuthListuserBody.md)|  | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_auth_modifyuser_post**
> InlineResponse2002 api_v2_auth_modifyuser_post(body)

Modify User Information

This API is responsible for modifying a user's information.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
body = swagger_client.AuthModifyuserBody() # AuthModifyuserBody | 

try:
    # Modify User Information
    api_response = api_instance.api_v2_auth_modifyuser_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->api_v2_auth_modifyuser_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthModifyuserBody**](AuthModifyuserBody.md)|  | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_auth_signin_post**
> InlineResponse200 api_v2_auth_signin_post(body)

User Signin

Authenticate a user and return a token.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
body = swagger_client.AuthSigninBody() # AuthSigninBody | 

try:
    # User Signin
    api_response = api_instance.api_v2_auth_signin_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->api_v2_auth_signin_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthSigninBody**](AuthSigninBody.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_auth_signup_post**
> InlineResponse201 api_v2_auth_signup_post(body)

User Signup

This API allows a user to create an account.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
body = swagger_client.AuthSignupBody() # AuthSignupBody | Signup payload

try:
    # User Signup
    api_response = api_instance.api_v2_auth_signup_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->api_v2_auth_signup_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthSignupBody**](AuthSignupBody.md)| Signup payload | 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

