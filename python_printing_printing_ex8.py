formatter = "%r %r %r %r"


print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "that you could type up right.",
    "but it didn't sting.",
    "so I said goodnight."
    )

# DEBUGGING ==> SHOULD LOOK LIKE THIS INSTEAD

#formatter should be using %s for a string it will print all the strings into one line
formatter = "%s %s %s %s"

# printing integers
print formatter % (1, 2, 3, 4)
# priting stringusing formatter
print formatter % ("one", "two", "three", "four")
# printing boolean
print formatter % (True, False, False, True)
# printing foramtter
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "that you could type up right.",
    "but it didn't sting.",
    "so I said goodnight."
    )