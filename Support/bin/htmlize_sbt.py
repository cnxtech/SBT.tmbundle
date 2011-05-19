#!/usr/bin/python

import sys, os.path, re, os
from collections import deque

matcher = re.compile(
    r'^(\[\w+\]) (/.*):(\d+):\s*(.*)$'
)

proj_dir = os.getcwd()

print """
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="file://%s/sbt.css" />
    </head>

    <body>
""" % (os.environ['TM_BUNDLE_SUPPORT'])

sys.stdout.flush()

## read all data from stdin

lines=deque()
lines.append(sys.stdin.readline())

while len(lines) > 0:
    line = lines.popleft().rstrip()
    
    match = matcher.search(line)

    print "<pre>"

    if not match:
        print line
    else:
        label = match.group(1)
        fn = match.group(2)
        lineNo = match.group(3)
        errText = match.group(4)

        if proj_dir and fn.startswith(proj_dir):
            short_name = "..." + fn[len(proj_dir):]
        else:
            short_name = fn

        colInd = -1

        # read the next few lines into the buffer
        while len(lines) < 6:
            nextline = sys.stdin.readline()
            if len(nextline) == 0:
                break
            lines.append(nextline)
        
        for i in range(6,0,-1):
            if i < len(lines) and lines[i][-2] == "^":
                carrotLine = lines[i].rstrip()
                brktInd = carrotLine.find("]")
                colInd = len(carrotLine[(brktInd + 2):])
        
        if colInd < 0:
            print "Unable to find ^ marker when parsing SBT output."
            colInd = 0
        
        print '%s <a href="txmt://open?url=file://%s&line=%s&column=%d">%s:%s</a>: %s' % (
            label, fn, lineNo, colInd, short_name, lineNo, errText
        ),
        print line[match.end():]

    print "</pre>"
    sys.stdout.flush()

    if len(lines) == 0:
        nextline = sys.stdin.readline()
        if len(nextline) != 0:
            lines.append(nextline)

print """
    </body>
</html>
"""
