def cheese_and_crackers(cheese_count, boxes_of_cracers):
    print "You have %d cheese!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "man that's enough for a party!"
    print "Get a blanket. \n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "and we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)