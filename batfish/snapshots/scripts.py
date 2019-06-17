def enum_tr_flows(tr_answer):
	for n, flow in enumerate(tr_answer['Flow']):
	    print("============{}============".format(flow))
	    for hop in tr_answer['Traces'][n]:
	       for step in hop:
	           print(step)
