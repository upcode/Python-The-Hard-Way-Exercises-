# Dictionaries
# created a list with string values and bound it to variable name things
things = ['a', 'b', 'c', 'd']
# printing item in the list with index of 1 and bound
print things[1]
# string z is rebound to index of 1 in list of things
things[1] = 'z'
# index 1 in things is z
print things[1]
# print list of times in things
print things

stuff = {'name': 'Uma', 'age': '29', 'height': 5 * 12 + 2}
# printing key vlaue of name in dic stuff
print stuff['name']
# priting key value age in dic stuff
print stuff['age']
# printing key value height in dic stuff
print stuff['height']  # in inches

# added key city and its value san francisco to the dic of stuff
stuff['city'] = "San Francisco"
# printing key and its value in dic stuff
print stuff['city']
# printing dic stuff
print stuff

# adding string wow to key 1 in dic stuff
stuff[1] = "wow"
# adding string neato to key 2 in dic stuff
stuff[2] = "Neato"
# print key 1 with its value in dic stuff
print stuff[1]

# print key 2 with its value in dic stuff
print stuff[2]
# print dic stuff
print stuff

# DELETING THINGS IN DICTIONARY using del as a keyword
# deleting key city and its value in dic stuff
del stuff['city']
# deleting key 1 and its value in dic stuff
del stuff[1]
# deleting key 2 and its value in dic stuff
del stuff[2]
# print dic stuff
print stuff
print '*' * 50
#DICTIONARIES: PUTTING IT ALL TOGETHER
# INSTRUNCTIONS:create a mapping of state to abbreviation
#creating dic named states with key of state names and its values state abbreviation
states = {
    'Oregon': 'OR',
    'Flordia': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}
print states
# INSTRUNCTIONS: create a basic set of states and some citites in them

cities = {
    'CA': 'San Francisco',
    'NY': 'New York City',
    'OR': 'Portland'

}
print cities

print '_' * 50  # pritining out 10 underscores

# INSTRUNCTIONS:print cities
# printing key value of NY in dic citites
print "NY States has: ", cities['NY']
# priting out  key value of OR in dic citites
print "OR State has: ", cities['OR']

print '_' * 50  # printing 10 underscores
# INSTRUNCTIONS:do it by using the state then cities dict

#print key value of michiagn in dict states
print "Michigan's abbreviation is: ", states['Michigan']
# print key value for Florida in dic states
print "Florida's abbreviation is: ", states['Flordia']

print '_' * 50  # printing 10 underscores

#INSTRUNCTIONS: print every state abbreviation

# for statement looking for items in cities dictionary that are cities with abbreviations
for state, abbrev in states.items():
    #priting cities abbrevations and city
    print "%s is abbreviated %s" % (state, abbrev)

print '_' * 10  # printing 10 underscores

# INSTRUNCTIONS:print every city in state
# for items in cities in the city dic looking for city and abgrv
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

print '_' * 10  # printing 10 underscores

# INSTRUNCTIONS: now do both at the same time
print '_' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])

print '_' * 10  # printing 10 underscores

# INSTRUNCTIONS: safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print "Sorry, no Texas."

print '_' * 10  # printing 10 underscores

# INSTRUNCTIONS: get a city with a default value
city = cities.get("TX", "Does Not Exixt")
print "the city for the state 'TX is: %s" % city
