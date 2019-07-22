```
cat .pynsotrc
[pynsot]
url = http://172.29.236.139:8990/api
secret_key = #####
default_site = 7
auth_method = auth_token
email = rick@nsot.local
```

## Steps
```
# environment added
nsot devices list
nsot networks list
nsot interfaces list
```
```
# query
nsot devices list -q 'vendor=juniper +vendor=cisco'
nsot devices list -q 'rack=r1 -vendor=cisco'
nsot devices list -a rack=r1 -a hw_type=switch
```

```
# getting next addresses and networks
from pprint import pprint as pp
from pynsot.client import get_api_client
c = get_api_client()

# get addresses
>>> pp(c.sites(7).networks('10.1.5.0/24').next_address().get(num=10))
[u'10.1.5.21/32',
 u'10.1.5.22/32',
 u'10.1.5.23/32',
 u'10.1.5.24/32',
 u'10.1.5.25/32',
 u'10.1.5.26/32',
 u'10.1.5.27/32',
 u'10.1.5.28/32',
 u'10.1.5.29/32',
 u'10.1.5.30/32']
 
 # get networks
>>> pp(c.sites(7).networks('10.1.0.0/16').next_network().get(prefix_length=29,num=20))
[u'10.1.0.0/29',
 u'10.1.0.8/29',
 u'10.1.0.16/29',
 u'10.1.0.24/29',
 u'10.1.0.32/29',
 u'10.1.0.40/29',
 u'10.1.0.48/29',
 u'10.1.0.56/29',
 u'10.1.0.64/29',
 u'10.1.0.72/29',
 u'10.1.0.80/29',
 u'10.1.0.88/29',
 u'10.1.0.96/29',
 u'10.1.0.104/29',
 u'10.1.0.112/29',
 u'10.1.0.120/29',
 u'10.1.0.128/29',
 u'10.1.0.136/29',
 u'10.1.0.144/29',
 u'10.1.0.152/29']
 
 # create network
net = {
  'attributes': {
    'description': 'backup',
    'vlan_id': '104',
    'vlan_name': 'VLAN-104-BACKUP',
    'vlan_desc': 'oob-mgmt',
    'vrf': 'infra'
  },
  'network_address': '10.1.0.144',
  'prefix_length': 29
}

>>> pp(c.sites(7).networks.post(net))
{u'attributes': {u'description': u'backup',
                 u'vlan_desc': u'oob-mgmt',
                 u'vlan_id': u'104',
                 u'vlan_name': u'VLAN-104-BACKUP',
                 u'vrf': u'infra'},
 u'cidr': u'10.1.0.144/29',
 u'id': 41,
 u'ip_version': u'4',
 u'is_ip': False,
 u'network_address': u'10.1.0.144',
 u'parent': u'10.1.0.0/16',
 u'parent_id': 6,
 u'prefix_length': 29,
 u'site_id': 7,
 u'state': u'allocated'}
 
 >>> pp(c.sites(7).networks('10.1.0.0/16').next_network().get(prefix_length=29,num=20))
[u'10.1.0.0/29',
 u'10.1.0.8/29',
 u'10.1.0.16/29',
 u'10.1.0.24/29',
 u'10.1.0.32/29',
 u'10.1.0.40/29',
 u'10.1.0.48/29',
 u'10.1.0.56/29',
 u'10.1.0.64/29',
 u'10.1.0.72/29',
 u'10.1.0.80/29',
 u'10.1.0.88/29',
 u'10.1.0.96/29',
 u'10.1.0.104/29',
 u'10.1.0.112/29',
 u'10.1.0.120/29',
 u'10.1.0.128/29',
 u'10.1.0.136/29',
 u'10.1.0.152/29',
 u'10.1.0.160/29']
```

## Misc
Use the following for constructing methods
* https://pynsot.readthedocs.io/en/latest/cli.html#debugging
* https://pynsot.readthedocs.io/en/latest/python_api.html#fetching-resources
