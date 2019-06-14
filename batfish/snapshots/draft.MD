## Installation
```
# service
docker pull ....
docker run --name batfish -d -v batfish-data:/data -p 8888:8888 -p 9997:9997 -p 9996:9996 batfish/allinone
Get token and add to screen. via docker logs

# client
apt install python3-pip
python3 -m pip install --upgrade git+https://github.com/batfish/pybatfish.git
```

## Imports
```
from pybatfish.client.commands import *
from pybatfish.question.question import load_questions
from pybatfish.datamodel.flow import (HeaderConstraints,
                                         PathConstraints)
from pybatfish.question import bfq

bf_session.host = "172.29.236.139"
load_questions()
```
## Initialize Network/Snapshot
```
cd /opt
git clone https://github.com/packetpimp1/network-automation.git
```
## Import
```
NETWORK_NAME = "network-spine_leaf"
SNAPSHOT_NAME = "snapshot-spine_leaf"
SNAPSHOT_PATH = "/opt/network-automation/batfish/snapshots/spine-leaf"

bf_set_network(NETWORK_NAME)
bf_init_snapshot(SNAPSHOT_PATH, name=SNAPSHOT_NAME, overwrite=True)
```
## Parsing Status
```
bfq.fileParseStatus().answer().frame()
bfq.parseWarning().answer().frame()
```
## Questions

* OSPF not on edge ports
* BGP multipath
* Leafs only peered with Spines
* Spines only peered with Leafs
* ~~BGP Adjancies formed.~~
* ~~Jumbo Frames~~

### Check Avail Options
```
interface_properties = bfq.interfaceProperties().answer().frame()
Interface_properties.columns
```
### Check Jumbo MTU Enabled on Non-Edge ports
```
node_props = bfq.interfaceProperties(nodes="/leaf|spine/", properties="Description|MTU").answer().frame()
node_props = node_props[~node_props['Description'].str.contains('to server|Loopback|OOB')]
violators = list(node_props[node_props["MTU"].apply(lambda x: x <= 1500)]['Interface'])
```
### Check BGP Adj
```
leafs = ['leaf1', 'leaf2']
spines = ['spine1', 'spine2']

def is_bgp_adj(leafs, spines):
    print("== CHECKING SPINE to LEAF BGP ADJ ==")
    for s in spines:
        for l in leafs:
            node_prop = bfq.bgpEdges(nodes=s, remoteNodes=l).answer().frame()
            if node_prop.empty:
                print(node_prop)
    print("== CHECKING LEAF TO SPINE BGP ADJ ==")
    for l in leafs:
        for s in spines:
           node_prop = bfq.bgpEdges(nodes=l, remoteNodes=s).answer().frame()
           if node_prop.empty:
               print(node_prop)
```
    
