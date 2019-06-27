def pprint_traceroute(tr_answer):
    for flow_n, flow in enumerate(tr_answer['Flow']):
        print("# FLOW = {}\n".format(flow))
        for trace_n, trace in enumerate(tr_answer['Traces'][flow_n]):
           print("\n-- TRACE{}".format(trace_n))
           for steps in trace:
               print(steps)
