my_name = 'Vikash Pateshwari'
my_age = 21 #not a lie
my_height = 185 #centimeter
my_weight = 60 #kg
my_eyes = "Brown_Black"
my_teeth = 'white'
my_hair = "Black"

print "Let's talk about %s." % my_name
print "He is %d centimeter tall" % my_height
print "He is %d kg heavy." % my_weight
print "Actually that's not too heavy :P."
print "He got %s eyes and %s hair."% (my_eyes,my_hair)
print "His teeth are usually %r depending on the coffee." % my_teeth

#this line is tricky,try to get it exactly right
print "If i add %r,%d and %d I get %d"%(my_age,my_height,my_weight,my_age + my_height + my_weight)
