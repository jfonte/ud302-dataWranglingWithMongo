
#open the file in read-only, r is optional, the open func returns a file ob that has itw own methods and attributes

stuff = open("test.txt", "r")


# read file and strip whitespaces (newlines included) from right side of the string "line"
for line in stuff:
	print(line.strip())


# close file
stuff.close()




















'''
QUESTIONS

- what does argv do?

'''
