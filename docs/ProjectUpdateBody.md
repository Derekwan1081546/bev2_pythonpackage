# ProjectUpdateBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | Access token to authenticate the request | [optional] 
**username** | **str** | User ID of the person attempting to update the project | [optional] 
**projectname** | **str** | Name of the project to be updated | [optional] 
**status** | **str** | New status of the project, used when action is &#x27;confirm_status&#x27; | [optional] 
**count** | **int** | The new remaining count for image generation, used when action is &#x27;modify_remain_count&#x27; | [optional] 
**quantity** | **int** | The new image quantity, used when action is &#x27;modify_img_quantity&#x27; | [optional] 
**action** | **str** | The type of update action to perform. Possible values &#x27;confirm_status&#x27;, &#x27;modify_remain_count&#x27;, &#x27;modify_img_quantity&#x27; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

