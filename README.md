# swagger-client
API documentation for BE v2, handling authentication, project management, image operations, model management, and EC2 context.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/Derekwan1081546/bev2_pythonpackage.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/Derekwan1081546/bev2_pythonpackage.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APPAPIApi(swagger_client.ApiClient(configuration))
body = swagger_client.V1DownloadImageOriginBody() # V1DownloadImageOriginBody | 

try:
    # Download Original Image from S3
    api_response = api_instance.api_v1_download_image_origin_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APPAPIApi->api_v1_download_image_origin_post: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.APPAPIApi(swagger_client.ApiClient(configuration))
body = swagger_client.V1DownloadImageBody() # V1DownloadImageBody | 

try:
    # Download Image After Inference
    api_response = api_instance.api_v1_download_image_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APPAPIApi->api_v1_download_image_post: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.APPAPIApi(swagger_client.ApiClient(configuration))
body = swagger_client.V1FeedbackBody() # V1FeedbackBody | 

try:
    # Model Inference Feedback
    api_response = api_instance.api_v1_feedback_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APPAPIApi->api_v1_feedback_post: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.APPAPIApi(swagger_client.ApiClient(configuration))
body = swagger_client.V1GetModelListBody() # V1GetModelListBody | 

try:
    # Get Model List from RDS and S3
    api_response = api_instance.api_v1_get_model_list_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APPAPIApi->api_v1_get_model_list_post: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.APPAPIApi(swagger_client.ApiClient(configuration))
body = swagger_client.V1GetModelBody() # V1GetModelBody | 

try:
    # Download Model from RDS and S3
    api_response = api_instance.api_v1_get_model_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APPAPIApi->api_v1_get_model_post: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.APPAPIApi(swagger_client.ApiClient(configuration))
body = swagger_client.V1RemoteInferenceByIdBody() # V1RemoteInferenceByIdBody | 

try:
    # Run Inference on Image by ID
    api_response = api_instance.api_v1_remote_inference_by_id_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APPAPIApi->api_v1_remote_inference_by_id_post: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.APPAPIApi(swagger_client.ApiClient(configuration))
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

# create an instance of the API class
api_instance = swagger_client.APPAPIApi(swagger_client.ApiClient(configuration))
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

## Documentation for API Endpoints

All URIs are relative to *https://virtserver.swaggerhub.com/ug61837361636/bev2/1.0.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*APPAPIApi* | [**api_v1_download_image_origin_post**](docs/APPAPIApi.md#api_v1_download_image_origin_post) | **POST** /api/v1/downloadImageOrigin | Download Original Image from S3
*APPAPIApi* | [**api_v1_download_image_post**](docs/APPAPIApi.md#api_v1_download_image_post) | **POST** /api/v1/downloadImage | Download Image After Inference
*APPAPIApi* | [**api_v1_feedback_post**](docs/APPAPIApi.md#api_v1_feedback_post) | **POST** /api/v1/feedback | Model Inference Feedback
*APPAPIApi* | [**api_v1_get_model_list_post**](docs/APPAPIApi.md#api_v1_get_model_list_post) | **POST** /api/v1/getModelList | Get Model List from RDS and S3
*APPAPIApi* | [**api_v1_get_model_post**](docs/APPAPIApi.md#api_v1_get_model_post) | **POST** /api/v1/getModel | Download Model from RDS and S3
*APPAPIApi* | [**api_v1_remote_inference_by_id_post**](docs/APPAPIApi.md#api_v1_remote_inference_by_id_post) | **POST** /api/v1/remoteInferenceById | Run Inference on Image by ID
*APPAPIApi* | [**api_v1_style_transform_post**](docs/APPAPIApi.md#api_v1_style_transform_post) | **POST** /api/v1/styleTransform | Style Transform for Image
*APPAPIApi* | [**api_v1_upload_image_post**](docs/APPAPIApi.md#api_v1_upload_image_post) | **POST** /api/v1/uploadImage | Upload Image for Inference or Dataset
*AuthApi* | [**api_v2_auth_deleteuser_post**](docs/AuthApi.md#api_v2_auth_deleteuser_post) | **POST** /api/v2/auth/deleteuser | Delete User Account
*AuthApi* | [**api_v2_auth_listuser_post**](docs/AuthApi.md#api_v2_auth_listuser_post) | **POST** /api/v2/auth/listuser | List All Users
*AuthApi* | [**api_v2_auth_modifyuser_post**](docs/AuthApi.md#api_v2_auth_modifyuser_post) | **POST** /api/v2/auth/modifyuser | Modify User Information
*AuthApi* | [**api_v2_auth_signin_post**](docs/AuthApi.md#api_v2_auth_signin_post) | **POST** /api/v2/auth/signin | User Signin
*AuthApi* | [**api_v2_auth_signup_post**](docs/AuthApi.md#api_v2_auth_signup_post) | **POST** /api/v2/auth/signup | User Signup
*EC2Api* | [**api_v2_ec2context_delete_ec2_post**](docs/EC2Api.md#api_v2_ec2context_delete_ec2_post) | **POST** /api/v2/ec2context/delete_ec2 | Delete EC2 Instance
*EC2Api* | [**api_v2_ec2context_deploy_ec2_post**](docs/EC2Api.md#api_v2_ec2context_deploy_ec2_post) | **POST** /api/v2/ec2context/deploy_ec2 | Deploy EC2 Instance
*EC2Api* | [**api_v2_ec2context_start_ec2_post**](docs/EC2Api.md#api_v2_ec2context_start_ec2_post) | **POST** /api/v2/ec2context/start_ec2 | Start EC2 Instance
*EC2Api* | [**api_v2_ec2context_stop_ec2_post**](docs/EC2Api.md#api_v2_ec2context_stop_ec2_post) | **POST** /api/v2/ec2context/stop_ec2 | Stop EC2 Instance
*ImageApi* | [**api_v2_image_delete_post**](docs/ImageApi.md#api_v2_image_delete_post) | **POST** /api/v2/image/delete | Delete Image Information
*ImageApi* | [**api_v2_image_feedbackinfo_post**](docs/ImageApi.md#api_v2_image_feedbackinfo_post) | **POST** /api/v2/image/feedbackinfo | Update Image Feedback Information
*ImageApi* | [**api_v2_image_get_post**](docs/ImageApi.md#api_v2_image_get_post) | **POST** /api/v2/image/get | Get Image Information
*ImageApi* | [**api_v2_image_getrequirement_post**](docs/ImageApi.md#api_v2_image_getrequirement_post) | **POST** /api/v2/image/getrequirement | Get Project Requirement Information
*ImageApi* | [**api_v2_image_list_post**](docs/ImageApi.md#api_v2_image_list_post) | **POST** /api/v2/image/list | List Images in a Project
*ImageApi* | [**api_v2_image_requirement_post**](docs/ImageApi.md#api_v2_image_requirement_post) | **POST** /api/v2/image/requirement | Upload Project Requirement
*ImageApi* | [**api_v2_image_upload_post**](docs/ImageApi.md#api_v2_image_upload_post) | **POST** /api/v2/image/upload | Upload Image
*ModelApi* | [**api_v2_model_delete_post**](docs/ModelApi.md#api_v2_model_delete_post) | **POST** /api/v2/model/delete | Delete Model
*ModelApi* | [**api_v2_model_download_post**](docs/ModelApi.md#api_v2_model_download_post) | **POST** /api/v2/model/download | Download Model
*ModelApi* | [**api_v2_model_get_post**](docs/ModelApi.md#api_v2_model_get_post) | **POST** /api/v2/model/get | Get Model Information
*ModelApi* | [**api_v2_model_list_post**](docs/ModelApi.md#api_v2_model_list_post) | **POST** /api/v2/model/list | List Models
*ModelApi* | [**api_v2_model_upload_post**](docs/ModelApi.md#api_v2_model_upload_post) | **POST** /api/v2/model/upload | Upload Model
*ProjectApi* | [**api_v2_project_create_post**](docs/ProjectApi.md#api_v2_project_create_post) | **POST** /api/v2/project/create | Create Project
*ProjectApi* | [**api_v2_project_delete_post**](docs/ProjectApi.md#api_v2_project_delete_post) | **POST** /api/v2/project/delete | Delete Project
*ProjectApi* | [**api_v2_project_get_post**](docs/ProjectApi.md#api_v2_project_get_post) | **POST** /api/v2/project/get | Get Single Project Information
*ProjectApi* | [**api_v2_project_list_post**](docs/ProjectApi.md#api_v2_project_list_post) | **POST** /api/v2/project/list | List All Projects From User Account
*ProjectApi* | [**api_v2_project_listall_post**](docs/ProjectApi.md#api_v2_project_listall_post) | **POST** /api/v2/project/listall | List All Projects
*ProjectApi* | [**api_v2_project_update_post**](docs/ProjectApi.md#api_v2_project_update_post) | **POST** /api/v2/project/update | Update Project Information
*SDApi* | [**api_v2_sd_getsdimg_post**](docs/SDApi.md#api_v2_sd_getsdimg_post) | **POST** /api/v2/sd/getsdimg | Get Stable Diffusion Image Base64
*SDApi* | [**api_v2_sd_listsdmodel_post**](docs/SDApi.md#api_v2_sd_listsdmodel_post) | **POST** /api/v2/sd/listsdmodel | List Stable Diffusion Models
*SDApi* | [**api_v2_sd_modifysdmodel_post**](docs/SDApi.md#api_v2_sd_modifysdmodel_post) | **POST** /api/v2/sd/modifysdmodel | Modify Stable Diffusion Model
*SDApi* | [**api_v2_sd_txt2img_post**](docs/SDApi.md#api_v2_sd_txt2img_post) | **POST** /api/v2/sd/txt2img | Text to Image Generation

## Documentation For Models

 - [Apiv2imagerequirementRequest](docs/Apiv2imagerequirementRequest.md)
 - [Apiv2imagerequirementRequestRequirement1](docs/Apiv2imagerequirementRequestRequirement1.md)
 - [Apiv2sdtxt2imgOverrideSettings](docs/Apiv2sdtxt2imgOverrideSettings.md)
 - [AuthDeleteuserBody](docs/AuthDeleteuserBody.md)
 - [AuthListuserBody](docs/AuthListuserBody.md)
 - [AuthModifyuserBody](docs/AuthModifyuserBody.md)
 - [AuthSigninBody](docs/AuthSigninBody.md)
 - [AuthSignupBody](docs/AuthSignupBody.md)
 - [Ec2contextDeleteEc2Body](docs/Ec2contextDeleteEc2Body.md)
 - [Ec2contextDeployEc2Body](docs/Ec2contextDeployEc2Body.md)
 - [Ec2contextStartEc2Body](docs/Ec2contextStartEc2Body.md)
 - [Ec2contextStopEc2Body](docs/Ec2contextStopEc2Body.md)
 - [ImageDeleteBody](docs/ImageDeleteBody.md)
 - [ImageFeedbackinfoBody](docs/ImageFeedbackinfoBody.md)
 - [ImageGetBody](docs/ImageGetBody.md)
 - [ImageGetrequirementBody](docs/ImageGetrequirementBody.md)
 - [ImageListBody](docs/ImageListBody.md)
 - [ImageRequirementBody](docs/ImageRequirementBody.md)
 - [ImageUploadBody](docs/ImageUploadBody.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse20010](docs/InlineResponse20010.md)
 - [InlineResponse20011](docs/InlineResponse20011.md)
 - [InlineResponse20012](docs/InlineResponse20012.md)
 - [InlineResponse20013](docs/InlineResponse20013.md)
 - [InlineResponse20014](docs/InlineResponse20014.md)
 - [InlineResponse20015](docs/InlineResponse20015.md)
 - [InlineResponse20016](docs/InlineResponse20016.md)
 - [InlineResponse20017](docs/InlineResponse20017.md)
 - [InlineResponse20018](docs/InlineResponse20018.md)
 - [InlineResponse20019](docs/InlineResponse20019.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse20020](docs/InlineResponse20020.md)
 - [InlineResponse20021](docs/InlineResponse20021.md)
 - [InlineResponse20022](docs/InlineResponse20022.md)
 - [InlineResponse20023](docs/InlineResponse20023.md)
 - [InlineResponse20024](docs/InlineResponse20024.md)
 - [InlineResponse20025](docs/InlineResponse20025.md)
 - [InlineResponse20026](docs/InlineResponse20026.md)
 - [InlineResponse20027](docs/InlineResponse20027.md)
 - [InlineResponse20028](docs/InlineResponse20028.md)
 - [InlineResponse20029](docs/InlineResponse20029.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse20030](docs/InlineResponse20030.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse2007](docs/InlineResponse2007.md)
 - [InlineResponse2008](docs/InlineResponse2008.md)
 - [InlineResponse2009](docs/InlineResponse2009.md)
 - [InlineResponse201](docs/InlineResponse201.md)
 - [InlineResponse2011](docs/InlineResponse2011.md)
 - [InlineResponse2012](docs/InlineResponse2012.md)
 - [InlineResponse2013](docs/InlineResponse2013.md)
 - [ModelDeleteBody](docs/ModelDeleteBody.md)
 - [ModelDownloadBody](docs/ModelDownloadBody.md)
 - [ModelGetBody](docs/ModelGetBody.md)
 - [ModelListBody](docs/ModelListBody.md)
 - [ModelUploadBody](docs/ModelUploadBody.md)
 - [ProjectCreateBody](docs/ProjectCreateBody.md)
 - [ProjectDeleteBody](docs/ProjectDeleteBody.md)
 - [ProjectGetBody](docs/ProjectGetBody.md)
 - [ProjectListBody](docs/ProjectListBody.md)
 - [ProjectListallBody](docs/ProjectListallBody.md)
 - [ProjectUpdateBody](docs/ProjectUpdateBody.md)
 - [SdGetsdimgBody](docs/SdGetsdimgBody.md)
 - [SdListsdmodelBody](docs/SdListsdmodelBody.md)
 - [SdModifysdmodelBody](docs/SdModifysdmodelBody.md)
 - [SdTxt2imgBody](docs/SdTxt2imgBody.md)
 - [V1DownloadImageBody](docs/V1DownloadImageBody.md)
 - [V1DownloadImageOriginBody](docs/V1DownloadImageOriginBody.md)
 - [V1FeedbackBody](docs/V1FeedbackBody.md)
 - [V1GetModelBody](docs/V1GetModelBody.md)
 - [V1GetModelListBody](docs/V1GetModelListBody.md)
 - [V1RemoteInferenceByIdBody](docs/V1RemoteInferenceByIdBody.md)
 - [V1StyleTransformBody](docs/V1StyleTransformBody.md)
 - [V1UploadImageBody](docs/V1UploadImageBody.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author
    bev2_pythonpackage