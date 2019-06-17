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

## Reduce Logging
```
import logging
logging.getLogger('pybatfish').setLevel(logging.WARN)
```

## Initialize Network/Snapshot
```
cd /opt
git clone https://github.com/packetpimp1/network-automation.git
```

## Parsing Status
```
bfq.fileParseStatus().answer().frame()
bfq.parseWarning().answer().frame()
```
