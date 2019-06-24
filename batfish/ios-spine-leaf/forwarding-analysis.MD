```
bf_set_network(NETWORK_NAME)
bf_init_snapshot(SNAPSHOT_PATH, name=SNAPSHOT_NAME, overwrite=True)

tr_answer = bfq.traceroute(startLocation="leaf1",headers=HeaderConstraints(dstIps='server-2')).answer().frame()

for n, flow in enumerate(tr_answer['Flow']):
    print("============{}============".format(flow))
    for hop in tr_answer['Traces'][n]:
       for step in hop:
           print(step)
```
