```
NETWORK_NAME = "network-spine_leaf"
BASE_SNAPSHOT_NAME = "snapshot-spine_leaf"
SNAPSHOT_PATH = "/opt/network-automation/batfish/snapshots/spine-leaf"

bf_set_network(NETWORK_NAME)
bf_init_snapshot(SNAPSHOT_PATH, name=BASE_SNAPSHOT_NAME, overwrite=True)


FAIL_SPINE1_SNAPSHOT_NAME = "fail_spine1"
bf_fork_snapshot(BASE_SNAPSHOT_NAME, FAIL_SPINE1_SNAPSHOT_NAME, deactivate_nodes=["spine1"], overwrite=True)

tr_answer = bfq.traceroute(startLocation="leaf1",headers=HeaderConstraints(dstIps='server-2')).answer(FAIL_SPINE1_SNAPSHOT_NAME).frame()
tr_answer
```
