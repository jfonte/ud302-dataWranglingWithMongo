# this is python 2.7 code btw
from io import open

DATAFILE = "beatles.csv"

def parse_file(datafile):
	
	# storage for data output
	data = []

	# open the file in read only mode and with binary mode, see eof for explanation

	with open(datafile, "rb") as f:

		# read first line and split
		header = f.readline().split(",")
		# counter & loop to read first 10 lines
		counter = 0
		for line in f:
			if counter == 10: 
				break

			fields = line.split(",")
			entry = {}

			for i, value in enumerate(fields):
				entry[header[i].strip()]= value.strip()

			data.append(entry)
			counter +=1
		return data


print(parse_file(DATAFILE))
