# kube_resource.DefaultApi

All URIs are relative to *https://kubernetes.default.svc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apis_fqdn_v1_namespaces_namespace_resource_name_get**](DefaultApi.md#apis_fqdn_v1_namespaces_namespace_resource_name_get) | **GET** /apis/{fqdn}/v1/namespaces/{namespace}/{resource}/{name} | Gets a specific Resource
[**apis_fqdn_v1_resource_get**](DefaultApi.md#apis_fqdn_v1_resource_get) | **GET** /apis/{fqdn}/v1/{resource} | Gets Resources
[**apis_fqdn_v1_resource_post**](DefaultApi.md#apis_fqdn_v1_resource_post) | **POST** /apis/{fqdn}/v1/{resource} | Create a Resource


# **apis_fqdn_v1_namespaces_namespace_resource_name_get**
> object apis_fqdn_v1_namespaces_namespace_resource_name_get(namespace, name, fqdn, resource)

Gets a specific Resource

Returns a specific Resource in a namespace

### Example 
```python
from __future__ import print_statement
import time
import kube_resource
from kube_resource.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
kube_resource.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kube_resource.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kube_resource.DefaultApi()
namespace = 'namespace_example' # str | The Resource's namespace
name = 'name_example' # str | The Resource's name
fqdn = 'fqdn_example' # str | The Third party Resource fqdn
resource = 'resource_example' # str | The Resource type

try: 
    # Gets a specific Resource
    api_response = api_instance.apis_fqdn_v1_namespaces_namespace_resource_name_get(namespace, name, fqdn, resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->apis_fqdn_v1_namespaces_namespace_resource_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The Resource&#39;s namespace | 
 **name** | **str**| The Resource&#39;s name | 
 **fqdn** | **str**| The Third party Resource fqdn | 
 **resource** | **str**| The Resource type | 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apis_fqdn_v1_resource_get**
> object apis_fqdn_v1_resource_get(fqdn, resource, watch=watch)

Gets Resources

Returns a list of Resources

### Example 
```python
from __future__ import print_statement
import time
import kube_resource
from kube_resource.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
kube_resource.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kube_resource.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kube_resource.DefaultApi()
fqdn = 'fqdn_example' # str | The Third party Resource fqdn
resource = 'resource_example' # str | The Resource type
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    # Gets Resources
    api_response = api_instance.apis_fqdn_v1_resource_get(fqdn, resource, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->apis_fqdn_v1_resource_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fqdn** | **str**| The Third party Resource fqdn | 
 **resource** | **str**| The Resource type | 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apis_fqdn_v1_resource_post**
> object apis_fqdn_v1_resource_post(fqdn, resource, resource2=resource2)

Create a Resource

Creates a third party resource of the type specified

### Example 
```python
from __future__ import print_statement
import time
import kube_resource
from kube_resource.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
kube_resource.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kube_resource.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kube_resource.DefaultApi()
fqdn = 'fqdn_example' # str | The Third party Resource fqdn
resource = 'resource_example' # str | The Resource type
resource2 = NULL # object | The Resource to create. (optional)

try: 
    # Create a Resource
    api_response = api_instance.apis_fqdn_v1_resource_post(fqdn, resource, resource2=resource2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->apis_fqdn_v1_resource_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fqdn** | **str**| The Third party Resource fqdn | 
 **resource** | **str**| The Resource type | 
 **resource2** | **object**| The Resource to create. | [optional] 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

