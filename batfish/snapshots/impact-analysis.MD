```
from pybatfish.client.commands import *
from pybatfish.question.question import load_questions
from pybatfish.datamodel.flow import (HeaderConstraints,
                                         PathConstraints)
from pybatfish.question import bfq

bf_session.host = "172.29.236.139"
load_questions()
```

```
from pybatfish.datamodel.primitives import Interface

NETWORK_NAME = "network-spine_leaf"
BASE_SNAPSHOT_NAME = "snapshot-spine_leaf"
SNAPSHOT_PATH = "/opt/network-automation/batfish/snapshots/spine-leaf"

bf_set_network(NETWORK_NAME)
bf_init_snapshot(SNAPSHOT_PATH, name=BASE_SNAPSHOT_NAME, overwrite=True)


#FAIL_SPINE1_SNAPSHOT_NAME = "fail_spine1"
bf_fork_snapshot(BASE_SNAPSHOT_NAME, 'leaf1-gi0_1-fail', deactivate_interfaces=[Interface('leaf1', 'GigabitEthernet0/1')], overwrite=True)
bf_fork_snapshot(BASE_SNAPSHOT_NAME, 'leaf1-gi0_2-fail', deactivate_interfaces=[Interface('leaf1', 'GigabitEthernet0/2')], overwrite=True)

tr_answer = bfq.traceroute(startLocation="server-1",headers=HeaderConstraints(dstIps='server-2')).answer("leaf1-gi0_1-fail").frame()
pprint_tr_flows(tr_answer)

tr_answer = bfq.traceroute(startLocation="server-1",headers=HeaderConstraints(dstIps='server-2')).answer("leaf1-gi0_2-fail").frame()
pprint_tr_flows(tr_answer)
```
