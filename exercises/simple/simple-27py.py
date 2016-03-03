'''Your task is:
 1. read the input DATAFILE line by line
 2. for the first 10 lines (not including the header) split each line on "," 
 3. then for each line, create a dictionary where the key is the header title of the field, and the value is the value of that field in the row.
 4. The function parse_file should return a list of dictionaries, each data line in the file being a single list entry.
 5. Field names and values should not contain extra whitespace, like spaces or newline characters.

 You can use the Python string method strip() to remove the extra whitespace.

Remember, you have to parse only the first 10 data lines in this exercise, so the returned list should have 10 entries!
'''

# load modules to make my life easier
import os
import csv # used to read CSV files
import pprint
from io import open

# define location of file

DATADIR = ''
DATAFILE = "beatles.csv"

def parse_csv(datafile):

	# initialize dictionary stores
	data = []
	count = 0
	# let's open the file & create a dict from it
	with open(datafile, 'rb') as f:
		readCSV = csv.DictReader(f) # automatically takes first line as headers!
		for line in readCSV:
			if count == 10:
				break
			data.append(line)
			count +=1
	return data

if __name__ == '__main__':
	datafile = os.path.join(DATADIR, DATAFILE)
	# parse_csv(datafile)
	d = parse_csv(datafile)
	pprint.pprint(d)

def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    firstline = {u'Title': u'Please Please Me', u'UK Chart Position': u'1', u'Label': u'Parlophone(UK)', u'Released': u'22 March 1963', u'US Chart Position': u'-', u'RIAA Certification': u'Platinum', u'BPI Certification': u'Gold'}
    tenthline = {u'Title': u'', u'UK Chart Position': u'1', u'Label': u'Parlophone(UK)', u'Released': u'10 July 1964', u'US Chart Position': u'-', u'RIAA Certification': u'', u'BPI Certification': u'Gold'}

    assert d[0] == firstline
    assert d[9] == tenthline

# print(parse_file(DATAFILE))
