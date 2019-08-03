# swagger_client.AuctionApi

All URIs are relative to *http://localhost:8080/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**close_auction**](AuctionApi.md#close_auction) | **POST** /auction/close | 
[**close_auction_pledge**](AuctionApi.md#close_auction_pledge) | **POST** /auction/closePledge | 
[**create_auction**](AuctionApi.md#create_auction) | **POST** /auction | Create auction
[**create_bid**](AuctionApi.md#create_bid) | **POST** /auction/bid | Create bid
[**get_auction**](AuctionApi.md#get_auction) | **GET** /auction | 
[**get_bids**](AuctionApi.md#get_bids) | **GET** /auction/bid | 
[**get_winning_bids**](AuctionApi.md#get_winning_bids) | **GET** /auction/bid/wins | 


# **close_auction**
> close_auction(body)



This can only be done by NGO

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuctionApi()
body = swagger_client.Auction() # Auction | 

try:
    api_instance.close_auction(body)
except ApiException as e:
    print("Exception when calling AuctionApi->close_auction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Auction**](Auction.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **close_auction_pledge**
> close_auction_pledge(body)



This can only be done by NGO

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuctionApi()
body = swagger_client.Auction() # Auction | 

try:
    api_instance.close_auction_pledge(body)
except ApiException as e:
    print("Exception when calling AuctionApi->close_auction_pledge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Auction**](Auction.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_auction**
> create_auction(body)

Create auction

This can only be done by NGO

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuctionApi()
body = swagger_client.Auction() # Auction | 

try:
    # Create auction
    api_instance.create_auction(body)
except ApiException as e:
    print("Exception when calling AuctionApi->create_auction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Auction**](Auction.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_bid**
> create_bid(body)

Create bid

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuctionApi()
body = swagger_client.Bid() # Bid | 

try:
    # Create bid
    api_instance.create_bid(body)
except ApiException as e:
    print("Exception when calling AuctionApi->create_bid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Bid**](Bid.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auction**
> list[Auction] get_auction(auction_id=auction_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuctionApi()
auction_id = 'auction_id_example' # str |  (optional)

try:
    api_response = api_instance.get_auction(auction_id=auction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuctionApi->get_auction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auction_id** | **str**|  | [optional] 

### Return type

[**list[Auction]**](Auction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bids**
> list[Bid] get_bids(auction_id=auction_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuctionApi()
auction_id = 'auction_id_example' # str |  (optional)

try:
    api_response = api_instance.get_bids(auction_id=auction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuctionApi->get_bids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auction_id** | **str**|  | [optional] 

### Return type

[**list[Bid]**](Bid.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_winning_bids**
> list[Bid] get_winning_bids(auction_id=auction_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuctionApi()
auction_id = 'auction_id_example' # str |  (optional)

try:
    api_response = api_instance.get_winning_bids(auction_id=auction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuctionApi->get_winning_bids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auction_id** | **str**|  | [optional] 

### Return type

[**list[Bid]**](Bid.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

