from sys import argv
from time import gmtime, strftime

def main():
        try:
                var1 = float(argv[1])
                var2 = float(argv[2])
        except IndexError:
                print 'the number of parameters must be 2'
                exit(0)
        print var1 + var2
        print strftime("%a %b %d %X %Z %Y", gmtime())
if __name__ == '__main__':
        main()
