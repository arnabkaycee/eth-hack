# swagger_client.DeviceApi

All URIs are relative to *http://localhost:8080/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_device_usage**](DeviceApi.md#get_device_usage) | **GET** /device/usage | 
[**log_usage_stats**](DeviceApi.md#log_usage_stats) | **POST** /device/usage | logUsageStats


# **get_device_usage**
> list[DeviceUsageStats] get_device_usage(device_id=device_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceApi()
device_id = 'device_id_example' # str |  (optional)

try:
    api_response = api_instance.get_device_usage(device_id=device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->get_device_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | [optional] 

### Return type

[**list[DeviceUsageStats]**](DeviceUsageStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **log_usage_stats**
> log_usage_stats(body)

logUsageStats

This can only be done by NGO

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceApi()
body = swagger_client.Body() # Body | 

try:
    # logUsageStats
    api_instance.log_usage_stats(body)
except ApiException as e:
    print("Exception when calling DeviceApi->log_usage_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](Body.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

