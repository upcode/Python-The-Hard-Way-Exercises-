# string using formatted character is bound to variable name x
x = "There are %d types of people." % 10
# string bound to variable name binary
binary = "binary"
# string "dont" is bound to variable name do_not
do_not = "dont"
# string using  two formatted character isbound to variable name y place holders using previous variable names
y = "those who know %s and those who %s." % (binary, do_not)

print x
print y
print "I said: %r." % x
print "I also said: '%s'. " % y
# boolean False is binded to variable name hailarious
hilarious = False
# binded string to variable name joke_evaluation
joke_evaluation = "Isn't that joke so funny?! %r"
print joke_evaluation % hilarious
# binded string to the variable name w
w = "this is the left side of ..."
# binded string to the variable name e
e = "a string with a right side."

# print vaiable w plus variable name e adding two strings together
print w + e