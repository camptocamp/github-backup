#!/usr/bin/env python

import re
import sys
import datetime
import os

logfiles = ['/var/log/syslog', '/var/log/syslog.1']
REGEX = r"(?P<month>\D{3})\s+(?P<day>\d+).*github-backup: session is now completed,.(?P<stats>.*)"

now = datetime.datetime.now()
today = now.strftime("%b-%d")
yesterday = (now-datetime.timedelta(days=1)).strftime("%b-%d")

results = []

for logfile in logfiles:
  for line in open(logfile):
     result = re.match(REGEX, line)
     if result: results.append(result)

for r in results:
  date = "%s-%s" % ( r.group('month'), r.group('day').rjust(2,'0'))
  if date in (today, yesterday):
    print "OK - github-backup, %s" % r.group('stats')
    sys.exit(0)

print "CRITICAL - github-backup failed"
sys.exit(2)
