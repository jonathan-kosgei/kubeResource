# kube_resource.DefaultApi

All URIs are relative to *https://kubernetes.default.svc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apis_fqdn_v1_namespaces_namespace_resource_name_delete**](DefaultApi.md#apis_fqdn_v1_namespaces_namespace_resource_name_delete) | **DELETE** /apis/{fqdn}/v1/namespaces/{namespace}/{resource}/{name} | Deletes a specific Resource
[**apis_fqdn_v1_namespaces_namespace_resource_name_get**](DefaultApi.md#apis_fqdn_v1_namespaces_namespace_resource_name_get) | **GET** /apis/{fqdn}/v1/namespaces/{namespace}/{resource}/{name} | Gets a specific Resource
[**apis_fqdn_v1_namespaces_namespace_resource_name_put**](DefaultApi.md#apis_fqdn_v1_namespaces_namespace_resource_name_put) | **PUT** /apis/{fqdn}/v1/namespaces/{namespace}/{resource}/{name} | Replace a Resource
[**apis_fqdn_v1_namespaces_namespace_resource_post**](DefaultApi.md#apis_fqdn_v1_namespaces_namespace_resource_post) | **POST** /apis/{fqdn}/v1/namespaces/{namespace}/{resource} | Create a Resource
[**apis_fqdn_v1_resource_get**](DefaultApi.md#apis_fqdn_v1_resource_get) | **GET** /apis/{fqdn}/v1/{resource} | Gets Resources


# **apis_fqdn_v1_namespaces_namespace_resource_name_delete**
> object apis_fqdn_v1_namespaces_namespace_resource_name_delete(body, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)

Deletes a specific Resource

Deletes the specified Resource in the specified namespace

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
body = kube_resource.V1DeleteOptions() # V1DeleteOptions | 
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
propagation_policy = 'propagation_policy_example' # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. (optional)

try: 
    # Deletes a specific Resource
    api_response = api_instance.apis_fqdn_v1_namespaces_namespace_resource_name_delete(body, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->apis_fqdn_v1_namespaces_namespace_resource_name_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional] 
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. | [optional] 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

# **apis_fqdn_v1_namespaces_namespace_resource_name_put**
> object apis_fqdn_v1_namespaces_namespace_resource_name_put(namespace, fqdn, resource, body)

Replace a Resource

Replaces the specified third party resource of the type specified

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
fqdn = 'fqdn_example' # str | The Third party Resource fqdn
resource = 'resource_example' # str | The Resource type
body = NULL # object | The JSON schema of the Resource to create.

try: 
    # Replace a Resource
    api_response = api_instance.apis_fqdn_v1_namespaces_namespace_resource_name_put(namespace, fqdn, resource, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->apis_fqdn_v1_namespaces_namespace_resource_name_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The Resource&#39;s namespace | 
 **fqdn** | **str**| The Third party Resource fqdn | 
 **resource** | **str**| The Resource type | 
 **body** | **object**| The JSON schema of the Resource to create. | 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apis_fqdn_v1_namespaces_namespace_resource_post**
> object apis_fqdn_v1_namespaces_namespace_resource_post(namespace, fqdn, resource, body)

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
namespace = 'namespace_example' # str | The Resource's namespace
fqdn = 'fqdn_example' # str | The Third party Resource fqdn
resource = 'resource_example' # str | The Resource type
body = NULL # object | The JSON schema of the Resource to create.

try: 
    # Create a Resource
    api_response = api_instance.apis_fqdn_v1_namespaces_namespace_resource_post(namespace, fqdn, resource, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->apis_fqdn_v1_namespaces_namespace_resource_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The Resource&#39;s namespace | 
 **fqdn** | **str**| The Third party Resource fqdn | 
 **resource** | **str**| The Resource type | 
 **body** | **object**| The JSON schema of the Resource to create. | 

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

