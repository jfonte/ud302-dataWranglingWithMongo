'''
Your task is:
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
from io import open

# define location of file

DATADIR = ''
DATAFILE = "beatles.csv"

def parse_file(datafile):

	# initialize dictionary stores

	data = []

	# let's open the file
	with open(datafile, "r", encoding='ascii') as f:
		readCSV = csv.reader(f, delimiter =',', quotechar='"')
	
		# counter to read only the first 10 lines
		count = 1
		for row in readCSV:
			temp = {}
			# grab headers
			if count == 1:
				headers = row
				# print headers
			# create dictionary for each row
			if count>1:
				for i in xrange(0, len(headers)):
					# check if field exists, if not create & add keypair
					temp.setdefault(headers[i], row[i])
					# print headers[i],row[i]
				# add dictionary from row to data
				data.append(temp)
			# jump to next row
			count +=1

			# get only first 10 rows
			if count>11:
				break
		
	return data

def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    firstline = {u'Title': u'Please Please Me', u'UK Chart Position': u'1', u'Label': u'Parlophone(UK)', u'Released': u'22 March 1963', u'US Chart Position': u'-', u'RIAA Certification': u'Platinum', u'BPI Certification': u'Gold'}
    tenthline = {u'Title': u'', u'UK Chart Position': u'1', u'Label': u'Parlophone(UK)', u'Released': u'10 July 1964', u'US Chart Position': u'-', u'RIAA Certification': u'', u'BPI Certification': u'Gold'}

    assert d[0] == firstline
    assert d[9] == tenthline

print(parse_file(DATAFILE))
