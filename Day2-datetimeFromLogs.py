'''Extract datetimes from log entries and calculate the time
   between the first and last shutdown events'''
from datetime import datetime
import os
import urllib.request
import re

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('C:\\Users\\jolynn\\Python100\\100Days\\data', 'log')
# urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglinesA = f.readlines()


# for you to code:

def convert_to_datetime(line):
    partsAll = line.split()
    timeStamp = datetime.strptime((partsAll[1]), "%Y-%m-%d" + "T" + "%H:%M:%S")
    # print(timeStamp)
    return(timeStamp)


def time_between_shutdowns(loglines):
    start = 0
    end = 0
    for line in loglines:
        if re.match("(.*)Shutdown initiated(.*)", line):
            if (start):
                end = convert_to_datetime(line)
            else:
                start = convert_to_datetime(line)
        else:
            pass

    return(end - start)

""" Their answer is much different
# They make a dictionary of all entries
shutdown_entries = [line for line in loglines if SHUTDOWN_EVENT in line]
# then they convert all entries in the dictionary
shutdown_times = [convert_to_datetime(event) for event in shutdown_entries]
# then they use min and max to get start and end
return max(shutdown_times) - min(shutdown_times)
"""

print(time_between_shutdowns(loglinesA))

