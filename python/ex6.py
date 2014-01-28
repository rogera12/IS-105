x = "There are %d types of people." % 10 #string inside
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)# string inside

print x
print y

print "I said: %r." % x #string inside
print "I also said: '%s'." % y #string inside

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r" #string inside

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e

# because its printing out string w and e after eachother
