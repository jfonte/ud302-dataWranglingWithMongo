# Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
# split each line on "," and then for each line, create a dictionary
# where the key is the header title of the field, and the value is the value of that field in the row.
# The function parse_file should return a list of dictionaries,
# each data line in the file being a single list entry.
# Field names and values should not contain extra whitespace, like spaces or newline characters.
# You can use the Python string method strip() to remove the extra whitespace.
# You have to parse only the first 10 data lines in this exercise,
# so the returned list should have 10 entries!

from __future__ import with_statement
from __future__ import absolute_import
import os
import csv
from io import open

é

DATADIR = u""
DATAFILE = u"beatles.csv"
datafile = DATAFILE


with open(datafile, u"r", encoding=u'ascii') as f:
    data = []
    readCSV = csv.reader(f, delimiter=u',',quotechar=u'"')
    count = 1
    for row in readCSV:
        temp = {}
        # grab headers
        if count == 1:
            headers = row
        # create dictionary for each row
        if count >1:
            count2 = len(headers)-1
            for i in xrange(0,len(headers)):
                temp.setdefault(headers[count2],row[count2])
                count2-=1
            data.append(temp)
        #
        count +=1
        # get only first 10 rows
        if count > 11:
            break

print data

def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    firstline = {u'Title': u'Please Please Me', u'UK Chart Position': u'1', u'Label': u'Parlophone(UK)', u'Released': u'22 March 1963', u'US Chart Position': u'-', u'RIAA Certification': u'Platinum', u'BPI Certification': u'Gold'}
    tenthline = {u'Title': u'', u'UK Chart Position': u'1', u'Label': u'Parlophone(UK)', u'Released': u'10 July 1964', u'US Chart Position': u'-', u'RIAA Certification': u'', u'BPI Certification': u'Gold'}

    assert d[0] == firstline
    assert d[9] == tenthline
