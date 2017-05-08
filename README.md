# kube_resource
Manage Resources from k8s

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/jonathan-kosgei/kubeResource.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/jonathan-kosgei/kubeResource.git`)

Then import the package:
```python
import kube_resource 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import kube_resource
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
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

## Documentation for API Endpoints

All URIs are relative to *https://kubernetes.default.svc*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**apis_fqdn_v1_namespaces_namespace_resource_name_get**](docs/DefaultApi.md#apis_fqdn_v1_namespaces_namespace_resource_name_get) | **GET** /apis/{fqdn}/v1/namespaces/{namespace}/{resource}/{name} | Gets a specific Resource
*DefaultApi* | [**apis_fqdn_v1_resource_get**](docs/DefaultApi.md#apis_fqdn_v1_resource_get) | **GET** /apis/{fqdn}/v1/{resource} | Gets Resources
*DefaultApi* | [**apis_fqdn_v1_resource_post**](docs/DefaultApi.md#apis_fqdn_v1_resource_post) | **POST** /apis/{fqdn}/v1/{resource} | Create a Resource


## Documentation For Models



## Documentation For Authorization


## Bearer

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

jonathan@saharacluster.com

