days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months: ", months

print """
There's something going on here.
With there double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, for 5, or 6.
"""
# DEBUGGING ==> SHOULD LOOK LIKE THIS INSTEAD
# string of days of week bound it to the variable name days
days = "Mon Tue Wed Thu Fri Sat Sun"
# sring of months bound variable name to months and added \n before jan
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"  # added new line char before jan

# using formatter %s for a string print days
print "Here are the %s: " % (days)  # added %s in the string and put days in prenthisis

# using formatter %s for a string print months
print "Here are the %s: " % (months)  # added %s in the string and put months in prenthis

#print a string with three quotes called a dogstring
print """
There's something going on here.
With there double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, for 5, or 6.
"""