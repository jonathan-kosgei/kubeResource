# Watch for resources of kind Repo

The Kubernetes Third party specification for Repos
```
apiVersion: extensions/v1beta1
kind: ThirdPartyResource
metadata:
  name: re-po.git.k8s.com
description: "A specification of a Repo resource mapped to a volume"
versions:
- name: v1
```

**_An example of a Repo resource_**

```
apiVersion: "git.k8s.com/v1"
kind: RePo
metadata:
  name: blog-repo
repo: github.com/user/my-blog
oauth: 123456789
branch: master
key: user-git-deploy-secret
path: /path/in/volume
image: image to run job in
then: hugo --destination=/home/user/hugosite/public
pvc: persistent-volume-claim
username: repo username
password: repo password
```

**_Monitor for add/delete/update events on resources of type repo_**

```
from __future__ import print_function
import time
import kube_resource
from kube_resource.rest import ApiException
from pprint import pprint

with open('/var/run/secrets/kubernetes.io/serviceaccount/token', 'r') as token_file:
    token=token_file.read()

kube_resource.configuration.api_key['Authorization'] = token
kube_resource.configuration.api_key_prefix['Authorization'] = 'Bearer'
kube_resource.configuration.ssl_ca_cert = '/var/run/secrets/kubernetes.io/serviceaccount/ca.crt'
api_instance = kube_resource.DefaultApi()

##
import watch
count = 10
resource = 'repos'
fqdn = 'git.k8s.com'
w = watch.Watch()
for event in w.stream(api_instance.apis_fqdn_v1_resource_get,resource=resource, fqdn=fqdn, _request_timeout=60):
    print("Event: %s " % (event['type']))
    event['raw_object']
    count -= 1
    if not count:
        w.stop()
```