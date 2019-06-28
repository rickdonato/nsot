# pretty prints the answer from bfq.traceroute()
def pprint_traceroute(answer):
    for flow_n, flow in enumerate(answer['Flow']):
        print("# FLOW = {}\n".format(flow))
        for trace_n, trace in enumerate(answer['Traces'][flow_n]):
           print("\n-- TRACE{}".format(trace_n))
           for steps in trace:
               print(steps)

# pretty prints the answer from bfq.differentialReachability()
def pprint_diffreach(answer):
    for flow_n, flow in enumerate(answer['Flow']):
        print("# FLOW = {}\n".format(flow))
        for trace_n, trace in enumerate(answer['Snapshot_Traces'][flow_n]):
           print("\n-- SNAPSHOT TRACE{}".format(trace_n))
           for steps in trace:
               print(steps)
        for ref_trace_n, trace in enumerate(answer['Reference_Traces'][flow_n]):
           print("\n-- REFERENCE/BASELINE TRACE{}".format(ref_trace_n))
           for steps in trace:
               print(steps)

# improve output display
def set_pd_display():
   import pandas as pd
   pd.set_option('display.max_rows', 500)
   pd.set_option('display.max_columns', 500)
   pd.set_option('display.width', 1000)
