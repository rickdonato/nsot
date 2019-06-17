## Questions

* OSPF not on edge ports
~~* BGP multipath~~
* Leafs only peered with Spines
* Spines only peered with Leafs
* ~~BGP Adjancies formed?~~
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
### Check BGP Adj 1 
```
leafs = ['leaf1', 'leaf2']
spines = ['spine1', 'spine2']

def is_bgp_adj(leafs, spines):
    print("== CHECKING SPINE to LEAF BGP ADJ ==")
    for s in spines:
        for l in leafs:
            node_prop = bfq.bgpEdges(nodes=s, remoteNodes=l).answer().frame()
            if node_prop.empty:
                print("No BGP Adj: {}-{}".format(s,l))
                
    print("== CHECKING LEAF TO SPINE BGP ADJ ==")
    for l in leafs:
        for s in spines:
           node_prop = bfq.bgpEdges(nodes=l, remoteNodes=s).answer().frame()
           if node_prop.empty:
               print("No BGP Adj: {}-{}".format(l,s))
```
### Check BGP Adj 2
```
# configuration check
node_props = bfq.bgpSessionCompatibility().answer().frame()

# session check (sits outside of config analysis
node_props = bfq.bgpSessionStatus().answer().frame()
node_props[~node_props['Established_Status'].str.contains('ESTABLISHED')]
```

## Check Multipath
```
bfq.bgpProcessConfiguration(properties="Multipath_EBGP").answer()
```
