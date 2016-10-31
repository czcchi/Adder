from sys import argv
from time import gmtime, strftime

def main():
	#verify the number of input
        try:
                var1 = argv[1]
                var2 = argv[2]
        except IndexError:
                print 'the number of parameters must be 2'
                exit(0)
	
	#verity the type of input
	try:
		var1 = float(var1)
		var2 = float(var2)
	except ValueError:
		print 'the input value must be number'
		exit(0)
	#print the sum of two number
        print var1 + var2
	#print the current time
        print strftime("%a %b %d %X %Z %Y", gmtime())


if __name__ == '__main__':
        main()
