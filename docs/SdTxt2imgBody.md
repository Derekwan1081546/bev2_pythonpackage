# SdTxt2imgBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | Access token to authenticate the request | [optional] 
**username** | **str** | User ID requesting the image generation | [optional] 
**projectname** | **str** | The project name for which the images are being generated | [optional] 
**count** | **int** | Number of images to generate | [optional] 
**enable_hr** | **bool** | Enable high-resolution generation | [optional] 
**denoising_strength** | **float** | The denoising strength for the high-resolution pass | [optional] 
**hr_scale** | **float** | High-resolution scaling factor | [optional] 
**hr_upscaler** | **str** | The upscaler to use for high-resolution images | [optional] 
**hr_second_pass_steps** | **int** | The number of steps for the second pass during high-resolution processing | [optional] 
**hr_resize_x** | **int** | Horizontal resize value for the high-resolution pass | [optional] 
**hr_resize_y** | **int** | Vertical resize value for the high-resolution pass | [optional] 
**prompt** | **str** | The main text prompt for generating images | [optional] 
**styles** | **list[str]** | Array of styles to apply to the generated image | [optional] 
**seed** | **int** | The seed for the random number generator, -1 for random | [optional] 
**batch_size** | **int** | The number of images per batch | [optional] 
**n_iter** | **int** | Number of iterations for generating images | [optional] 
**steps** | **int** | Number of steps for the generation process | [optional] 
**cfg_scale** | **float** | Classifier free guidance scale | [optional] 
**width** | **int** | Width of the generated image | [optional] 
**height** | **int** | Height of the generated image | [optional] 
**restore_faces** | **bool** | Restore faces in the generated images | [optional] 
**tiling** | **bool** | Enable tiling for the generated images | [optional] 
**negative_prompt** | **str** | Text prompt to avoid in the generated images | [optional] 
**eta** | **float** | ETA value for generation | [optional] 
**override_settings** | [**Apiv2sdtxt2imgOverrideSettings**](Apiv2sdtxt2imgOverrideSettings.md) |  | [optional] 
**script_args** | **list[str]** | Arguments for additional scripts | [optional] 
**sampler_index** | **str** | Sampler to use for generation | [optional] 
**alwayson_scripts** | **object** | Always-on scripts to use during generation | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

