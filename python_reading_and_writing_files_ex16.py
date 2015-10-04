from sys import argv
filename = argv

print "Opeing the file....."
#passing one argument in open function name of txt file to open and signed it variable name quotes
quotes = open("el_quotes_ex16.txt")
print quotes

fav_quotes = quotes.read().rstrip(" ").split("\n")

print fav_quotes
#closes txt file quotes
quotes.close()