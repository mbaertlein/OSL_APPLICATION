import os
import sys
from random import randint
import time

def generate_file():

# This try and open a file called cypher1.txt. If this file is empty,
# Then it will put a special code at the top, and return the name of the file.
# If the file is not empty, it will look for the special code. If that code
# is not at the top of the file, then it will increment the number, such that it 
# will now look for cypher2.txt. It will do this until it either creates a new file,
# or encounters a file with the special code at the top.

	cont = True
	count = 0
	filename = "cypher"

	while(cont):

		count=count+1

		# Generate the file, but don't erase it's contents if it is already there.
		f = open(filename+str(count)+".txt", 'a')
		f.close()

		# Check if the file is empty. If it is, then put the special code at the top of it.
		if os.stat(filename+str(count)+".txt").st_size==0:
			cont = False;
			f = open(filename+str(count)+".txt", 'a')
			f.write("2322244223_92dkaKDsasdfjklAssdkl\n")
			f.close()

		# Oh no! It's not empty!
		else:
			f = open(filename+str(count)+".txt", 'r')
			f.seek(0)

			# Check to see if it has the special code at the top. If it does, then
			# We can exit the loop! 
			if(f.readline()=="2322244223_92dkaKDsasdfjklAssdkl\n"):
				cont=False

			f.close()

	return filename+str(count)+".txt"


def generate_cyphers(source):

# This will convert the what is in the file into two lists.
# The first list (cypher_in) will contain what the input letters are.
# I.E if M is to be replaced with % then the index in cypher_in will be 
# M, and the index for cypher_out will be %.

	count = 1
	cypher_in = []
	cypher_out = []

	f=open(source,'r')

	#Pull information from the file and put it in a list
	cypher = [line.rstrip('\n').rstrip('') for line in f]

	while count < len(cypher):
		
		if count % 2 == 1 and cypher[count]!= '':
			cypher_in.append(cypher[count])

		elif cypher[count]!='':
			cypher_out.append(cypher[count])
			
		count = count + 1

	f.close()
	return (cypher_in, cypher_out)

def generate_rand(ch):

# Will generate a new ascii character that is not
# equal to the character ch

	cont = True
	while(cont):

		new_asc=randint(33,127)

		if new_asc == ord(ch):
			cont = True

		else:
			cont = False

	return chr(new_asc)

def lower_case_argv():

# Returns the lower case version of 
# the command line argument in the "first" position

	d = 0
	l = ""

	while d < len(sys.argv[1]):
		l = l + sys.argv[1][d].lower()
		d = d + 1

	return l

def start_cypher(inp,cypher_i,cypher_o,cypher_file):
	
	count = 0
	new = ""

	if len(cypher_i)==0:

		cypher_i.append(inp[0])
		cypher_o.append(generate_rand(inp[0]))
		
		cypher_file.write(cypher_i[0]+"\n")
		cypher_file.write(cypher_o[0]+"\n")


	while count < len(inp):

		count_c = 0

		while count_c < len(cypher_i):
			
			if cypher_i[count_c]==inp[count]:

				new=new+(cypher_o[count_c])
				break

			elif count_c == (len(cypher_i)-1):

				conti=True

				while conti:

					new_ascii = randint(33,126)

					if new_ascii == ord(inp[count]):
						conti=True

					else:
						c = 0
						while c < len(cypher_o):

							if ord(cypher_o[c]) == new_ascii:
								conti = True
								break

							elif c == (len(cypher_o)-1):
								conti=False
								break

							c = c + 1

				cypher_file.write(inp[count]+"\n")
				cypher_file.write(chr(new_ascii)+"\n")
				cypher_i.append(inp[count])
				cypher_o.append(chr(new_ascii))

			

			

			count_c=count_c+1


		count = count+1

	cypher_file.close()

	print "Cyphered Name: "+new


if __name__ == "__main__":
	
	#Create the file we will store our cypher in (if it does not exist). Source will
	#contain the name of the file.
	source = generate_file()
	
	# Read in from the file and seperate into a cypher in and a cypher out.
	# Indexes will match up such that cypher_in[0] will match up with 
	# cypher_out[0].
	cypher = generate_cyphers(source)
	cypher_in = cypher[0]
	cypher_out = cypher[1]

	# Check the argument(s) and then send them on their way.
	if len(sys.argv)==1:
		print "\nYou need to enter a name as an argument\nmake your command like this:\n\n python app.py name\n"

	elif len(sys.argv)==2:
		print "\nThis program will now cypher the first name \nprovided: "+str(sys.argv[1])+"\n"
		start_cypher(lower_case_argv(),cypher_in,cypher_out,open(source,'a'))
		print "Original Name: "+sys.argv[1]+"\n"

	elif len(sys.argv)>2:
		print "\nYou should only enter one name at a time.\nThis program will now cypher the first name \nprovided: "+str(sys.argv[1])+"\n"
		start_cypher(lower_case_argv(),cypher_in,cypher_out,open(source,'a'))










