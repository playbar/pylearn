#!/usr/bin/env python

import os
import re

f = os.popen('ps aux', 'r')
for eachLine in f:
    print (re.findall(
        '([\w.]+(?: [\w.]+)*)\s\s+(\d+) \w+\s\s+\d+\s\s+([\d,]+ K)',
        eachLine.rstrip()))
    print(eachLine.rstrip())
f.close()
